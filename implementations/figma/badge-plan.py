"""Derive Badge's minimal recipe from captured source; never accesses Figma."""
from pathlib import Path
import copy, hashlib, json
ROOT=Path(__file__).resolve().parents[2]
BASE='evidence/badge-pilot/'
MODES=['Contable','Administrativo','Servicios','Personas']
def read(p):return json.loads((ROOT/p).read_text())
def ref(p):return {'path':p,'sha256':hashlib.sha256((ROOT/p).read_bytes()).hexdigest()}
def save(p,v):
 p=ROOT/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def signature(t):return json.dumps({k:t.get(k)for k in ['type','unit','scopes','values']},sort_keys=True)
def analyze():
 old=read(BASE+'history/blueheart.6.0.0.json'if(ROOT/BASE/'history/blueheart.6.0.0.json').exists()else'norms/tokens/blueheart.6.0.0.json');tokens={t['id']:t for t in old['tokens']}
 mapping=read('evidence/figma-application/application-map.json')['variables']
 variables={v['id']:v for v in read(BASE+'source/variables-and-notes.json')['variables']+read(BASE+'source/variables-remaining.json')['variables']}
 semantic={}
 for v in variables.values():
  aliases={x['id']for x in v['values'].values()};assert len(aliases)==1,('Non-invariant source',v['id'])
  primitive=[r['layer']+'.'+r['name']for r in mapping if next(iter(aliases))in r.get('source_ids',[])and r['layer']=='primitive']
  found=[t['id']for t in tokens.values()if t['layer']=='semantic'and t['values']['Value']['alias']in primitive];assert len(found)==1,(v['id'],found)
  semantic[v['id']]=found[0]
 definitions={t['id']:copy.deepcopy(t)for t in old['tokens']if t['id'].startswith('badge.')}
 previous=read('consumption/badge/manifest.json');routes={t['logicalId']:t['figmaName']for t in previous['variables']}
 # The historical manifest is fixed after adoption so regeneration stays deterministic.
 if (ROOT/BASE/'history/badge/manifest.json').exists():routes={t['logicalId']:t['figmaName']for t in read(BASE+'history/badge/manifest.json')['variables']}
 groups={signature(t):t['id']for t in definitions.values()};uses=[];recipes=[]
 def use(rec,field,scope,typ,source_var,path,source,source_index):
  sem=semantic[source_var];t=dict(type=typ,scopes=[scope],values={m:{'alias':sem}for m in MODES})
  sig=signature(t)
  if sig not in groups:
   tid='badge.'+path.replace('/','-');groups[sig]=tid
   ni=next(i for i,n in enumerate(read(source)['rows'][source_index]['nodes'])if n['id']==rec['id'])
   definitions[tid]=dict(id=tid,name='--'+tid.replace('.','-'),layer='component',collection='component',description='Badge: '+path,source=dict(**ref(source),original_id=rec['id'],selector='JSON:/rows/'+str(source_index)+'/nodes/'+str(ni),source_file_key='9zs5RMR8LB5wHjW9Bd59BA'),**t);routes[tid]='badge/'+path
  tid=groups[sig];rec['bindings'][field]=tid;uses.append(dict(sourceNodeId=rec['id'],field=field,tokenId=tid,semantic=sem,sourceVariableId=source_var))
 def alias(n,field):
  b=n['boundVariables'].get(field)
  if b is None and field=='cornerRadius':b=n['boundVariables'].get('topLeftRadius')
  if b is None and field=='strokeWeight':b=n['boundVariables'].get('strokeTopWeight')
  assert b is not None,(n['id'],field)
  return (b[0]if isinstance(b,list)else b)['id']
 for size in ['small','medium','large']:
  source=BASE+'source/'+size+'.json'
  for ri,row in enumerate(read(source)['rows']):
   nodes=copy.deepcopy(row['nodes']);root=nodes[0];typ=row['variant'].split(',')[0].split('=')[1]
   for n in nodes:n['bindings']={}
   for f,scope,kind,path in [('fills','FRAME_FILL','color','color/bg/'+typ),('paddingTop','GAP','number','spacing/compact'),('paddingBottom','GAP','number','spacing/compact'),('paddingLeft','GAP','number','spacing/large'),('paddingRight','GAP','number','spacing/large'),('itemSpacing','GAP','number','spacing/compact'),('cornerRadius','CORNER_RADIUS','number','radius/container')]:use(root,f,scope,kind,alias(root,f),path,source,ri)
   if root['strokes']:
    use(root,'strokes','STROKE_COLOR','color',alias(root,'strokes'),'color/stroke/subtle',source,ri)
    use(root,'strokeWeight','STROKE_FLOAT','number',alias(root,'strokeWeight'),'border/width-regular',source,ri)
   if root['maxHeight']is not None:use(root,'maxHeight','WIDTH_HEIGHT','number',alias(root,'maxHeight'),'size/height-'+size,source,ri)
   label=next(n for n in nodes if n['type']=='TEXT')
   for f,scope,kind,path in [('fills','TEXT_FILL','color','color/text/'+typ),('fontFamily','FONT_FAMILY','string','font/family'),('fontStyle','FONT_STYLE','string','font/label-style'),('fontSize','FONT_SIZE','number','font/size-'+size),('lineHeight','LINE_HEIGHT','number','font/line-height-'+size),('letterSpacing','LETTER_SPACING','number','font/letter-spacing')]:use(label,f,scope,kind,alias(label,f),path,source,ri)
   icons=[n for n in nodes if n['type']=='INSTANCE']
   for n in icons:
    for field in ['width','height']:use(n,field,'WIDTH_HEIGHT','number',alias(n,field),'size/icon-'+('small'if size=='small'else'regular'),source,ri)
    for vector in [x for x in nodes if x['parent']==n['id']]:
     for field in ['fills','strokes']:
      if vector.get(field):use(vector,field,'SHAPE_FILL','color',alias(vector,field),'color/icon/'+typ,source,ri)
   recipes.append(dict(sourceId=root['id'],axes=dict(type=typ,size=size),nodes=nodes))
 # Existing identities are deliberately reused for each exact signature.
 enriched=[dict(t,figmaName=routes[t['id']],web='var('+t['name']+')',themeBehavior='INVARIANT')for t in definitions.values()]
 result=dict(role='DERIVED_RECIPE_NOT_RULES',decision='ADR-025',source=ref(BASE+'source/identity.json'),tokens=enriched,variants=recipes,uses=uses,semanticIds={r['layer']+'.'+r['name']:r['destination_id']for r in mapping if r['layer']=='semantic'},previousCount=12,addedTokens=len(enriched)-12,retiredTokens=[],counts=dict(variants=len(recipes),candidateUses=len(uses),distinctSignatures=len(groups),tokens=len(enriched),redundancies=len(enriched)-len(groups)),themeBehavior='ALL_ROLES_INVARIANT',icon=read(BASE+'source/variables-remaining.json')['icon'],exampleIcons=read(BASE+'source/example-icons.json'))
 assert len(enriched)==len(groups)
 save(BASE+'build-plan.json',result)
 save(BASE+'token-minimum.json',dict(role='DERIVED_MINIMUM_NOT_RULES',tokens=len(enriched),distinctSignatures=len(groups),redundancies=0,candidateUses=len(uses),retained=12,added=len(enriched)-12))
 return result
def validate_recipe(document,plan):
 tokens={t['id']:t for t in document['tokens']};owned={t['id']for t in plan['tokens']};used=set()
 for use in plan['uses']:
  tid=use['tokenId'];used.add(tid)
  if tid not in owned or any(value!={'alias':use['semantic']}for value in tokens[tid]['values'].values()):raise ValueError('Badge source alias mismatch: '+tid)
 if used!=owned:raise ValueError('Badge recipe coverage mismatch')
 for v in plan['variants']:
  label=next(n for n in v['nodes']if n['type']=='TEXT');text=tokens[label['bindings']['fills']]
  for n in v['nodes']:
   if n['type']=='VECTOR':
    for field,id in n['bindings'].items():
     icon=tokens[id]
     if icon['scopes']!=['SHAPE_FILL']or text['scopes']!=['TEXT_FILL']or icon['values']!=text['values']:raise ValueError('Badge icon/text mismatch')
 signatures={signature(tokens[id])for id in owned}
 if len(signatures)!=len(owned):raise ValueError('Badge redundant signature')
 return {'tokens':len(owned),'uses':len(plan['uses']),'variants':len(plan['variants'])}
if __name__=='__main__':print(json.dumps(analyze()['counts']))
