"""Derive icon/text pairings from Blue Heart observations; no source-Figma access."""
from pathlib import Path
import copy,hashlib,json
ROOT=Path(__file__).resolve().parents[2]
BASE='evidence/icon-color-audit/'
def read(p):return json.loads((ROOT/p).read_text())
def ref(p):return dict(path=p,sha256=hashlib.sha256((ROOT/p).read_bytes()).hexdigest())
def save(p,v):(ROOT/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def analyze():
 catalog=read('norms/catalog.json');entry=next(e for e in catalog['token_sets']if e['current']);tokens={t['id']:t for t in read(entry['path'])['tokens']}
 if entry['version']!='5.1.0':return read(BASE+'pairing-plan.json')
 logical={v['id']:'button.'+v['name']for v in read('consumption/button/manifest.json')['componentVariables']}
 for f in ['tab','avatar','input']:logical.update({v:k for k,v in read('consumption/'+f+'/current-native-ledger.json')['variableIds'].items()})
 variables={v['id']:v for v in read(BASE+'before/variables.json')};semantics={v['layer']+'.'+v['name']:v['destination_id']for v in read('evidence/figma-application/application-map.json')['variables']}
 source=dict(**ref('evidence/authorization/icon-color-alignment-request.txt'),original_id='USER-ICON-COLOR-ALIGNMENT',selector='TEXT:line1')
 updated={};new=[]
 for icon,text in [('button.color-button-icon-brand','button.color-button-text-brand'),('button.color-button-icon-brand-hover','button.color-button-text-brand-emphasis'),('tab.color-tab-icon-brand','tab.color-tab-text-brand'),('tab.color-tab-icon-secondary','tab.color-tab-text-secondary')]:
  t=copy.deepcopy(tokens[icon]);t['values']=copy.deepcopy(tokens[text]['values']);t['source']=source;updated[icon]=t
 for id,text,path in [('tab.color-tab-icon-inverse','tab.color-tab-text-inverse','tab/color/icon/inverse'),('tab.color-tab-icon-brand-hover','tab.color-tab-text-brand-hover','tab/color/icon/brand-hover')]:
  t=copy.deepcopy(tokens[text]);t.update(id=id,name='--'+id.replace('.','-'),scopes=['SHAPE_FILL'],description='Tab: icono alineado con Label en todos los temas; '+path,source=source);new.append(dict(t,figmaName=path,web='var('+t['name']+')'))
 secondary=copy.deepcopy(tokens['input.color-icon-tooltip']);secondary.update(id='input.color-icon-secondary',name='--input-color-icon-secondary',description='Input: icono junto al placeholder secundario; mismo vector que el texto.',source=source,values=copy.deepcopy(tokens['input.color-text-secondary']['values']));new.append(dict(secondary,figmaName='input/color/icon/secondary',web='var(--input-color-icon-secondary)'))
 final={**tokens,**updated,**{t['id']:t for t in new}};final.pop('input.color-icon-tooltip')
 rows=[]
 for path in sorted((ROOT/BASE/'before').glob('*.json')):
  if path.name=='variables.json':continue
  data=json.loads(path.read_text());family=path.stem
  if 'rows'not in data:continue
  for variant in data['rows']:
   for icon in variant['icons']:
    if family=='avatar':
     target_variant=next(v for v in data['rows']if v['axes']['type']=='text'and v['axes']['size']==variant['axes']['size']);text=target_variant['texts'][0]
    elif family.startswith('input')and icon['name']!='Question':text=next(t for t in variant['texts']if t['refs'].get('characters','').startswith('Placeholder#'))
    else:text=next(t for t in variant['texts']if t['name']=='Label')
    text_token=logical[text['fills'][0]['variable']];group=family.split('-')[0];candidates=[t for t in final.values()if t['id'].startswith(group+'.')and t['scopes']==['SHAPE_FILL']and t['type']=='color'and t['values']==tokens[text_token]['values']];assert len(candidates)==1,(family,variant['id'],text_token,candidates)
    wanted=candidates[0]['id']
    for vec in icon['vectors']:
     for field in ['fills','strokes']:
      for paint in vec[field]:
       assert paint['type']=='SOLID'and paint['variable'];before=variables[paint['variable']];target=variables[text['fills'][0]['variable']];diff=[m for m in before['values']if before['values'][m]!=target['values'][m]]
       rows.append(dict(family=group,subfamily=family,variantId=variant['id'],axes=variant['axes'],iconId=icon['id'],vectorId=vec['id'],field=field,textId=text['id'],textToken=text_token,oldIconToken=logical[paint['variable']],oldNativeVariable=paint['variable'],targetToken=wanted,differentModesBefore=diff,visibleBefore=icon['visible']))
 plan=dict(role='DERIVED_PAIRING_PLAN_NOT_RULES',decision='ADR-024',source=source,baselineTokenSet=entry,updatedTokens=list(updated.values()),newTokens=new,retiredLogicalTokens=['input.color-icon-tooltip'],reusedNativeIdentity={'input.color-icon-secondary':'VariableID:281:17'},pairs=rows,counts=dict(pairs=len(rows),mismatchedPairs=sum(bool(r['differentModesBefore'])for r in rows),addedNativeVariables=2,retiredNativeVariables=0),expectedMinimum=dict(button=45,tab=41,input=41,avatar=22),semanticIds=semantics)
 save(BASE+'pairing-plan.json',plan);return plan
def apply_input(plan):
 """Project the current adopted pairing onto the historical Input recipe, without rewriting evidence."""
 pairs=read(BASE+'pairing-plan.json')['pairs'];ledger=read('evidence/input-pilot/state.json');built=ledger['empty']['built']+ledger['filled']['built']
 for path in ledger['batches']:built+=read('evidence/input-pilot/'+path)['built']
 by_source={v['sourceId']:v for v in built};wanted={r['iconId']:r['targetToken']for r in pairs if r['family']=='input'}
 for v in plan['variants']:
  paths={n['path']:n['id']for n in by_source[v['id']]['nodes']}
  for n in v['rows']:
   for vector in n.get('vectors',[]):
    for field in vector['bindings']:vector['bindings'][field]=wanted[paths[n['path']]]
 plan['iconColorAlignment']=ref(BASE+'pairing-plan.json');return plan
def apply_input_state(state):
 state=copy.deepcopy(state);state['variableIds']['input.color-icon-secondary']=state['variableIds'].pop('input.color-icon-tooltip');state['variableKeys']['input.color-icon-secondary']=state['variableKeys'].pop('input.color-icon-tooltip');return state
def validate_pairings(document,plan=None):
 tokens={t['id']:t for t in document['tokens']};plan=plan or read(BASE+'pairing-plan.json')
 for pair in plan['pairs']:
  icon,text=tokens[pair['targetToken']],tokens[pair['textToken']]
  if not icon['id'].startswith(pair['family']+'.')or not text['id'].startswith(pair['family']+'.')or icon['scopes']!=['SHAPE_FILL']or text['scopes']!=['TEXT_FILL']or icon['type']!=text['type']or icon['values']!=text['values']:raise ValueError('Icon/text mismatch: '+pair['variantId']+' '+pair['targetToken'])
 return len(plan['pairs'])
def apply_button(plan):
 cat=read('norms/catalog.json');ts=next(e for e in cat['token_sets']if e['current']);tokens={t['id']:t for t in read(ts['path'])['tokens']};native=read('consumption/button/manifest.json')['componentVariables'];names={v['name']:v['figmaName']for v in native}
 for t in plan['tokens']:
  id='button.'+t['name'];current=tokens[id];t['aliases']={m:v['alias'][9:]for m,v in current['values'].items()};t.update(logicalId=id,figmaName=names[t['name']],web='var('+current['name']+')')
 for v in plan['variants']:
  text=tokens['button.'+v['labelBindings']['fills']];candidates=[t for t in tokens.values()if t['id'].startswith('button.')and t['scopes']==['SHAPE_FILL']and t['values']==text['values']];assert len(candidates)==1
  for icon in v['icons']:icon['colorToken']=candidates[0]['id'].split('.',1)[1]
 plan['iconColorAlignment']=ref(BASE+'pairing-plan.json');return plan
def apply_tab(plan):
 cat=read('norms/catalog.json');ts=next(e for e in cat['token_sets']if e['current']);registered={t['id']:t for t in read(ts['path'])['tokens']};pairings=read(BASE+'pairing-plan.json');pairs={tuple(sorted(p['axes'].items())):p for p in pairings['pairs']if p['family']=='tab'}
 for t in pairings['newTokens']:
  if t['id'].startswith('tab.')and not any(x['id']==t['id']for x in plan['tokens']):plan['tokens'].append(dict(registered[t['id']],figmaName=t['figmaName'],web=t['web']))
 for v in plan['variants']:
  wanted=pairs[tuple(sorted(v['axes'].items()))]['targetToken'];shape=v['roles']['iconShape'];plan['nodes'][shape]['bindings']['fills.0']=wanted
  for use in plan['uses']:
   if use['sourceNodeId']==shape and use['field']=='fills.0':use['tokenId']=wanted
 plan['statistics'].update(source_binding_uses=plan['statistics']['binding_uses'],binding_uses=len(plan['uses']),current_owned_nodes=len(plan['nodes']),unique_signatures=len(plan['tokens']),component_variables=len(plan['tokens']),own_property_bindings=len(plan['uses']));plan['authority'].append('ADR-024');plan['iconColorAlignment']=ref(BASE+'pairing-plan.json');return plan
def apply_tab_ledger(state):
 state=copy.deepcopy(state)
 for row in read(BASE+'after/variables-write.json')['rows']:
  if row['logicalId'].startswith('tab.'):state['variableIds'][row['logicalId']]=row['id']
 state['iconColorAlignment']=ref(BASE+'pairing-plan.json');return state
def materialize_tab_maps(plan):
 import csv
 native=read(BASE+'after/native-map.json');before=read(BASE+'history/tab/manifest.json');known={v['id']:v for v in before['variables']};actual={v['id']:v for v in read(BASE+'after/variables-final.json')['rows']};variables=[]
 for t in plan['tokens']:
  old=copy.deepcopy(known.get(t['id'],{}));v=actual.get(native[t['id']]);old.update(id=t['id'],name=t['name'],figmaName=v['name']if v else old['figmaName'],web='var('+t['name']+')',nativeId=native[t['id']],nativeKey=v['key']if v else old['nativeKey'],scope=t['scopes'][0],aliases=t['values']);variables.append(old)
 with(ROOT/'consumption/tab/variable-map.csv').open('w')as stream:
  keys=['logicalTokenId','name','figmaName','web','nativeId','nativeKey','scope','Contable','Administrativo','Servicios','Personas'];writer=csv.DictWriter(stream,fieldnames=keys,lineterminator='\n');writer.writeheader()
  for t in variables:writer.writerow(dict(logicalTokenId=t['id'],**{k:t[k]for k in keys[1:7]},**{m:t['aliases'][m]['alias']for m in keys[7:]}))
 with(ROOT/BASE/'history/tab/binding-map.csv').open()as stream:oldrows=list(csv.DictReader(stream))
 destinations={r['sourceNodeId']:r['destinationNodeId']for r in oldrows};rows=[dict(sourceNodeId=u['sourceNodeId'],destinationNodeId=destinations[u['sourceNodeId']],field=u['field'],tokenId=u['tokenId'],destinationVariableId=native[u['tokenId']])for u in plan['uses']]
 with(ROOT/'consumption/tab/binding-map.csv').open('w')as stream:
  writer=csv.DictWriter(stream,fieldnames=list(rows[0]),lineterminator='\n');writer.writeheader();writer.writerows(rows)
 manifest=read('consumption/tab/manifest.json');manifest['variables']=variables;manifest['recipes']='build-plan.'+plan['version']+'.json';save('consumption/tab/manifest.json',manifest);save('consumption/tab/current-build-plan.json',plan)
 return plan
if __name__=='__main__':print(json.dumps(analyze()['counts']))
