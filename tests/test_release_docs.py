"""Real Git DAGs in temporary directories; no commits or remotes in the workspace."""
import copy
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from blueheart.io import Invalid, canonical, sha
from blueheart import release_docs as rd


class ReleaseDocsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.g('init', '-q', '-b', 'main')
        self.g('config', 'user.email', 'fixture@example.invalid')
        self.g('config', 'user.name', 'Synthetic fixture')
        self.write('norms/catalog.json', {'contracts': [], 'token_sets': []})
        self.write('governance/decisions.json', {'decisions': [{'id': 'ADR-TEST', 'status': 'ADOPTED'}]})
        self.write('sample.txt', 'initial')
        self.initial = self.save('feat: initial fixture')
        self.tests = [{'command': ['python3', *args[1:]], 'exit_code': 0, 'status': 'PASS',
                       'output': 'synthetic PASS\n', 'sha256': sha(b'synthetic PASS\n')} for args in rd.CHECKS]

    def g(self, *args):
        return rd.git(self.root, *args).decode().strip()

    def write(self, name, value):
        target = self.root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(canonical(value) if isinstance(value, (dict, list)) else value.encode())

    def save(self, subject):
        self.g('add', '-A')
        self.g('commit', '-q', '-m', subject)
        return self.g('rev-parse', 'HEAD')

    def note(self, base=rd.EMPTY, **kwargs):
        return rd.build(self.root, base, 'HEAD', self.tests, kwargs.pop('pending', []),
                        kwargs.pop('decisions', []), kwargs.pop('declarations', {}), **kwargs)

    def close(self, record=None):
        record = record or self.note()
        name = rd.PREFIX + record['payload'] + '.md'
        self.write(name, rd.render(record))
        return self.save('docs: record payload'), name

    def bootstrap(self):
        return self.close()[0]

    def component(self, version='1.0.0', color=1, text='Contract', identity='CMP-ONE', dependencies=None):
        meta = {'profile': 'component', 'dependencies': dependencies if dependencies is not None else [{'kind': 'token', 'id': 'component.bg'}]}
        name = 'norms/' + identity + '-' + version + '.md'
        raw = '---\n' + json.dumps(meta) + '\n---\n' + text
        self.write(name, raw)
        self.write('norms/tokens.json', {'tokens': [
            {'id': 'primitive.color', 'values': {'light': color, 'dark': 2}},
            {'id': 'semantic.color', 'values': {'light': {'alias': 'primitive.color'}, 'dark': {'alias': 'primitive.color'}}},
            {'id': 'component.bg', 'values': {'light': {'alias': 'semantic.color'}, 'dark': {'alias': 'semantic.color'}}}]})
        cat = json.loads((self.root / 'norms/catalog.json').read_text())
        for e in cat['contracts']:
            if e['id'] == identity:
                e['current'] = False
        cat['contracts'] = [e for e in cat['contracts'] if not (e['id'] == identity and e['version'] == version)]
        cat['contracts'].append({'id': identity, 'version': version, 'path': name, 'sha256': sha(raw.encode()), 'current': True})
        cat['token_sets'] = [{'id': 'TOKENS', 'version': '1.0.0', 'path': 'norms/tokens.json',
                              'sha256': sha((self.root / 'norms/tokens.json').read_bytes()), 'current': True}]
        self.write('norms/catalog.json', cat)

    def test_valid_initial_push_and_receipt_cover_document_commit(self):
        head, name = self.close()
        result = rd.verify(self.root, rd.EMPTY, head)
        self.assertEqual(result['status'], 'PASS')
        self.assertEqual(result['commits'], [self.initial, head])
        self.assertEqual(result['records'], [name])
        self.assertIn({'status': 'A', 'path': name}, result['files'])
        before = self.g('status', '--porcelain')
        self.assertEqual(result, rd.verify(self.root, rd.EMPTY, head))
        self.assertEqual(before, self.g('status', '--porcelain'))

    def test_undocumented_push_fails(self):
        with self.assertRaisesRegex(Invalid, 'Undocumented'):
            rd.verify(self.root, rd.EMPTY, self.initial)

    def test_content_after_envelope_is_not_covered(self):
        self.bootstrap()
        self.write('extra.txt', 'uncovered')
        head = self.save('fix: forgot a change')
        with self.assertRaisesRegex(Invalid, 'Undocumented'):
            rd.verify(self.root, rd.EMPTY, head)

    def test_note_and_content_cannot_be_committed_together(self):
        record = self.note()
        self.write('extra.txt', 'uncovered')
        head, _ = self.close(record)
        with self.assertRaisesRegex(Invalid, 'alongside payload'):
            rd.verify(self.root, rd.EMPTY, head)

    def test_stale_or_tampered_files_and_rendering_rejected(self):
        for mutation in ('files', 'body', 'tests'):
            with self.subTest(mutation=mutation):
                record = self.note()
                if mutation == 'files':
                    record['files'] = []
                if mutation == 'tests':
                    record['tests'][0]['sha256'] = '0' * 64
                name = rd.PREFIX + record['payload'] + '.md'
                self.write(name, rd.render(record) + ('edited\n' if mutation == 'body' else ''))
                head = self.save('docs: malformed')
                with self.assertRaises(Invalid):
                    rd.verify(self.root, rd.EMPTY, head)
                self.g('reset', '--hard', self.initial)

    def test_record_rewrites_are_rejected(self):
        base, name = self.close()
        self.write(name, (self.root/name).read_text() + 'correction')
        head = self.save('docs: rewrite historical record')
        with self.assertRaises(Invalid):
            rd.verify(self.root, base, head)
        with self.assertRaises(Invalid):
            self.note(base)

    def test_multiple_disjoint_batches_and_pr_coverage(self):
        base = self.bootstrap()
        self.write('sample.txt', 'second')
        self.save('fix: second fixture')
        second, _ = self.close(self.note(base))
        self.write('sample.txt', 'third')
        self.save('remove: third fixture')
        third, _ = self.close(self.note(second))
        receipt = rd.verify(self.root, base, third)
        self.assertEqual(len(receipt['records']), 2)
        self.assertEqual(rd.ci(self.root, {'pull_request': {'base': {'sha': base}, 'head': {'sha': third}}}, 'pull_request'), receipt)
        self.assertEqual(len(rd.ci(self.root, {'before': '0'*40, 'after': third, 'ref': 'refs/heads/new'}, 'push')['records']), 3)

    def test_no_content_integration_merge_preserves_coverage(self):
        base = self.bootstrap()
        self.g('checkout', '-q', '-b', 'feature')
        self.write('sample.txt', 'feature')
        self.save('feat: reusable content')
        feature, _ = self.close(self.note(base))
        self.g('checkout', '-q', 'main')
        self.g('merge', '--no-ff', '-q', '-m', 'Merge feature', 'feature')
        merged = self.g('rev-parse', 'HEAD')
        result = rd.verify(self.root, base, merged)
        self.assertEqual(result['integrations'], [merged])
        self.assertEqual(rd.files(self.root, feature, merged), [])

    def test_merge_with_unrecorded_resolution_fails(self):
        base = self.bootstrap()
        self.g('checkout', '-q', '-b', 'feature')
        self.write('feature.txt', 'feature')
        self.save('feat: feature')
        self.close(self.note(base))
        self.g('checkout', '-q', 'main')
        self.g('merge', '--no-ff', '--no-commit', 'feature')
        self.write('resolution.txt', 'unrecorded merge edit')
        head = self.save('Merge with extra edit')
        with self.assertRaisesRegex(Invalid, 'unrecorded content'):
            rd.verify(self.root, base, head)

    def test_updating_feature_from_documented_main_references_existing_batches(self):
        base = self.bootstrap()
        self.g('checkout', '-q', '-b', 'feature')
        self.write('feature.txt', 'feature')
        self.save('feat: feature')
        feature_base, _ = self.close(self.note(base))
        self.g('checkout', '-q', 'main')
        self.write('main.txt', 'main')
        self.save('fix: current main')
        main, main_note = self.close(self.note(base))
        self.g('checkout', '-q', 'feature')
        self.g('merge', '--no-ff', '-q', '-m', 'Merge current main', 'main')
        record = self.note(feature_base)
        self.assertEqual(record['references'], [main_note])
        feature, _ = self.close(record)
        self.assertEqual(rd.verify(self.root, feature_base, feature)['status'], 'PASS')
        self.assertEqual(rd.verify(self.root, main, feature)['status'], 'PASS')
        self.g('checkout', '-q', 'main')
        self.g('merge', '--no-ff', '-q', '-m', 'Merge updated feature', 'feature')
        self.assertEqual(rd.verify(self.root, main, 'HEAD')['status'], 'PASS')

    def test_official_release_tag_requires_matching_record_and_no_pending(self):
        head, _ = self.close(self.note(kind='release', version='1.0.0'))
        self.assertEqual(rd.ci(self.root, {'ref': 'refs/tags/v1.0.0', 'after': head}, 'push')['tag'], 'refs/tags/v1.0.0')
        with self.assertRaises(Invalid):
            rd.ci(self.root, {'ref': 'refs/tags/v2.0.0', 'after': head}, 'push')
        self.g('reset', '--hard', self.initial)
        head, _ = self.close(self.note(kind='release', version='1.0.0', pending=['Destination QA not run']))
        with self.assertRaisesRegex(Invalid, 'pending'):
            rd.verify(self.root, rd.EMPTY, head)

    def test_development_record_cannot_be_used_as_release_tag(self):
        head = self.bootstrap()
        with self.assertRaises(Invalid):
            rd.ci(self.root, {'ref': 'refs/tags/v1.0.0', 'after': head}, 'push')

    def test_failed_tests_do_not_become_a_compliant_record(self):
        self.tests[0].update(exit_code=1, status='FAIL')
        head, _ = self.close()
        with self.assertRaisesRegex(Invalid, 'tests failed'):
            rd.verify(self.root, rd.EMPTY, head)

    def test_unknown_decision_and_bad_version_rejected(self):
        with self.assertRaisesRegex(Invalid, 'architectural decision'):
            self.note(decisions=['ADR-MISSING'])
        for version in ('v1.0.0', '1.0', '01.2.3'):
            with self.assertRaises(Invalid):
                self.note(kind='release', version=version)

    def test_first_component_version_preserved_and_governance_does_not_bump_it(self):
        self.component('2.0.0')
        self.save('feat: initial component import')
        record = self.note()
        self.assertEqual(record['components'][0]['to']['version'], '2.0.0')
        with self.assertRaisesRegex(Invalid, 'destination QA evidence'):
            self.note(kind='release', version='1.0.0')
        base, _ = self.close(record)
        self.write('governance/text.md', 'documentation only')
        self.save('docs: governance')
        self.assertEqual(self.note(base)['components'], [])

    def test_transitive_primitive_change_requires_component_version(self):
        self.component()
        self.save('feat: component')
        base = self.close(self.note())[0]
        self.component(color=3)
        self.save('fix: shared primitive')
        with self.assertRaisesRegex(Invalid, 'Declare impact'):
            self.note(base)
        with self.assertRaisesRegex(Invalid, 'new component version'):
            self.note(base, declarations={'CMP-ONE': {'impact': 'patch', 'reason': 'Compatible correction'}})

    def test_compatibility_impact_must_match_component_bump(self):
        self.component()
        self.save('feat: component')
        base = self.close(self.note())[0]
        self.component('1.0.1', text='Breaking API')
        self.save('feat!: remove component prop')
        with self.assertRaisesRegex(Invalid, 'compatibility impact'):
            self.note(base, declarations={'CMP-ONE': {'impact': 'major', 'reason': 'Migrate consumers'}})
        self.component('2.0.0', text='Breaking API')
        self.save('chore: new major')
        record = self.note(base, pending=['Figma QA pending'], declarations={'CMP-ONE': {'impact': 'major', 'reason': 'Use replacement prop'}})
        head, _ = self.close(record)
        self.assertEqual(rd.verify(self.root, base, head)['status'], 'PASS')

    def test_component_removal_requires_major_and_migration(self):
        self.component()
        self.save('feat: component')
        base = self.close(self.note())[0]
        cat = json.loads((self.root/'norms/catalog.json').read_text()); cat['contracts'] = []
        self.write('norms/catalog.json', cat)
        self.save('remove: component')
        for declaration in ({}, {'CMP-ONE': {'impact': 'patch', 'reason': 'Removed'}}):
            with self.assertRaises(Invalid):
                self.note(base, declarations=declaration)
        record = self.note(base, pending=['Consumer migration pending'], declarations={'CMP-ONE': {'impact': 'major', 'reason': 'Use successor component'}})
        self.assertIsNone(record['components'][0]['to'])

    def test_component_qa_uses_evidence_hash_without_copy(self):
        self.component()
        self.save('feat: component')
        base = self.close(self.note())[0]
        self.component('1.0.1', text='Corrected')
        self.write('evidence/qa/check.json', {'status': 'PASS', 'scope': 'synthetic fixture'})
        self.save('fix: compatible correction')
        declarations = {'CMP-ONE': {'impact': 'patch', 'reason': 'Compatible correction'}}
        with self.assertRaisesRegex(Invalid, 'QA evidence'):
            self.note(base, declarations=declarations)
        record = self.note(base, declarations=declarations, evidence=['evidence/qa/check.json'])
        self.assertEqual(record['evidence'], [{'path': 'evidence/qa/check.json', 'sha256': sha((self.root/'evidence/qa/check.json').read_bytes())}])
        head, _ = self.close(record)
        self.assertEqual(rd.verify(self.root, base, head)['status'], 'PASS')

    def test_deleted_and_unicode_files_are_recorded(self):
        base = self.bootstrap()
        (self.root/'sample.txt').unlink()
        self.write('nombre á\ncon salto.txt', 'new')
        self.save('remove: replace file')
        record = self.note(base)
        self.assertIn({'status': 'D', 'path': 'sample.txt'}, record['files'])
        self.assertIn({'status': 'A', 'path': 'nombre á\ncon salto.txt'}, record['files'])
        head, _ = self.close(record)
        self.assertEqual(rd.verify(self.root, base, head)['status'], 'PASS')

    def test_force_push_nonancestor_and_deletion_fail(self):
        base = self.bootstrap()
        self.g('checkout', '--orphan', 'unrelated')
        self.g('rm', '-r', '-q', '-f', '.')
        self.write('different.txt', 'different root')
        unrelated = self.save('feat: unrelated')
        with self.assertRaisesRegex(Invalid, 'ancestor'):
            rd.verify(self.root, base, unrelated)
        with self.assertRaises(Invalid):
            rd.ci(self.root, {'deleted': True}, 'push')

    def test_pinned_child_version_does_not_follow_new_current_implicitly(self):
        self.component(identity='CHILD')
        self.component(identity='PARENT', dependencies=[{'kind': 'contract', 'id': 'CHILD', 'version': '1.0.0'}])
        self.save('feat: composed components')
        base = self.close(self.note())[0]
        self.component('2.0.0', identity='CHILD', text='New child API')
        self.save('feat!: new child version')
        record = self.note(base, pending=['Child QA pending'], declarations={'CHILD': {'impact': 'major', 'reason': 'Parent remains pinned to the old child'}})
        self.assertEqual([c['id'] for c in record['components']], ['CHILD'])

    def test_collection_default_mode_change_affects_component(self):
        self.component()
        tokens = json.loads((self.root/'norms/tokens.json').read_text())
        tokens['collections'] = [{'id': 'palette', 'default_mode': 'light', 'modes': [{'id': 'light'}, {'id': 'dark'}]}]
        for t in tokens['tokens']:
            t['collection'] = 'palette'
        def update():
            self.write('norms/tokens.json', tokens)
            cat = json.loads((self.root/'norms/catalog.json').read_text())
            cat['token_sets'][0]['sha256'] = sha((self.root/'norms/tokens.json').read_bytes())
            self.write('norms/catalog.json', cat)
        update(); self.save('feat: explicit collection modes')
        base = self.close(self.note())[0]
        tokens['collections'][0]['default_mode'] = 'dark'
        update(); self.save('fix: default mode')
        with self.assertRaisesRegex(Invalid, 'Declare impact'):
            self.note(base)

    def test_prepare_only_writes_note_runs_checks_and_never_commits(self):
        real_run = subprocess.run
        calls = []
        def run(args, **kwargs):
            if args[0] == 'git':
                return real_run(args, **kwargs)
            calls.append(args)
            return subprocess.CompletedProcess(args, 0, b'PASS synthetic check\n')
        with patch.object(rd.subprocess, 'run', side_effect=run):
            result = rd.prepare(self.root, rd.EMPTY, [], ['ADR-TEST'], {})
        self.assertEqual(result['status'], 'READY')
        self.assertFalse(result['committed'])
        self.assertFalse(result['pushed'])
        self.assertEqual(self.g('rev-parse', 'HEAD'), self.initial)
        self.assertEqual(len(calls), 2)
        self.assertEqual(self.g('status', '--porcelain'), '?? docs/')
        with self.assertRaisesRegex(Invalid, 'clean'):
            rd.prepare(self.root, rd.EMPTY, [], [], {})
