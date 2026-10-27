if(figma.fileKey!==DATA.fileKey)throw Error('Wrong destination');
const page=await figma.getNodeByIdAsync(DATA.pageId);await figma.setCurrentPageAsync(page);
await figma.loadFontAsync({family:'Manrope',style:'Bold'});await figma.loadFontAsync({family:'Manrope',style:'Regular'});
figma.skipInvisibleInstanceChildren=false;
const issues=[],families={},icons=[],near=(a,b)=>Math.abs(a-b)<=0.00001;
function check(field,a,b){if(typeof a==='number'&&typeof b==='number'?!near(a,b):JSON.stringify(a)!==JSON.stringify(b))issues.push({field,actual:a,expected:b});}
for(const f of DATA.families){const set=await figma.getNodeByIdAsync(f.setId);families[f.kind]={id:set.id,key:set.key,properties:set.componentPropertyDefinitions};
 for(const key of [f.properties.leftKey,f.properties.rightKey]){const def=set.componentPropertyDefinitions[key];const main=await figma.getNodeByIdAsync(def.defaultValue);check(set.id+':'+key,main.key,DATA.newGlyphKey);check(set.id+':preferred',def.preferredValues,[{type:'COMPONENT',key:DATA.newGlyphKey}]);}
 for(const r of f.variants){const root=await figma.getNodeByIdAsync(r.id);check(root.id+':width',root.width,r.width);check(root.id+':height',root.height,r.height);
  for(const i of r.icons){const n=await figma.getNodeByIdAsync(i.id),main=await n.getMainComponentAsync();check(n.id+':key',main.key,DATA.newGlyphKey);check(n.id+':remote',main.remote,true);check(n.id+':width',n.width,i.size);check(n.id+':height',n.height,i.size);check(n.id+':visible',n.visible,i.visible);
   check(n.id+':width-binding',n.boundVariables.width.id,i.sizeTokenId);check(n.id+':height-binding',n.boundVariables.height.id,i.sizeTokenId);
   check(n.id+':property-visibility',n.componentPropertyReferences.visible,i.name==='Left icon'?f.properties.showLeftKey:f.properties.showRightKey);
   check(n.id+':property-swap',n.componentPropertyReferences.mainComponent,i.name==='Left icon'?f.properties.leftKey:f.properties.rightKey);
   const vectors=n.findAllWithCriteria({types:['VECTOR']});check(n.id+':vector-count',vectors.length,1);for(const v of vectors)check(v.id+':color-binding',v.fills[0].boundVariables.color.id,i.colorTokenId);icons.push({node:n,token:i.colorTokenId});
  }
 }
}
const review=await figma.getNodeByIdAsync('16:32'),consumerRoots=review.findAllWithCriteria({types:['INSTANCE']}).filter(n=>n.parent.type!=='INSTANCE'&&n.mainComponent.parent?.type==='COMPONENT_SET'&&n.mainComponent.parent.name.startsWith('Button/'));
check('consumer-count',consumerRoots.length,94);
let inherited=0;for(const n of consumerRoots){for(const icon of n.findAllWithCriteria({types:['INSTANCE']}).filter(i=>i.name==='Left icon'||i.name==='Right icon')){const main=await icon.getMainComponentAsync();check(icon.id+':inherited-key',main.key,DATA.newGlyphKey);check(icon.id+':inherited-remote',main.remote,true);inherited++;}}
const cs=await figma.variables.getLocalVariableCollectionsAsync(),collection=cs.find(c=>c.name==='component');const beforePage=page.explicitVariableModes[collection.id],beforeReview=review.explicitVariableModes[collection.id];let themeColorChecks=0;
try{for(const mode of collection.modes){page.setExplicitVariableModeForCollection(collection,mode.modeId);review.setExplicitVariableModeForCollection(collection,mode.modeId);
 for(const {node,token}of icons){const variable=await figma.variables.getVariableByIdAsync(token),expected=variable.resolveForConsumer(node).value;const paint=node.findAllWithCriteria({types:['VECTOR']})[0].fills[0];for(const k of ['r','g','b'])check(mode.name+':'+node.id+':'+k,paint.color[k],expected[k]);themeColorChecks++;}
}}finally{if(beforePage)page.setExplicitVariableModeForCollection(collection,beforePage);else page.clearExplicitVariableModeForCollection(collection);if(beforeReview)review.setExplicitVariableModeForCollection(collection,beforeReview);else review.clearExplicitVariableModeForCollection(collection);}
const old=await figma.getNodeByIdAsync(DATA.oldGlyphId);const references=page.findAllWithCriteria({types:['INSTANCE']}).filter(n=>n.mainComponent.id===DATA.oldGlyphId).map(n=>n.id);
return{status:issues.length?'FAIL':'PASS_LINKED_PHOSPHOR',mainIconInstances:icons.length,consumerInstances:consumerRoots.length,inheritedIconInstances:inherited,themeColorChecks,componentVariables:(await figma.variables.getLocalVariablesAsync()).length,families,oldGlyph:{id:old?.id,references},issues};
