"""Badge family, source fidelity, compatible dependency upgrade and native evidence."""
import copy,hashlib,json,runpy,unittest
from pathlib import Path
from blueheart.workspace import Workspace
ROOT=Path(__file__).resolve().parents[1]
BASE='evidence/badge-pilot/'
def read(p):return json.loads((ROOT/p).read_text())
class FullBadgeTests(unittest.TestCase):
 def document(self):
  w=Workspace(ROOT);e=next(e for e in w.catalog['token_sets']if e['current']);return read(e['path'])
 def test_additive_cut_preserves_all_470_tokens_and_twelve_native_identities(self):
  old={t['id']:t for t in read(BASE+'history/blueheart.6.0.0.json')['tokens']};new={t['id']:t for t in self.document()['tokens']};self.assertEqual(len(new),493)
  for id,t in old.items():self.assertEqual(t,new[id],id)
  self.assertEqual(len(set(new)-set(old)),23);self.assertTrue(all(id.startswith('badge.')for id in set(new)-set(old)))
  m=read(BASE+'migration-map.json');self.assertTrue(all(v['identityPreserved']for v in m['variables']));self.assertEqual(len(m['variables']),12);self.assertFalse(m['retiredVariables']);self.assertFalse(m['deletedNodes'])
 def test_recipe_covers_source_and_rejects_one_wrong_mode_or_scope(self):
  module=runpy.run_path(str(ROOT/'implementations/figma/badge-plan.py'));p=read('consumption/badge/current-build-plan.json');document=self.document();self.assertEqual(module['validate_recipe'](document,p),dict(tokens=35,uses=360,variants=18))
  bad=copy.deepcopy(document);next(t for t in bad['tokens']if t['id']=='badge.color-icon-warning')['values']['Personas']={'alias':'semantic.danger-default'}
  with self.assertRaisesRegex(ValueError,'Badge source alias mismatch'):module['validate_recipe'](bad,p)
  bad=copy.deepcopy(document);next(t for t in bad['tokens']if t['id']=='badge.color-icon-warning')['scopes']=['TEXT_FILL']
  with self.assertRaisesRegex(ValueError,'Badge icon/text mismatch'):module['validate_recipe'](bad,p)
 def test_no_temporal_scope_or_unrequested_states_remain_selected(self):
  w=Workspace(ROOT);m=w.check()['component_token_minimum'];self.assertEqual(m['BADGE-001@1.1.0']['distinct_signatures'],35)
  p=read('consumption/badge/current-build-plan.json');self.assertEqual({(v['axes']['type'],v['axes']['size'])for v in p['variants']},{(t,s)for t in ['neutral','subtle','info','success','warning','error']for s in ['small','medium','large']})
  self.assertTrue(all(set(v['axes'])=={'type','size'}for v in p['variants']));self.assertEqual(read(BASE+'after/reverse-after.json')['sets'],[dict(id='282:3',name='Badge',variants=18)])
  ledger=read('consumption/badge/current-native-ledger.json');self.assertEqual(ledger['variantId'],'282:2');self.assertEqual(ledger['labelProperty'],'Label#282:0');self.assertEqual(read(BASE+'after/reverse-after.json')['defaultVariant']['id'],'282:2')
 def test_native_matrix_swaps_consumers_and_limits_are_integral(self):
  q=read('evidence/qa/badge-pilot-check.json');self.assertEqual(q['status'],'PASS_FOR_EXECUTED_SCOPE');self.assertEqual(q['independent_review'],'NOT_RUN');self.assertEqual(q['web_implementation'],'NOT_IMPLEMENTED')
  for e in q['evidence']:self.assertEqual(hashlib.sha256((ROOT/e['path']).read_bytes()).hexdigest(),e['sha256'],e['path'])
  cases=swaps=pairs=0
  for type in ['neutral','subtle','info','success','warning','error']:
   d=read(BASE+'after/qa-'+type+'.json');self.assertEqual(d['status'],'PASS');self.assertFalse(d['issues']);self.assertTrue(all(x['pass']for x in d['cases']+d['swaps']));cases+=d['counts']['cases'];swaps+=d['counts']['swaps'];pairs+=d['counts']['colorPairs']
  self.assertEqual((cases,swaps,pairs),(288,216,1008))
  for i in [1,2,3]:self.assertEqual(read(BASE+'after/input-instances-'+str(i)+'.json')['counts'],dict(cases=56,labelEdits=168))
  d=read(BASE+'after/input-preservation.json');self.assertEqual(d['checked'],113);self.assertFalse(d['issues']);self.assertTrue(all(r['pass']for r in d['rows']))
  self.assertEqual(read(BASE+'after/master-bindings.json')['bindingUses'],360)
  warning=next(r for r in read(BASE+'after/contrast.json')['rows']if r['type']=='warning');self.assertLess(warning['ratio'],4.5);self.assertEqual(warning['exception'],'USER_APPROVED_SOURCE_FIDELITY')
 def test_observation_model_is_read_only_complete_and_every_variable_is_used(self):
  model=read(BASE+'source/component-contract.yaml');self.assertTrue(model['inspection']['read_only']);self.assertEqual(model['inspection']['status'],'COMPLETE');self.assertEqual(model['inspection']['traversal']['pending_nodes'],0);self.assertEqual(model['dependency_inventory']['components']['total_instances'],36);self.assertEqual(len(model['variable_dependencies']),35);self.assertTrue(all(v['used_by']for v in model['variable_dependencies']));self.assertEqual(model['dependency_inventory']['styles']['total'],0)
  for e in read(BASE+'history/manifest.json')['entries']:self.assertEqual(hashlib.sha256((ROOT/e['archive']).read_bytes()).hexdigest(),e['sha256'])
 def test_consumption_is_deterministic_and_contexts_are_bounded_in_every_mode(self):
  w=Workspace(ROOT)
  for mode in ['Contable','Administrativo','Servicios','Personas']:
   for id in ['INPUT-001','BADGE-001']:
    c=w.context(id,compact=True,modes={'component':mode});self.assertEqual(c['status'],'PASS',c);self.assertLessEqual(c['context_bytes'],65536)
  files=[ROOT/'consumption'/f/n for f in ['input','badge']for n in ['current-build-plan.json','current-native-ledger.json','manifest.json','variable-map.csv','binding-map.csv','token-minimum.json']];before={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in files};runpy.run_path(str(ROOT/'consumption/input/materialize-consumption.py'))['materialize']();self.assertEqual(before,{str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in files})
