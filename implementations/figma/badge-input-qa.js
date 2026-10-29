// Run in batches of 14 source variants to retain every generated node ID.
if(figma.fileKey!=='98xEw6sK8FRVNEhopM5SSz')throw Error('Destination only');
figma.skipInvisibleInstanceChildren=false;
const p=await figma.getNodeByIdAsync('281:62');await figma.setCurrentPageAsync(p);
await figma.loadFontAsync({family:'Manrope',style:'Regular'});await figma.loadFontAsync({family:'Manrope',style:'Bold'});
const col=await figma.variables.getVariableCollectionByIdAsync('VariableCollectionId:11:2');
const rows=[],issues=[],created=[],removed=[];function mark(n){created.push(n.id);if('children'in n)for(const c of n.children)mark(c)}
for(const rec of DATA.variants){for(const mode of col.modes){
 const n=(await figma.getNodeByIdAsync(rec.id)).createInstance();p.appendChild(n);mark(n);n.x=10000;n.y=80;n.setExplicitVariableModeForCollection(col,mode.modeId);const before=issues.length;n.setProperties({[rec.showBadgeKey]:true});const b=n.findOne(c=>c.type==='INSTANCE'&&c.name==='Badge');if(!b)throw Error('Missing Badge '+rec.id);
 for(const content of ['MXN','USD','Pesos mexicanos']){
  b.setProperties({[DATA.badgeLabelKey]:content});const t=b.findOne(c=>c.type==='TEXT'&&c.name==='Label'),m=await b.getMainComponentAsync();
  if(t.characters!==content||b.height!==20||Math.abs(b.width-t.width-16)>.01||m.id!=='282:2'||b.variantProperties.type!=='subtle'||b.variantProperties.size!=='small'||!b.visible||b.children.filter(c=>c.type==='INSTANCE').some(i=>i.visible))issues.push({variant:rec.axes,mode:mode.name,content,actual:{w:b.width,h:b.height,visible:b.visible,text:t.characters,main:m.id}});
 }
 n.setProperties({[rec.showBadgeKey]:false});if(b.visible)issues.push({hideFailed:n.id});rows.push({id:rec.id,axes:rec.axes,mode:mode.name,labels:3,pass:before===issues.length});n.remove();removed.push(n.id);
}}
return {status:issues.length?'FAIL':'PASS',rows,issues,counts:{cases:rows.length,labelEdits:rows.length*3},createdNodeIds:created,removedNodeIds:removed};
