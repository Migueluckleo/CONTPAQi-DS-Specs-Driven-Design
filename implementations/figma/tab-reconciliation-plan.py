"""Proyección TAB-001 vigente; decisiones en MD/ADR, evidencia fuente inmutable."""
from pathlib import Path
import json,copy,hashlib
root=Path.cwd()
def load(p):return json.loads(Path(p).read_text())
def save(p,d):Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
plan=load('evidence/tab-pilot/build-plan.json');plan['version']='1.1.0';names={x['id']:x['after'] for x in load('evidence/tabs-page-reconciliation/naming-map.json')['changes']}
for t in plan['tokens']:t['figmaName']=names[t['id']]
vars=load('evidence/tab-pilot/source/variables.json')['variables']
for state,sem,vid in [('default','semantic.brand-personas-medium','VariableID:2496:186'),('hover','semantic.brand-personas-soft','VariableID:2496:185')]:
 tid='tab.color-tab-bg-segmented-selected-'+state
 old=copy.deepcopy(next(t for t in plan['tokens'] if t['id']=='tab.color-tab-bg-surface'));old.update(id=tid,name='--color-tab-bg-segmented-selected-'+state,figmaName='tab/color/bg/segmented-selected-'+state,web='var(--color-tab-bg-segmented-selected-'+state+')',description='Segmented seleccionado '+state+': morado fijo independiente del tema, ADR-016/017.');old['values']={m:{'alias':sem} for m in plan['modes']};old['source']['original_id']=vid;old['source']['selector']='JSON:/variables/'+str(next(i for i,v in enumerate(vars) if v['id']==vid));plan['tokens'].append(old)
for n in plan['normalizations'][:6]:
 node=plan['nodes'][n['sourceId']];node['fills']=[{k:v for k,v in f.items() if k!='boundVariables'} for f in n['before']]
 if n['sourceId'] in ['9058:244','9058:249']:tid='tab.color-tab-bg-segmented-selected-'+('default' if n['sourceId']=='9058:244' else 'hover')
 elif n['sourceId'] in ['9058:385','9058:390']:tid='tab.color-tab-text-inverse'
 else:tid='tab.color-tab-icon-primary'
 node['bindings']['fills.0']=tid
 for u in plan['uses']:
  if u['sourceNodeId']==n['sourceId'] and u['field']=='fills.0':u['tokenId']=tid
plan['normalizations']=plan['normalizations'][6:];plan['authority']=['ADR-016','ADR-017'];plan['statistics'].update(unique_signatures=45,component_variables=45,source_fields_normalized=1);catalog=load('norms/catalog.json');token_set=next(e for e in catalog['token_sets'] if e['current'] and e['id']=='BLUEHEART-TOKENS');registered={t['id']:t for t in load(token_set['path'])['tokens']};paths={v['logicalId']:v['figmaName'] for v in load('evidence/collection-consolidation/migration-map.json')['variables']};plan['tokens']=[dict(registered[t['id']],figmaName=paths[t['id']],web=t['web']) for t in plan['tokens']];plan['version']=next(e['version'] for e in catalog['contracts'] if e['current'] and e['id']=='TAB-001');plan['authority'].append('ADR-020');save('consumption/tab/build-plan.2.0.0.json',plan)
