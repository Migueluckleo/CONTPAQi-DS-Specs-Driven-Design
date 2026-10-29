"""Source-fidelity and shared dependency regression gates for Input's authorized scope."""
import hashlib,json,runpy,unittest
from pathlib import Path
from blueheart.workspace import Workspace
ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads((ROOT/p).read_text())
class SharedInputTests(unittest.TestCase):
 def test_additive_cut_preserves_every_existing_token(self):
  old={t['id']:t for t in read('evidence/input-pilot/history/blueheart.5.0.0.json')['tokens']};w=Workspace(ROOT);entry=next(e for e in w.catalog['token_sets']if e['current']);new={t['id']:t for t in read(entry['path'])['tokens']}
  self.assertEqual(len(old),411);self.assertEqual(len(new),468)
  for id,t in old.items():self.assertEqual(new[id],t,id)
  extra=set(new)-set(old);self.assertEqual(len([id for id in extra if id.startswith('input.')]),41);self.assertEqual(len([id for id in extra if id.startswith('badge.')]),12)
  self.assertEqual(extra-{id for id in extra if id.startswith(('input.','badge.'))},{'primitive.font-letter-spacing-label-px','semantic.font-letter-spacing-label-px','primitive.neutral-50','semantic.neutral-minimum'})
 def test_all_effect_layers_and_percent_tracking_are_preserved(self):
  p=read('consumption/input/current-build-plan.json');self.assertEqual(len(p['variants']),42);effects=[e for v in p['variants']for n in v['rows']for e in n.get('effects',[])];self.assertEqual(len(effects),11)
  double=[(v,n)for v in p['variants']for n in v['rows']if len(n.get('effects',[]))==2];self.assertEqual({(v['axes']['size'],v['axes']['value'])for v,n in double},{('medium','false'),('small','false')})
  for v,n in double:self.assertEqual(n['bindings']['effect.0.spread'],'input.size-focus-outer-spread');self.assertEqual(n['bindings']['effect.1.color'],'input.color-effect-separation')
  registry={t['id']:t for t in read('norms/tokens/blueheart.5.1.0.json')['tokens']};value=registry['primitive.font-letter-spacing-label-px']['values']['Value'];self.assertAlmostEqual(value,.10000000149011612*14/100,places=12)
  self.assertEqual(registry['input.font-letter-spacing-normal']['values']['Contable']['alias'],'semantic.font-letter-spacing-normal')
  for v in p['variants']:
   for n in v['rows']:
    if n.get('layoutSizingVertical')=='HUG':self.assertNotIn('height',n['bindings'])
    if n['type']=='TEXT':self.assertEqual(n['letterSpacing']['unit'],'PERCENT')
 def test_minimum_covers_real_consumers_and_one_shared_badge(self):
  w=Workspace(ROOT);report=w.check()['component_token_minimum'];self.assertEqual(report['INPUT-001@1.0.0']['component_tokens'],41);self.assertEqual(report['BADGE-001@1.0.0']['component_tokens'],12)
  p=read('consumption/input/current-build-plan.json');used=set()
  for v in p['variants']:
   for n in v['rows']:
    used.update(n['bindings'].values())
    for vector in n.get('vectors',[]):used.update(vector['bindings'].values())
  self.assertEqual(used,{t['id']for t in p['tokens']});s=read('consumption/input/current-native-ledger.json');self.assertEqual([len(x['variants'])for x in s['sets']],[21,21]);self.assertEqual(len(s['variants']),42)
  b=read('consumption/badge/current-native-ledger.json');self.assertEqual(b['variantId'],'282:2');self.assertNotIn('Icon',b)
  for batch in read('evidence/input-pilot/destination/native-matrix.json')['batches']:self.assertEqual(batch['counts']['badges'],6)
 def test_native_checks_and_evidence_are_honest_and_integral(self):
  q=read('evidence/qa/input-pilot-check.json');self.assertEqual(q['status'],'PASS_FOR_EXECUTED_SCOPE');self.assertEqual(q['independent_review'],'NOT_RUN');self.assertEqual(q['web_implementation'],'NOT_IMPLEMENTED')
  for e in q['evidence']:self.assertEqual(hashlib.sha256((ROOT/e['path']).read_bytes()).hexdigest(),e['sha256'],e['path'])
  for name in ['native-matrix','showcase-and-properties','registry-qa','reverse-after','icon-swap']:self.assertEqual(read('evidence/input-pilot/destination/'+name+'.json')['status'],'PASS')
  self.assertLess(read('evidence/input-pilot/destination/contrast.json')['border_default'],3)
  reverse=read('evidence/input-pilot/destination/reverse-after.json');self.assertFalse(reverse['substitutions']);tabs=next(r for r in reverse['rows']if r['name']=='Tabs');self.assertEqual(tabs['namedBadgeCount'],177);self.assertEqual(tabs['namedBadgeMains'],['201:1558'])
 def test_contexts_and_regeneration_are_bounded_and_deterministic(self):
  w=Workspace(ROOT)
  for mode in ['Contable','Administrativo','Servicios','Personas']:
   for id in ['INPUT-001','BADGE-001']:
    c=w.context(id,compact=True,modes={'component':mode});self.assertEqual(c['status'],'PASS');self.assertLessEqual(c['context_bytes'],65536)
  paths=[ROOT/'consumption'/f/n for f in ['input','badge']for n in ['current-build-plan.json','manifest.json','variable-map.csv','binding-map.csv','current-native-ledger.json']];before={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths};runpy.run_path(str(ROOT/'consumption/input/materialize-consumption.py'))['materialize']();self.assertEqual(before,{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
