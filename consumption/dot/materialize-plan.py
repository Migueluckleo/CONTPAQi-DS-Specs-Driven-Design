"""Derive Dot recipes from the selected MD/token owners and immutable Figma evidence."""
from pathlib import Path
import json,re,hashlib,csv
ROOT=Path(__file__).resolve().parents[2]
def read(p):return json.loads((ROOT/p).read_text())
def save(p,value):(ROOT/p).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def ref(p):return dict(path=p,sha256=hashlib.sha256((ROOT/p).read_bytes()).hexdigest())
def materialize():
 c=read('norms/catalog.json');entry=next(e for e in c['contracts']if e['current']and e['id']=='DOT-001');raw=(ROOT/entry['path']).read_text();meta=json.loads(raw.split('\n---\n',1)[0][4:]);routes=dict(re.findall(r'^\| (dot\.[^ ]+) \| ([^ ]+) \|$',raw,re.M));ts=next(e for e in c['token_sets']if e['current']);ids={d['id']for d in meta['dependencies']if d['kind']=='token'};tokens=[dict(t,figmaName=routes[t['id']],web='var('+t['name']+')',themeBehavior='INVARIANT')for t in read(ts['path'])['tokens']if t['id']in ids];application=read('evidence/figma-application/application-map.json')['variables'];native={v['layer']+'.'+v['name']:v['destination_id']for v in application};source=read('evidence/dot-pilot/source/variants.json')['nodes'];plan=dict(role='DERIVED_RECIPE_NOT_RULES',contract=entry,token_set=ts,tokens=tokens,modes=['Contable','Administrativo','Servicios','Personas'],semanticIds={a:native[a]for t in tokens for a in [t['values']['Contable']['alias']]},variants=[{k:v[k]for k in ['id','name','width','height','paddingLeft','paddingRight']}for v in source if v['type']=='COMPONENT'],source=ref('evidence/dot-pilot/source/variants.json'));save('consumption/dot/current-build-plan.json',plan)
 qa=read('evidence/dot-pilot/destination/native-qa.json');ledger=read('consumption/dot/current-native-ledger.json');reverse={v:k for k,v in ledger['variableIds'].items()};counts={tid:sum(r[2]==nid for r in qa['bindings'])for tid,nid in ledger['variableIds'].items()};signatures={json.dumps({k:t.get(k)for k in ['type','unit','scopes','values']},sort_keys=True)for t in tokens};assert len(signatures)==len(tokens)==19 and all(counts.values());save('consumption/dot/token-minimum.json',dict(role='DERIVED_MINIMUM_NOT_RULES',tokens=len(tokens),distinctSignatures=len(signatures),redundancies=0,candidatePropertyBindings=len(qa['bindings']),nativeUsesByToken=counts))
 with (ROOT/'consumption/dot/binding-map.csv').open('w',newline='')as f:
  w=csv.writer(f,lineterminator="\n");w.writerow(['nativeNodeOrStyleId','property','nativeVariableId','logicalTokenId']);w.writerows([*r,reverse[r[2]]]for r in qa['bindings'])
 return plan
if __name__=='__main__':materialize()
