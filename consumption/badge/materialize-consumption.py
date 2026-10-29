"""Project the selected Badge MD and captured native identities; no authority inference."""
from pathlib import Path
import copy,csv,hashlib,json,re
ROOT=Path(__file__).resolve().parents[2]
BASE='evidence/badge-pilot/'
def read(p):return json.loads((ROOT/p).read_text())
def ref(p):return dict(path=p,sha256=hashlib.sha256((ROOT/p).read_bytes()).hexdigest())
def write(p,v):(ROOT/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def recipe():
 c=read('norms/catalog.json');entry=next(e for e in c['contracts']if e['id']=='BADGE-001'and e['current']);ts=next(e for e in c['token_sets']if e['current']);text=(ROOT/entry['path']).read_text();meta=json.loads(text[4:].split('\n---\n',1)[0]);routes=dict(re.findall(r'^\| (badge\.[^ ]+) \| ([^ ]+) \|$',text,re.M));ids={d['id']for d in meta['dependencies']if d['kind']=='token'}
 p=copy.deepcopy(read(BASE+'build-plan.json'));p.update(contract=entry,token_set=ts);p['tokens']=[dict(t,figmaName=routes[t['id']],web='var('+t['name']+')',themeBehavior='INVARIANT')for t in read(ts['path'])['tokens']if t['id']in ids];assert len(p['tokens'])==35
 write('consumption/badge/current-build-plan.json',p)
 sig={json.dumps({k:t.get(k)for k in ['type','unit','scopes','values']},sort_keys=True)for t in p['tokens']};assert len(sig)==len(p['tokens']);write('consumption/badge/token-minimum.json',dict(role='DERIVED_MINIMUM_NOT_RULES',tokens=len(p['tokens']),distinctSignatures=len(sig),redundancies=0,candidateUses=len(p['uses']),retained=12,added=23))
 return p
def materialize():
 p=recipe();f=read(BASE+'after/foundations.json');b=read(BASE+'after/components.json');old=read(BASE+'history/badge/current-native-ledger.json');show=read(BASE+'after/showcase.json');fixed=read(BASE+'after/showcase-fix.json')
 ledger=dict(role='DERIVED_CURRENT_NATIVE_LEDGER_NOT_RULES',pageId='281:63',collection=f['collection'],variableIds=f['variableIds'],variableKeys=f['variableKeys'],styles={'badge/subtle-small':f['styles']['small'],'badge/label-medium':f['styles']['medium'],'badge/label-large':f['styles']['large']},setId=b['setId'],setKey=b['setKey'],variantId=old['variantId'],variantKey=old['variantKey'],labelId=old['labelId'],labelProperty=old['labelProperty'],propertyKeys=b['propertyKeys'],variants=b['variants'],reviewFrame=fixed['frame'],compatibilityFrame=show['compatibilityFrame'],decision='ADR-025')
 write('consumption/badge/current-native-ledger.json',ledger)
 variables=[dict(logicalId=t['id'],nativeId=f['variableIds'][t['id']],nativeKey=f['variableKeys'][t['id']],figmaName=t['figmaName'],name=t['name'],web=t['web'],scope=t['scopes'][0],aliases=t['values'],themeBehavior='INVARIANT')for t in p['tokens']]
 bindings=[]
 for v in p['variants']:
  dest=next(x for x in b['variants']if x['sourceId']==v['sourceId']);mapped={}
  for n in v['nodes']:
   if n['type']=='COMPONENT':native=dest['id']
   elif n['type']=='TEXT':native=dest['labelId']
   elif n['type']=='INSTANCE':native=next(i['id']for i in dest['icons']if i['name']==n['name'])
   else:
    choices=[id for id in b['mutatedNodeIds']if id.startswith('I'+mapped[n['parent']]+';')];assert len(choices)==1,(n['id'],choices);native=choices[0]
   mapped[n['id']]=native
   for field,tid in n['bindings'].items():bindings.append(dict(sourceVariantId=v['sourceId'],sourceNodeId=n['id'],nativeVariantId=dest['id'],nativeNodeId=native,part=n['name'],property=field,logicalId=tid,nativeVariableId=f['variableIds'][tid],resolution='shared-style'if n['type']=='TEXT'and field!='fills'else'direct'))
 for name,rows in [('variable-map.csv',variables),('binding-map.csv',bindings)]:
  with(ROOT/'consumption/badge'/name).open('w')as stream:
   writer=csv.DictWriter(stream,fieldnames=list(rows[0]),lineterminator='\n');writer.writeheader();writer.writerows({k:json.dumps(v,ensure_ascii=False,sort_keys=True)if isinstance(v,(dict,list))else v for k,v in row.items()}for row in rows)
 manifest=dict(schema_version=1,role='DERIVED_CONSUMPTION_INDEX_NOT_RULES',contract=p['contract'],token_sets=[p['token_set']],fileKey='98xEw6sK8FRVNEhopM5SSz',page=dict(id='281:63',name='Badge'),collection=f['collection'],variables=variables,nativeLedger=ref('consumption/badge/current-native-ledger.json'),build_plan='current-build-plan.json',minimum='token-minimum.json',variable_map='variable-map.csv',binding_map='binding-map.csv',qa=ref('evidence/qa/badge-pilot-check.json'),distribution='LOCAL_COMPONENTS_NOT_PUBLISHED_LIBRARY',web_implementation='NOT_IMPLEMENTED')
 write('consumption/badge/manifest.json',manifest);return {'variants':len(b['variants']),'tokens':len(variables),'bindings':len(bindings)}
if __name__=='__main__':print(json.dumps(materialize()))
