// Scoped materializer. DATA contains registered Tab recipes and destination IDs.
// Never execute against the reference file. Mutations are limited to new Tab assets.
if (figma.fileKey !== '98xEw6sK8FRVNEhopM5SSz') throw new Error('Wrong destination');
figma.skipInvisibleInstanceChildren = false;
const created = [], mutated = [];
function mark(n) { created.push(n.id); return n; }
const variables = {};
if (DATA.variableIds) {
  const entries = await Promise.all(Object.entries(DATA.variableIds).map(async ([k,id]) => [k,await figma.variables.getVariableByIdAsync(id)]));
  for (const [k,v] of entries) { if (!v) throw new Error('Missing Tab variable '+k); variables[k]=v; }
}
for (const style of ['Regular','SemiBold','Bold']) await figma.loadFontAsync({family:'Manrope',style});

async function paints(node, record) {
  node.fills = record.fills || []; node.strokes = record.strokes || [];
  const b={};
  if(record.bindings['fills.0']) b.fills=variables[record.bindings['fills.0']].id;
  if(record.bindings['strokes.0']) b.strokes=variables[record.bindings['strokes.0']].id;
  await bindVariablesToComponent(node,b);
}
async function apply(node, record, textStyleId) {
  const p=record.props; node.name=p.name;
  if(node.type==='TEXT') {
    node.fontName={family:p.fontName.family,style:p.fontName.style};
    for(const key of ['fontSize','lineHeight','letterSpacing','textAlignHorizontal','textAlignVertical','textAutoResize','textTruncation','textCase','textDecoration']) if(p[key]!==undefined)node[key]=p[key];
    node.characters=p.characters;
  } else {
    node.resize(p.width,p.height);
    for(const key of ['layoutMode','primaryAxisSizingMode','counterAxisSizingMode','primaryAxisAlignItems','counterAxisAlignItems','itemSpacing','paddingTop','paddingRight','paddingBottom','paddingLeft','clipsContent','strokesIncludedInLayout','strokeAlign','strokeTopWeight','strokeRightWeight','strokeBottomWeight','strokeLeftWeight','topLeftRadius','topRightRadius','bottomLeftRadius','bottomRightRadius','minWidth','minHeight']) {
      if(key==='strokesIncludedInLayout' && node.layoutMode==='NONE')continue;
      if(p[key]!==undefined && p[key]!==null && key in node) node[key]=p[key];
    }
  }
  for(const key of ['visible','opacity','blendMode']) if(p[key]!==undefined)node[key]=p[key];
  await paints(node,record);
  const helperFields=['paddingTop','paddingRight','paddingBottom','paddingLeft','itemSpacing'];
  const helperBindings={};
  for(const key of helperFields) if(record.bindings[key])helperBindings[key]=variables[record.bindings[key]].id;
  await bindVariablesToComponent(node,helperBindings);
  for(const [field,token] of Object.entries(record.bindings)) {
    if(field.includes('.') || helperFields.includes(field))continue;
    node.setBoundVariable(field,variables[token]);
  }
  // Applying typography fields after a style detaches its ID. Link last, with
  // the same variables bound on the shared style, preserving both contracts.
  if(node.type==='TEXT' && textStyleId)await node.setTextStyleIdAsync(textStyleId);
  // Size binding can normalize instance-frame stroke metadata. Preserve the
  // source's uniform, unpainted frame default after the size operation.
  if(node.type==='INSTANCE' && p.name==='Icon' && !record.strokes.length)node.strokeWeight=p.strokeTopWeight;
  if(record.effectStyle) await node.setEffectStyleIdAsync(DATA.styleIds.shadow);
  const inAutoLayout=node.parent && 'layoutMode' in node.parent && node.parent.layoutMode!=='NONE';
  const isAutoLayout='layoutMode' in node && node.layoutMode!=='NONE';
  if(p.layoutSizingHorizontal && (inAutoLayout || isAutoLayout))node.layoutSizingHorizontal=p.layoutSizingHorizontal;
  if(p.layoutSizingVertical && (inAutoLayout || isAutoLayout))node.layoutSizingVertical=p.layoutSizingVertical;
  mutated.push(node.id); return node;
}

async function foundation() {
  const collections=await figma.variables.getLocalVariableCollectionsAsync();
  if(collections.some(c=>c.name==='tab') || figma.root.children.some(p=>p.name==='Tabs')) throw new Error('Tab assets already exist; inspect ledger before retry');
  const before=await figma.variables.getLocalVariablesAsync();
  if(before.length!==298)throw new Error('Baseline variable count changed');
  // Compact transport guard; full before/after preservation uses SHA-256 in QA.
  function fingerprint(value){let hash=2166136261;for(let i=0;i<value.length;i++)hash=Math.imul(hash^value.charCodeAt(i),16777619);return hash>>>0;}
  for(const [id,expected] of Object.entries(DATA.baseline)) {
    const actual=before.find(v=>v.id===id);
    const observed={name:actual?.name,type:actual?.resolvedType,collectionId:actual?.variableCollectionId,scopes:actual?.scopes,valuesByMode:actual?.valuesByMode,codeSyntax:actual?.codeSyntax,description:actual?.description};
    if(fingerprint(JSON.stringify(observed))!==expected)throw new Error('Baseline changed: '+id);
  }
  const semantic={};
  for(const [logical,id] of Object.entries(DATA.semanticIds)) {
    const v=before.find(v=>v.id===id);
    if(!v || v.scopes.length)throw new Error('Semantic unavailable or scoped: '+logical);
    semantic[logical]=v;
  }
  const {collection,modeIds}=await createVariableCollection('tab',DATA.modes);
  const variableIds={};
  for(const token of DATA.tokens) {
    const variable=figma.variables.createVariable(token.figmaName,collection,({number:'FLOAT',color:'COLOR',string:'STRING'})[token.type]);
    variable.scopes=token.scopes; variable.description=token.description;
    variable.setVariableCodeSyntax('WEB',token.web);
    for(const mode of DATA.modes)variable.setValueForMode(modeIds[mode],figma.variables.createVariableAlias(semantic[token.values[mode].alias]));
    variables[token.id]=variable; variableIds[token.id]=variable.id;
  }
  const page=figma.createPage();page.name='Tabs';await figma.setCurrentPageAsync(page);
  const styleIds={};
  for(const [role,style,size,height] of [['regular','Regular',14,20],['selected','SemiBold',14,20],['count','Bold',10,16]]) {
    const s=figma.createTextStyle();s.name='tab/'+(role==='count'?'count':'label/'+role);s.fontName={family:'Manrope',style};s.fontSize=size;s.lineHeight={unit:'PIXELS',value:height};s.letterSpacing={unit:'PIXELS',value:0};
    const suffix=role==='count'?'count':'label';
    const fields={fontFamily:'family',fontStyle:role==='count'?'count-style':role==='selected'?'selected-style':'label-style',fontSize:'size-'+suffix,lineHeight:'line-height-'+suffix,letterSpacing:'letter-spacing'};
    for(const[field,token]of Object.entries(fields))s.setBoundVariable(field,variables['tab.font-tab-'+token]);
    styleIds[role]=s.id;
  }
  const shadow=figma.createEffectStyle();shadow.name='tab/elevation/selected';
  shadow.effects=DATA.shadowStyle.effects.map(({boundVariables,...effect})=>effect);styleIds.shadow=shadow.id;
  const count=mark(figma.createComponent());page.appendChild(count);count.layoutMode='HORIZONTAL';
  const countText=mark(figma.createText());count.appendChild(countText);
  await apply(countText,DATA.countText,styleIds.count);await apply(count,DATA.count);
  count.name='__Tab/Count';count.visible=true;count.x=1600;count.y=900;
  count.description='Dependencia privada de TAB-001@1.0.0. Solo Count textual observado; no representa la familia Dot. Conserva HUG, mínimo 16 y las recetas registradas.';
  const countProperty=count.addComponentProperty('Count','TEXT','1');countText.componentPropertyReferences={characters:countProperty};
  return {pageId:page.id,collectionId:collection.id,modeIds,variableIds,styleIds,countId:count.id,countTextId:countText.id,countProperty,createdNodeIds:created,mutatedNodeIds:mutated,createdVariableIds:Object.values(variableIds),createdStyleIds:Object.values(styleIds)};
}

async function family() {
  const page=await figma.getNodeByIdAsync(DATA.pageId);
  if(page.children.some(n=>n.name==='Tab'))throw new Error('Tab family already exists');
  const result=await createComponentWithVariants({name:'Tab',description:'TAB-001@1.0.0 · 24 variantes · 43 tokens. type × selected × state. Selección y paneles pertenecen al consumidor; ver contrato MD.',variantAxes:{type:['underline','pill','segmented'],selected:['false','true'],state:['default','hover','focus','disabled']},baseProps:{width:100,height:52,fills:[]},page});
  result.componentSet.x=1600;result.componentSet.y=80;result.componentSet.resize(640,640);
  for(const [i,n] of result.variants.entries()){n.x=40+(i%4)*144;n.y=40+Math.floor(i/4)*92;created.push(n.id);}
  created.push(result.componentSet.id);
  return {setId:result.componentSet.id,variants:result.variants.map(n=>({id:n.id,axes:n.variantProperties})),createdNodeIds:created,mutatedNodeIds:[result.componentSet.id]};
}

async function populate() {
  const page=await figma.getNodeByIdAsync(DATA.pageId);await figma.setCurrentPageAsync(page);
  const set=await figma.getNodeByIdAsync(DATA.setId), countMain=await figma.getNodeByIdAsync(DATA.countId);
  const glyph=await figma.importComponentByKeyAsync('f273018f11d7d4e938078bd0b21b0b3a9e7f2634');
  if(!glyph.remote)throw new Error('Phosphor must remain a remote dependency');
  let properties=DATA.properties;
  if(!properties)properties={Label:set.addComponentProperty('Label','TEXT','Tab'),ShowIcon:set.addComponentProperty('Show icon','BOOLEAN',false),Icon:set.addComponentProperty('Icon','INSTANCE_SWAP',glyph.id),ShowBadge:set.addComponentProperty('Show badge','BOOLEAN',false)};
  const sourceToTarget={};
  for(const recipe of DATA.variants) {
    const target=await figma.getNodeByIdAsync(DATA.variantIds[recipe.sourceId]);
    if(target.children.length)throw new Error('Variant already populated '+target.id);
    const r=recipe.roles;
    const icon=mark(glyph.createInstance());icon.rescale(20/32);target.appendChild(icon);
    await apply(icon,DATA.nodes[r.icon]);
    const shape=icon.findOne(n=>n.type==='VECTOR');if(!shape)throw new Error('Missing Phosphor vector');
    await paints(shape,DATA.nodes[r.iconShape]);mutated.push(shape.id);
    const label=mark(figma.createText());target.appendChild(label);await apply(label,DATA.nodes[r.label],DATA.styleIds[recipe.axes.selected==='true'?'selected':'regular']);
    const badge=mark(countMain.createInstance());target.appendChild(badge);badge.name='Badge';badge.visible=false;badge.isExposedInstance=true;
    const badgeText=badge.findOne(n=>n.type==='TEXT');
    icon.componentPropertyReferences={visible:properties.ShowIcon,mainComponent:properties.Icon};label.componentPropertyReferences={characters:properties.Label};badge.componentPropertyReferences={visible:properties.ShowBadge};
    await apply(target,DATA.nodes[r.container]);
    if(r.focus) {
      const ring=mark(figma.createFrame());target.appendChild(ring);ring.layoutPositioning='ABSOLUTE';await apply(ring,DATA.nodes[r.focus]);
      ring.resize(target.width+8,target.height+8);ring.x=-4;ring.y=-4;ring.constraints={horizontal:'STRETCH',vertical:'STRETCH'};sourceToTarget[r.focus]=ring.id;
    }
    Object.assign(sourceToTarget,{[r.container]:target.id,[r.icon]:icon.id,[r.iconShape]:shape.id,[r.label]:label.id,[r.count]:badge.id,[r.countLabel]:badgeText.id});
    if(recipe.reactions.length)await target.setReactionsAsync(recipe.reactions.map(reaction=>({trigger:reaction.trigger,actions:reaction.actions.map(action=>({...action,destinationId:DATA.variantIds[action.destinationId]}))})));
  }
  return {properties,sourceToTarget,createdNodeIds:created,mutatedNodeIds:mutated,remoteGlyph:{id:glyph.id,key:glyph.key,remote:glyph.remote}};
}
return await ({foundation,family,populate})[DATA.operation]();
