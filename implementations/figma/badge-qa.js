// Native instance exercises; temporary probes are removed in the same call.
if(figma.fileKey!=='98xEw6sK8FRVNEhopM5SSz')throw Error('Destination only');
figma.skipInvisibleInstanceChildren=false;
const page=await figma.getNodeByIdAsync('281:63');await figma.setCurrentPageAsync(page);
await figma.loadFontAsync({family:'Manrope',style:'Regular'});
const collection=await figma.variables.getVariableCollectionByIdAsync('VariableCollectionId:11:2');
const createdNodeIds=[],removedNodeIds=[],issues=[],cases=[],swaps=[];
const close=(a,b,t=.01)=>Math.abs(a-b)<=t;
function eqcolor(a,b){return ['r','g','b'].every(k=>close(a[k],b[k],1e-6))}
function assert(ok,where,actual,expected){if(!ok)issues.push({where,actual,expected})}
function record(n){createdNodeIds.push(n.id);if('children'in n)for(const c of n.children)record(c)}
const imported=[];for(const i of DATA.exampleIcons)imported.push({source:i,component:await figma.importComponentByKeyAsync(i.key)});
for(const recipe of DATA.recipes){
 const main=await figma.getNodeByIdAsync(recipe.id),size=recipe.axes.size;const fontSize=size==='large'?14:12,line=size==='small'?20:size==='medium'?16:24,padH=size==='large'?12:8,padV=size==='small'?0:4,expectedHeight=size==='small'?20:size==='medium'?24:32,iconSize=size==='small'?12:16;
 for(const mode of collection.modes){
  for(const flags of [[false,false],[true,false],[false,true],[true,true]]){
   const n=main.createInstance();page.appendChild(n);n.x=6000;n.y=80;n.setExplicitVariableModeForCollection(collection,mode.modeId);n.setProperties({[DATA.keys['Show left icon']]:true,[DATA.keys['Show right icon']]:true});
   const label=n.findOne(x=>x.type==='TEXT'&&x.name==='Label'),icons=n.children.filter(x=>x.type==='INSTANCE');record(n);n.setProperties({[DATA.keys['Show left icon']]:flags[0],[DATA.keys['Show right icon']]:flags[1]});assert(icons.length===2,'two icon slots',icons.length,2);
   const start=issues.length;
   for(const content of ['Label','Pendiente de timbrar']){
    n.setProperties({[DATA.keys.Label]:content});
    assert(label.characters===content,'Label',label.characters,content);
    assert(label.textStyleId===DATA.styles[size],'style',label.textStyleId,DATA.styles[size]);
    assert(label.fontName.family==='Manrope'&&label.fontName.style==='Regular','font',label.fontName,'Manrope Regular');
    assert(label.fontSize===fontSize&&label.lineHeight.unit==='PIXELS'&&label.lineHeight.value===line,'typography',{size:label.fontSize,line:label.lineHeight},{fontSize,line});
    assert(label.letterSpacing.unit==='PIXELS'&&label.letterSpacing.value===0,'tracking',label.letterSpacing,{unit:'PIXELS',value:0});
    assert(n.layoutSizingHorizontal==='HUG'&&n.layoutSizingVertical==='HUG','HUG',[n.layoutSizingHorizontal,n.layoutSizingVertical],['HUG','HUG']);
    const count=flags.filter(Boolean).length;assert(close(n.width,label.width+padH*2+count*(iconSize+4)),'width',n.width,label.width+padH*2+count*(iconSize+4));assert(close(n.height,expectedHeight),'height',n.height,expectedHeight);
    assert(n.paddingLeft===padH&&n.paddingRight===padH&&n.paddingTop===padV&&n.paddingBottom===padV&&n.itemSpacing===4,'spacing',[n.paddingLeft,n.paddingTop,n.itemSpacing],[padH,padV,4]);
    assert(eqcolor(label.fills[0].color,recipe.textColor),'source text color',label.fills[0].color,recipe.textColor);assert(eqcolor(n.fills[0].color,recipe.bgColor),'source background',n.fills[0].color,recipe.bgColor);
    assert(n.strokes.length===(recipe.axes.type==='subtle'?1:0),'stroke presence',n.strokes.length,recipe.axes.type==='subtle'?1:0);
    if(n.strokes.length)assert(n.strokeWeight===1&&n.strokeAlign==='INSIDE'&&n.strokesIncludedInLayout===false&&eqcolor(n.strokes[0].color,recipe.strokeColor),'stroke',n.strokes,recipe.strokeColor);
    for(let index=0;index<icons.length;index++){
     const icon=icons[index];assert(icon.visible===flags[index],'visibility',icon.visible,flags[index]);
     if(!flags[index])continue;
     const m=await icon.getMainComponentAsync();assert(m.remote&&m.key===DATA.defaultIconKey,'remote key',{key:m.key,remote:m.remote},DATA.defaultIconKey);
     assert(icon.width===iconSize&&icon.height===iconSize,'icon size',[icon.width,icon.height],iconSize);assert(icon.boundVariables.width?.id===DATA.variableIds[recipe.iconSizeToken]&&icon.boundVariables.height?.id===DATA.variableIds[recipe.iconSizeToken],'icon size bindings',icon.boundVariables,recipe.iconSizeToken);
     const shapes=icon.findAll(x=>x.type==='VECTOR'||x.type==='BOOLEAN_OPERATION');assert(shapes.length>0,'icon shapes',shapes.length,'>0');for(const v of shapes)for(const p of v.fills??[]){if(p.type!=='SOLID')continue;assert(eqcolor(p.color,label.fills[0].color),'icon/text parity',p.color,label.fills[0].color);assert(p.boundVariables?.color?.id===DATA.variableIds[recipe.iconColorToken],'icon binding',p.boundVariables?.color?.id,DATA.variableIds[recipe.iconColorToken]);}
    }
   }
   cases.push({axes:recipe.axes,mode:mode.name,left:flags[0],right:flags[1],labels:2,iconPairs:flags.filter(Boolean).length*2,pass:issues.length===start});
   n.remove();removedNodeIds.push(n.id);
  }
  for(const asset of imported){
   const n=main.createInstance();page.appendChild(n);record(n);n.x=6000;n.y=80;n.setExplicitVariableModeForCollection(collection,mode.modeId);n.setProperties({[DATA.keys['Show left icon']]:true,[DATA.keys['Show right icon']]:true,[DATA.keys['Left icon']]:asset.component.id,[DATA.keys['Right icon']]:asset.component.id});
   const label=n.findOne(x=>x.type==='TEXT'&&x.name==='Label');const start=issues.length;
   for(const icon of n.children.filter(x=>x.type==='INSTANCE')){const m=await icon.getMainComponentAsync();assert(m.key===asset.source.key&&m.remote,'swap remote',{key:m.key,remote:m.remote},asset.source.key);assert(icon.width===iconSize&&icon.height===iconSize,'swap size',[icon.width,icon.height],iconSize);assert(icon.boundVariables.width?.id===DATA.variableIds[recipe.iconSizeToken]&&icon.boundVariables.height?.id===DATA.variableIds[recipe.iconSizeToken],'swap size binding',icon.boundVariables,recipe.iconSizeToken);const shapes=icon.findAll(x=>x.type==='VECTOR'||x.type==='BOOLEAN_OPERATION');assert(shapes.length>0,'swap nonempty',shapes.length,'>0');for(const v of shapes)for(const p of v.fills??[]){if(p.type==='SOLID')assert(eqcolor(p.color,label.fills[0].color)&&p.boundVariables?.color?.id===DATA.variableIds[recipe.iconColorToken],'swap color parity',{color:p.color,b:p.boundVariables?.color?.id},{color:label.fills[0].color,id:DATA.variableIds[recipe.iconColorToken]});}}
   swaps.push({axes:recipe.axes,mode:mode.name,key:asset.source.key,iconPairs:2,pass:issues.length===start});n.remove();removedNodeIds.push(n.id);
  }
 }
}
return {status:issues.length?'FAIL':'PASS',issues,cases,swaps,counts:{cases:cases.length,swaps:swaps.length,colorPairs:cases.reduce((a,c)=>a+c.iconPairs,0)+swaps.reduce((a,c)=>a+c.iconPairs,0)},createdNodeIds,removedNodeIds};
