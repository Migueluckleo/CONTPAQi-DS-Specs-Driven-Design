"""Project selected MD/token owners and captured native IDs; never write Figma."""
from pathlib import Path
import copy,csv,hashlib,json,re
ROOT=Path(__file__).resolve().parents[2];BASE='evidence/breadcrumb-pilot/'
def read(p):return json.loads((ROOT/p).read_text())
def ref(p):return dict(path=p,sha256=hashlib.sha256((ROOT/p).read_bytes()).hexdigest())
def write(p,v):
 p=ROOT/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def signature(t):return json.dumps({k:t.get(k)for k in ['type','unit','scopes','values']},sort_keys=True)
def validate_recipe(document,plan):
 source_tokens={t['id']:t for t in read(BASE+'build-plan.json')['tokens']};tokens={t['id']:t for t in document['tokens']};owned={t['id']for t in plan['tokens']};used=set()
 for u in plan['uses']:
  id=u['tokenId'];used.add(id)
  if id not in owned or tokens[id]['values']!=u['aliases']:raise ValueError('Breadcrumb source alias mismatch: '+id)
  source=source_tokens[id]
  if any(tokens[id].get(k)!=source.get(k)for k in ['type','unit','scopes']):raise ValueError('Breadcrumb property scope/type mismatch: '+id)
 if used!=owned:raise ValueError('Breadcrumb recipe coverage mismatch')
 if len({signature(tokens[id])for id in owned})!=len(owned):raise ValueError('Breadcrumb redundant signature')
 variants=plan['variants']
 if plan['contract']['id']=='BREADCRUMB-ITEM-001':
  expected={('text','true','default')}|{(t,'false',s)for t in ['text','icon','overflow']for s in ['default','hover','focus','disabled']}
  if len(variants)!=13 or {(r['axes']['type'],r['axes']['current'],r['axes']['state'])for r in variants}!=expected:raise ValueError('Breadcrumb sparse matrix mismatch')
 else:
  if len(variants)!=5 or {r['axes']['levels']for r in variants}!={'2','3','4','5','collapsed'}:raise ValueError('Breadcrumb composition matrix mismatch')
 return dict(tokens=len(owned),uses=len(plan['uses']),variants=len(variants))
def materialize():
 c=read('norms/catalog.json');ts=next(e for e in c['token_sets']if e['current']);document=read(ts['path']);captured=read(BASE+'build-plan.json');f=read(BASE+'foundations-event.json');b=read(BASE+'build-event.json');q=read(BASE+'native-bindings.json');show=read(BASE+'showcase-event.json');counts={}
 for family,identity,kind,variants_key in [('breadcrumb-item','BREADCRUMB-ITEM-001','items','itemVariants'),('breadcrumb','BREADCRUMB-001','compositions','compositions')]:
  entry=next(e for e in c['contracts']if e['current']and e['id']==identity);text=(ROOT/entry['path']).read_text();meta=json.loads(text[4:].split('\n---\n',1)[0]);routes=dict(re.findall(r'^\| ([^ ]+) \| (breadcrumb/[^ ]+) \|$',text,re.M));owned={d['id']for d in meta['dependencies']if d['kind']=='token'};p=dict(role='DERIVED_RECIPE_NOT_RULES',decision='ADR-026',contract=entry,token_set=ts,tokens=[dict(t,figmaName=routes[t['id']],web='var('+t['name']+')',themeBehavior='THEMED'if len({json.dumps(v,sort_keys=True)for v in t['values'].values()})>1 else'INVARIANT')for t in document['tokens']if t['id']in owned],variants=copy.deepcopy(captured[kind]),uses=[u for u in captured['uses']if u['family']==family],interaction=captured['interaction'],source_recipe=ref(BASE+'build-plan.json'))
  if family=='breadcrumb':p['dependency']=next(e for e in c['contracts']if e['current']and e['id']=='BREADCRUMB-ITEM-001')
  counts[family]=validate_recipe(document,p);out='consumption/'+family+'/';write(out+'current-build-plan.json',p)
  write(out+'token-minimum.json',dict(role='DERIVED_MINIMUM_NOT_RULES',tokens=len(owned),distinctSignatures=len(owned),redundancies=0,candidateUses=len(p['uses']),minimizationScope=identity))
  setId=b['itemSet'if family=='breadcrumb-item'else'parentSet'];setNative=next(s for s in q['sets']if s['id']==setId);ledger=dict(role='DERIVED_CURRENT_NATIVE_LEDGER_NOT_RULES',pageId=f['pageId'],setId=setId,setKey=setNative['key'],defaultVariantId=setNative['defaultVariant'],collection=dict(id='VariableCollectionId:11:2',name='component',modeIds={'Contable':'11:0','Administrativo':'11:1','Servicios':'11:2','Personas':'11:3'}),variableIds={id:f['variables'][id]for id in sorted(owned)},styles=f['styles']if family=='breadcrumb-item'else{},propertyKeys={'Label':b['labelKey']}if family=='breadcrumb-item'else{'Show back':b['backKey']},variants=b[variants_key],reviewFrame=show['reviewFrame'],decision='ADR-026');write(out+'current-native-ledger.json',ledger)
  native={v['logicalId']:v for v in q['variables']};variables=[dict(logicalId=t['id'],nativeId=f['variables'][t['id']],nativeKey=native[t['id']]['key'],figmaName=t['figmaName'],name=t['name'],web=t['web'],scope=t['scopes'][0],aliases=t['values'],themeBehavior=t['themeBehavior'])for t in p['tokens']]
  bindings=[dict(sourceNodeId=u['sourceNodeId'],nativeNodeId=b['map'][u['sourceNodeId']],property=u['field'],logicalId=u['tokenId'],nativeVariableId=f['variables'][u['tokenId']])for u in p['uses']]
  for name,rows in [('variable-map.csv',variables),('binding-map.csv',bindings)]:
   with(ROOT/out/name).open('w')as stream:
    w=csv.DictWriter(stream,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows({k:json.dumps(v,ensure_ascii=False,sort_keys=True)if isinstance(v,(dict,list))else v for k,v in r.items()}for r in rows)
  manifest=dict(schema_version=1,role='DERIVED_CONSUMPTION_INDEX_NOT_RULES',contract=entry,token_sets=[ts],fileKey='98xEw6sK8FRVNEhopM5SSz',page=dict(id=f['pageId'],name='Breadcrumbs'),collection=ledger['collection'],variables=variables,nativeLedger=ref(out+'current-native-ledger.json'),build_plan='current-build-plan.json',minimum='token-minimum.json',variable_map='variable-map.csv',binding_map='binding-map.csv',qa=ref('evidence/qa/breadcrumb-pilot-check.json'),distribution='LOCAL_COMPONENTS_NOT_PUBLISHED_LIBRARY',web_implementation='NOT_IMPLEMENTED')
  if family=='breadcrumb':manifest['dependency']=p['dependency'];manifest['dependencyManifest']=ref('consumption/breadcrumb-item/manifest.json')
  write(out+'manifest.json',manifest)
 return counts
if __name__=='__main__':print(json.dumps(materialize()))
