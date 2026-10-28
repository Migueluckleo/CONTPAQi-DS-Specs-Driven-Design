if (figma.fileKey !== DATA.fileKey) throw new Error("Wrong target");
const page = await figma.getNodeByIdAsync(DATA.pageId);
await figma.setCurrentPageAsync(page);
figma.skipInvisibleInstanceChildren = false;
const issues = [], summary = []; let bindingsChecked = 0;
const near = (a, b) => Math.abs(a - b) <= 0.00001;
function equal(a, b) {
  if (typeof a === "number" && typeof b === "number") return near(a, b);
  if (Array.isArray(a) && Array.isArray(b)) return a.length === b.length && a.every((x, i) => equal(x, b[i]));
  if (a && b && typeof a === "object" && typeof b === "object") return Object.keys(a).length === Object.keys(b).length && Object.keys(a).every(k => equal(a[k], b[k]));
  return a === b;
}
function check(id, field, actual, expected) {
  if (!equal(actual, expected)) issues.push({id, field, actual, expected});
}
function binding(node, field) {
  if (field === "fills" || field === "strokes") return node[field][0]?.boundVariables?.color?.id;
  if (field === "strokeWeight" && !node.boundVariables?.strokeWeight) {
    const ids = ["strokeTopWeight","strokeRightWeight","strokeBottomWeight","strokeLeftWeight"].map(k=>node.boundVariables?.[k]?.id);
    if (ids[0] && ids.every(id=>id===ids[0])) return ids[0];
  }
  const value = node.boundVariables?.[field]; return Array.isArray(value) ? value[0]?.id : value?.id;
}
function checkBindings(node, expected) {
  for (const [field, token] of Object.entries(expected)) {
    check(node.id, "binding:" + field, binding(node, field), DATA.tokenIds[token]); bindingsChecked++;
  }
}
for (const recipe of DATA.variants) {
  const record = DATA.mapping.find(v => v.sourceId === recipe.sourceId);
  const node = await figma.getNodeByIdAsync(record.id);
  check(node.id, "type", node.type, "COMPONENT");
  check(node.id, "dimensions", [node.width, node.height], [recipe.sourceWidth, recipe.height]);
  check(node.id, "padding", [node.paddingTop, node.paddingRight, node.paddingBottom, node.paddingLeft], recipe.padding);
  check(node.id, "gap", node.itemSpacing, recipe.gap);
  check(node.id, "radius", node.cornerRadius, recipe.radius);
  check(node.id, "strokesIncludedInLayout", node.strokesIncludedInLayout, recipe.strokesIncludedInLayout);
  check(node.id, "layoutMode", node.layoutMode, "HORIZONTAL");
  checkBindings(node, recipe.bindings); checkBindings(node, recipe.paints);
  for (const field of ["fills", "strokes"]) {
    if (!(field in recipe.paints)) check(node.id, field + ":empty", node[field].length, 0);
    else check(node.id, field + ":color", node[field][0].color, recipe.expectedPaints[field]);
  }
  const label = await figma.getNodeByIdAsync(record.labelId);
  check(label.id, "text", label.characters, recipe.label.characters);
  check(label.id, "font", {family:label.fontName.family,style:label.fontName.style}, {family:recipe.label.fontName.family,style:recipe.label.fontName.style});
  for (const field of ["fontSize", "lineHeight", "letterSpacing", "textDecoration"]) check(label.id, field, label[field], recipe.label[field]);
  checkBindings(label, recipe.labelBindings);
  check(label.id, "text-color", label.fills[0].color, recipe.expectedTextColor);
  for (const icon of recipe.icons) {
    const instance = await figma.getNodeByIdAsync(icon.side === "left" ? record.leftIconId : record.rightIconId);
    check(instance.id, "linked-icon", instance.mainComponent.id, DATA.helpers.glyphId);
    check(instance.id, "visible", instance.visible, icon.visible);
    check(instance.id, "size", [instance.width, instance.height], [icon.size, icon.size]);
    checkBindings(instance, {width:icon.sizeToken,height:icon.sizeToken});
    for (const vector of instance.findAllWithCriteria({types:["VECTOR"]})) checkBindings(vector, {fills:icon.colorToken});
  }
  if (recipe.focus) {
    const ring = node.children.find(c => c.name === "Focus ring");
    check(node.id, "focus-present", Boolean(ring), true);
    if (ring) {
      check(ring.id, "focus-geometry", [ring.width,ring.height,ring.x,ring.y], [node.width+8,node.height+8,-4,-4]);
      check(ring.id, "focus-width", ring.strokeWeight, 2); check(ring.id, "focus-radius", ring.cornerRadius,12);
      checkBindings(ring,{strokes:recipe.focus.colorToken,strokeWeight:recipe.focus.widthToken,
        topLeftRadius:recipe.focus.radiusToken,topRightRadius:recipe.focus.radiusToken,
        bottomLeftRadius:recipe.focus.radiusToken,bottomRightRadius:recipe.focus.radiusToken});
    }
  }
  if (recipe.loader) {
    const loader = node.children.find(c => c.name === "Loader");
    check(loader.id, 'loader-linked', (await loader.getMainComponentAsync()).id, recipe.loader.variantId);
    const dim = DATA.loader.variableIds['loader.size-' + recipe.loader.axes.size];
    check(loader.id, 'loader-size-binding', binding(loader, 'width'), dim);
    check(loader.id, 'loader-dimensions', [loader.width, loader.height], [recipe.loader.size, recipe.loader.size]);
    // The child owns colors, width and animation; verify them through LOADER-001 QA.
  }
  const expectedReactions = recipe.reactions.map(r=>({trigger:r.trigger,actions:(r.actions??[r.action]).map(a=>({type:a.type,navigation:a.navigation,destinationId:DATA.mapping.find(m=>m.sourceId===a.destinationId)?.id}))}));
  const actualReactions = node.reactions.map(r=>({trigger:r.trigger,actions:(r.actions??[r.action]).map(a=>({type:a.type,navigation:a.navigation,destinationId:a.destinationId}))}));
  check(node.id,"reactions",actualReactions,expectedReactions);
  summary.push({id:node.id,key:node.key,type:recipe.type,size:recipe.size,state:recipe.state,width:node.width,height:node.height});
}
const set = await figma.getNodeByIdAsync(DATA.componentSetId);
check(set.id,"variant-count",set.children.length,18);
const definitions = Object.fromEntries(Object.entries(set.componentPropertyDefinitions).map(([k,v])=>[k,{type:v.type,defaultValue:v.defaultValue}]));
for (const key of [DATA.properties.showLeftKey,DATA.properties.showRightKey]) check(set.id,key,definitions[key].defaultValue,false);
check(set.id,DATA.properties.labelKey,definitions[DATA.properties.labelKey].defaultValue,"Button");
return {status:issues.length?"FAIL":"PASS_FIGMA_VARIANTS",type:DATA.kind,variants:summary,bindingsChecked,issues};
