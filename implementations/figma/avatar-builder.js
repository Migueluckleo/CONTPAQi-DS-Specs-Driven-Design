// Scoped materializer for AVATAR-001 / AVATAR-GROUP-001. DATA is a derived recipe.
// Helpers createVariableCollection/createComponentWithVariants are loaded verbatim
// from figma-generate-library; this script never executes against the source file.
if(figma.fileKey!=='98xEw6sK8FRVNEhopM5SSz')throw new Error('Wrong destination');
figma.skipInvisibleInstanceChildren=false;
const created=[],mutated=[],vars={};
const mark=n=>{created.push(n.id);return n;};
for(const [id,native]of Object.entries(DATA.variableIds||{}))vars[id]=await figma.variables.getVariableByIdAsync(native);
for(const style of ['Regular','SemiBold'])await figma.loadFontAsync({family:'Manrope',style});
const A=route=>vars['avatar.'+route.replaceAll('/','-')];
const G=route=>vars['avatar-group.'+route.replaceAll('/','-')];
function paint(n,field,v){n[field]=[figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:1,g:1,b:1}},'color',v)];mutated.push(n.id);}
function bind(n,field,v){n.setBoundVariable(field,v);mutated.push(n.id);}
function sizeToken(size){return A('size/'+size);}
function contentToken(number){return A('size/'+({48:'extra-large',32:'large',24:'medium',20:'small',16:'content-regular',12:'content-compact',8:'content-small'})[number]);}
function dims(n,w,h){n.resize(w,h);bind(n,'width',contentToken(w));bind(n,'height',contentToken(h));}
function round(n){bind(n,'cornerRadius',A('radius/container'));}
function border(n){paint(n,'strokes',A('color/stroke/separator'));bind(n,'strokeWeight',A('border/width-regular'));}
function zero(n){for(const f of ['paddingTop','paddingRight','paddingBottom','paddingLeft','itemSpacing'])bind(n,f,A('spacing/none'));}

async function foundation(){
 const collections=await figma.variables.getLocalVariableCollectionsAsync();
 if(figma.root.children.some(p=>p.name==='Avatars')||collections.some(c=>['avatar','avatar-group'].includes(c.name)))throw new Error('Avatar assets exist: inspect ledger before retry');
 const before=await figma.variables.getLocalVariablesAsync();if(before.length!==348)throw new Error('Unexpected baseline');
 const foundationIds={};
 for(const t of DATA.foundationTokens){
  const c=collections.find(c=>c.name===t.collection);if(!c)throw new Error('Missing base collection');
  if(before.some(v=>v.name===t.name&&v.variableCollectionId===c.id))throw new Error('Foundation name already exists');
  const v=figma.variables.createVariable(t.name,c,'FLOAT');v.scopes=[];v.description=t.description;v.setVariableCodeSyntax('WEB','var(--'+t.name+')');
  const value=t.values.Value;v.setValueForMode(c.modes[0].modeId,typeof value==='number'?value:figma.variables.createVariableAlias(await figma.variables.getVariableByIdAsync(foundationIds[value.alias])));
  foundationIds[t.id]=v.id;
 }
 const semanticIds={...DATA.semanticIds,...foundationIds}, variableIds={}, nativeCollections={};
 for(const [family,modes]of [['avatar',DATA.modes],['avatar-group',['Value']]]){
  const {collection,modeIds}=await createVariableCollection(family,modes);nativeCollections[family]={id:collection.id,modeIds};
  for(const t of DATA.tokens.filter(t=>t.collection===family)){
   const v=figma.variables.createVariable(t.figmaName,collection,({number:'FLOAT',color:'COLOR',string:'STRING'})[t.type]);v.scopes=t.scopes;v.description=t.description;v.setVariableCodeSyntax('WEB',t.web);
   for(const mode of modes){const alias=await figma.variables.getVariableByIdAsync(semanticIds[t.values[mode].alias]);if(!alias)throw new Error('Unresolved semantic '+t.values[mode].alias);v.setValueForMode(modeIds[mode],figma.variables.createVariableAlias(alias));}
   vars[t.id]=v;variableIds[t.id]=v.id;
  }
 }
 const page=mark(figma.createPage());page.name='Avatars';
 const styles={};
 for(const [role,size,height]of [['extra-large',20,20],['large',14,16],['compact',10,16]]){
  const s=figma.createTextStyle();s.name='avatar/initials/'+role;s.fontName={family:'Manrope',style:'SemiBold'};s.fontSize=size;s.lineHeight={unit:'PIXELS',value:height};s.letterSpacing={unit:'PIXELS',value:0};s.textCase='ORIGINAL';
  for(const [field,route]of Object.entries({fontFamily:'family',fontStyle:'initials-style',fontSize:'size-'+role,lineHeight:'line-height-'+(role==='extra-large'?'extra-large':'compact'),letterSpacing:'letter-spacing'}))s.setBoundVariable(field,A('font/'+route));
  styles[role]=s.id;
 }
 // This helper sets page context once. Nine variants are the observed presence subset.
 const r=await createComponentWithVariants({name:'__Avatar/Presence',description:'Dependencia privada de AVATAR-001@1.0.0: presencia active/busy/inactive, no familia Dot completa. Color acompañado de texto en el consumidor.',variantAxes:{type:['active','busy','inactive'],size:['large','medium','small']},baseProps:{width:16,height:16,fills:[],layoutMode:'HORIZONTAL'},page});
 created.push(r.componentSet.id,...r.variants.map(n=>n.id));r.componentSet.x=4200;r.componentSet.y=1600;r.componentSet.resize(340,260);
 const presence=[];
 for(const [i,c]of r.variants.entries()){
  const axes=c.variantProperties;const num={large:16,medium:12,small:8}[axes.size];dims(c,num,num);c.layoutMode='HORIZONTAL';c.primaryAxisSizingMode='FIXED';c.counterAxisSizingMode='FIXED';zero(c);round(c);border(c);c.strokeAlign='OUTSIDE';c.clipsContent=false;paint(c,'fills',A('color/bg/status-'+axes.type));c.x=32+(i%3)*90;c.y=32+Math.floor(i/3)*72;presence.push({id:c.id,key:c.key,axes});
 }
 return {pageId:page.id,collections:nativeCollections,foundationIds,variableIds,styleIds:styles,presenceSetId:r.componentSet.id,presence,createdNodeIds:created,mutatedNodeIds:[...new Set(mutated)],createdVariableIds:[...Object.values(foundationIds),...Object.values(variableIds)],createdStyleIds:Object.values(styles)};
}

async function avatar(){
 const page=await figma.getNodeByIdAsync(DATA.pageId);await page.loadAsync();
 if(page.children.some(n=>n.type==='COMPONENT_SET'&&n.name==='Avatar'))throw new Error('Avatar already exists');
 const glyph=await figma.importComponentByKeyAsync('77a821b72c03fcfbd0ca9b2910c3fb5c98ed210f');
 if(!glyph.remote)throw new Error('Phosphor User must remain remote');
 const r=await createComponentWithVariants({name:'Avatar',description:DATA.description,variantAxes:{type:['image','icon','text'],size:['extra-large','large','medium','small']},baseProps:{width:48,height:48,fills:[],layoutMode:'VERTICAL'},page});
 const set=r.componentSet;created.push(set.id,...r.variants.map(n=>n.id));set.x=4200;set.y=1050;set.resize(600,420);
 const props={Initials:set.addComponentProperty('Initials','TEXT','JA'),Icon:set.addComponentProperty('Icon','INSTANCE_SWAP',glyph.id,{preferredValues:DATA.iconPreferred}),ShowStatus:set.addComponentProperty('Show status','BOOLEAN',true)};
 const ledger=[],sourceToTarget={};
 for(const [i,c]of r.variants.entries()){
  const axes=c.variantProperties,recipe=DATA.variants.find(v=>v.axes.type===axes.type&&v.axes.size===axes.size),num=recipe.content.width;
  c.layoutMode='VERTICAL';c.primaryAxisSizingMode='AUTO';c.counterAxisSizingMode='AUTO';c.primaryAxisAlignItems='MIN';c.counterAxisAlignItems='MIN';c.clipsContent=false;c.fills=[];zero(c);c.strokesIncludedInLayout=recipe.root.strokesIncludedInLayout;c.strokeWeight=recipe.root.strokeWeight;c.strokeAlign=recipe.root.strokeAlign;
  const content=mark(figma.createAutoLayout('VERTICAL'));c.appendChild(content);content.name='Avatar';dims(content,num,num);content.primaryAxisSizingMode='FIXED';content.counterAxisSizingMode='FIXED';content.primaryAxisAlignItems='CENTER';content.counterAxisAlignItems='CENTER';zero(content);round(content);border(content);content.strokeAlign='INSIDE';content.strokesIncludedInLayout=false;content.clipsContent=true;
  if(axes.type==='image')content.fills=[];
  else paint(content,'fills',A('color/bg/primary-default'));
  let text=null,icon=null;
  if(axes.type==='text'){
   const record=recipe.kids.find(n=>n.type==='TEXT');text=mark(figma.createText());content.appendChild(text);text.name='Initials';text.strokeWeight=record.strokeWeight;text.strokeAlign=record.strokeAlign;text.fontName={family:'Manrope',style:'SemiBold'};text.characters=record.characters;text.textAutoResize='WIDTH_AND_HEIGHT';text.componentPropertyReferences={characters:props.Initials};
   await text.setTextStyleIdAsync(DATA.styleIds[['medium','small'].includes(axes.size)?'compact':axes.size]);paint(text,'fills',A('color/text/inverse'));text.layoutSizingHorizontal='HUG';text.layoutSizingVertical='HUG';sourceToTarget[record.id]=text.id;
  }
  if(axes.type==='icon'){
   const record=recipe.kids.find(n=>n.type==='INSTANCE');icon=mark(glyph.createInstance());content.appendChild(icon);icon.name='Icon';icon.rescale(record.width/32);dims(icon,record.width,record.height);icon.strokeWeight=1;icon.componentPropertyReferences={mainComponent:props.Icon};
   for(const n of icon.findAll(n=>n.type==='VECTOR'))paint(n,'fills',A('color/icon/inverse'));
   sourceToTarget[record.id]=icon.id;
  }
  const ps=DATA.presence.find(p=>p.axes.type==='active'&&p.axes.size===recipe.status.properties.size.value);const main=await figma.getNodeByIdAsync(ps.id);const status=mark(main.createInstance());c.appendChild(status);status.name='Status';status.layoutPositioning='ABSOLUTE';status.x=recipe.status.x;status.y=recipe.status.y;status.constraints={horizontal:'MAX',vertical:'MAX'};status.componentPropertyReferences={visible:props.ShowStatus};status.isExposedInstance=true;
  c.x=32+(i%4)*130;c.y=32+Math.floor(i/4)*114;
  Object.assign(sourceToTarget,{[recipe.sourceId]:c.id,[recipe.content.id]:content.id,[recipe.status.id]:status.id});ledger.push({id:c.id,key:c.key,axes,contentId:content.id,textId:text?.id,iconId:icon?.id,statusId:status.id});
 }
 return {setId:set.id,setKey:set.key,propertyKeys:props,variants:ledger,sourceToTarget,remoteGlyph:{id:glyph.id,key:glyph.key,remote:glyph.remote},createdNodeIds:created,mutatedNodeIds:[...new Set(mutated)]};
}

async function group(){
 const page=await figma.getNodeByIdAsync(DATA.pageId);await page.loadAsync();
 if(page.children.some(n=>n.type==='COMPONENT_SET'&&n.name==='Avatar group'))throw new Error('Group already exists');
 const aSet=await figma.getNodeByIdAsync(DATA.setId);
 const r=await createComponentWithVariants({name:'Avatar group',description:DATA.description,variantAxes:{size:['extra-large','large','medium','small']},baseProps:{width:168,height:48,fills:[],layoutMode:'HORIZONTAL'},page});
 created.push(r.componentSet.id,...r.variants.map(n=>n.id));r.componentSet.x=4900;r.componentSet.y=1050;r.componentSet.resize(350,350);
 const slotKey=r.componentSet.addComponentProperty('Avatars','SLOT','',{description:'2–4 Avatar, tamaño coherente y sin Status. Para >4 personas: tres + contador +N calculado por el consumidor.',slotSettings:{stretchChildOnInsert:false,displayEmptyByDefault:false,minChildren:2,maxChildren:4,allowPreferredValuesOnly:true},preferredValues:[{type:'COMPONENT_SET',key:aSet.key}]});
 const groups=[];
 for(const [i,c]of r.variants.entries()){
  const size=c.variantProperties.size;c.primaryAxisSizingMode='AUTO';c.counterAxisSizingMode='AUTO';c.counterAxisAlignItems='CENTER';c.clipsContent=false;c.fills=[];
  const slot=mark(c.createSlot());slot.name='Avatars';const auto=slot.componentPropertyReferences.slotContentId;slot.componentPropertyReferences={slotContentId:slotKey};if(auto!==slotKey&&auto in r.componentSet.componentPropertyDefinitions)r.componentSet.deleteComponentProperty(auto);
  slot.layoutMode='HORIZONTAL';slot.primaryAxisSizingMode='AUTO';slot.counterAxisSizingMode='AUTO';slot.counterAxisAlignItems='CENTER';slot.clipsContent=false;slot.fills=[];slot.itemReverseZIndex=false;bind(slot,'itemSpacing',G('spacing/overlap-'+(['medium','small'].includes(size)?'compact':size)));
  const master=await figma.getNodeByIdAsync(DATA.variants.find(v=>v.axes.type==='text'&&v.axes.size===size).id);const children=[];
  for(let j=0;j<4;j++){
   const child=mark(master.createInstance());slot.appendChild(child);child.name=j===3?'Overflow':'Avatar '+(j+1);child.setProperties({[DATA.propertyKeys.Initials]:['JA','MA','KM','+4'][j],[DATA.propertyKeys.ShowStatus]:false});
   const content=child.findOne(n=>n.type==='FRAME'&&n.name==='Avatar'),text=child.findOne(n=>n.type==='TEXT'&&n.name==='Initials');
   if(j>0)paint(content,'fills',G('color/bg/'+(['alternate-warning','alternate-positive','overflow-default'][j-1])));
   if(j===3)paint(text,'fills',G('color/text/overflow-default'));
   children.push(child.id);
  }
  c.x=32;c.y=32+i*76;groups.push({id:c.id,key:c.key,size,slotId:slot.id,children,width:c.width,height:c.height});
 }
 return {setId:r.componentSet.id,setKey:r.componentSet.key,slotKey,groups,createdNodeIds:created,mutatedNodeIds:[...new Set(mutated)]};
}
return await ({foundation,avatar,group})[DATA.operation]();
