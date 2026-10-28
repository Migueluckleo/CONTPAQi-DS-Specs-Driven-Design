// TABS-001: native group slots built from existing linked Tab masters.
if(figma.fileKey!=='98xEw6sK8FRVNEhopM5SSz')throw new Error('Wrong destination');
figma.skipInvisibleInstanceChildren=false;
for(const style of ['Regular','SemiBold','Bold'])await figma.loadFontAsync({family:'Manrope',style});
const page=await figma.getNodeByIdAsync('78:97');await page.loadAsync();
if(page.findAllWithCriteria({types:['COMPONENT_SET']}).some(n=>n.name==='Tabs'))throw new Error('Tabs group already exists; inspect ledger');
const collection=(await figma.variables.getLocalVariableCollectionsAsync()).find(c=>c.name==='component');if(!collection||collection.modes.length!==4)throw new Error('BH-P07: missing shared component collection/modes');const modeIds=Object.fromEntries(collection.modes.map(m=>[m.name,m.modeId]));
const routes=DATA.tokens.map(t=>t.figmaName);const existingVariables=await figma.variables.getLocalVariablesAsync();if(new Set(routes).size!==routes.length||existingVariables.some(v=>v.variableCollectionId===collection.id&&routes.includes(v.name)))throw new Error('BH-P07: duplicate component route; reconcile the manifest');
const variables={},variableIds={};
for(const t of DATA.tokens){const v=figma.variables.createVariable(t.figmaName,collection,t.type==='color'?'COLOR':'FLOAT');v.description=t.description;v.scopes=t.scopes;v.setVariableCodeSyntax('WEB',t.web);for(const mode of collection.modes){const semantic=await figma.variables.getVariableByIdAsync(DATA.semanticIds[t.values[mode.name].alias]);v.setValueForMode(mode.modeId,figma.variables.createVariableAlias(semantic));}variables[t.id]=v;variableIds[t.id]=v.id;}
const {componentSet,variants}=await createComponentWithVariants({name:'Tabs',description:'TABS-001@1.0.0 · Grupo con slot editable. Cuatro tabs por defecto, mínimo dos, máximo no impuesto. Ver contrato MD; el consumidor coordina tipo, selección y panel.',variantAxes:{type:['underline','pill','segmented']},baseProps:{width:277,height:44,fills:[],layoutMode:'HORIZONTAL'},page});
componentSet.x=2350;componentSet.y=80;componentSet.resize(365,252);
const tabSet=await figma.getNodeByIdAsync('79:26');
const slotKey=componentSet.addComponentProperty('Tabs','SLOT','',{description:'Agrega, quita o reordena Tab del mismo type; conserva una selección.',slotSettings:{stretchChildOnInsert:false,displayEmptyByDefault:false,minChildren:2,maxChildren:null,allowPreferredValuesOnly:false},preferredValues:[{type:'COMPONENT_SET',key:tabSet.key}]});
const created=[componentSet.id,...variants.map(n=>n.id)],groups=[];
const P=DATA.propertyKeys;
for(const [index,component]of variants.entries()){
 const type=component.variantProperties.type;
 component.layoutMode='HORIZONTAL';component.primaryAxisSizingMode='AUTO';component.counterAxisSizingMode='AUTO';component.primaryAxisAlignItems='MIN';component.counterAxisAlignItems='CENTER';component.itemSpacing=0;component.clipsContent=false;component.fills=[];
 const slot=component.createSlot();created.push(slot.id);slot.name='Tabs';const automaticKey=slot.componentPropertyReferences.slotContentId;slot.layoutMode='HORIZONTAL';slot.fills=[];slot.clipsContent=false;slot.primaryAxisSizingMode='AUTO';slot.counterAxisSizingMode='AUTO';slot.counterAxisAlignItems='CENTER';slot.itemSpacing=type==='underline'?0:4;
 slot.componentPropertyReferences={slotContentId:slotKey};
 if(automaticKey!==slotKey){
  if(automaticKey in componentSet.componentPropertyDefinitions)componentSet.deleteComponentProperty(automaticKey);
 }
 if(slot.type!=='SLOT')throw new Error('Expected native SLOT after property binding');
 if(type!=='underline')slot.setBoundVariable('itemSpacing',variables['tabs.spacing-tabs-container']);
 const children=[];
 for(let i=0;i<4;i++){
  const master=tabSet.children.find(n=>n.variantProperties.type===type&&n.variantProperties.selected===(i===0?'true':'false')&&n.variantProperties.state==='default');
  const child=master.createInstance();slot.appendChild(child);child.name='Tab '+(i+1);child.setProperties({type,selected:i===0?'true':'false',state:'default',[P.Label]:'Tab '+(i+1)});children.push(child.id);created.push(child.id);
 }
 if(type==='segmented'){
  await bindVariablesToComponent(component,{fills:variables['tabs.color-tabs-bg-segmented-default'].id,paddingTop:variables['tabs.spacing-tabs-container'].id,paddingBottom:variables['tabs.spacing-tabs-container'].id,paddingLeft:variables['tabs.spacing-tabs-container'].id,paddingRight:variables['tabs.spacing-tabs-container'].id,cornerRadius:variables['tabs.radius-tabs-container'].id});
 }
 let divider=null;
 if(type==='underline'){
  divider=figma.createRectangle();component.appendChild(divider);created.push(divider.id);divider.name='Divider';divider.layoutPositioning='ABSOLUTE';divider.resize(component.width,1);divider.x=0;divider.y=component.height-1;divider.constraints={horizontal:'STRETCH',vertical:'MAX'};divider.fills=[{type:'SOLID',color:{r:.5,g:.5,b:.5}}];divider.setBoundVariable('height',variables['tabs.size-tabs-divider']);await bindVariablesToComponent(divider,{fills:variables['tabs.color-tabs-divider-default'].id});component.insertChild(0,divider);
 }
 component.x=24;component.y=[24,100,168][index];
 groups.push({id:component.id,key:component.key,type,width:component.width,height:component.height,slotId:slot.id,slotType:slot.type,limitViolations:slot.limitViolations,children,dividerId:divider?.id});
}
return{setId:componentSet.id,setKey:componentSet.key,collectionId:collection.id,modeIds,variableIds,slotKey,groups,properties:componentSet.componentPropertyDefinitions,createdNodeIds:created,mutatedNodeIds:created,createdVariableIds:Object.values(variableIds)};
