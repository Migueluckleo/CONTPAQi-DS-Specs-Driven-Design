if(figma.fileKey!=='98xEw6sK8FRVNEhopM5SSz')throw new Error('Wrong destination');
figma.skipInvisibleInstanceChildren=false;const page=await figma.getNodeByIdAsync('78:97');await page.loadAsync();await figma.setCurrentPageAsync(page);
for(const style of ['Regular','SemiBold','Bold'])await figma.loadFontAsync({family:'Manrope',style});
if(page.children.some(n=>n.name==='Tabs · QA de slot y temas'))throw new Error('QA exists; inspect ledger');
const f=figma.createFrame();page.appendChild(f);f.name='Tabs · QA de slot y temas';f.x=80;f.y=4400;f.resize(1920,1200);f.fills=[{type:'SOLID',color:{r:1,g:1,b:1}}];f.clipsContent=false;
const created=[f.id],cases=[],themes=[];const gs=await figma.getNodeByIdAsync('105:223'),ts=await figma.getNodeByIdAsync('79:26');const P=DATA.propertyKeys;
const label=(text,x,y)=>{const t=figma.createText();f.appendChild(t);t.fontName={family:'Manrope',style:'Regular'};t.fontSize=16;t.characters=text;t.x=x;t.y=y;created.push(t.id);return t;};
label('Slots nativos · 2 y 6 hijos · contenido, orden y foco desde instancias',32,24);
for(const [r,type]of ['underline','pill','segmented'].entries())for(const [c,count]of [2,6].entries()){
 const master=gs.children.find(n=>n.variantProperties.type===type);const n=master.createInstance();f.appendChild(n);created.push(n.id);n.x=32+c*760;n.y=112+r*136;n.setExplicitVariableModeForCollection('VariableCollectionId:11:2','11:0');
 let slot=()=>n.findOne(x=>x.type==='SLOT');while(slot().children.length>count)slot().children.at(-1).remove();
 while(slot().children.length<count){const child=ts.children.find(v=>v.variantProperties.type===type&&v.variantProperties.selected==='false'&&v.variantProperties.state==='default').createInstance();slot().appendChild(child);created.push(child.id);child.setProperties({[P.Label]:'Tab '+slot().children.length});}
 const selected=slot().children.find(x=>x.componentProperties.selected.value==='true');selected.setProperties({state:'focus',[P.Label]:count===6?'Vista de comprobación ampliada':'Vista',[P.ShowIcon]:true,[P.ShowBadge]:true});
 const badge=selected.findOne(x=>x.type==='INSTANCE'&&x.name==='Badge');if(badge)badge.setProperties({[DATA.countProperty]:'99+'});
 let moved=null;if(count===6){moved=slot().children.at(-1).id;slot().insertChild(0,slot().children.at(-1));}
 const s=slot();const ring=selected.findOne(x=>x.name==='Focus ring');
 const result={type,count,instanceId:n.id,slotId:s.id,slotType:s.type,actualCount:s.children.length,violations:s.limitViolations,selectedCount:s.children.filter(x=>x.componentProperties.selected.value==='true').length,types:s.children.map(x=>x.componentProperties.type.value),firstId:s.children[0].id,movedId:moved,label:selected.componentProperties[P.Label].value,focus:ring?{id:ring.id,marginWidth:ring.width-selected.width,marginHeight:ring.height-selected.height,slotClips:s.clipsContent,groupClips:n.clipsContent}:null};
 result.pass=result.actualCount===count&&result.slotType==='SLOT'&&result.violations.length===0&&result.selectedCount===1&&result.types.every(x=>x===type)&&(!moved||moved===result.firstId)&&result.focus&&Math.abs(result.focus.marginWidth-8)<.01&&Math.abs(result.focus.marginHeight-8)<.01&&!result.focus.slotClips&&!result.focus.groupClips;cases.push(result);label(type+' · '+count+' hijos',n.x,n.y-30);
}
label('Segmented seleccionado · morado fijo en default/hover · blanco en focus/disabled',32,550);
for(const [r,[name,mode]]of DATA.modes.entries()){
 label(name,32,610+r*120);for(const [c,state]of ['default','hover','focus','disabled'].entries()){
  const n=ts.children.find(v=>v.variantProperties.type==='segmented'&&v.variantProperties.selected==='true'&&v.variantProperties.state===state).createInstance();f.appendChild(n);created.push(n.id);n.x=300+c*260;n.y=610+r*120;n.setExplicitVariableModeForCollection('VariableCollectionId:11:2',mode);n.setProperties({[P.Label]:state});const text=n.children.find(x=>x.type==='TEXT');themes.push({mode:name,state,id:n.id,background:n.fills[0].color,foreground:text.fills[0].color,fillVariableId:n.fills[0].boundVariables?.color?.id,textVariableId:text.fills[0].boundVariables?.color?.id});
 }
}
const definitions=gs.componentPropertyDefinitions;return{status:cases.every(x=>x.pass)?'PASS':'FAIL',frameId:f.id,cases,themes,publicProperties:definitions,createdNodeIds:created};
