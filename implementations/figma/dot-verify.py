"""Aggregate immutable native observations; never infer Figma QA from core tests."""
from pathlib import Path
import hashlib,json,math
ROOT=Path(__file__).resolve().parents[2]
def read(p):return json.loads((ROOT/p).read_text())
def ref(p):return dict(path=p,sha256=hashlib.sha256((ROOT/p).read_bytes()).hexdigest())
def save(p,d):(ROOT/p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def verify():
 native=read('evidence/dot-pilot/destination/native-qa.json');tab=read('evidence/dot-pilot/destination/migrated-tab.json');avatar=read('evidence/dot-pilot/destination/migrated-avatar.json');retired=read('evidence/dot-pilot/destination/retirement.json');audit=read('evidence/dot-pilot/destination/dependency-audit.json');checks=[]
 def check(name,value):checks.append(dict(id=name,status='PASS'if value else'FAIL'))
 check('dot-64-native-theme-cases',len(native['cases'])==64 and all(r[-1]for r in native['cases'])and not native['errors'])
 check('independent-count-properties-and-growth',len(native['edits'])==6 and all(r['pass']for r in native['edits']))
 check('tab-177-consumers-preserved',len(tab['cases'])==177 and all(r['mainPass']and r['count']==r['expectedCount']and abs(r['width']-r['beforeWidth'])<.01 and abs(r['height']-r['beforeHeight'])<.01 and r['visible']==r['beforeVisible']for r in tab['cases']))
 check('avatar-238-consumers-preserved',len(avatar['cases'])==238 and all(r[13]and abs(r[7]-r[9])<.01 and abs(r[8]-r[10])<.01 and r[11]==r[12]for r in avatar['cases']))
 check('retirement-with-zero-current-references',not audit['legacyReferences']and not retired['legacyInstanceReferences']and len(retired['deletedVariables'])==9)
 check('exact-three-collections', {c['name']:c['count']for c in retired['remainingCollections']}=={'primitive':148,'semantic':109,'component':139})
 for group in ['primitive','semantic','component']:
  d=read('evidence/dot-pilot/destination/registry-'+group+'.json');check('native-registry-'+group,d['status']=='PASS'and not d['errors'])
 consumerBindings=read('evidence/dot-pilot/destination/all-consumer-bindings.json');check('all-503-dot-consumers-use-owned-bindings-and-canonical-style-projections',consumerBindings['status']=='PASS'and consumerBindings['instances']==503 and len(consumerBindings['scaledPreviews'])==11)
 positions=read('evidence/dot-pilot/destination/position-preservation.json');check('all-avatar-presence-positions-and-regenerated-slot-ids-preserved',positions['status']=='PASS'and positions['checked']==238 and len(positions['mappings'])==96)
 styleAudit=read('evidence/dot-pilot/destination/style-alias-audit.json');check('all-styles-and-text-ranges-have-no-retired-aliases',styleAudit['status']=='PASS'and not styleAudit['hits'])
 check('button-has-no-dot-dependency',next(p for p in audit['pages']if p['name']=='Buttons')['dotReferences']==0)
 expected={'79:2':'79:3','79:6':'79:7','79:10':'79:11','79:14':'79:15'};check('tab-four-structurally-preserved-hover-transitions',len(audit['tabReactions'])==4 and all(r['reactions'][0]['trigger']['type']=='ON_HOVER'and r['reactions'][0]['actions'][0]['destinationId']==expected[r['id']]for r in audit['tabReactions']))
 minimum=read('consumption/dot/token-minimum.json');check('nineteen-used-unique-signatures',minimum['tokens']==minimum['distinctSignatures']==19 and all(minimum['nativeUsesByToken'].values()))
 # Resolved source colors, relative luminance and ratios; a local measurement, not a web certification.
 def lum(c):return sum(w*(x/12.92 if x<=.04045 else((x+.055)/1.055)**2.4)for w,x in zip([.2126,.7152,.0722],c))
 contrast={k:(1.05/(lum(v)+.05))for k,v in {'active':[9/255,131/255,0],'alert':[212/255,0,0],'inactive':[100/255,116/255,139/255]}.items()};save('evidence/dot-pilot/contrast.json',dict(role='DERIVED_MEASUREMENT_NOT_CERTIFICATION',foreground='white or white separator',ratios=contrast,scope='Dot source colors only; host semantics, names and web accessibility are consumer responsibilities.'))
 from blueheart.workspace import Workspace
 w=Workspace(ROOT);check('registered-structure-and-minima',w.check()['status']=='PASS')
 refs=[ref('evidence/dot-pilot/destination/'+p+'.json')for p in ['native-qa','migrated-tab','migrated-avatar','retirement','dependency-audit','registry-primitive','registry-semantic','registry-component','style-alias-audit','position-preservation','all-consumer-bindings','scaled-preview-bindings']]
 report=dict(schema_version=1,id='DOT-PILOT-ADR021',status='PASS_FOR_EXECUTED_SCOPE'if all(c['status']=='PASS'for c in checks)else'FAIL',decisions=['ADR-021'],source=dict(fileKey='9zs5RMR8LB5wHjW9Bd59BA',pageId='1133:20620',project='/Users/miguel.leo/Desktop/CONTPAQi-designSystem-Optimizado',access='READ_ONLY'),destination=dict(fileKey='98xEw6sK8FRVNEhopM5SSz',pageId='201:1543',setId='201:1556',qaFrameId=native['frameId']),counts=dict(variants=16,DotTokens=19,retiredPrivateTokens=9,netTokenIncrease=10,variables=396,styles=2,themeCases=64,editedCountCases=6,preservedTabConsumers=177,preservedAvatarConsumers=238,nativeDotBindings=250),checks=checks,evidence=refs,contrast=ref('evidence/dot-pilot/contrast.json'),selectedContracts=[w.entries[w.current[k]]for k in ['DOT-001','AVATAR-001','AVATAR-GROUP-001','TAB-001','TABS-001']],visualReview=dict(status='PASS',files=[ref('evidence/dot-pilot/destination/overview.png'),ref('evidence/dot-pilot/destination/variants.png')]),limits=dict(nativeDotPlayback='NOT_APPLICABLE_NO_REACTIONS',tabPlayback='NOT_RERUN; four stored reactions preserved; previous playback proof remains historical',web='NOT_IMPLEMENTED_OR_CERTIFIED',independentReviewer='NOT_RUN',libraryPublication='LOCAL_ONLY',officialRelease='NOT_PUBLISHED'))
 save('evidence/qa/dot-pilot-check.json',report);return report
if __name__=='__main__':
 import sys
 sys.path.insert(0,str(ROOT));report=verify();print(json.dumps(dict(status=report['status'],checks=len(report['checks']),failures=[c for c in report['checks']if c['status']!='PASS'])));raise SystemExit(report['status']=='FAIL')
