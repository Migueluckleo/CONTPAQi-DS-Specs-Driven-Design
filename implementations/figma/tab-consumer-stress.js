// Consumer QA only. Own temporary nodes are removed after their facts are captured.
if(figma.fileKey!=='98xEw6sK8FRVNEhopM5SSz')throw new Error('Wrong destination');
figma.skipInvisibleInstanceChildren=false;
await figma.setCurrentPageAsync(await figma.getNodeByIdAsync(DATA.pageId));
for(const style of ['Regular','SemiBold','Bold'])await figma.loadFontAsync({family:'Manrope',style});
const collection=await figma.variables.getVariableCollectionByIdAsync(DATA.collectionId);
const staging=figma.createAutoLayout('VERTICAL');staging.name='__TabQA/Focus consumers';staging.x=5000;staging.y=80;staging.fills=[];staging.clipsContent=false;
const records=[];const P=DATA.properties;
for(const mode of DATA.modes)for(const variant of DATA.variants.filter(v=>v.axes.state==='focus')){
 const context=figma.createAutoLayout('HORIZONTAL');staging.appendChild(context);context.resize(160,60);context.fills=[];context.clipsContent=false;context.setExplicitVariableModeForCollection(collection,DATA.modeIds[mode]);
 const main=await figma.getNodeByIdAsync(variant.id),n=main.createInstance();context.appendChild(n);
 n.setProperties({...variant.axes,[P.Label]:'Movimientos del periodo actual',[P.ShowIcon]:true,[P.ShowBadge]:true});
 const badge=n.children.find(c=>c.name==='Badge');badge.setProperties({[DATA.countProperty]:'99+'});
 const ring=n.children.find(c=>c.name==='Focus ring'),label=n.children.find(c=>c.name==='Label'),icon=n.children.find(c=>c.name==='Icon');
 const properties=n.componentProperties;
 records.push({mode,axes:variant.axes,id:n.id,mainId:(await n.getMainComponentAsync()).id,width:n.width,height:n.height,containerWidth:context.width,containerClips:context.clipsContent,label:{characters:label.characters,width:label.width,height:label.height,fontName:label.fontName,fontSize:label.fontSize,lineHeight:label.lineHeight,textStyleId:label.textStyleId},icon:{width:icon.width,height:icon.height,remote:(await icon.getMainComponentAsync()).remote},count:{width:badge.width,height:badge.height,text:badge.children[0].characters,mainId:(await badge.getMainComponentAsync()).id},ring:{x:ring.x,y:ring.y,width:ring.width,height:ring.height,stroke:ring.strokes[0],constraints:ring.constraints},properties});
}
function ids(n){return[n.id,...('children'in n?n.children.flatMap(ids):[])];}
const temporaryIds=ids(staging);staging.remove();
return{records,createdNodeIds:temporaryIds,removedNodeIds:temporaryIds,mutatedNodeIds:temporaryIds,retainedQaNodes:0};
