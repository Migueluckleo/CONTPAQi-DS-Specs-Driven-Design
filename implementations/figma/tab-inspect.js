// Read-only destination evidence. DATA selects bounded batches, not mutations.
figma.skipInvisibleInstanceChildren=false;
if(figma.fileKey!=='98xEw6sK8FRVNEhopM5SSz')throw new Error('Wrong destination');
if(DATA.operation==='variables'){
 const vars=await figma.variables.getLocalVariablesAsync();
 return {variables:vars.slice(DATA.start,DATA.start+75).map(v=>({id:v.id,key:v.key,name:v.name,type:v.resolvedType,collectionId:v.variableCollectionId,scopes:v.scopes,valuesByMode:v.valuesByMode,codeSyntax:v.codeSyntax,description:v.description})),total:vars.length,readOnly:true};
}
if(DATA.operation==='nodes'){
 const all={};function visit(n){all[n.id]=n;if('children'in n)n.children.forEach(visit);}
 for(const id of DATA.rootIds)visit(await figma.getNodeByIdAsync(id));
 const nodes=[];
 for(const r of DATA.records){const n=all[r.targetId];if(!n)throw new Error('Missing target '+r.targetId);const props={};for(const field of r.fields)if(field in n)props[field]=n[field];
  let main=null;if(n.type==='INSTANCE'){const m=await n.getMainComponentAsync();main={id:m.id,key:m.key,remote:m.remote};}
  nodes.push({sourceId:r.sourceId,id:n.id,type:n.type,props,fills:n.fills,strokes:n.strokes,boundVariables:n.boundVariables,textStyleId:'textStyleId'in n?n.textStyleId:null,effectStyleId:'effectStyleId'in n?n.effectStyleId:null,effects:n.effects,componentPropertyReferences:n.componentPropertyReferences,reactions:'reactions'in n?n.reactions:[],main,fontWeight:'fontWeight'in n?n.fontWeight:null,children:'children'in n?n.children.map(c=>({id:c.id,name:c.name,type:c.type})):[]});
 }
 return{nodes,readOnly:true};
}
if(DATA.operation==='consumers'){
 const all={};function visit(n){all[n.id]=n;if('children'in n)n.children.forEach(visit);}
 const records=[];
 for(const item of DATA.instances){const n=await figma.getNodeByIdAsync(item.id);visit(n);const role=name=>n.children.find(c=>c.name===name);const label=role('Label'),icon=role('Icon'),badge=role('Badge'),ring=role('Focus ring');const iconMain=await icon.getMainComponentAsync();const badgeMain=await badge.getMainComponentAsync();
  const simple=c=>c?{id:c.id,name:c.name,type:c.type,width:c.width,height:c.height,x:c.x,y:c.y,visible:c.visible,fills:c.fills,strokes:c.strokes,boundVariables:c.boundVariables,characters:'characters'in c?c.characters:null,fontName:'fontName'in c?c.fontName:null,fontSize:'fontSize'in c?c.fontSize:null,lineHeight:'lineHeight'in c?c.lineHeight:null,letterSpacing:'letterSpacing'in c?c.letterSpacing:null,fontWeight:'fontWeight'in c?c.fontWeight:null}:null;
  records.push({...item,width:n.width,height:n.height,bounds:n.absoluteBoundingBox,properties:n.componentProperties,mainId:(await n.getMainComponentAsync()).id,label:simple(label),icon:{...simple(icon),mainKey:iconMain.key,remote:iconMain.remote,shapes:icon.findAll(c=>c.type==='VECTOR').map(simple)},count:{...simple(badge),mainId:badgeMain.id,text:simple(badge.findOne(c=>c.type==='TEXT'))},ring:simple(ring)});
 }
 const resolution=[];
 for(const {mode,id} of DATA.themeConsumers){const consumer=await figma.getNodeByIdAsync(id);for(const[logical,varId]of Object.entries(DATA.variableIds)){const v=await figma.variables.getVariableByIdAsync(varId);resolution.push({mode,token:logical,...v.resolveForConsumer(consumer)});}}
 const set=await figma.getNodeByIdAsync(DATA.setId);
 return{records,resolution,properties:set.componentPropertyDefinitions,textStyles:(await figma.getLocalTextStylesAsync()).map(s=>({id:s.id,name:s.name,fontName:s.fontName,fontSize:s.fontSize,lineHeight:s.lineHeight,letterSpacing:s.letterSpacing})),effectStyles:(await figma.getLocalEffectStylesAsync()).map(s=>({id:s.id,name:s.name,effects:s.effects})),readOnly:true};
}
if(DATA.operation==='preservation'){
 const buttons=[];for(const id of DATA.buttonIds){const n=await figma.getNodeByIdAsync(id);buttons.push({id:n.id,name:n.name,description:n.description,properties:n.componentPropertyDefinitions,variants:n.children.map(c=>({id:c.id,name:c.name,width:c.width,height:c.height,reactions:c.reactions,variantProperties:c.variantProperties}))});}
 return{button:buttons,pages:figma.root.children.map(p=>({id:p.id,name:p.name})),collections:(await figma.variables.getLocalVariableCollectionsAsync()).map(c=>({id:c.id,name:c.name,modes:c.modes,variableIds:c.variableIds})),readOnly:true};
}
