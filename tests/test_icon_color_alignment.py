"""Regression gates for adopted icon/text equality; captured native QA is not web certification."""
import copy,hashlib,json,runpy,unittest
from pathlib import Path
from blueheart.workspace import Workspace
ROOT=Path(__file__).resolve().parents[1]
BASE='evidence/icon-color-audit/'
def read(p):return json.loads((ROOT/p).read_text())
class IconColorAlignmentTests(unittest.TestCase):
 def document(self):
  w=Workspace(ROOT);entry=next(e for e in w.catalog['token_sets']if e['current']);return read(entry['path'])
 def test_every_icon_pair_has_exact_full_alias_vector_and_separate_scope(self):
  module=runpy.run_path(str(ROOT/'implementations/figma/icon-color-plan.py'));self.assertEqual(module['validate_pairings'](self.document()),262)
 def test_one_bad_mode_or_text_scope_is_rejected(self):
  validate=runpy.run_path(str(ROOT/'implementations/figma/icon-color-plan.py'))['validate_pairings'];doc=self.document();bad=copy.deepcopy(doc)
  token=next(t for t in bad['tokens']if t['id']=='tab.color-tab-icon-inverse');token['values']['Personas']={'alias':'semantic.neutral-maximum'}
  with self.assertRaisesRegex(ValueError,'Icon/text mismatch'):validate(bad)
  bad=copy.deepcopy(doc);next(t for t in bad['tokens']if t['id']=='input.color-icon-secondary')['scopes']=['TEXT_FILL']
  with self.assertRaisesRegex(ValueError,'Icon/text mismatch'):validate(bad)
 def test_only_needed_icon_tokens_change_and_all_texts_backgrounds_and_foundations_survive(self):
  old={t['id']:t for t in read(BASE+'history/blueheart.5.1.0.json')['tokens']};new={t['id']:t for t in self.document()['tokens']};plan=read(BASE+'pairing-plan.json')
  self.assertEqual(len(new),470);self.assertEqual(set(old)-set(new),{'input.color-icon-tooltip'});self.assertEqual(set(new)-set(old),{t['id']for t in plan['newTokens']})
  changed={t['id']for t in plan['updatedTokens']}
  for id in set(old)&set(new):
   if id not in changed:self.assertEqual(old[id],new[id],id)
  minimum=Workspace(ROOT).check()['component_token_minimum'];self.assertEqual(minimum['BUTTON-001@4.0.1']['component_tokens'],45);self.assertEqual(minimum['TAB-001@3.1.0']['component_tokens'],41);self.assertEqual(minimum['INPUT-001@2.0.0']['component_tokens'],41)
 def test_native_cases_swaps_overrides_and_preservation_are_complete(self):
  q=read('evidence/qa/icon-color-audit-check.json');self.assertEqual(q['status'],'PASS_FOR_EXECUTED_SCOPE');self.assertEqual(q['counts']['nativeColorPairCases'],1032);self.assertEqual(q['independent_review'],'NOT_RUN')
  for e in q['evidence']:self.assertEqual(hashlib.sha256((ROOT/e['path']).read_bytes()).hexdigest(),e['sha256'],e['path'])
  cases=0;pairs=0;empty=0
  for p in (ROOT/BASE/'after').glob('qa-*.json'):
   data=json.loads(p.read_text());self.assertEqual(data['status'],'PASS');self.assertFalse(data['issues']);cases+=len(data['cases'])
   for c in data['cases']:pairs+=len(c['pairs']);empty+=not c['pairs'];self.assertTrue(all(x['pass']for x in c['pairs']))
   for s in data['swaps']:self.assertTrue(all(x['pass']for x in s['rows']))
  self.assertEqual((cases,pairs,empty),(624,1032,60))
  for family in ['button','tab','input']:
   before=read(BASE+'before/'+family+'-preservation.json');after=read(BASE+'after/'+family+'-preservation.json');self.assertEqual(after['status'],'PASS');self.assertEqual(before['rows'],after['rows']);self.assertEqual(before['sets'],after['sets']);self.assertEqual(read(BASE+'after/'+family+'-consumers.json')['status'],'PASS');self.assertTrue(all(r['pass']for r in read(BASE+'after/'+family+'-swap-sizing.json')['rows']))
 def test_input_reuses_native_identity_without_keeping_retired_name(self):
  ledger=read('consumption/input/current-native-ledger.json');self.assertNotIn('input.color-icon-tooltip',ledger['variableIds']);self.assertEqual(ledger['variableIds']['input.color-icon-secondary'],'VariableID:281:17')
  final=read(BASE+'after/variables-final.json');self.assertFalse(final['retiredNames']);self.assertFalse(final['duplicates']);self.assertEqual({r['name']:r['count']for r in final['inventory']},{'primitive':151,'semantic':112,'component':207});self.assertEqual(next(r['name']for r in final['rows']if r['id']=='VariableID:303:3'),'tab/color/icon/primary-hover')
 def test_current_recipes_reproduce_all_adopted_counterparts(self):
  tokens={t['id']:t for t in self.document()['tokens']};button=runpy.run_path(str(ROOT/'consumption/button/materialize-plan.py'))['materialize']()
  for v in button['variants']:
   text=tokens['button.'+v['labelBindings']['fills']]
   for icon in v['icons']:self.assertEqual(tokens['button.'+icon['colorToken']]['values'],text['values'])
  tab=read('consumption/tab/current-build-plan.json')
  for v in tab['variants']:
   a=tab['nodes'][v['roles']['iconShape']]['bindings']['fills.0'];b=tab['nodes'][v['roles']['label']]['bindings']['fills.0'];self.assertEqual(tokens[a]['values'],tokens[b]['values'])
  self.assertEqual(len(tab['tokens']),41)
 def test_protocol_owner_and_history_integrity(self):
  w=Workspace(ROOT)
  for id in ['BH-P02','BH-P03']:
   context=w.context(id);self.assertEqual(context['status'],'PASS');p=next(d for d in context['documents']if d['id']=='BH-P06');self.assertEqual(p['version'],'2.1.0');self.assertIn('mismos aliases',next(r['statement']for r in p['requirements']if r['id']=='REQ-P06-03'))
  for e in read(BASE+'history/manifest.json')['entries']:self.assertEqual(hashlib.sha256((ROOT/e['archive']).read_bytes()).hexdigest(),e['sha256'])
