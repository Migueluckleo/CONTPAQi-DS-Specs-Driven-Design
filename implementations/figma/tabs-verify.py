"""Verify captured native evidence for the scoped Tabs page reconciliation."""
import csv,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];E=ROOT/'evidence/tabs-page-reconciliation'
def read(p):return json.loads(p.read_text())
failures=[];checks=[]
def check(ok,name,**detail):
 checks.append({'control':name,'status':'PASS'if ok else'FAIL',**detail})
 if not ok:failures.append(name)
final={v['id']:v for p in E.glob('variables-*.json') for v in read(p)['records']};baseline={v['id']:v for p in (ROOT/'evidence/tab-pilot/destination').glob('after-variables-*.json')for v in read(p)['variables']};before=read(E/'destination-before.json');names={r['id']:r['after']for r in read(E/'naming-map.json')['changes']};m=read(ROOT/'consumption/tab/manifest.json');gm=read(ROOT/'consumption/tabs/manifest.json');logical={v['nativeId']:v['id']for v in m['variables']}
check(len(final)==348 and len(set(final)-set(baseline))==7,'native-inventory',variables=len(final),added=7)
for vid,old in baseline.items():
 n=final.get(vid);fields={'name':names[logical[vid]] if vid in logical else old['name'],'resolvedType':old['type'],'variableCollectionId':old['collectionId'],'scopes':old['scopes'],'valuesByMode':old['valuesByMode'],'codeSyntax':old['codeSyntax'],'key':old['key']}
 check(n is not None and all(n[k]==v for k,v in fields.items()),'preserved-variable-'+vid)
check(sum(v['scopes']==[]for v in final.values())==251,'foundation-scopes-empty')
sem={v['layer']+'.'+v['name']:v['destination_id']for v in read(ROOT/'evidence/figma-application/application-map.json')['variables']}
for manifest in [m,gm]:
 for v in manifest['variables']:
  n=final[v['nativeId']];check(n['name']==v['figmaName']and n['scopes']==[v['scope']]and n['codeSyntax']['WEB']==v['web'],'native-token-'+v['id'])
  for mode,alias in v['aliases'].items():check(n['valuesByMode'][manifest['collection']['modeIds'][mode]]=={'type':'VARIABLE_ALIAS','id':sem[alias['alias']]},'alias-'+v['id']+'-'+mode)
 for ref in [manifest['contract'],*manifest.get('token_sets',[])]:check(hashlib.sha256((ROOT/ref['path']).read_bytes()).hexdigest()==ref['sha256'],'manifest-hash-'+ref.get('id',ref['path']))
old=read(ROOT/'evidence/tab-pilot/destination/after-preservation.json')
check(all(b==read(E/('button-'+b['id'].replace(':','-')+'.json'))for b in old['button']),'button-five-families-preserved')
bindings=[read(p)for p in E.glob('bindings-current-*.json')];check(sum(x['checked']for x in bindings)==1026 and all(x['status']=='PASS'for x in bindings),'current-1026-bindings')
slot=read(E/'slot-qa.json');check(slot['status']=='PASS'and len(slot['cases'])==6,'slot-2-and-6-three-types');check(read(E/'slot-count-qa.json')['status']=='PASS','editable-count-99plus-focus-growth')
identity=read(E/'final-identity.json');props=identity['groups']['properties'];check(len(props)==2 and props[gm['slotKey']]['slotSettings']['minChildren']==2 and props[gm['slotKey']]['slotSettings']['maxChildren']is None,'single-public-slot-property')
expected={'underline':(265,44),'pill':(277,36),'segmented':(253,36)}
for v in identity['groups']['variants']:
 typ=v['axes']['type'];kids=v['slot']['children'];check((v['width'],v['height'])==expected[typ]and len(kids)==4 and sum(k['properties']['selected']['value']=='true'for k in kids)==1 and all(k['properties']['type']['value']==typ for k in kids),'default-group-'+typ)
 if typ=='underline':check(v['divider']['height']==1 and v['divider']['width']==v['width']and v['divider']['constraints']=={'horizontal':'STRETCH','vertical':'MAX'},'stretching-divider')
gv={v['id']:v['nativeId']for v in gm['variables']}
for v in identity['groups']['variants']:
 typ=v['axes']['type']
 if typ!='underline':check(v['slot']['boundVariables']['itemSpacing']['id']==gv['tabs.spacing-tabs-container'],'group-gap-binding-'+typ)
 if typ=='underline':
  check(v['divider']['fills'][0]['boundVariables']['color']['id']==gv['tabs.color-tabs-divider-default']and v['divider']['boundVariables']['height']['id']==gv['tabs.size-tabs-divider'],'divider-shape-height-bindings')
 if typ=='segmented':
  check(v['fills'][0]['boundVariables']['color']['id']==gv['tabs.color-tabs-bg-segmented-default'],'segmented-frame-fill-binding')
  check(all(v['boundVariables'][k]['id']==gv['tabs.spacing-tabs-container']for k in ['paddingLeft','paddingTop','paddingRight','paddingBottom']),'segmented-four-padding-bindings')
  check(all(v['boundVariables'][k]['id']==gv['tabs.radius-tabs-container']for k in ['topLeftRadius','topRightRadius','bottomLeftRadius','bottomRightRadius']),'segmented-four-radius-bindings')
check({c['name']:c['count']for c in identity['collections']}=={'primitive':145,'semantic':106,'component':47,'tab':45,'tabs':5},'collection-counts')
roots={x['name']:x for x in identity['roots']};check(all((roots[n]['width'],roots[n]['height'])==wh for n,wh in [('Overview',(1920,2374)),('Variants & states',(1920,1506)),('Tabs',(842,936))]),'three-source-page-sections')
# Four existing ON_HOVER transitions are preserved, no unobserved segmented interaction is invented.
check(sum(len(v['reactions'])for v in identity['tab']['variants'])==4,'four-observed-hover-reactions')
def luminance(c):
 vals=[c[k]/12.92 if c[k]<=.04045 else((c[k]+.055)/1.055)**2.4 for k in 'rgb'];return sum(x*w for x,w in zip(vals,[.2126,.7152,.0722]))
contrasts=[]
for t in slot['themes']:
 expected_rgb={'default':(161,70,251),'hover':(198,152,251),'focus':(255,255,255),'disabled':(255,255,255)}[t['state']];check(tuple(round(t['background'][k]*255)for k in 'rgb')==expected_rgb,'fixed-segmented-'+t['mode']+'-'+t['state'])
 if t['state']in['default','hover']:
  a,b=sorted([luminance(t['foreground']),luminance(t['background'])]);contrasts.append({'mode':t['mode'],'state':t['state'],'ratio':round((b+.05)/(a+.05),4),'threshold':4.5,'conformance':'BELOW_THRESHOLD_ACCEPTED_FOR_FIDELITY_ADR_017'})
report={'schema_version':1,'id':'TABS-PAGE-RECONCILIATION-20261027','status':'FAIL'if failures else'PASS_FOR_EXECUTED_SCOPE','decisions':['ADR-016','ADR-017'],'source':{'project':'/Users/miguel.leo/Desktop/CONTPAQi-designSystem-Optimizado','fileKey':'9zs5RMR8LB5wHjW9Bd59BA','pageId':'268:20245','access':'READ_ONLY'},'destination':{'fileKey':'98xEw6sK8FRVNEhopM5SSz','pageId':'78:97','overviewId':'111:461','variantsId':'113:298','mastersId':'111:442','slotQaId':slot['frameId']},'counts':{'native_variables':348,'preserved_foundations':251,'preserved_button_tokens':47,'Tab':45,'Tabs':5,'renamed_native_tokens':17,'native_bindings_checked':1026,'slot_cases':6,'theme_state_cases':16},'checks':checks,'contrast':contrasts,'limits':{'independent_review':'NOT_RUN','web_keyboard_aria':'NOT_IMPLEMENTED_OR_CERTIFIED','official_release':'NOT_PUBLISHED','library_publication':'LOCAL_ONLY','native_playback':'Existing four unchanged hover transitions: prior native playback evidence retained; no new playback execution claimed.','initial_reader':'Initial direct-field reader misread text-range arrays and one lazy hidden descendant; corrected range-aware traversal passed all 1026 bindings.'},'failures':failures}
out=ROOT/'evidence/qa/tabs-page-reconciliation-check.json';out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'status':report['status'],'checks':len(checks),'failures':failures,'counts':report['counts']}));raise SystemExit(bool(failures))
