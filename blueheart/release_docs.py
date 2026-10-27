"""BH-P08 implementation. Local generation and read-only Git verification; never commit/push.

The final documentation envelope resolves the self-hash problem. CI derives its SHA,
checks every introduced commit, and emits a receipt without changing the repository.
"""
import argparse
from functools import lru_cache
import json
import os
from pathlib import Path
import re
import subprocess
import sys

from .io import Invalid, canonical, loads, path, sha

EMPTY = 'EMPTY'
PREFIX = 'docs/releases/pushes/'
CATEGORIES = ('added', 'changed', 'fixed', 'removed')
CHECKS = ([sys.executable, '-B', '-m', 'blueheart', 'check'],
          [sys.executable, '-B', '-m', 'unittest', 'discover', '-s', 'tests', '-q'])


def _git(root, args):
    result = subprocess.run(['git', '-C', str(root), *args], capture_output=True)
    if result.returncode:
        raise Invalid('Git: ' + result.stderr.decode('utf-8', 'replace').strip())
    return result.stdout


@lru_cache(maxsize=512)
def _immutable_git(root, args):
    return _git(root, args)


def git(root, *args):
    # Only object-addressed reads are cached; refs, status and every mutation remain live.
    if args and args[0] in {'show', 'ls-tree', 'diff', 'rev-list'} and 'HEAD' not in args:
        return _immutable_git(str(root), tuple(args))
    return _git(root, args)


def commit(root, ref):
    if ref != 'HEAD' and not re.fullmatch(r'(?:[a-f0-9]{40}|[a-f0-9]{64})', ref):
        raise Invalid('Use HEAD or a full commit SHA; base may also be EMPTY')
    return git(root, 'rev-parse', '--verify', '--end-of-options', ref + '^{commit}').decode().strip()


def ancestor(root, base, tip):
    if base == EMPTY:
        return
    if base not in commits(root, EMPTY, tip):
        raise Invalid('Base is not an ancestor of payload')


def commits(root, base, tip):
    args = ['rev-list', '--reverse', '--topo-order', tip]
    if base != EMPTY:
        args.append('^' + base)
    return git(root, *args).decode().splitlines()


def parents(root, oid):
    return git(root, 'show', '-s', '--format=%P', oid).decode().split()


def blob(root, oid, name, optional=False):
    path(root, name)
    names = git(root, 'ls-tree', '-z', '--name-only', oid, '--', name).decode().split('\0')
    if name not in names:
        if optional:
            return None
        raise Invalid('Missing tracked file at ' + oid + ': ' + name)
    return git(root, 'show', oid + ':' + name)


def files(root, base, tip):
    if base == EMPTY:
        names = git(root, 'ls-tree', '-r', '-z', '--name-only', tip).decode().split('\0')
        return [{'status': 'A', 'path': n} for n in names if n]
    fields = git(root, 'diff', '--no-renames', '--name-status', '-z', base, tip, '--').decode().split('\0')
    return [{'status': fields[i], 'path': fields[i+1]} for i in range(0, len(fields)-1, 2)]


def catalog(root, oid):
    raw = None if oid == EMPTY else blob(root, oid, 'norms/catalog.json', True)
    return loads(raw) if raw else {'contracts': [], 'token_sets': []}


def components(root, oid):
    cat = catalog(root, oid)
    result, tokens, collections = {}, {}, {}
    for entry in cat['token_sets']:
        if entry['current']:
            raw = blob(root, oid, entry['path'])
            if sha(raw) != entry['sha256']:
                raise Invalid('Token catalog hash mismatch')
            tokens.update({t['id']: t for t in loads(raw)['tokens']})
            collections.update({c['id']: c for c in loads(raw).get('collections', [])})
    contracts = {}
    for entry in cat['contracts']:
        raw = blob(root, oid, entry['path'])
        if sha(raw) != entry['sha256']:
            raise Invalid('Contract catalog hash mismatch')
        meta = loads(raw.decode().split('\n---\n', 1)[0][4:])
        contracts[(entry['id'], entry['version'])] = (entry, meta)
    def fingerprint(key, active):
        if key in active:
            raise Invalid('Cycle in component dependencies')
        if key not in contracts:
            raise Invalid('Missing contract dependency')
        entry, meta = contracts[key]
        active = active | {key}
        used = {}
        def token(tid):
            if tid in used:
                return
            if tid not in tokens:
                raise Invalid('Missing token dependency')
            used[tid] = tokens[tid]
            for value in tokens[tid]['values'].values():
                if isinstance(value, dict) and 'alias' in value:
                    token(value['alias'])
        children = {}
        for dep in meta['dependencies']:
            if dep['kind'] == 'token':
                token(dep['id'])
            elif dep['kind'] == 'contract':
                child = (dep['id'], dep.get('version'))
                children[dep['id'] + '@' + str(child[1])] = fingerprint(child, active)
        modes = {t['collection']: collections[t['collection']] for t in used.values() if t.get('collection') in collections}
        return sha(canonical({'contract': entry['sha256'], 'tokens': used, 'collections': modes, 'children': children}))
    for key, (entry, meta) in contracts.items():
        if meta['profile'] == 'component' and entry['current']:
            result[key[0]] = {'version': entry['version'], 'path': entry['path'],
                             'sha256': entry['sha256'], 'fingerprint': fingerprint(key, set())}
    return result


def semver(value):
    if not isinstance(value, str) or not re.fullmatch(r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)', value):
        raise Invalid('Expected stable SemVer x.y.z')
    return tuple(map(int, value.split('.')))


def component_changes(root, base, tip, declarations):
    old, new = components(root, base), components(root, tip)
    changed = {i for i in old.keys() | new.keys() if old.get(i) != new.get(i)}
    if set(declarations) - changed:
        raise Invalid('Component impact declared for an unchanged or unknown component')
    result = []
    for identity in sorted(changed):
        before, after = old.get(identity), new.get(identity)
        declaration = declarations.get(identity)
        if before is None:
            impact, reason = ('minor', 'Primera incorporación de la versión registrada al historial Git.') if declaration is None else (declaration['impact'], declaration['reason'])
            semver(after['version'])
        else:
            if declaration is None:
                raise Invalid('Declare impact and migration rationale for affected component: ' + identity)
            impact, reason = declaration['impact'], declaration['reason']
            if after is None:
                if impact != 'major':
                    raise Invalid('Removing a component requires major impact and migration rationale')
            else:
                a, b = semver(before['version']), semver(after['version'])
                if b <= a:
                    raise Invalid('Changed component or token dependency requires a new component version: ' + identity)
                rank = {'major': 0, 'minor': 1, 'patch': 2}.get(impact)
                if rank is None or b[:rank+1] <= a[:rank+1]:
                    raise Invalid('Component version does not satisfy declared compatibility impact')
        if impact not in {'major', 'minor', 'patch'} or not isinstance(reason, str) or not reason.strip():
            raise Invalid('Invalid component impact or missing migration rationale')
        result.append({'id': identity, 'from': before, 'to': after, 'impact': impact, 'reason': reason})
    return result


def render(record):
    # The body is a disposable projection of the single record, never another editable source.
    body = '# Envío ' + record['payload'] + '\n\nTipo: ' + record['kind'] + '. Base: `' + record['base'] + '`.\n'
    for category in CATEGORIES:
        body += '\n## ' + category + '\n\n'
        body += '\n'.join('- `' + c['sha'] + '` ' + c['subject'] for c in record['commits'] if c['category'] == category) or 'Sin cambios clasificados en esta categoría.'
        body += '\n'
    body += '\n## Trazabilidad\n\nLos commits, archivos, pruebas, pendientes, decisiones y versiones de componentes están en el frontmatter de este único registro. El comprobante CI identifica el commit documental y el rango efectivo del push.\n'
    return '---\n' + json.dumps(record, ensure_ascii=False, sort_keys=True, indent=2) + '\n---\n' + body


def build(root, base, payload, tests, pending, decisions, declarations, kind='development', version=None, evidence=None):
    payload = commit(root, payload)
    base = EMPTY if base == EMPTY else commit(root, base)
    ancestor(root, base, payload)
    ids = commits(root, base, payload)
    if not ids:
        raise Invalid('No payload commits to document')
    changes = files(root, base, payload)
    # Incoming merge ancestry may already contain documented batches. Reference those
    # records instead of documenting their payload commits a second time. CI validates
    # every newly introduced envelope independently before accepting this projection.
    reused, documented = [], set()
    for oid in ids:
        ps = parents(root, oid)
        altered = files(root, ps[0] if ps else EMPTY, oid)
        notes = [f for f in altered if f['path'].startswith(PREFIX)]
        if notes and len(ps) <= 1:
            if len(altered) != 1 or notes[0]['status'] != 'A' or len(ps) != 1:
                raise Invalid('Existing release records are immutable; only documentation envelopes may add records')
            previous = parse_record(blob(root, oid, notes[0]['path']))
            if previous['payload'] != ps[0]:
                raise Invalid('Incoming record is not a documentation envelope')
            reused.append(notes[0]['path'])
            documented.update(c['sha'] for c in previous['commits'])
            documented.add(oid)
    info = []
    for oid in ids:
        if oid in documented:
            continue
        subject = git(root, 'show', '-s', '--format=%s', oid).decode().strip()
        match = re.match(r'([a-z]+)(?:\([^)]*\))?!?:', subject)
        category = {'feat': 'added', 'fix': 'fixed', 'remove': 'removed'}.get(match[1] if match else '', 'changed')
        info.append({'sha': oid, 'subject': subject, 'category': category})
    if kind not in {'development', 'release'} or (kind == 'release') != (version is not None):
        raise Invalid('Official release requires an explicit stable version; development has none')
    if version is not None:
        semver(version)
    known = loads(blob(root, payload, 'governance/decisions.json'))['decisions'] if decisions else []
    if set(decisions) - {d['id'] for d in known if d['status'] == 'ADOPTED'}:
        raise Invalid('Unknown or unadopted architectural decision')
    if not isinstance(pending, list) or any(not isinstance(p, str) or not p.strip() for p in pending):
        raise Invalid('Pending verifications must be explicit nonempty descriptions')
    if len(tests) != 2:
        raise Invalid('Both architecture and infrastructure test results are required')
    for test, args in zip(tests, CHECKS):
        if set(test) != {'command', 'exit_code', 'status', 'output', 'sha256'} or test['command'] != ['python3', *args[1:]]:
            raise Invalid('Unexpected test result structure or command')
        if type(test['exit_code']) is not int or not isinstance(test['output'], str):
            raise Invalid('Invalid test evidence')
        if test['status'] != ('PASS' if test['exit_code'] == 0 else 'FAIL') or sha(test['output'].encode()) != test['sha256']:
            raise Invalid('Test status or output hash mismatch')
    refs = [{'path': name, 'sha256': sha(blob(root, payload, name))} for name in sorted(set(evidence or []))]
    changes_components = component_changes(root, base, payload, declarations)
    if any(c['from'] is not None for c in changes_components) and not refs and not pending:
        raise Invalid('Component changes need QA evidence references or explicit pending destination checks')
    if kind == 'release' and changes_components and not refs:
        raise Invalid('Official release with component changes requires destination QA evidence references')
    return {'schema_version': 1, 'base': base, 'payload': payload, 'kind': kind, 'release_version': version,
            'commits': info, 'references': sorted(reused), 'files': changes, 'tests': tests, 'pending': pending,
            'evidence': refs, 'decisions': sorted(set(decisions)), 'components': changes_components}


def parse_record(raw):
    text = raw.decode('utf-8')
    if not text.startswith('---\n') or '\n---\n' not in text[4:]:
        raise Invalid('Release record needs JSON frontmatter')
    return loads(text[4:].split('\n---\n', 1)[0])


def validate_envelope(root, envelope, name):
    ps = parents(root, envelope)
    if len(ps) != 1:
        raise Invalid('Documentation envelope needs exactly one parent')
    changed = files(root, ps[0], envelope)
    if changed != [{'status': 'A', 'path': name}]:
        raise Invalid('Envelope must add exactly its new generated record, with no payload edits')
    raw = blob(root, envelope, name)
    record = parse_record(raw)
    if name != PREFIX + record['payload'] + '.md' or record['payload'] != ps[0]:
        raise Invalid('Record filename, payload and envelope parent disagree')
    declarations = {c['id']: {'impact': c['impact'], 'reason': c['reason']} for c in record['components']}
    expected = build(root, record['base'], record['payload'], record['tests'], record['pending'], record['decisions'], declarations, record['kind'], record['release_version'], [e['path'] for e in record['evidence']])
    if record != expected or raw.decode() != render(expected):
        raise Invalid('Stale, incomplete or noncanonical release documentation')
    if any(t['status'] != 'PASS' for t in record['tests']):
        raise Invalid('Recorded tests failed; documentation does not make failed QA compliant')
    if record['kind'] == 'release' and record['pending']:
        raise Invalid('Official release has pending verifications')
    return record


def verify(root, base, head):
    """Cover every newly introduced commit exactly once; accept preserved-SHA integrations."""
    head = commit(root, head)
    base = EMPTY if base == EMPTY else commit(root, base)
    ancestor(root, base, head)
    introduced = commits(root, base, head)
    if not introduced:
        raise Invalid('Empty update is not a documented push')
    remaining, covered, records, envelopes, integrations = set(introduced), set(), [], [], []
    candidates = []
    for oid in introduced:
        ps = parents(root, oid)
        if len(ps) == 1:
            changed = files(root, ps[0], oid)
            if any(c['path'].startswith(PREFIX) for c in changed):
                if len(changed) != 1:
                    raise Invalid('Release record changed alongside payload')
                name = changed[0]['path']
                record = validate_envelope(root, oid, name)
                candidates.append((oid, name, record))
    for oid, name, record in candidates:
        batch = set(c['sha'] for c in record['commits']) | {oid}
        new_batch = batch & set(introduced)
        if new_batch & covered or batch - new_batch - set(commits(root, EMPTY, base) if base != EMPTY else []):
            raise Invalid('Record duplicates another record or claims commits outside the update ancestry')
        covered |= new_batch
        remaining -= new_batch
        records.append(name)
        envelopes.append(oid)
    # Only no-content merge commits may close an integration. Require the current base
    # in the feature branch and preserve commit SHAs (no squash/rebase).
    for oid in introduced:
        if oid not in remaining:
            continue
        ps = parents(root, oid)
        if len(ps) == 2 and ps[1] in covered:
            ancestor(root, ps[0], ps[1])
            if files(root, ps[1], oid):
                raise Invalid('Merge introduces unrecorded content; resolve and document on the feature branch')
            covered.add(oid); remaining.remove(oid); integrations.append(oid)
    if remaining:
        raise Invalid('Undocumented commits in push: ' + ', '.join(sorted(remaining)))
    # Every branch update ends with an envelope or verified no-content integration.
    if head not in envelopes + integrations:
        raise Invalid('Push head is not a documentation envelope or verified integration')
    return {'status': 'PASS', 'base': base, 'head': head, 'commits': introduced, 'files': files(root, base, head),
            'records': sorted(records), 'envelopes': envelopes, 'integrations': integrations,
            'scope': 'Recorded architecture/infrastructure tests; destination QA remains explicit in pending/evidence'}


def prepare(root, base, pending, decisions, declarations, kind='development', version=None, evidence=None):
    git(root, 'rev-parse', '--show-toplevel')
    if git(root, 'status', '--porcelain', '--untracked-files=all').strip():
        raise Invalid('Commit payload first; prepare requires a clean tracked/untracked worktree')
    payload = commit(root, 'HEAD')
    tests = []
    for args in CHECKS:
        result = subprocess.run(args, cwd=root, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = result.stdout.decode('utf-8', 'replace')
        tests.append({'command': ['python3', *args[1:]], 'exit_code': result.returncode,
                      'status': 'PASS' if result.returncode == 0 else 'FAIL', 'output': output, 'sha256': sha(output.encode())})
    if git(root, 'status', '--porcelain', '--untracked-files=all').strip() or commit(root, 'HEAD') != payload:
        raise Invalid('Checks changed the worktree or HEAD; review before generating a record')
    record = build(root, base, payload, tests, pending, decisions, declarations, kind, version, evidence)
    target = path(root, PREFIX + payload + '.md')
    if target.exists():
        raise Invalid('Record already exists; existing records are immutable')
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render(record), encoding='utf-8')
    return {'status': 'READY' if all(t['status'] == 'PASS' for t in tests) else 'FAIL',
            'path': str(target), 'payload': payload, 'committed': False, 'pushed': False}


def ci(root, event, event_name):
    if event_name == 'push':
        if event.get('deleted'):
            raise Invalid('Ref deletion is outside the documented update policy')
        if event.get('ref', '').startswith('refs/tags/'):
            head = commit(root, event['after'])
            ps = parents(root, head)
            if len(ps) != 1:
                raise Invalid('Release tag must point to a documentation envelope')
            name = PREFIX + ps[0] + '.md'
            record = validate_envelope(root, head, name)
            if record['kind'] != 'release' or event['ref'] != 'refs/tags/v' + str(record['release_version']):
                raise Invalid('Tag does not match an explicit official release record')
            receipt = verify(root, record['base'], head)
            receipt['tag'] = event['ref']
            return receipt
        before = event['before']
        return verify(root, EMPTY if set(before) == {'0'} else before, event['after'])
    if event_name == 'pull_request':
        pr = event['pull_request']
        base, head = pr['base']['sha'], pr['head']['sha']
        ancestor(root, base, head)  # Require branch updated, preserving IDs.
        return verify(root, base, head)
    if event_name == 'merge_group':
        group = event['merge_group']
        return verify(root, group['base_sha'], group['head_sha'])
    raise Invalid('Unsupported CI event')


def failure_receipt(root, event, event_name, reason):
    """A failed check still leaves an honest receipt for the condensed PDF report."""
    if event_name == 'pull_request':
        base, head = event['pull_request']['base']['sha'], event['pull_request']['head']['sha']
    elif event_name == 'push':
        base, head = event.get('before', EMPTY), event['after']
        if base != EMPTY and set(base) == {'0'}:
            base = EMPTY
    else:
        raise Invalid('No failure receipt for unsupported event')
    head = commit(root, head)
    base = EMPTY if base == EMPTY else commit(root, base)
    return {'status': 'NONCOMPLIANT', 'reason': reason, 'base': base, 'head': head,
            'commits': commits(root, base, head), 'files': files(root, base, head),
            'records': [], 'envelopes': [], 'integrations': [],
            'run_id': os.environ.get('GITHUB_RUN_ID'),
            'scope': 'Actual Git update; documentation validation failed, no compliance certified'}


def main():
    parser = argparse.ArgumentParser(description='BH-P08 · never commits or pushes')
    parser.add_argument('--root', type=Path, default=Path.cwd())
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('prepare')
    p.add_argument('--base', required=True)
    p.add_argument('--pending', action='append', default=[])
    p.add_argument('--decision', action='append', default=[])
    p.add_argument('--evidence', action='append', default=[], help='Tracked BH-P04 evidence path; reused by hash, never copied')
    p.add_argument('--component-change', action='append', default=[], metavar='ID:patch|minor|major:RATIONALE')
    p.add_argument('--kind', choices=['development', 'release'], default='development')
    p.add_argument('--release-version')
    v = sub.add_parser('verify'); v.add_argument('--base', required=True); v.add_argument('--head', default='HEAD')
    c = sub.add_parser('ci'); c.add_argument('--receipt', type=Path, required=True)
    args = parser.parse_args()
    event = None
    try:
        root = args.root.resolve()
        if args.command == 'prepare':
            declarations = {}
            for value in args.component_change:
                identity, impact, reason = value.split(':', 2)
                if identity in declarations:
                    raise Invalid('Duplicate component impact declaration')
                declarations[identity] = {'impact': impact, 'reason': reason}
            result = prepare(root, args.base, args.pending, args.decision, declarations, args.kind, args.release_version, args.evidence)
        elif args.command == 'verify':
            result = verify(root, args.base, args.head)
        else:
            event = loads(Path(os.environ['GITHUB_EVENT_PATH']).read_bytes())
            result = ci(root, event, os.environ['GITHUB_EVENT_NAME'])
            result['run_id'] = os.environ.get('GITHUB_RUN_ID')
            # Receipt is an ephemeral CI artifact, not a repository change.
            if args.receipt.resolve().is_relative_to(root):
                raise Invalid('CI receipt must be outside the worktree')
            args.receipt.write_bytes(canonical(result) + b'\n')
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
        return 0 if result['status'] in {'PASS', 'READY'} else 2
    except (Invalid, OSError, KeyError, TypeError, ValueError, UnicodeError) as error:
        if args.command == 'ci' and event is not None and not args.receipt.resolve().is_relative_to(args.root.resolve()):
            try:
                failed = failure_receipt(args.root, event, os.environ['GITHUB_EVENT_NAME'], str(error))
                args.receipt.write_bytes(canonical(failed) + b'\n')
            except (Invalid, OSError, KeyError, TypeError, ValueError):
                pass  # The check still fails; never fabricate a receipt without resolvable Git refs.
        print(json.dumps({'status': 'NONCOMPLIANT', 'reason': str(error)}, ensure_ascii=False))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
