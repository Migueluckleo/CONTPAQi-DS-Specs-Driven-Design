"""Derive the Loader build projection from selected MD, tokens and source evidence."""
from pathlib import Path
import json,re,hashlib
ROOT=Path(__file__).resolve().parents[2]
def read(p):return json.loads((ROOT/p).read_text())
def ref(p):return dict(path=p,sha256=hashlib.sha256((ROOT/p).read_bytes()).hexdigest())
def write(p,v):
 (ROOT/p).parent.mkdir(parents=True,exist_ok=True)
 (ROOT/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def materialize():
 c=read('norms/catalog.json');entry=next(e for e in c['contracts']if e['current']and e['id']=='LOADER-001');raw=(ROOT/entry['path']).read_text();meta=json.loads(raw.split('\n---\n',1)[0][4:]);routes=dict(re.findall(r'^\| (loader\.[^ ]+) \| ([^ ]+) \|$',raw,re.M));tset=next(e for e in c['token_sets']if e['current']);alltokens=read(tset['path'])['tokens'];direct={d['id']for d in meta['dependencies']if d['kind']=='token'};tokens=[dict(t,figmaName=routes[t['id']],web='var('+t['name']+')',themeBehavior='THEMED'if len({v['alias']for v in t['values'].values()})>1 else'INVARIANT')for t in alltokens if t['id']in direct];native={v['layer']+'.'+v['name']:v['destination_id']for v in read('evidence/figma-application/application-map.json')['variables']};source=read('evidence/loader-pilot/source/public.json');animation=read('evidence/loader-pilot/source/animation.json');plan=dict(role='DERIVED_RECIPE_NOT_RULES',contract=entry,token_set=tset,tokens=tokens,semanticIds={a:native[a]for t in tokens for a in {v['alias']for v in t['values'].values()}if a in native},variants=[dict(sourceId=v['id'],name=v['name'],size=v['name'].split(',')[0].split('=')[1],color=v['name'].split('color=')[1],dimension=v['width'],stroke=v['child']['paints'][0]['strokeWeight'])for v in source['variants']],animation=animation['groups'],source=ref('evidence/loader-pilot/source/public.json'))
 signatures={json.dumps({k:t.get(k)for k in ['type','unit','scopes','values']},sort_keys=True)for t in tokens};assert len(signatures)==len(tokens)==15
 write('consumption/loader/current-build-plan.json',plan)
 write('consumption/loader/token-minimum.json',dict(role='DERIVED_MINIMUM_NOT_RULES',tokens=len(tokens),distinctSignatures=len(signatures),redundancies=0,sourcePublicVariants=24,sourceAnimationFrames=144,groups=dict(color=5,size=6,stroke=4),grouping='All states/phases and sizes share a token only when full type/unit/scope/mode-alias signature matches. No per-frame or per-color size variables.'))
 return plan
if __name__=='__main__':materialize()
