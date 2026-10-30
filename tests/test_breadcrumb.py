"""Breadcrumb additive adoption, sparse source contract and native consumer evidence."""
import copy,hashlib,json,runpy,unittest
from pathlib import Path
from blueheart.workspace import Workspace
ROOT=Path(__file__).resolve().parents[1];BASE='evidence/breadcrumb-pilot/'
def read(p):return json.loads((ROOT/p).read_text())
class BreadcrumbTests(unittest.TestCase):
 def document(self):
  w=Workspace(ROOT);return read(next(e['path']for e in w.catalog['token_sets']if e['current']))
 def test_additive_cut_preserves_every_existing_token_and_foundation(self):
  old={t['id']:t for t in read(BASE+'history/norms/tokens/blueheart.6.1.0.json')['tokens']};new={t['id']:t for t in self.document()['tokens']};self.assertEqual((len(old),len(new)),(493,518));self.assertEqual(set(old)-set(new),set())
  for id,t in old.items():self.assertEqual(t,new[id],id)
  self.assertEqual(len(set(new)-set(old)),25);self.assertTrue(all(id.startswith(('breadcrumb-item.','breadcrumb.'))for id in set(new)-set(old)))
  for e in read(BASE+'history/manifest.json')['entries']:self.assertEqual(hashlib.sha256((ROOT/e['archive']).read_bytes()).hexdigest(),e['sha256'])
 def test_minimum_source_recipe_and_negative_mode_scope_and_matrix(self):
  validate=runpy.run_path(str(ROOT/'consumption/breadcrumb/materialize-consumption.py'))['validate_recipe'];document=self.document()
  for family,expected in [('breadcrumb-item',dict(tokens=20,uses=176,variants=13)),('breadcrumb',dict(tokens=5,uses=65,variants=5))]:
   p=read('consumption/'+family+'/current-build-plan.json');self.assertEqual(validate(document,p),expected)
   bad=copy.deepcopy(document);t=next(t for t in bad['tokens']if t['id']==family+'.color-icon-'+('link-default'if family=='breadcrumb-item'else'back-default'));t['values']['Personas']={'alias':'semantic.neutral-soft'}
   with self.assertRaisesRegex(ValueError,'source alias mismatch'):validate(bad,p)
   bad=copy.deepcopy(document);next(t for t in bad['tokens']if t['id']==family+'.color-icon-'+('link-default'if family=='breadcrumb-item'else'back-default'))['scopes']=['TEXT_FILL']
   with self.assertRaisesRegex(ValueError,'scope/type mismatch'):validate(bad,p)
   bad=copy.deepcopy(p);bad['variants'].append(copy.deepcopy(bad['variants'][0]))
   with self.assertRaisesRegex(ValueError,'matrix mismatch'):validate(document,bad)
 def test_sparse_api_and_theme_classification_not_cartesian(self):
  p=read('consumption/breadcrumb-item/current-build-plan.json');axes=[r['axes']for r in p['variants']];self.assertEqual(len(axes),13);self.assertEqual([a for a in axes if a['current']=='true'],[dict(type='text',current='true',state='default')])
  tokens={t['id']:t for t in self.document()['tokens']};new=[t for t in tokens.values()if t['id'].startswith(('breadcrumb-item.','breadcrumb.'))];self.assertEqual([t['id']for t in new if len({v['alias']for v in t['values'].values()})>1],['breadcrumb-item.color-text-current-default'])
  for role in ['link-default','link-hover','disabled']:
   a=tokens['breadcrumb-item.color-icon-'+role];b=tokens['breadcrumb-item.color-text-'+role];self.assertEqual(a['values'],b['values']);self.assertEqual(a['scopes'],['SHAPE_FILL']);self.assertEqual(b['scopes'],['TEXT_FILL'])
  self.assertNotEqual(tokens['breadcrumb-item.color-icon-separator-default']['values'],tokens['breadcrumb-item.color-text-link-default']['values']);self.assertEqual(tokens['breadcrumb.color-icon-back-default']['values'],tokens['breadcrumb-item.color-text-link-hover']['values'])
 def test_native_bindings_and_collection_counts_are_complete(self):
  q=read(BASE+'native-bindings.json');self.assertEqual(q['status'],'PASS');self.assertFalse(q['errors']);self.assertEqual(len(q['bindings']),241);self.assertTrue(all(r[-1]for r in q['bindings']));self.assertEqual({r['name']:r['count']for r in q['collections']},{'primitive':151,'semantic':112,'component':255});self.assertEqual(len(q['variables']),25)
  for s in q['styles']:self.assertEqual(len(s['boundVariables']),5);self.assertEqual(s['fontSize'],14);self.assertEqual(s['lineHeight']['value'],20)
  self.assertEqual([s['fontName']['style']for s in q['styles']if s['name'].endswith('/current')],['SemiBold'])
 def test_native_instances_back_and_label_focus_growth(self):
  i=read(BASE+'native-item-qa.json');p=read(BASE+'native-parent-qa.json');self.assertEqual(i['counts'],dict(cases=52,focusEdits=8));self.assertEqual(p['counts'],dict(cases=40,nestedEdits=5))
  for d in [i,p]:self.assertEqual(d['status'],'PASS');self.assertFalse(d['issues']);self.assertEqual(len(d['removedNodeIds']),13 if d is i else 5)
  self.assertTrue(all(x['pass']for x in i['cases']+i['focusEdits']+p['cases']+p['edits']));self.assertTrue(all(x['ringWidth']==x['width']+8 for x in i['focusEdits']));self.assertTrue(all(x['after']>x['before']for x in p['edits']))
  for c in p['cases']:self.assertEqual(c['current'],c['items']-1);self.assertEqual(c['labels'][-1],'Póliza P-0458')
  self.assertEqual(read(BASE+'native-closure.json')['temporaryProbes'],0);self.assertEqual(read(BASE+'native-closure.json')['componentCount'],18)
 def test_reverse_audit_has_no_consumers_and_uses_shared_child(self):
  m=read(BASE+'migration-map.json');self.assertEqual(len(m['reverseDependencyAudit']['pages']),9);self.assertEqual(m['reverseDependencyAudit']['previousConsumers'],0);self.assertFalse(m['substitutions']);self.assertFalse(m['retiredTokens']);self.assertFalse(m['deletedExistingNodes']);self.assertEqual(m['directDependencies'][0]['instances'],18);self.assertEqual(len(m['excludedInvisiblePaints']),16)
  w=Workspace(ROOT);c=w.contracts[w.current['BREADCRUMB-001']]['metadata'];self.assertEqual([d for d in c['dependencies']if d['kind']=='contract'],[dict(kind='contract',id='BREADCRUMB-ITEM-001',version='1.0.0',relation='composition')])
 def test_observation_models_are_complete_and_effectively_referenced(self):
  for family,nodes,instances,definitions in [('breadcrumb-item',58,16,2),('breadcrumb',83,36,5)]:
   m=read(BASE+'source/'+family+'-component-contract.yaml');self.assertTrue(m['inspection']['read_only']);self.assertEqual(m['inspection']['status'],'COMPLETE');self.assertEqual(m['inspection']['traversal']['inspected_nodes'],nodes);self.assertEqual(m['inspection']['traversal']['pending_nodes'],0);self.assertEqual(m['dependency_inventory']['components']['total_instances'],instances);self.assertEqual(len(m['dependencies']),definitions);self.assertTrue(all(v['used_by']for v in m['variable_dependencies']));self.assertEqual(m['dependency_inventory']['styles']['total'],0);self.assertEqual(m['interactions']['status'],'UNDEFINED')
 def test_qa_evidence_and_limits_are_integral(self):
  q=read('evidence/qa/breadcrumb-pilot-check.json');self.assertEqual(q['status'],'PASS_FOR_EXECUTED_SCOPE');self.assertEqual(q['independent_review'],'NOT_RUN');self.assertEqual(q['web_implementation'],'NOT_IMPLEMENTED');self.assertEqual(q['source_access']['source_write_operations'],0)
  for r in q['evidence']:self.assertEqual(hashlib.sha256((ROOT/r['path']).read_bytes()).hexdigest(),r['sha256'],r['path'])
  c=read(BASE+'contrast.json');self.assertTrue(all(r['ratio']>=4.5 for r in c['rows']if r['axes']['state']!='disabled'));self.assertTrue(all(r['status']=='INACTIVE_EXEMPT_NOT_AA_CLAIM'for r in c['rows']if r['axes']['state']=='disabled'));self.assertEqual(len([r for r in c['rows']if r['axes']['current']=='true']),4)
 def test_consumption_and_source_derivation_are_deterministic_with_bounded_context(self):
  files=[p for f in ['breadcrumb-item','breadcrumb']for p in (ROOT/'consumption'/f).iterdir()if p.suffix in ['.json','.csv']]+[ROOT/BASE/'build-plan.json'];before={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in files};runpy.run_path(str(ROOT/'implementations/figma/breadcrumb-plan.py'))['analyze']();runpy.run_path(str(ROOT/'consumption/breadcrumb/materialize-consumption.py'))['materialize']();self.assertEqual(before,{str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in files})
  w=Workspace(ROOT)
  for id in ['BREADCRUMB-ITEM-001','BREADCRUMB-001']:
   for mode in ['Contable','Administrativo','Servicios','Personas']:
    c=w.context(id,compact=True,modes={'component':mode});self.assertEqual(c['status'],'PASS');self.assertLessEqual(c['context_bytes'],65536)
