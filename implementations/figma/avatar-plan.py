"""Materialize Avatar contracts and recipes from preserved evidence; no Figma/network writes.

The registered MD/token sets remain the only normative owners. Re-running only
regenerates the derived build plan from selected registered token data.
"""
from pathlib import Path
import json
import hashlib

ROOT = Path(__file__).resolve().parents[2]
def read(p): return json.loads((ROOT / p).read_text())
def digest(p): return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
def write(p, d):
    f = ROOT / p; f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
def ref(p, **kw): return dict(path=p, sha256=digest(p), **kw)

SOURCE = 'evidence/avatar-pilot/source/page-snapshot.json'
DISCOVERY = 'evidence/avatar-pilot/source/discovery.json'
AUTH = 'evidence/authorization/avatar-pilot-request.txt'
MODES = ['Contable', 'Administrativo', 'Servicios', 'Personas']

def plan():
    catalog=read('norms/catalog.json'); entry=next(e for e in catalog['token_sets'] if e['id']=='BLUEHEART-TOKENS' and e['current']); ts=read(entry['path']); ts['tokens']=[t for t in ts['tokens'] if t['id'].startswith(('avatar.','avatar-group.'))]; names={v['logicalId']:v['figmaName'] for v in read('evidence/collection-consolidation/migration-map.json')['variables']}; ns=read(SOURCE)['nodes']; ix={n['id']:n for n in ns}
    sem={t['id']:t for t in read(entry['path'])['tokens']}
    native={v['layer']+'.'+v['name']:v['destination_id'] for v in read('evidence/figma-application/application-map.json')['variables']}
    recipes=[]
    for n in ns:
        if n['type']=='COMPONENT' and n['parent']=='1132:21344':
            axes=dict(part.strip().split('=') for part in n['name'].split(',')); content=next(c for c in ns if c['parent']==n['id'] and c['name']=='Avatar'); kids=[c for c in ns if c['parent']==content['id']]
            recipes.append(dict(sourceId=n['id'],axes=axes,root=n,content=content,kids=[c for c in kids if c['type']!='VECTOR'],status=next(c for c in ns if c['parent']==n['id'] and c['name']=='Status')))
    data=dict(expectedNativeVariableCount=len(read(entry['path'])['tokens']),dot=read('consumption/dot/current-native-ledger.json'),sourceFileKey='9zs5RMR8LB5wHjW9Bd59BA',destinationFileKey='98xEw6sK8FRVNEhopM5SSz',pageName='Avatars',modes=MODES,tokens=[dict(t,figmaName=names[t['id']],web='var('+t['name']+')',themeBehavior='THEMED' if t['id']=='avatar.color-bg-primary-default' else 'INVARIANT') for t in ts['tokens']],semanticIds={alias['alias']:native.get(alias['alias']) for t in ts['tokens'] for alias in t['values'].values()},variants=recipes,presence=read('evidence/avatar-pilot/source/presence-and-gaps.json')['presence'],portrait=dict(path='evidence/avatar-pilot/assets/portrait.png',sha256=digest('evidence/avatar-pilot/assets/portrait.png'),imageHash='33f6b019db4382817513e4485e94d3a7dd5a6ca2'),phosphor=read('evidence/avatar-pilot/source/phosphor.json'))
    write('consumption/avatar/current-build-plan.json',data)
    summary={'role':'DERIVED_MINIMUM_NOT_RULES','families':{}}
    for family in ['avatar','avatar-group']:
        selected=[t for t in data['tokens'] if t['id'].startswith(family+'.')]
        signatures={json.dumps({k:t.get(k) for k in ['type','unit','collection','scopes','values']},sort_keys=True) for t in selected}
        assert len(signatures)==len(selected)
        summary['families'][family]=dict(tokens=len(selected),distinctSignatures=len(signatures),redundancies=0,themeRoles={t['figmaName']:t['themeBehavior'] for t in selected})
    import csv
    for family in ['avatar','avatar-group']:
        with (ROOT/'consumption'/family/'binding-map.csv').open(newline='') as f:
            uses=sum(row['logicalTokenId'].startswith(family+'.') for row in csv.DictReader(f))
        summary['families'][family].update(candidatePropertyBindings=uses,candidateMethod='Mapa de bindings por identidad lógica del contrato; sin producto cartesiano.',uniqueSelectedSignatures=summary['families'][family]['tokens'])
    write('consumption/avatar/token-minimum.json',summary)
    print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__=='__main__':
    plan()
