"""Regression gates for a real shared dependency migration, not a second UI implementation."""
import hashlib,json,runpy,unittest
from pathlib import Path
from blueheart.workspace import Workspace
ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads((ROOT/p).read_text())
class SharedLoaderTests(unittest.TestCase):
 def test_public_contract_and_owned_token_minimum(self):
  w=Workspace(ROOT);deps=w.contracts[w.current['BUTTON-001']]['metadata']['dependencies']
  self.assertIn(dict(kind='contract',id='LOADER-001',version='1.0.0',relation='uses'),deps)
  report=w.check()['component_token_minimum'];self.assertEqual(report['BUTTON-001@4.0.1']['component_tokens'],45);self.assertEqual(report['LOADER-001@1.0.0']['component_tokens'],15)
  p=read('consumption/loader/current-build-plan.json');self.assertEqual(len(p['variants']),24);self.assertEqual(len(p['animation']),6)
  for g in p['animation'].values():
   self.assertEqual(len(g['phases']),24);self.assertEqual(g['phases'][-1]['to'],g['phases'][0]['id'])
 def test_retired_colors_have_exact_owned_alias_replacements_and_history(self):
  old={t['id']:t for t in read('evidence/loader-pilot/history/blueheart.4.0.0.json')['tokens']};new={t['id']:t for t in read('evidence/input-pilot/history/blueheart.5.0.0.json')['tokens']};mapping=read('evidence/loader-pilot/migration-map.json')
  self.assertEqual(set(old)-set(new),set(mapping['retired']))
  for tid,r in mapping['replacementTokens'].items():
   self.assertEqual(tuple(old[tid][k]for k in ['type','scopes','values']),tuple(new[r['logicalId']][k]for k in ['type','scopes','values']))
  for tid in set(old)&set(new):self.assertEqual(old[tid],new[tid])
  self.assertEqual({t for t in set(new)-set(old)if not t.startswith('loader.')},{'primitive.size-88','semantic.size-8xl'})
  for e in read('evidence/loader-pilot/history/manifest.json')['contracts']:self.assertEqual(hashlib.sha256((ROOT/e['archive']).read_bytes()).hexdigest(),e['sha256'])
 def test_current_button_recipe_cannot_recreate_private_cycles(self):
  p=runpy.run_path(str(ROOT/'consumption/button/materialize-plan.py'))['materialize']();self.assertEqual(p['version'],'4.0.1');self.assertEqual(len(p['tokens']),45);self.assertNotIn('spinnerFrames',p)
  loading=[v for v in p['variants']if v.get('loader')];self.assertEqual(len(loading),15)
  for v in loading:self.assertEqual(v['loader']['axes']['size'],{'small':'extra-small','medium':'small','large':'medium'}[v['size']])
  script=(ROOT/'implementations/figma/button-builder.js').read_text();self.assertNotIn('DATA.spinnerFrames',script);self.assertIn('recipe.loader.variantId',script)
 def test_native_evidence_and_all_existing_consumers_are_preserved(self):
  q=read('evidence/qa/loader-pilot-check.json');self.assertEqual(q['status'],'PASS_FOR_EXECUTED_SCOPE');self.assertEqual(q['counts']['replacedExistingUses'],31);self.assertEqual(q['counts']['preservedButtonPrincipals'],90)
  native=read('evidence/loader-pilot/destination/native-qa.json');self.assertFalse(native['issues']);self.assertTrue(all(c[-1]for c in native['preserved']));self.assertFalse(read('evidence/loader-pilot/destination/retirement.json')['references']);self.assertFalse(read('evidence/loader-pilot/destination/registry-qa.json')['activeRetired'])
  for e in q['evidence']:self.assertEqual(hashlib.sha256((ROOT/e['path']).read_bytes()).hexdigest(),e['sha256'],e['path'])
  play=read('evidence/loader-pilot/playback/observations.json');self.assertEqual(play['status'],'PASS_PLAYBACK_SAMPLES');self.assertTrue(all(c['animationObserved']for c in play['cases']))
 def test_current_contexts_fit_with_all_requirements(self):
  w=Workspace(ROOT)
  for mode in ['Contable','Administrativo','Servicios','Personas']:
   for identity in ['BUTTON-001','LOADER-001']:
    c=w.context(identity,compact=True,modes={'component':mode});self.assertEqual(c['status'],'PASS');self.assertLessEqual(c['context_bytes'],65536)
    selected=next(d for d in c['documents']if d['id']==identity);self.assertEqual({r['id']for r in selected['requirements']},set(w.contracts[w.current[identity]]['requirements']))
