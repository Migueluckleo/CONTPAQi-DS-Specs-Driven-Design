// Narrow UPDATE: preserve component/property identities and restore token bindings.
if(figma.fileKey!==DATA.fileKey)throw Error('Wrong destination');
const page=await figma.getNodeByIdAsync(DATA.pageId);await figma.setCurrentPageAsync(page);
figma.skipInvisibleInstanceChildren=false;
await figma.loadFontAsync({family:'Manrope',style:'Bold'});await figma.loadFontAsync({family:'Manrope',style:'Regular'});
const glyph=await figma.importComponentByKeyAsync(DATA.newGlyphKey);
if(!glyph.remote||glyph.key!==DATA.newGlyphKey)throw Error('Expected linked Phosphor component');
const changes=[],issues=[];
try{
for(const f of DATA.families){
 for(const v of f.variants){
  for(const r of v.icons){const n=await figma.getNodeByIdAsync(r.id),main=await n.getMainComponentAsync();
   if(main.id!==DATA.oldGlyphId&&main.key!==DATA.newGlyphKey)throw Error('Unrecognized icon main '+n.id);
   const references=n.componentPropertyReferences;
   n.swapComponent(glyph);n.name=r.name;n.resize(r.size,r.size);n.visible=r.visible;n.componentPropertyReferences=references;
   const size=await figma.variables.getVariableByIdAsync(r.sizeTokenId),color=await figma.variables.getVariableByIdAsync(r.colorTokenId);
   n.setBoundVariable('width',size);n.setBoundVariable('height',size);
   for(const vector of n.findAllWithCriteria({types:['VECTOR']}))vector.fills=[figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:0,g:0,b:0}},'color',color)];
   changes.push(n.id);
  }
  const main=await figma.getNodeByIdAsync(v.id);if(Math.abs(main.width-v.width)>0.00001||Math.abs(main.height-v.height)>0.00001)issues.push({id:main.id,field:'geometry'});
 }
 const set=await figma.getNodeByIdAsync(f.setId);
 for(const key of [f.properties.leftKey,f.properties.rightKey])set.editComponentProperty(key,{defaultValue:glyph.id,preferredValues:[{type:'COMPONENT',key:glyph.key}]});
 set.description=set.description.replace('v1.0.0','v1.1.0')+' Iconos vinculados a Phosphor; desarrollo consume @phosphor-icons/react oficial.';
}
return{status:issues.length?'FAIL_GEOMETRY':'APPLIED_PHOSPHOR_LINKS',swapped:changes.length,changedInstanceIds:changes,glyph:{id:glyph.id,key:glyph.key,remote:glyph.remote},setsUpdated:DATA.families.map(f=>f.setId),issues};
}catch(e){return{status:'PARTIAL_FAILURE',error:String(e),changedInstanceIds:changes,issues};}
