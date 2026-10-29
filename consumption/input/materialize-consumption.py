"""Project Input/Badge identities and maps from selected owners and captured native evidence."""
from pathlib import Path
import json,hashlib,csv,runpy
ROOT=Path(__file__).resolve().parents[2]
def read(p):return json.loads((ROOT/p).read_text())
def ref(p):return {'path':p,'sha256':hashlib.sha256((ROOT/p).read_bytes()).hexdigest()}
def write(p,v):(ROOT/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def materialize():
 runpy.run_path(str(ROOT/'implementations/figma/input-plan.py'))['materialize']()
 s=read('evidence/input-pilot/state.json');show=read('evidence/input-pilot/destination/showcase-and-properties.json')
 c=read('norms/catalog.json');contracts={e['id']:e for e in c['contracts']if e['current']};ts=next(e for e in c['token_sets']if e['current'])
 build=s['empty']['built']+s['filled']['built']
 for path in s['batches']:build+=read('evidence/input-pilot/'+path)['built']
 by_source={v['sourceId']:v for v in build}
 for family,identity in [('input','INPUT-001'),('badge','BADGE-001')]:
  p=read('consumption/'+family+'/current-build-plan.json');tokens=p['tokens'];variables=[dict(logicalId=t['id'],nativeId=s['variableIds'][t['id']],nativeKey=s['variableKeys'][t['id']],figmaName=t['figmaName'],name=t['name'],web=t['web'],scope=t['scopes'][0],aliases=t['values'],themeBehavior=t['themeBehavior'])for t in tokens]
  ledger=dict(role='DERIVED_CURRENT_NATIVE_LEDGER_NOT_RULES',pageId=s['pages'][family],collection=s['collection'],variableIds={v['logicalId']:v['nativeId']for v in variables},variableKeys={v['logicalId']:v['nativeKey']for v in variables},styles={k:v for k,v in s['styles'].items()if k.startswith(family+'/')})
  bindings=[]
  if family=='input':
   ledger['sets']=[{k:s[kind][k]for k in ['setId','setKey','kind','propertyKeys','variants']}for kind in ['empty','filled']];ledger['reviewFrame']=show['doc'];ledger['qaFrame']=show['qa'];ledger['variants']=build
   for v in p['variants']:
    native={n['path']:n['id']for n in by_source[v['id']]['nodes']}
    for n in v['rows']:
     for field,tid in n['bindings'].items():bindings.append(dict(sourceVariantId=v['id'],sourceNodeId=n['id'],nativeVariantId=by_source[v['id']]['id'],nativeNodeId=native[n['path']],part=n['path'],property=field,logicalId=tid,nativeVariableId=s['variableIds'][tid],resolution='shared-style'if n['type']=='TEXT'and field in ['fontFamily','fontStyle','fontSize','lineHeight','letterSpacing']or field.startswith('effect.')else'direct'))
     for vector in n.get('vectors',[]):
      for field,tid in vector['bindings'].items():bindings.append(dict(sourceVariantId=v['id'],sourceNodeId=vector['id'],nativeVariantId=by_source[v['id']]['id'],nativeNodeId=native[n['path']],part=n['path']+'/VECTOR',property=field,logicalId=tid,nativeVariableId=s['variableIds'][tid],resolution='nested-Phosphor-vectors'))
  else:
   ledger.update(setId=s['badge']['setId'],setKey=s['badge']['setKey'],variantId=s['badge']['id'],variantKey=s['badge']['key'],labelId=s['badge']['labelId'],labelProperty=s['badge']['labelProperty'],reviewFrame=read('evidence/input-pilot/destination/badge-documentation.json')['frame'])
   for part,nid in [('root',s['badge']['id']),('label',s['badge']['labelId'])]:
    for field,tid in p['badge'][part]['bindings'].items():bindings.append(dict(sourceVariantId='8851:26563',sourceNodeId=p['badge'][part]['id'],nativeVariantId=s['badge']['id'],nativeNodeId=nid,part=part,property=field,logicalId=tid,nativeVariableId=s['variableIds'][tid],resolution='shared-style'if part=='label'and field!='fills'else'direct'))
  prefix='consumption/'+family+'/'
  write(prefix+'current-native-ledger.json',ledger)
  for name,rows in [('variable-map.csv',variables),('binding-map.csv',bindings)]:
   with (ROOT/prefix/name).open('w')as stream:
    writer=csv.DictWriter(stream,fieldnames=list(rows[0]));writer.writeheader();writer.writerows({k:json.dumps(v,ensure_ascii=False,sort_keys=True)if isinstance(v,(dict,list))else v for k,v in row.items()}for row in rows)
  manifest=dict(schema_version=1,role='DERIVED_CONSUMPTION_INDEX_NOT_RULES',contract=contracts[identity],token_sets=[ts],fileKey='98xEw6sK8FRVNEhopM5SSz',page={'id':s['pages'][family],'name':family.capitalize()},collection=s['collection'],variables=variables,nativeLedger=ref(prefix+'current-native-ledger.json'),build_plan='current-build-plan.json',minimum='token-minimum.json',variable_map='variable-map.csv',binding_map='binding-map.csv',qa=ref('evidence/qa/input-pilot-check.json'),distribution='LOCAL_COMPONENTS_NOT_PUBLISHED_LIBRARY',web_implementation='NOT_IMPLEMENTED')
  if family=='input':manifest['dependencies']=[{'contract':contracts['BADGE-001'],'manifest':ref('consumption/badge/manifest.json')}]if(ROOT/'consumption/badge/manifest.json').exists()else[]
  write(prefix+'manifest.json',manifest)
 # Refresh Input dependency after Badge's manifest has been projected.
 m=read('consumption/input/manifest.json');m['dependencies']=[{'contract':contracts['BADGE-001'],'manifest':ref('consumption/badge/manifest.json')}];write('consumption/input/manifest.json',m)
 return {'input':len(by_source),'badge':1}
if __name__=='__main__':print(json.dumps(materialize()))
