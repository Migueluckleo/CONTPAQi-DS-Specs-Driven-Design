// Read-only source extraction. Stop at nested component boundaries; omit swap preference inventories.
const page=await figma.getNodeByIdAsync('20:3');await page.loadAsync();await figma.setCurrentPageAsync(page);figma.skipInvisibleInstanceChildren=false;
async function snapshot(root){
 const rows=[];
 async function visit(n,path){
  const o={id:n.id,path,name:n.name,type:n.type,w:n.width,h:n.height,x:n.x,y:n.y,visible:n.visible,opacity:n.opacity,b:n.boundVariables,refs:n.componentPropertyReferences,layoutSizingHorizontal:n.layoutSizingHorizontal,layoutSizingVertical:n.layoutSizingVertical,layoutPositioning:n.layoutPositioning,constraints:n.constraints};
  if(['FRAME','COMPONENT'].includes(n.type))for(const k of ['layoutMode','primaryAxisSizingMode','counterAxisSizingMode','primaryAxisAlignItems','counterAxisAlignItems','paddingTop','paddingRight','paddingBottom','paddingLeft','itemSpacing','cornerRadius','strokeWeight','strokeAlign','strokesIncludedInLayout','clipsContent','fills','strokes','effects','minWidth','maxWidth','minHeight','maxHeight'])o[k]=n[k];
  else if(n.type==='RECTANGLE')for(const k of ['cornerRadius','strokeWeight','strokeAlign','fills','strokes','effects'])o[k]=n[k];
  else if(n.type==='TEXT')Object.assign(o,{text:n.characters,font:n.fontName,fontSize:n.fontSize,lineHeight:n.lineHeight,letterSpacing:n.letterSpacing,textStyleId:n.textStyleId,textAutoResize:n.textAutoResize,fills:n.fills});
  else if(n.type==='INSTANCE'){
   const m=await n.getMainComponentAsync();o.main={id:m.id,key:m.key,name:m.name,parent:m.parent?.id};
   o.exposed=n.isExposedInstance;if(n.name==='Badge'){const label=n.findOne(c=>c.type==='TEXT'&&c.name==='Label');o.badgeLabel=label?{id:label.id,text:label.characters,w:label.width,h:label.height,font:label.fontName,fontSize:label.fontSize,lineHeight:label.lineHeight,letterSpacing:label.letterSpacing,b:label.boundVariables,fills:label.fills}:null;}
   if(n.name!=='Badge')o.vectors=n.findAll(c=>c.type==='VECTOR').map(c=>({id:c.id,name:c.name,w:c.width,h:c.height,opacity:c.opacity,fills:c.fills,b:c.boundVariables}));
  }
  rows.push(o);if('children'in n&&n.type!=='INSTANCE')for(let i=0;i<n.children.length;i++)await visit(n.children[i],path+'/'+i);
 }
 await visit(root,'root');return {id:root.id,name:root.name,reactions:root.reactions,rows};
}
const out=[];for(const id of DATA.ids)out.push(await snapshot(await figma.getNodeByIdAsync(id)));
if(JSON.stringify(out).length>47000)throw new Error('Split source ID batch before returning');return out;
