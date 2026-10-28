// LOADER-001. Embed the official createComponentWithVariants helper before this script.
if(figma.fileKey!=='98xEw6sK8FRVNEhopM5SSz')throw new Error('Destination only');
const cols=await figma.variables.getLocalVariableCollectionsAsync();if(cols.length!==3)throw new Error('Exactly three collections required');
const collection=cols.find(c=>c.name==='component');const createdNodeIds=[],mutatedNodeIds=[],createdVariableIds=[];
if(DATA.operation==='foundations'){
 const all=await figma.variables.getLocalVariablesAsync();if(figma.root.children.some(p=>p.name==='Loader')||all.some(v=>v.name.startsWith('loader/')))throw new Error('Reconcile existing Loader ledger first');
 const variableIds={},variableKeys={},extensions=[];
 for(const t of DATA.extensions){const col=cols.find(c=>c.name===t.layer);if(all.some(v=>v.variableCollectionId===col.id&&v.name===t.nativeName))throw new Error('Foundation already exists');const v=figma.variables.createVariable(t.nativeName,col,'FLOAT');v.scopes=[];v.description=t.description;v.setVariableCodeSyntax('WEB','var('+t.name+')');v.setValueForMode(col.modes[0].modeId,t.literal??figma.variables.createVariableAlias(await figma.variables.getVariableByIdAsync(variableIds[t.alias])));variableIds[t.id]=v.id;variableKeys[t.id]=v.key;extensions.push({logicalId:t.id,nativeId:v.id,nativeKey:v.key,nativeName:v.name});createdVariableIds.push(v.id);}
 const semanticIds={...DATA.semanticIds,'semantic.size-8xl':variableIds['semantic.size-8xl']};
 for(const t of DATA.tokens){const v=figma.variables.createVariable(t.figmaName,collection,t.type==='color'?'COLOR':'FLOAT');v.scopes=t.scopes;v.description=t.description;v.setVariableCodeSyntax('WEB',t.web);for(const m of collection.modes)v.setValueForMode(m.modeId,figma.variables.createVariableAlias(await figma.variables.getVariableByIdAsync(semanticIds[t.values[m.name].alias])));variableIds[t.id]=v.id;variableKeys[t.id]=v.key;createdVariableIds.push(v.id);}
 const page=figma.createPage();page.name='Loader';createdNodeIds.push(page.id);
 return {pageId:page.id,variableIds,variableKeys,extensions,collection:{id:collection.id,key:collection.key,name:collection.name,modeIds:Object.fromEntries(collection.modes.map(m=>[m.name,m.modeId]))},createdNodeIds,mutatedNodeIds,createdVariableIds};
}
const page=await figma.getNodeByIdAsync(DATA.ledger.pageId);if(!page||page.type!=='PAGE'||page.name!=='Loader')throw new Error('Invalid Loader page');
const vars={};for(const [id,native]of Object.entries(DATA.ledger.variableIds))vars[id]=await figma.variables.getVariableByIdAsync(native);
const V=k=>vars['loader.'+k];const bind=(n,f,k)=>n.setBoundVariable(f,V(k));const paint=(n,k)=>{n.strokes=[figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:0,g:0,b:0}},'color',V(k))]};
function mark(n){createdNodeIds.push(n.id);if('children'in n)for(const c of n.children)mark(c)}
if(DATA.operation==='cycle'){
 await page.loadAsync();if(page.children.some(n=>n.name==='__Loader/Frames/'+DATA.size))throw new Error('Cycle already exists; reconcile exact ledger');
 const src=DATA.animation[DATA.size],dim=src.first.w,widthKey={16:'regular',20:'regular',24:'regular',40:'large',64:'extra-large',88:'2x-large'}[dim];
 const result=await createComponentWithVariants({name:'__Loader/Frames/'+DATA.size,description:'LOADER-001 · Ciclo interno de 24 fases, 15°/fase y vuelta nominal 0.8 s; consumir Loader, no estas fases.',variantAxes:{frame:src.phases.map(f=>f.frame)},baseProps:{width:dim,height:dim,fills:[]},page});
 const set=result.componentSet;createdNodeIds.push(set.id);const map={},phases=[];
 for(const n of result.variants){createdNodeIds.push(n.id);const phase=src.phases.find(f=>f.frame===n.variantProperties.frame);map[phase.id]=n;n.clipsContent=false;bind(n,'width','size-'+DATA.size);bind(n,'height','size-'+DATA.size);
  for(const part of src.first.children){const e=figma.createEllipse();n.appendChild(e);createdNodeIds.push(e.id);e.name=part.name;e.resize(dim,dim);e.x=0;e.y=0;e.fills=[];e.arcData=part.name==='Arc'?phase.arc:part.arc;e.strokeAlign=part.align;e.strokeCap=part.cap;bind(e,'width','size-'+DATA.size);bind(e,'height','size-'+DATA.size);bind(e,'strokeWeight','border-width-'+widthKey);paint(e,part.name==='Track'?'color-stroke-track':'color-stroke-primary-default');e.constraints={horizontal:'SCALE',vertical:'SCALE'};}
  const i=Number(phase.frame)-1;n.x=40+(i%6)*(dim+24);n.y=40+Math.floor(i/6)*(dim+24);phases.push({sourceId:phase.id,id:n.id,key:n.key,frame:phase.frame});
 }
 for(const phase of src.phases)await map[phase.id].setReactionsAsync([{trigger:{type:'AFTER_TIMEOUT',timeout:phase.timeout},actions:[{type:'NODE',destinationId:map[phase.to].id,navigation:'CHANGE_TO',transition:null}]}]);
 set.resize(80+6*(dim+24),80+4*(dim+24));set.x=3300;set.y=80+DATA.sizeIndex*730;set.fills=[];
 return {size:DATA.size,setId:set.id,setKey:set.key,firstId:map[src.phases[0].id].id,phases,createdNodeIds,mutatedNodeIds};
}
if(DATA.operation==='public'){
 await page.loadAsync();if(page.children.some(n=>n.name==='Loader'))throw new Error('Public Loader exists; reconcile ledger');
 const sizes=['extra-small','small','medium','large','extra-large','2x-large'],colors=['brand','neutral','strong','on-color'];
 const {componentSet,variants}=await createComponentWithVariants({name:'Loader',description:'LOADER-001@1.0.0 · Indicador circular indeterminado. Size 16/20/24/40/64/88 y color brand/neutral/strong/on-color. Brand sigue el tema; otros roles fijos. Animación nominal 0.8 s, 24 fases. Mensaje y semántica accesible pertenecen al host.',variantAxes:{size:sizes,color:colors},baseProps:{width:24,height:24,fills:[],layoutMode:'HORIZONTAL'},page});
 createdNodeIds.push(componentSet.id);const records=[];
 for(const n of variants){createdNodeIds.push(n.id);const axes=n.variantProperties,recipe=DATA.variants.find(v=>v.size===axes.size&&v.color===axes.color);n.resize(recipe.dimension,recipe.dimension);n.primaryAxisSizingMode='FIXED';n.counterAxisSizingMode='FIXED';n.primaryAxisAlignItems='CENTER';n.counterAxisAlignItems='CENTER';n.clipsContent=false;bind(n,'width','size-'+axes.size);bind(n,'height','size-'+axes.size);const first=await figma.getNodeByIdAsync(DATA.ledger.cycles[axes.size].firstId);const spinner=first.createInstance();n.appendChild(spinner);spinner.name='Spinner';mark(spinner);for(const e of spinner.findAll(c=>c.type==='ELLIPSE')){paint(e,e.name==='Track'?(axes.color==='on-color'?'color-stroke-inverse':'color-stroke-track'):{brand:'color-stroke-primary-default',neutral:'color-stroke-secondary',strong:'color-stroke-strong','on-color':'color-stroke-inverse'}[axes.color]);e.opacity=e.name==='Track'&&axes.color==='on-color'?0.30000001192092896:1;mutatedNodeIds.push(e.id);}n.x=40+colors.indexOf(axes.color)*160;n.y=40+sizes.indexOf(axes.size)*140;records.push({id:n.id,key:n.key,axes,sourceId:recipe.sourceId,spinnerId:spinner.id});}
 componentSet.resize(700,900);componentSet.x=2450;componentSet.y=80;componentSet.fills=[];
 return {setId:componentSet.id,setKey:componentSet.key,variants:records,properties:componentSet.componentPropertyDefinitions,createdNodeIds,mutatedNodeIds};
}
throw new Error('Unknown Loader build operation');
