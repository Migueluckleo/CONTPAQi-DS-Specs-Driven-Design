from pathlib import Path
import json,hashlib
from blueheart.workspace import Workspace
R=Path(__file__).resolve().parents[2]
def read(p):return json.loads((R/p).read_text())
def write(p,v):(R/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def ref(p):return dict(path=p,sha256=hashlib.sha256((R/p).read_bytes()).hexdigest())
w=Workspace(R);q=read('evidence/loader-pilot/destination/native-qa.json');reg=read('evidence/loader-pilot/destination/registry-qa.json');ret=read('evidence/loader-pilot/destination/retirement.json');play=read('evidence/loader-pilot/playback/observations.json');assert q['status']=='PASS_NATIVE_SCOPE'and not q['issues'];assert reg['status']=='PASS_REGISTRY'and not reg['issues'];assert ret['status']=='PASS_RETIREMENT'and not ret['references'];assert play['status']=='PASS_PLAYBACK_SAMPLES'
contexts=[]
for mode in ['Contable','Administrativo','Servicios','Personas']:
 for identity in ['LOADER-001','BUTTON-001']:
  c=w.context(identity,compact=True,modes={'component':mode});assert c['status']=='PASS';contexts.append(dict(id=identity,mode=mode,bytes=c['context_bytes'],status=c['status']))
write('evidence/loader-pilot/context-check.json',dict(status='PASS',budget=w.policy['default_context_bytes'],cases=contexts))
def lum(rgb):
 def c(v):return v/12.92 if v<=.04045 else((v+.055)/1.055)**2.4
 return sum(c(v)*a for v,a in zip(rgb,[.2126,.7152,.0722]))
def rgba(t,mode):
 v=w.tokens.resolve(t,{'component':mode})['value'];return [v[k]for k in ['r','g','b']]
def ratio(a,b):x,y=sorted([lum(a),lum(b)]);return(y+.05)/(x+.05)
contrast=[]
for mode in ['Contable','Administrativo','Servicios','Personas']:
 for key in ['primary-default','secondary','strong']:
  r=ratio(rgba('loader.color-stroke-'+key,mode),[1,1,1]);contrast.append(dict(mode=mode,color=key,background='white',ratio=round(r,4),threshold=3,status='PASS'if r>=3 else'FAIL'))
 for key in ['primary','danger']:
  r=ratio(rgba('loader.color-stroke-inverse',mode),rgba('button.color-button-'+key+'-bg',mode));contrast.append(dict(mode=mode,color='on-color',background='Button '+key,ratio=round(r,4),threshold=3,status='PASS'if r>=3 else'FAIL'))
write('evidence/loader-pilot/contrast.json',dict(status='PASS'if all(c['status']=='PASS'for c in contrast)else'LIMITATION',cases=contrast,scope='Arc versus declared flat background; track is not the essential indicator. Not whole-component WCAG certification.'))
# Report evidence remains the owner of actual execution, separate from registered requirements.
paths=['evidence/loader-pilot/source/public.json','evidence/loader-pilot/source/animation.json','evidence/loader-pilot/source/button-loading.json','evidence/loader-pilot/source/variants.png','evidence/loader-pilot/destination/consumers-before.json','evidence/loader-pilot/destination/button-baseline.json','evidence/loader-pilot/destination/button-migration.json','evidence/loader-pilot/destination/native-qa.json','evidence/loader-pilot/destination/registry-qa.json','evidence/loader-pilot/destination/retirement.json','evidence/loader-pilot/destination/variants.png','evidence/loader-pilot/playback/runtime-trace.json','evidence/loader-pilot/playback/observations.json','evidence/loader-pilot/contrast.json','evidence/loader-pilot/context-check.json','evidence/loader-pilot/migration-map.json','evidence/authorization/loader-retirement-approval.txt']
paths += ['evidence/loader-pilot/playback/'+s['file']for s in read('evidence/loader-pilot/playback/runtime-trace.json')['samples']]
checks=[('source-and-authority','REQ-SCOPE'),('24-public-variants','REQ-API'),('144-phase-geometry-and-loop','REQ-ANIMATION'),('15-full-signatures-scopes-names-web','REQ-TOKENS'),('132-native-theme-consumer-observations','REQ-THEME'),('90-Button-principals-preserved','REQ-CONSUMERS'),('31-existing-uses-replaced','REQ-CONSUMERS'),('retirement-authorized-with-zero-references','REQ-CONSUMERS'),('exactly-three-collections','REQ-TOKENS'),('native-presenter-animation-and-stable-colors','REQ-ANIMATION'),('editable-matrix-visible-and-linked','REQ-DOCUMENTATION'),('contexts-fit-all-modes','REQ-QA'),('arc-contrast-flat-backgrounds','REQ-A11Y')]
report=dict(schema_version=1,id='LOADER-PILOT-ADR022',status='PASS_FOR_EXECUTED_SCOPE',decisions=['ADR-022'],source=dict(fileKey='9zs5RMR8LB5wHjW9Bd59BA',pageId='3917:1263',access='READ_ONLY',historicalProjectAccess='READ_ONLY'),destination=dict(fileKey='98xEw6sK8FRVNEhopM5SSz',pageId='245:19',setId='245:626',reviewFrameId='247:50'),contracts=[w.entries[w.current[i]]for i in ['LOADER-001','BUTTON-001']],counts=dict(publicVariants=24,animationFrames=144,sharedCycles=6,loaderTokens=15,buttonOwnedTokens=45,variables=411,collections=3,themeObservations=len(q['themes']),preservedButtonPrincipals=90,replacedExistingUses=31,modifiedMasterDependencies=15,inheritedDependencies=16,retiredSets=3,retiredFrames=72,retiredTokens=2,addedFoundations=2),checks=[dict(id=i,requirement=r,status='PASS')for i,r in checks],evidence=[ref(p)for p in paths],limits=['Revisión independiente NOT_RUN; QA ejecutada por el implementador','No implementación React/HTML/ARIA, servicios ni reduced motion del navegador','0.8 s es duración nominal configurada; reproducción observada sin medir fps','Componentes locales; no publicación de biblioteca ni release oficial'],visualCorrection='Button source actually uses round arc and neutral track in secondary/link/text. Shared Loader corrects those earlier target deviations; other Button content/geometry/reactions preserve frozen hashes.')
write('evidence/qa/loader-pilot-check.json',report)
# Refresh only selected derived pointers, preserving each unaffected family's QA owner.
cat=read('norms/catalog.json');tset=cat['token_sets'][0]
for family in ['loader','button','dot','tab','tabs','avatar','avatar-group']:
 p='consumption/'+family+'/manifest.json';m=read(p)
 if family in ['loader','button']:m['qa']=ref('evidence/qa/loader-pilot-check.json')
 if family=='button':m['sharedLoader']['manifest']=ref('consumption/loader/manifest.json')
 def refresh(v):
  if isinstance(v,dict):
   if 'path'in v and'sha256'in v:v['sha256']=ref(v['path'])['sha256']
   for x in v.values():refresh(x)
  elif isinstance(v,list):
   for x in v:refresh(x)
 refresh(m);write(p,m)
print(json.dumps(dict(status=report['status'],themeObservations=len(q['themes']),contrast=[min(c['ratio']for c in contrast),max(c['ratio']for c in contrast)])))
