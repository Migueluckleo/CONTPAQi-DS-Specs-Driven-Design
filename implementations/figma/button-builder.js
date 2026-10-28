// Scoped Button adapter. DATA is a verified projection of BUTTON-001, supplied by the caller.
if (figma.fileKey !== DATA.fileKey) throw new Error("Wrong destination file");
const page = await figma.getNodeByIdAsync(DATA.pageId);
if (!page || page.type !== "PAGE" || page.name !== "Buttons") throw new Error("Wrong Button page");
await figma.setCurrentPageAsync(page);
await figma.loadFontAsync({family: "Manrope", style: "Bold"});
await figma.loadFontAsync({family: "Manrope", style: "Regular"});
const entries = Object.entries(DATA.tokenIds);
const loaded = await Promise.all(entries.map(([, id]) => figma.variables.getVariableByIdAsync(id)));
const variables = Object.fromEntries(entries.map(([name], i) => [name, loaded[i]]));
if (loaded.some(v => !v)) throw new Error("Missing component token");
const createdNodeIds = [], mutatedNodeIds = [page.id];
const mark = n => { if (!createdNodeIds.includes(n.id)) createdNodeIds.push(n.id); return n; };
function markTree(n) { mark(n); if ("children" in n) for (const child of n.children) markTree(child); }
function color(name) {
  if (!variables[name]) throw new Error("Unknown color token: " + name);
  return figma.variables.setBoundVariableForPaint({type: "SOLID", color: {r: 0, g: 0, b: 0}}, "color", variables[name]);
}
function bindVariablesToComponent(node, bindings) {
  for (const [field, name] of Object.entries(bindings)) {
    if (field === "fills" || field === "strokes") node[field] = [color(name)];
    else node.setBoundVariable(field, variables[name]);
  }
}
// Adapted from createComponentWithVariants: use only observed recipes, then lay out after combining.
function combineObservedVariants(name, components, columns, cellWidth, cellHeight, x, y) {
  const set = mark(figma.combineAsVariants(components, page));
  set.name = name;
  set.fills = [];
  for (let i = 0; i < components.length; i++) {
    components[i].x = 24 + (i % columns) * cellWidth;
    components[i].y = 24 + Math.floor(i / columns) * cellHeight;
  }
  set.resize(48 + columns * cellWidth, 48 + Math.ceil(components.length / columns) * cellHeight);
  set.x = x; set.y = y;
  return set;
}

async function createHelpers() {
  if (page.children.some(n => n.name === "__Button/PlusCircle" || n.name.startsWith("__Button/Loader/")))
    throw new Error("Helpers already exist; read state before retry");
  const glyphKey = "46d251bb4099700c5852180f2370d265e5166432";
  if (DATA.icon.key !== glyphKey) throw new Error("Phosphor mapping differs from selected contract");
  if (!DATA.loader || DATA.loader.contract.id !== 'LOADER-001') throw new Error('Resolve the selected shared Loader before Button');
  return {glyphKey, glyphRemote: true, sharedLoader: DATA.loader.contract};
}

async function createFamily() {
  if (page.children.some(n => n.name === "Button/" + DATA.kind)) throw new Error("Family already exists; inspect before retry");
  if (!DATA.contractVersion) throw new Error("Missing selected contract version");
  // Fail before importing or creating nodes if historical, uncorrected recipes are supplied.
  for (const recipe of DATA.variants.filter(v => v.type === "secondary" && v.state === "focus")) {
    for (const reaction of recipe.reactions.filter(r => r.trigger.type === "ON_HOVER")) {
      const actions = reaction.actions ?? [reaction.action];
      const target = DATA.variants.find(v => v.sourceId === actions[0]?.destinationId);
      if (actions.length !== 1 || target?.type !== recipe.type || target?.size !== recipe.size || target?.state !== "hover")
        throw new Error("Secondary focus requires current same-size hover recipes; materialize the selected plan");
    }
  }
  // Unreferenced imports need not persist between calls: import and instantiate here.
  const glyph = await figma.importComponentByKeyAsync(DATA.helpers.glyphKey);
  if (!DATA.loader) throw new Error("Current Loader dependency required");
  const ordered = [...DATA.variants].sort((a, b) => DATA.states.indexOf(a.state) - DATA.states.indexOf(b.state) || DATA.sizes.indexOf(a.size) - DATA.sizes.indexOf(b.size));
  const components = [], sourceToTarget = {}, nodeRecords = [];
  for (const recipe of ordered) {
    const component = mark(figma.createComponent());
    component.name = "size=" + recipe.size + ", state=" + recipe.state;
    component.resize(recipe.sourceWidth, recipe.height); component.fills = []; component.strokes = []; component.effects = [];
    component.layoutMode = "HORIZONTAL"; component.primaryAxisSizingMode = "AUTO"; component.counterAxisSizingMode = "FIXED";
    component.primaryAxisAlignItems = "CENTER"; component.counterAxisAlignItems = "CENTER";
    component.strokesIncludedInLayout = recipe.strokesIncludedInLayout;
    component.clipsContent = false; component.minHeight = recipe.height; component.maxHeight = recipe.height;
    bindVariablesToComponent(component, recipe.bindings);
    for (const [field, token] of Object.entries(recipe.paints)) component[field] = [color(token)];
    component.strokeAlign = "INSIDE";
    if (recipe.loader) {
      const target = await figma.getNodeByIdAsync(recipe.loader.variantId);
      if (!target || target.type !== 'COMPONENT' || target.parent.name !== 'Loader') throw new Error('Missing shared Loader variant');
      const instance = target.createInstance(); markTree(instance); instance.name = 'Loader';
      component.appendChild(instance);
      const sizeId = DATA.loader.variableIds['loader.size-' + recipe.loader.axes.size];
      const sizeVariable = await figma.variables.getVariableByIdAsync(sizeId);
      instance.setBoundVariable('width', sizeVariable); instance.setBoundVariable('height', sizeVariable);
    }
    async function addIcon(icon) {
      const instance = glyph.createInstance(); markTree(instance);
      instance.name = icon.side === "left" ? "Left icon" : "Right icon";
      component.appendChild(instance); instance.resize(icon.size, icon.size);
      bindVariablesToComponent(instance, {width: icon.sizeToken, height: icon.sizeToken});
      for (const vector of instance.findAllWithCriteria({types: ["VECTOR"]})) vector.fills = [color(icon.colorToken)];
      instance.visible = icon.visible;
      return instance;
    }
    const leftRecipe = recipe.icons.find(x => x.side === "left");
    const rightRecipe = recipe.icons.find(x => x.side === "right");
    const left = leftRecipe ? await addIcon(leftRecipe) : null;
    const label = mark(figma.createText()); label.name = "Label";
    label.fontName = {family: recipe.label.fontName.family, style: recipe.label.fontName.style};
    label.fontSize = recipe.label.fontSize; label.lineHeight = recipe.label.lineHeight; label.letterSpacing = recipe.label.letterSpacing;
    label.textDecoration = recipe.label.textDecoration; label.textAlignHorizontal = "CENTER"; label.textAlignVertical = "CENTER";
    label.characters = recipe.label.characters; label.textAutoResize = "WIDTH_AND_HEIGHT";
    component.appendChild(label); label.layoutSizingHorizontal = "HUG"; label.layoutSizingVertical = "HUG";
    bindVariablesToComponent(label, recipe.labelBindings);
    const right = rightRecipe ? await addIcon(rightRecipe) : null;
    if (recipe.focus) {
      const ring = mark(figma.createFrame()); ring.name = "Focus ring"; ring.fills = [];
      component.appendChild(ring); ring.layoutPositioning = "ABSOLUTE";
      ring.resize(recipe.focus.width, recipe.focus.height); ring.x = recipe.focus.x; ring.y = recipe.focus.y;
      ring.constraints = {horizontal: "STRETCH", vertical: "STRETCH"}; ring.strokeAlign = "INSIDE";
      ring.strokes = [color(recipe.focus.colorToken)]; ring.clipsContent = true;
      bindVariablesToComponent(ring, {strokeWeight: recipe.focus.widthToken, topLeftRadius: recipe.focus.radiusToken,
        topRightRadius: recipe.focus.radiusToken, bottomLeftRadius: recipe.focus.radiusToken, bottomRightRadius: recipe.focus.radiusToken});
    }
    page.appendChild(component); components.push(component); sourceToTarget[recipe.sourceId] = component;
    nodeRecords.push({sourceId: recipe.sourceId, id: component.id, type: recipe.type, size: recipe.size, state: recipe.state,
      labelId: label.id, leftIconId: left?.id ?? null, rightIconId: right?.id ?? null});
  }
  const set = combineObservedVariants("Button/" + DATA.kind, components, 3, 160, 76, 1400, 80 + DATA.typeIndex * 560);
  set.description = "Button " + DATA.kind + ". Contrato MD BUTTON-001 v" + DATA.contractVersion + "; propiedades editables Label e iconos Phosphor vinculados apagados por defecto. Usa tokens de componente y cuatro temas; no implementa servicios ni certifica accesibilidad web.";
  const labelKey = set.addComponentProperty("Label", "TEXT", "Button");
  const showLeftKey = set.addComponentProperty("Show left icon", "BOOLEAN", false);
  const showRightKey = set.addComponentProperty("Show right icon", "BOOLEAN", false);
  const leftKey = set.addComponentProperty("Left icon", "INSTANCE_SWAP", glyph.id);
  const rightKey = set.addComponentProperty("Right icon", "INSTANCE_SWAP", glyph.id);
  for (const record of nodeRecords) {
    const label = await figma.getNodeByIdAsync(record.labelId); label.componentPropertyReferences = {characters: labelKey};
    if (record.leftIconId) (await figma.getNodeByIdAsync(record.leftIconId)).componentPropertyReferences = {visible: showLeftKey, mainComponent: leftKey};
    if (record.rightIconId) (await figma.getNodeByIdAsync(record.rightIconId)).componentPropertyReferences = {visible: showRightKey, mainComponent: rightKey};
  }
  for (const recipe of ordered) {
    const reactions = recipe.reactions.map(r => ({trigger: r.trigger, actions: (r.actions ?? [r.action]).map(a => {
      if (a.type === "NODE" && sourceToTarget[a.destinationId]) return {...a, destinationId: sourceToTarget[a.destinationId].id};
      throw new Error("Reaction leaves the observed type set: " + recipe.sourceId);
    })}));
    if (reactions.length) await sourceToTarget[recipe.sourceId].setReactionsAsync(reactions);
  }
  return {componentSetId: set.id, kind: DATA.kind, variants: nodeRecords,
    properties: {labelKey, showLeftKey, showRightKey, leftKey, rightKey}};
}

try {
  const result = DATA.operation === "helpers" ? await createHelpers() : await createFamily();
  return {status: "APPLIED", result, createdNodeIds, mutatedNodeIds};
} catch (error) {
  return {status: "PARTIAL_FAILURE", error: String(error), createdNodeIds, mutatedNodeIds};
}
