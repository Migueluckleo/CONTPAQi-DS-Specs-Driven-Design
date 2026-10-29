// Destination-only, idempotent expansion of the shared Badge identity.
if(figma.fileKey!=='98xEw6sK8FRVNEhopM5SSz')throw Error('Destination only');
const createdNodeIds=[],mutatedNodeIds=[],createdVariableIds=[],createdStyleIds=[];
const page=await figma.getNodeByIdAsync('281:63');await figma.setCurrentPageAsync(page);
const available=await figma.listAvailableFontsAsync();
if(!available.some(f=>f.fontName.family==='Manrope'&&f.fontName.style==='Regular'))throw Error('Manrope Regular unavailable');
await figma.loadFontAsync({family:'Manrope',style:'Regular'});
const collection=await figma.variables.getVariableCollectionByIdAsync('VariableCollectionId:11:2');
if(collection.name!=='component'||collection.modes.map(m=>m.name).join('|')!=='Contable|Administrativo|Servicios|Personas')throw Error('Collection drift');
const ids={...DATA.previous.variableIds},keys={...DATA.previous.variableKeys};
if(DATA.operation==='foundations'){
 const inventory=await figma.variables.getLocalVariablesAsync();const rows=[];
 for(const t of DATA.tokens){
  let v=ids[t.id]?await figma.variables.getVariableByIdAsync(ids[t.id]):inventory.find(v=>v.variableCollectionId===collection.id&&v.name===t.figmaName);
  if(!v){v=figma.variables.createVariable(t.figmaName,collection,t.type==='number'?'FLOAT':t.type==='color'?'COLOR':'STRING');v.scopes=t.scopes;v.description=t.description;v.setVariableCodeSyntax('WEB',t.web);for(const m of collection.modes){const s=await figma.variables.getVariableByIdAsync(DATA.semanticIds[t.values[m.name].alias]);v.setValueForMode(m.modeId,figma.variables.createVariableAlias(s));}createdVariableIds.push(v.id);}
  if(v.name!==t.figmaName||JSON.stringify(v.scopes)!==JSON.stringify(t.scopes)||v.codeSyntax.WEB!==t.web)throw Error('Variable identity drift '+t.id);
  for(const m of collection.modes)if(v.valuesByMode[m.modeId]?.id!==DATA.semanticIds[t.values[m.name].alias])throw Error('Variable alias drift '+t.id+' '+m.name);
  ids[t.id]=v.id;keys[t.id]=v.key;rows.push({logicalId:t.id,id:v.id,key:v.key,name:v.name,type:v.resolvedType,scopes:v.scopes,web:v.codeSyntax.WEB,values:v.valuesByMode});
 }
 const styles={small:DATA.previous.styles['badge/subtle-small']};const oldStyles=await figma.getLocalTextStylesAsync();
 for(const [size,fs,lh]of [['medium',12,16],['large',14,24]]){
  const name='badge/label-'+size;let s=oldStyles.find(s=>s.name===name);
  if(!s){s=figma.createTextStyle();s.name=name;s.fontName={family:'Manrope',style:'Regular'};s.fontSize=fs;s.lineHeight={unit:'PIXELS',value:lh};s.letterSpacing={unit:'PIXELS',value:0};for(const [f,id]of Object.entries({fontFamily:'badge.font-family',fontStyle:'badge.font-label-style',fontSize:size==='large'?'badge.font-size-large':'badge.font-size',lineHeight:'badge.font-line-height-'+size,letterSpacing:'badge.font-letter-spacing'}))s.setBoundVariable(f,await figma.variables.getVariableByIdAsync(ids[id]));createdStyleIds.push(s.id);}styles[size]=s.id;
 }
 return {status:'PASS_FOUNDATIONS',pageId:page.id,collection:{id:collection.id,key:collection.key,name:collection.name,modeIds:Object.fromEntries(collection.modes.map(m=>[m.name,m.modeId]))},variableIds:ids,variableKeys:keys,styles,rows,createdNodeIds,mutatedNodeIds,createdVariableIds,createdStyleIds};
}
const variables={};for(const[id,native]of Object.entries(DATA.ledger.variableIds))variables[id]=await figma.variables.getVariableByIdAsync(native);
const owner=await figma.getNodeByIdAsync('282:3');const imported=await figma.importComponentByKeyAsync(DATA.icon.key);
const propKeys={Label:DATA.previous.labelProperty};
for(const[name,type,value]of [['Show left icon','BOOLEAN',false],['Show right icon','BOOLEAN',false],['Left icon','INSTANCE_SWAP',imported.id],['Right icon','INSTANCE_SWAP',imported.id]]){
 const found=Object.keys(owner.componentPropertyDefinitions).find(k=>k.split('#')[0]===name);propKeys[name]=found||owner.addComponentProperty(name,type,value);
}
owner.description='BADGE-001@1.1.0 · Etiqueta no interactiva. 6 tipos ×3 tamaños; Label editable e iconos Phosphor opcionales/swaps. 35 tokens compartidos, colores invariantes en 4 temas. Warning conserva contraste ~3:1 de la raíz por decisión humana; no cumple AA de texto. Input consume subtle/small. Contrato y mapa: consumption/badge.';
const built=[];
function mark(n){createdNodeIds.push(n.id);if('children'in n)for(const c of n.children)mark(c)}
for(const recipe of DATA.recipes){
 const {type,size}=recipe.axes;const name='type='+type+', size='+size;let n=owner.children.find(c=>c.name===name);const reused=!!n;
 if(!n){n=figma.createComponent();owner.appendChild(n);createdNodeIds.push(n.id);n.name=name;n.layoutMode='HORIZONTAL';}
 const p=recipe.root;n.primaryAxisSizingMode='AUTO';n.counterAxisSizingMode='AUTO';n.primaryAxisAlignItems='MIN';n.counterAxisAlignItems='CENTER';n.clipsContent=p.clipsContent;n.strokesIncludedInLayout=false;n.strokeAlign='INSIDE';n.fills=[];n.strokes=[];
 await bindVariablesToComponent(n,Object.fromEntries(Object.entries(p.bindings).filter(([k])=>!['maxHeight','strokeWeight'].includes(k)).map(([k,id])=>[k,variables[id].id])));
 for(const f of ['maxHeight','strokeWeight'])if(p.bindings[f])n.setBoundVariable(f,variables[p.bindings[f]]);
 if(!p.bindings.maxHeight)n.maxHeight=null;
 let text=n.children.find(c=>c.type==='TEXT'&&c.name==='Label');
 if(!text){text=figma.createText();n.appendChild(text);createdNodeIds.push(text.id);text.name='Label';text.fontName={family:'Manrope',style:'Regular'};text.characters='Label';}else for(const seg of text.getStyledTextSegments(['fontName']))await figma.loadFontAsync(seg.fontName);
 text.textAutoResize='WIDTH_AND_HEIGHT';text.textTruncation='DISABLED';text.componentPropertyReferences={characters:propKeys.Label};
 await text.setTextStyleIdAsync(DATA.ledger.styles[size]);text.fills=[figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:0,g:0,b:0}},'color',variables[recipe.label.bindings.fills])];
 const icons=[];
 for(const side of ['Left icon','Right icon']){
  let icon=n.children.find(c=>c.type==='INSTANCE'&&c.name===side);
  if(!icon){icon=imported.createInstance();n.insertChild(side==='Left icon'?0:n.children.length,icon);mark(icon);icon.name=side;}
  icon.visible=true;icon.resize(recipe.iconSize,recipe.iconSize);icon.setBoundVariable('width',variables[recipe.iconBindings.width]);icon.setBoundVariable('height',variables[recipe.iconBindings.height]);
  for(const shape of icon.findAll(c=>c.type==='VECTOR'||c.type==='BOOLEAN_OPERATION')){if('fills'in shape&&Array.isArray(shape.fills)&&shape.fills.length){shape.fills=shape.fills.map(p=>p.type==='SOLID'?figma.variables.setBoundVariableForPaint(p,'color',variables[recipe.iconColor]):p);mutatedNodeIds.push(shape.id);}}
  icon.componentPropertyReferences={visible:propKeys['Show '+side.toLowerCase()],mainComponent:propKeys[side]};icon.visible=false;icons.push({id:icon.id,name:icon.name});
 }
 text.layoutSizingHorizontal='HUG';text.layoutSizingVertical='HUG';n.layoutSizingHorizontal='HUG';n.layoutSizingVertical='HUG';
 n.x=40+['small','medium','large'].indexOf(size)*180;n.y=40+['subtle','neutral','info','success','warning','error'].indexOf(type)*68;
 mutatedNodeIds.push(n.id,text.id,...icons.map(i=>i.id));built.push({sourceId:recipe.sourceId,id:n.id,key:n.key,name,axes:recipe.axes,labelId:text.id,icons,w:n.width,h:n.height,reused});
}
owner.resize(580,460);mutatedNodeIds.push(owner.id);
return {status:'BUILT',setId:owner.id,setKey:owner.key,propertyKeys:propKeys,variants:built,createdNodeIds:[...new Set(createdNodeIds)],mutatedNodeIds:[...new Set(mutatedNodeIds)],variantCount:owner.children.length};
