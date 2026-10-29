"""Derive Input and the authorized Badge subset from immutable observations and selected MD owners."""
from pathlib import Path
import json,hashlib,copy,re
ROOT=Path(__file__).resolve().parents[2]
MODES=['Contable','Administrativo','Servicios','Personas']
def read(p):return json.loads((ROOT/p).read_text())
def ref(p):return dict(path=p,sha256=hashlib.sha256((ROOT/p).read_bytes()).hexdigest())
def save(p,v):
 (ROOT/p).parent.mkdir(parents=True,exist_ok=True);(ROOT/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def observations():
 rows=[]
 for value in ['false','true']:
  for status in ['default','hover','focus','success','error','read-only','disabled']:
   p='evidence/input-pilot/source/'+status+'-'+value+'.json'
   for i,v in enumerate(read(p)):
    v=copy.deepcopy(v);v['source']=dict(**ref(p),original_id=v['id'],selector='JSON:/'+str(i),source_file_key='9zs5RMR8LB5wHjW9Bd59BA');rows.append(v)
 limits={n['id']:n for n in read('evidence/input-pilot/source/text-limits.json')}
 for v in rows:
  for n in v['rows']:
   if n['type']=='TEXT':n.update(limits[n['id']])
 return rows
def derive():
 catalog=read('norms/catalog.json');selected=next(e for e in catalog['token_sets']if e['current']);old=read(selected['path']);tokens={t['id']:t for t in old['tokens']};sourcevars={v['id']:v for v in read('evidence/input-pilot/source/variables.json')};rows=observations()
 primitive_by_source={t['source']['original_id']:t['id']for t in tokens.values()if t['layer']=='primitive'}
 semantic_by_primitive={t['values']['Value']['alias']:t['id']for t in tokens.values()if t['layer']=='semantic'}
 def oldprimitive(id,mode):
  v=sourcevars[id];mid=next((m['modeId']for m in v['collection']['modes']if m['name']==mode),v['collection']['modes'][0]['modeId']);val=v['values'][mid]
  return oldprimitive(val['id'],mode)if isinstance(val,dict)and val.get('type')=='VARIABLE_ALIAS'else id
 def aliases(id):
  return {m:{'alias':semantic_by_primitive[primitive_by_source[oldprimitive(id,m)]]}for m in MODES}
 def fixed(sem):return {m:{'alias':'semantic.'+sem}for m in MODES}
 def number(sem):
  t=tokens['semantic.'+sem];return tokens[t['values']['Value']['alias']]['values']['Value']
 candidates=[];groups={};definitions={};routes={}
 def use(family,node,field,scope,typ,values,name,source,unit=None):
  signature=json.dumps(dict(family=family,type=typ,unit=unit,scope=scope,values=values),sort_keys=True);tid=family+'.'+name.replace('/','-')
  if signature in groups:tid=groups[signature]
  else:
   if tid in definitions:raise ValueError('Name collision '+tid)
   t=dict(id=tid,name='--'+tid.replace('.','-'),layer='component',type=typ,collection='component',scopes=[scope],description=family.capitalize()+': '+name,values=values,source=source)
   if unit:t['unit']=unit
   definitions[tid]=t;groups[signature]=tid;routes[tid]=family+'/'+name
  node.setdefault('bindings',{})[field]=tid;candidates.append(dict(component=family,variant=node.get('variant'),sourceNodeId=node['id'],part=node.get('path',node.get('name')),property=field,token=tid));return tid
 def sourceuse(n,field,id,scope,v):
  vals=aliases(id);sv=sourcevars[id];typ={'FLOAT':'number','COLOR':'color','STRING':'string'}[sv['type']]
  if scope=='FRAME_FILL':name='color/bg/'+('surface'if id=='VariableID:2849:196104'else'read-only-disabled')
  elif scope=='TEXT_FILL':name='color/text/'+{'color/text/primary':'primary','color/text/tertiary':'secondary','color/text/disabled':'disabled','color/feedback/danger/text':'error','color/feedback/positive/text':'success'}[sv['name']]
  elif scope=='STROKE_COLOR':name='color/stroke/'+{'color/border/default':'default','color/border/control-disabled':'default','color/border/control':'value','color/border/strong':'read-only','color/border/hover':'hover','color/feedback/positive/border':'success','color/feedback/danger/border':'error'}[sv['name']]
  elif scope=='SHAPE_FILL':name='color/'+('indicator/focus'if id=='VariableID:2849:196132'else'icon/'+{'color/icon/brand':'tooltip','color/icon/primary':'default','color/icon/disabled':'disabled'}[sv['name']])
  elif scope=='GAP':name='spacing/'+{0:'none',4:'xs',8:'sm',12:'md',16:'lg'}[number(vals['Contable']['alias'][9:])]
  elif scope=='CORNER_RADIUS':name='radius/container'
  elif scope=='STROKE_FLOAT':name='border/width-regular'
  elif scope=='FONT_FAMILY':name='font/family'
  elif scope=='FONT_STYLE':name='font/'+('label-style'if sv['name'].endswith('bold')else'content-style')
  elif scope=='FONT_SIZE':name='font/'+('size'if sv['name'].endswith('/sm')else'helper-size')
  else:raise ValueError((scope,id))
  return use('input',n,field,scope,typ,vals,name,v['source'])
 for v in rows:
  axes=dict(x.strip().split('=')for x in v['name'].split(','));v['axes']=axes
  for n in v['rows']:
   n['variant']=v['name'];n['bindings']={}
   if n['type']=='INSTANCE'and n['name']=='Badge':continue
   for field,b in n.get('b',{}).items():
    if field in ['fills','strokes']:
     if n['type']=='INSTANCE':continue
     for paint in n.get(field,[]):
      if paint.get('visible',True)and paint.get('boundVariables',{}).get('color'):
       scope='STROKE_COLOR'if field=='strokes'else('TEXT_FILL'if n['type']=='TEXT'else'SHAPE_FILL'if n['type']=='RECTANGLE'else'FRAME_FILL');sourceuse(n,field,paint['boundVariables']['color']['id'],scope,v)
     continue
    if field.startswith('stroke')and field.endswith('Weight'):
     if n.get('strokes'):sourceuse(n,'strokeWeight',b['id'],'STROKE_FLOAT',v)
    elif field in ['fontFamily','fontStyle','fontSize']:
     bv=b[0]if isinstance(b,list)else b;sourceuse(n,field,bv['id'],{'fontFamily':'FONT_FAMILY','fontStyle':'FONT_STYLE','fontSize':'FONT_SIZE'}[field],v)
    elif field.startswith('padding')or field=='itemSpacing':sourceuse(n,field,b['id'],'GAP',v)
    elif field.endswith('Radius'):sourceuse(n,field,b['id'],'CORNER_RADIUS',v)
   if n['type']=='TEXT':
    if 'fontStyle'not in n['bindings']:sourceuse(n,'fontStyle','VariableID:2845:160888','FONT_STYLE',v)
    if n['lineHeight']['unit']=='PIXELS':use('input',n,'lineHeight','LINE_HEIGHT','number',fixed('font-line-height-sm'),'font/label-line-height',v['source'])
    key='label-px'if n['letterSpacing']['value']else'normal';use('input',n,'letterSpacing','LETTER_SPACING','number',fixed('font-letter-spacing-'+key),'font/letter-spacing-'+('label'if n['letterSpacing']['value']else'normal'),v['source'],'px'if n['letterSpacing']['value']else None)
   if n['type']=='INSTANCE':
    use('input',n,'width','WIDTH_HEIGHT','number',fixed('size-xl'),'size/icon',v['source']);use('input',n,'height','WIDTH_HEIGHT','number',fixed('size-xl'),'size/icon',v['source'])
    for vec in n.get('vectors',[]):
     vec['path']=n['path']+'/vector';vec['variant']=v['name'];vec['bindings']={};paint=next(p for p in vec['fills']if p.get('visible',True));sourceuse(vec,'fills',paint['boundVariables']['color']['id'],'SHAPE_FILL',v)
   if n['type']in ['FRAME','COMPONENT']:
    for field in ['paddingTop','paddingRight','paddingBottom','paddingLeft']:
     if field not in n['bindings']:
      val=n[field];sem={0:'spacing-none',4:'spacing-xs',8:'spacing-sm',12:'spacing-md',16:'spacing-lg'}[val];use('input',n,field,'GAP','number',fixed(sem),'spacing/'+{0:'none',4:'xs',8:'sm',12:'md',16:'lg'}[val],v['source'])
    if n['name']=='container-placeholder-text'or(n['path']=='root/1/0'and axes['status']=='focus'and n.get('layoutSizingVertical')!='HUG'):
     sem={'large':'size-5xl','medium':'size-4xl','small':'size-3xl'}[axes['size']];assert number(sem)==n['h'];use('input',n,'height','WIDTH_HEIGHT','number',fixed(sem),'size/height-'+axes['size'],v['source'])
   for index,effect in enumerate(n.get('effects',[])):
    color=effect['color'];matches=[t for t in tokens.values()if t['layer']=='primitive'and t['type']=='color'and all(abs(t['values']['Value'][k]-color[k])<1e-6 for k in ['r','g','b','a'])];assert len(matches)==1
    sem=semantic_by_primitive[matches[0]['id']];prefix='effect.'+str(index)+'.';use('input',n,prefix+'color','EFFECT_COLOR','color',fixed(sem[9:]),'color/effect/focus'if index==0 else'color/effect/separation',v['source'])
    for field,value in [('spread',effect['spread']),('radius',effect['radius']),('offsetX',effect['offset']['x']),('offsetY',effect['offset']['y'])]:use('input',n,prefix+field,'EFFECT_FLOAT','number',fixed({0:'spacing-none',2:'stroke-md',4:'spacing-xs'}[value]),{0:'spacing/effect-none',2:'size/focus-spread',4:'size/focus-outer-spread'}[value],v['source'])
  # Template requires one line for the value. Long helper text is allowed to grow, preserving the short baseline.
  v['normalizations']=['helper-height-for-long-messages'];v['value']=axes['value']=='true'
 badge_source='evidence/input-pilot/source/text-and-badge.json';badge=copy.deepcopy(next(n for n in read(badge_source)if n['id']=='8851:26563'));badge['bindings']={};badge['path']='badge';bs=dict(**ref(badge_source),original_id=badge['id'],selector='JSON:/3',source_file_key='9zs5RMR8LB5wHjW9Bd59BA')
 for field,scope,typ,sem,name in [('fills','FRAME_FILL','color','neutral-subtle','color/bg/subtle'),('strokes','STROKE_COLOR','color','neutral-muted','color/stroke/subtle'),('paddingTop','GAP','number','spacing-none','spacing/none'),('paddingBottom','GAP','number','spacing-none','spacing/none'),('paddingLeft','GAP','number','spacing-sm','spacing/inline'),('paddingRight','GAP','number','spacing-sm','spacing/inline'),('cornerRadius','CORNER_RADIUS','number','radius-sm','radius/container'),('strokeWeight','STROKE_FLOAT','number','stroke-xs','border/width-regular')]:use('badge',badge,field,scope,typ,fixed(sem),name,bs)
 label=copy.deepcopy(next(n for n in read(badge_source)if n['id']=='8851:26565'));label['bindings']={};label['path']='badge/label';ls=dict(**ref(badge_source),original_id=label['id'],selector='JSON:/4',source_file_key='9zs5RMR8LB5wHjW9Bd59BA')
 for field,scope,typ,sem,name in [('fills','TEXT_FILL','color','neutral-maximum','color/text/primary'),('fontFamily','FONT_FAMILY','string','font-family-base','font/family'),('fontStyle','FONT_STYLE','string','font-weight-regular','font/label-style'),('fontSize','FONT_SIZE','number','font-size-xs','font/size'),('lineHeight','LINE_HEIGHT','number','font-line-height-sm','font/line-height'),('letterSpacing','LETTER_SPACING','number','font-letter-spacing-normal','font/letter-spacing')]:use('badge',label,field,scope,typ,fixed(sem),name,ls)
 plan=dict(role='DERIVED_RECIPE_NOT_RULES',variants=rows,badge=dict(root=badge,label=label,scope='subtle/small and editable Label only'),tokens=list(definitions.values()),routes=routes,candidates=candidates,groups=dict(input=sum(k.startswith('input.')for k in definitions),badge=sum(k.startswith('badge.')for k in definitions)),primitiveInputCount=len(old['tokens']),sourceApi=ref('evidence/input-pilot/source/api.json'))
 save('evidence/input-pilot/token-analysis.json',plan);return plan
def materialize():
 c=read('norms/catalog.json');ts=next(e for e in c['token_sets']if e['current']);selected=read(ts['path']);analysis=read('evidence/input-pilot/token-analysis.json');app=read('evidence/figma-application/application-map.json');native={v['layer']+'.'+v['name']:v['destination_id']for v in app['variables']}
 for family,identity in [('input','INPUT-001'),('badge','BADGE-001')]:
  entry=next(e for e in c['contracts']if e['current']and e['id']==identity);text=(ROOT/entry['path']).read_text();meta=json.loads(text[4:].split('\n---\n',1)[0]);routes=dict(re.findall(r'^\| ('+family+r'\.[^ ]+) \| ([^ ]+) \|$',text,re.M));ids={d['id']for d in meta['dependencies']if d['kind']=='token'};tokens=[dict(t,figmaName=routes[t['id']],web='var('+t['name']+')',themeBehavior='THEMED'if len({v['alias']for v in t['values'].values()})>1 else'INVARIANT')for t in selected['tokens']if t['id']in ids]
  assert len(tokens)==analysis['groups'][family];plan=dict(role='DERIVED_RECIPE_NOT_RULES',contract=entry,token_set=ts,tokens=tokens,semanticIds={a:native[a]for t in tokens for a in sorted({v['alias']for v in t['values'].values()})if a in native},source=ref('evidence/input-pilot/token-analysis.json'))
  if family=='input':plan.update(variants=analysis['variants'],iconSource=read('evidence/input-pilot/source/phosphor.json'))
  else:plan.update(badge=analysis['badge'])
  save('consumption/'+family+'/current-build-plan.json',plan);signatures={json.dumps({k:t.get(k)for k in ['type','unit','scopes','values']},sort_keys=True)for t in tokens};assert len(signatures)==len(tokens);save('consumption/'+family+'/token-minimum.json',dict(role='DERIVED_MINIMUM_NOT_RULES',tokens=len(tokens),distinctSignatures=len(signatures),redundancies=0,candidateUses=sum(u['component']==family for u in analysis['candidates'])))
 return analysis['groups']
if __name__=='__main__':
 print(json.dumps(dict(groups=materialize()),ensure_ascii=False))
