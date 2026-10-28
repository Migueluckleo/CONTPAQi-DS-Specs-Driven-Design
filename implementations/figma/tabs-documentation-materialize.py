"""Prepare bounded arguments from immutable source recipes; no Figma/network write.
Run from workspace root. Review ledger before invoking generated operations.
"""
from pathlib import Path
import json
base=Path('evidence/tabs-page-reconciliation')
def l(p):return json.loads(Path(p).read_text())
map={s:v['destination_id'] for v in l('evidence/figma-application/application-map.json')['variables'] if v['layer']=='semantic' for s in v['source_ids']}
assets=l(base/'assets-native.json');pat=l(base/'pattern-native.json');props=l('consumption/tab/manifest.json')['propertyKeys']
for key in ['master','overview','variants-header','variants-type','variants-selected','variants-state','variants-options']:
 recipe=l(base/('source/recipe-'+key+'.json'));runs={r['id']:r['segments'] for r in l(base/'source/rich-text.json')};
 def augment(n):
  if n['id'] in runs:
   seg=runs[n['id']][0];n['fontName']={k:seg['fontName'][k] for k in ['family','style']};n.setdefault('fills',seg['fills'])
  for c in n.get('kids',[]):augment(c)
 augment(recipe);raw=json.dumps(recipe);selected={k:v for k,v in map.items()if k in raw}
 data={'recipe':recipe,'variableMap':selected,'propertyKeys':props,'patternHash':pat['imageHash'],'logoId':assets['logoId'],'lightbulbId':pat['lightbulbId'],'bulletSvg':(base/'assets/imgBullet.svg').read_text()}
 if key.startswith('variants-'):
  parents=l(base/'doc-variants-native.json');data['parentId']=parents['rootId' if key=='variants-header' else 'contentId']
 code='const DATA='+json.dumps(data,ensure_ascii=False)+';\n'+Path('implementations/figma/tabs-documentation-builder.js').read_text()
 if key=='variants-header':code=code.replace('const root=await build(DATA.recipe,groupParent);','const root=await build(DATA.recipe,groupParent);groupParent.insertChild(0,root);')
 obj={'fileKey':'98xEw6sK8FRVNEhopM5SSz','sessionId':'c61df69c-ad2c-4f85-ad12-ec154c4a5f9b','link_id':'link_6aa838b2077081918681c60e737a01c6','skillNames':'figma-use,figma-generate-design,figma-generate-library','description':'Project editable source Tabs documentation '+key+' using existing linked families','code':code}
 Path('/tmp/tabs-doc-'+key+'.json').write_text(json.dumps(obj,ensure_ascii=False));print(key,len(code),len(selected))
