"""Derive minimal Breadcrumb recipes from immutable observations and selected foundations."""
from pathlib import Path
import copy,hashlib,json
ROOT=Path(__file__).resolve().parents[2]
BASE='evidence/breadcrumb-pilot/'
MODES=['Contable','Administrativo','Servicios','Personas']
def read(p):return json.loads((ROOT/p).read_text())
def ref(p):return dict(path=p,sha256=hashlib.sha256((ROOT/p).read_bytes()).hexdigest())
def save(p,v):
 p=ROOT/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def signature(t):return json.dumps({k:t.get(k)for k in ['type','unit','scopes','values']},sort_keys=True)
def analyze():
 c=read(BASE+'history/norms/catalog.json')if(ROOT/BASE/'history/norms/catalog.json').exists()else read('norms/catalog.json');ts=next(e for e in c['token_sets']if e['current']);baseline=BASE+'history/'+ts['path']if(ROOT/BASE/'history'/ts['path']).exists()else ts['path'];tokens={t['id']:t for t in read(baseline)['tokens']};application=read('evidence/figma-application/application-map.json')['variables'];variables={v['id']:v for v in read(BASE+'source/variables-and-notes.json')['variables']}
 primitive={sid:r['layer']+'.'+r['name']for r in application if r['layer']=='primitive'for sid in r['source_ids']}
 semantic={}
 for id,v in variables.items():
  vector={}
  for m in v['collection']['modes']:
   p=primitive[v['values'][m['modeId']]['id']];found=[t['id']for t in tokens.values()if t['layer']=='semantic'and t['values']['Value']['alias']==p];assert len(found)==1,(id,found);vector[m['name']]={'alias':found[0]}
  semantic[id]=vector
 definitions={};groups={'breadcrumb-item':{},'breadcrumb':{}};uses=[];excluded=[];items=[];compositions=[]
 def use(family,n,field,scope,kind,path,source,ri,ni,sem=None):
  original=n.get('boundVariables',{}).get(field)
  if original is None and field=='cornerRadius':original=n['boundVariables'].get('topLeftRadius')
  if original is None and field=='strokeWeight':original=n['boundVariables'].get('strokeTopWeight')
  sourceid=(original[0]if isinstance(original,list)else original)['id']if original else None
  values={m:{'alias':sem}for m in MODES}if sem else semantic[sourceid]
  t=dict(type=kind,scopes=[scope],values=values);sig=signature(t)
  if sig not in groups[family]:
   tid=family+'.'+path.replace('/','-');groups[family][sig]=tid
   route='breadcrumb/'+path
   definitions[tid]=dict(id=tid,name='--'+tid.replace('.','-'),layer='component',collection='component',description='Breadcrumb: '+path,source=dict(**ref(source),original_id=n['id'],selector=f'JSON:/rows/{ri}/nodes/{ni}',source_file_key='9zs5RMR8LB5wHjW9Bd59BA'),figmaName=route,web='var(--'+tid.replace('.','-')+')',themeBehavior='THEMED'if len({v['alias']for v in values.values()})>1 else'INVARIANT',**t)
  tid=groups[family][sig];n['bindings'][field]=tid;uses.append(dict(family=family,sourceNodeId=n['id'],field=field,tokenId=tid,sourceVariableId=sourceid,aliases=values,adaptation='HOME_FOLLOWS_EQUIVALENT_LINK_TEXT'if sem=='semantic.neutral-strong'and family=='breadcrumb-item'and n['type']=='VECTOR'else'CURRENT_STYLE_VARIABLE_BINDING'if sem=='semantic.font-weight-semibold'else None));return tid
 keep=['id','parent','name','type','visible','opacity','width','height','x','y','layoutMode','primaryAxisSizingMode','counterAxisSizingMode','layoutSizingHorizontal','layoutSizingVertical','primaryAxisAlignItems','counterAxisAlignItems','paddingTop','paddingRight','paddingBottom','paddingLeft','itemSpacing','cornerRadius','strokeWeight','strokeAlign','strokesIncludedInLayout','clipsContent','layoutPositioning','constraints','maxHeight','minHeight','fills','strokes','effects','fontName','fontSize','lineHeight','letterSpacing','textAutoResize','textTruncation','maxLines','characters','textDecoration','mainComponent','componentPropertyReferences','properties','isExposedInstance','texts']
 for kind in ['text','icon','overflow']:
  source=BASE+'source/item-'+kind+'.json'
  for ri,row in enumerate(read(source)['rows']):
   raw=copy.deepcopy(row['nodes']);byid={n['id']:n for n in raw}
   for ni,n in enumerate(raw):
    n['bindings']={};f='breadcrumb-item'
    if n['type']=='COMPONENT':
     for p in ['paddingTop','paddingRight','paddingBottom','paddingLeft','itemSpacing']:use(f,n,p,'GAP','number','spacing/item-'+('gap'if p=='itemSpacing'else'none'),source,ri,ni)
    elif n['type']=='TEXT':
     current=row['axes']['current']=='true';state=row['axes']['state'];role='current-default'if current else'link-hover'if state=='hover'else'disabled'if state=='disabled'else'link-default'
     use(f,n,'fills','TEXT_FILL','color','color/text/'+role,source,ri,ni)
     for field,scope,typ,path in [('fontFamily','FONT_FAMILY','string','font/family'),('fontStyle','FONT_STYLE','string','font/'+('current-style'if current else'link-style')),('fontSize','FONT_SIZE','number','font/size'),('lineHeight','LINE_HEIGHT','number','font/line-height'),('letterSpacing','LETTER_SPACING','number','font/letter-spacing')]:use(f,n,field,scope,typ,path,source,ri,ni,sem='semantic.font-weight-semibold'if field=='fontStyle'and current else None)
    elif n['type']=='INSTANCE':
     if n.get('fills')and all(paint.get('visible')is False for paint in n['fills']):excluded.append(dict(sourceNodeId=n['id'],field='fills',reason='Paint invisible del contenedor Phosphor, sin control público ni efecto renderizante; fills vacíos en el destino, sin token ficticio.',source=ref(source)))
     for p in ['width','height']:use(f,n,p,'WIDTH_HEIGHT','number','size/icon',source,ri,ni,sem=None if n.get('boundVariables',{}).get(p)else'semantic.size-lg')
    elif n['type']=='VECTOR':
     owner=byid[n['parent']];state=row['axes']['state'];home=owner['name']=='Icon';sem='semantic.neutral-strong'if home and state in ['default','focus']else None
     path='color/icon/'+('disabled'if state=='disabled'else'link-hover'if home and state=='hover'else'link-default'if home else'separator-default')
     use(f,n,'fills','SHAPE_FILL','color',path,source,ri,ni,sem=sem)
    elif n['name']=='Focus ring':
     use(f,n,'strokes','STROKE_COLOR','color','color/stroke/focus',source,ri,ni);use(f,n,'strokeWeight','STROKE_FLOAT','number','border/focus-width',source,ri,ni);use(f,n,'cornerRadius','CORNER_RADIUS','number','radius/focus',source,ri,ni)
   items.append(dict(sourceId=row['id'],name=row['name'],axes=row['axes'],nodes=[dict(**{k:n[k]for k in keep if k in n},bindings=n['bindings'])for n in raw],source=ref(source)))
 for batch in [1,2]:
  source=BASE+f'source/composition-{batch}.json'
  for ri,row in enumerate(read(source)['rows']):
   raw=copy.deepcopy(row['nodes'])
   for ni,n in enumerate(raw):
    n['bindings']={};f='breadcrumb'
    if n['type']=='COMPONENT'or n['name']=='Items':
     for p in ['paddingTop','paddingRight','paddingBottom','paddingLeft','itemSpacing']:use(f,n,p,'GAP','number','spacing/'+('back-gap'if n['type']=='COMPONENT'else'container-gap')if p=='itemSpacing'else'spacing/container-none',source,ri,ni)
    elif n['name']=='Back':
     for p in ['width','height']:use(f,n,p,'WIDTH_HEIGHT','number','size/back',source,ri,ni)
     excluded.append(dict(sourceNodeId=n['id'],field='fills',reason='Paint visible=false: no renderiza y no forma parte de la API; el contenedor Phosphor conserva fills vacíos, sin literals ni token de fondo ficticio.',source=ref(source)))
    elif n['type']=='VECTOR':use(f,n,'fills','SHAPE_FILL','color','color/icon/back-default',source,ri,ni)
   compositions.append(dict(sourceId=row['id'],name=row['name'],axes=row['axes'],nodes=[dict(**{k:n[k]for k in keep if k in n},bindings=n['bindings'])for n in raw],source=ref(source)))
 definitions=list(definitions.values());expected={'breadcrumb-item':20,'breadcrumb':5}
 assert {f:len(g)for f,g in groups.items()}==expected,groups
 assets={n['mainComponent']['owner']['name']:n['mainComponent']for v in items+compositions for n in v['nodes']if n.get('mainComponent',{}).get('remote')}
 result=dict(role='DERIVED_RECIPE_NOT_RULES',decision='ADR-026',baselineTokenSet=ts,tokens=definitions,items=items,compositions=compositions,uses=uses,excludedUses=excluded,assets=assets,semanticIds={r['layer']+'.'+r['name']:r['destination_id']for r in application if r['layer']=='semantic'},counts=dict(itemVariants=len(items),compositions=len(compositions),tokens=len(definitions),minimumByContract=expected,bindings=len(uses),excludedInvisiblePaints=len(excluded)),focusGeometry=dict(outset=4,separation=2,stroke=2,formula='outset = item gap; outline inner separation = outset - stroke; bounds stretch parent + 2*outset'),theme=dict(current='THEMED_SOURCE_VECTOR',others='INVARIANT'),interaction=dict(nativeReactions='EMPTY_SOURCE',navigation='HOST_RESOLVES_DESTINATIONS',overflowMenu='HOST_REQUIRED_NOT_DEFINED_IN_SOURCE',mobile='HOST_PRESENTATION_RULE_NO_SOURCE_VARIANT'))
 selected=read('norms/catalog.json');contracts=[e for e in selected['contracts']if e['current']and e['id']in ['BREADCRUMB-ITEM-001','BREADCRUMB-001']]
 if contracts:result.update(contracts=contracts,token_set=next(e for e in selected['token_sets']if e['current']))
 save(BASE+'build-plan.json',result);return result
if __name__=='__main__':print(json.dumps(analyze()['counts']))
