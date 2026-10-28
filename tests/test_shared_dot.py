"""The current dependency graph and recorded native migration must remain traceable."""
import hashlib,json,unittest
from pathlib import Path
from blueheart.workspace import Workspace
ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads((ROOT/p).read_text())
class SharedDotTests(unittest.TestCase):
 def test_direct_and_transitive_dependencies_are_pinned(self):
  w=Workspace(ROOT)
  for identity,child,version in [('AVATAR-001','DOT-001','1.0.0'),('TAB-001','DOT-001','1.0.0'),('AVATAR-GROUP-001','AVATAR-001','3.0.0'),('TABS-001','TAB-001','3.0.0')]:
   deps=w.contracts[w.current[identity]]['metadata']['dependencies'];self.assertTrue(any(d['kind']=='contract'and d['id']==child and d['version']==version for d in deps))
  self.assertFalse(any(d['id']=='DOT-001'for d in w.contracts[w.current['BUTTON-001']]['metadata']['dependencies']))
 def test_retired_tokens_have_equivalent_owned_replacements(self):
  current={t['id']:t for t in read('norms/tokens/blueheart.4.0.0.json')['tokens']};old={t['id']:t for t in read('evidence/dot-pilot/history/blueheart.3.0.0.json')['tokens']};mapping=read('evidence/dot-pilot/migration-map.json')
  self.assertEqual(set(old)-set(current),set(mapping['replacementTokens']));self.assertEqual(len(mapping['replacementTokens']),9)
  for tid,entry in mapping['replacementTokens'].items():
   a=old[tid];b=current[entry['logicalId']]
   self.assertEqual((a['type'],a['scopes'],a['values']),(b['type'],b['scopes'],b['values']))
  for tid in set(old)&set(current):self.assertEqual(old[tid],current[tid])
 def test_minimum_is_used_and_independent_of_themes(self):
  p=read('consumption/dot/current-build-plan.json');minimum=read('consumption/dot/token-minimum.json');self.assertEqual(len(p['tokens']),19);self.assertEqual(minimum['tokens'],minimum['distinctSignatures']);self.assertTrue(all(minimum['nativeUsesByToken'].values()))
  for t in p['tokens']:self.assertEqual(len({v['alias']for v in t['values'].values()}),1)
 def test_future_component_plan_requires_reverse_audit(self):
  w=Workspace(ROOT);q=w.contracts[w.current['BH-P01']]['metadata']['requirements'];self.assertEqual(next(q for q in q if q['id']=='REQ-P01-07')['force'],'MUST')
  for change in ['contract','token','adapter']:self.assertIn('component-reverse-dependency-reuse',w.qa_plan(change,['norms/components/dot.1.0.0.md'])['required_gates'])
 def test_recorded_native_cases_preserve_all_existing_consumers(self):
  report=read('evidence/qa/dot-pilot-check.json');self.assertEqual(report['status'],'PASS_FOR_EXECUTED_SCOPE');self.assertEqual(report['counts']['preservedTabConsumers']+report['counts']['preservedAvatarConsumers'],415)
  for r in report['evidence']:self.assertEqual(hashlib.sha256((ROOT/r['path']).read_bytes()).hexdigest(),r['sha256'])
  self.assertFalse(read('evidence/dot-pilot/destination/dependency-audit.json')['legacyReferences'])
 def test_current_builders_do_not_recreate_retired_helpers(self):
  for name in ['tab-builder.js','avatar-builder.js']:
   s=(ROOT/'implementations/figma'/name).read_text();self.assertNotIn("name:'__Avatar/Presence'",s);self.assertNotIn("count.name='__Tab/Count'",s);self.assertIn('DATA.dot',s)

 def test_current_component_contexts_fit_without_raising_budget(self):
  w=Workspace(ROOT)
  for identity in ['BUTTON-001','DOT-001','TAB-001','TABS-001','AVATAR-001','AVATAR-GROUP-001']:
   result=w.context(identity,compact=True,modes={'component':'Contable'})
   self.assertEqual(result['status'],'PASS',identity)
   self.assertLessEqual(result['context_bytes'],w.policy['default_context_bytes'])
