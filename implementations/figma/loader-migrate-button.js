// ADR-022: modify only the 15 owned dependency nodes; inherited instances keep overrides.
if(figma.fileKey!=='98xEw6sK8FRVNEhopM5SSz')throw new Error('Destination only');
const page=await figma.getNodeByIdAsync('11:128');await page.loadAsync();await figma.setCurrentPageAsync(page);figma.skipInvisibleInstanceChildren=false;
const fonts=new Map();for(const n of page.findAllWithCriteria({types:['TEXT']}))for(const s of n.getStyledTextSegments(['fontName']))fonts.set(JSON.stringify(s.fontName),s.fontName);for(const f of fonts.values())await figma.loadFontAsync(f);
const mutatedNodeIds=[],cases=[];
for(const r of DATA.rows.filter(r=>r.parent.type==='COMPONENT')){
 const n=await figma.getNodeByIdAsync(r.id);if(n.type!=='INSTANCE'||n.parent.id!==r.parent.id)throw new Error('Unexpected consumer identity');
 const kind=n.parent.parent.name.split('/')[1];const size={16:'extra-small',20:'small',24:'medium'}[r.w];const color={primary:'on-color',danger:'on-color',secondary:'brand',link:'brand',text:'strong'}[kind];const variant=DATA.variants.find(v=>v.axes.size===size&&v.axes.color===color);if(!variant)throw new Error('Missing Loader variant');
 const oldMain=(await n.getMainComponentAsync()).id;if(oldMain!==r.main)throw new Error('Consumer drift');const before={x:n.x,y:n.y,w:n.width,h:n.height,visible:n.visible,name:n.name,modes:n.explicitVariableModes};
 n.swapComponent(await figma.getNodeByIdAsync(variant.id));n.resetOverrides();n.name=before.name;n.visible=before.visible;
 // Remove old parent-token dimension overrides; the shared child owns its size binding.
 for(const field of ['width','height'])n.setBoundVariable(field,await figma.variables.getVariableByIdAsync(DATA.variableIds['loader.size-'+size]));
 for(const [col,mode]of Object.entries(before.modes))n.setExplicitVariableModeForCollection(await figma.variables.getVariableCollectionByIdAsync(col),mode);
 mutatedNodeIds.push(n.id,...n.findAll(()=>true).map(c=>c.id));cases.push({id:n.id,buttonId:n.parent.id,kind,buttonSize:n.parent.variantProperties.size,oldMain,newMain:(await n.getMainComponentAsync()).id,size,color,before,after:{x:n.x,y:n.y,w:n.width,h:n.height,visible:n.visible},children:n.findAll(c=>c.type==='ELLIPSE').map(c=>({id:c.id,name:c.name,opacity:c.opacity,cap:c.strokeCap,b:c.boundVariables}))});
}
const inherited=[];for(const r of DATA.rows.filter(r=>r.parent.type==='INSTANCE')){const n=await figma.getNodeByIdAsync(r.id);if(!n)throw new Error('Inherited dependency disappeared');inherited.push({id:n.id,parent:n.parent.id,main:(await n.getMainComponentAsync()).id,w:n.width,h:n.height,visible:n.visible,overrides:n.overrides});}
return {mutatedNodeIds,cases,inherited};
