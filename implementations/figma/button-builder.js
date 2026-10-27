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
  const spinnerSets = {}, spinnerFirst = {}, sourceToTarget = {};
  const sizeNames = {"extra-small": "small", small: "medium", medium: "large"};
  for (const [sourceSize, buttonSize] of Object.entries(sizeNames)) {
    const frames = DATA.spinnerFrames.filter(f => f.size === sourceSize).sort((a, b) => Number(a.frame) - Number(b.frame));
    const components = [];
    for (const frame of frames) {
      const component = mark(figma.createComponent());
      component.name = "frame=" + frame.frame;
      component.resize(frame.width, frame.height); component.fills = []; component.strokes = []; component.clipsContent = false;
      bindVariablesToComponent(component, {width: "size-button-" + buttonSize + "-content", height: "size-button-" + buttonSize + "-content"});
      for (const name of ["Track", "Arc"]) {
        const ellipse = mark(figma.createEllipse()); ellipse.name = name;
        ellipse.resize(frame.width, frame.height); ellipse.arcData = name === "Track" ? frame.track : frame.arc;
        ellipse.fills = []; ellipse.strokes = [color("color-button-loader-inverse")];
        ellipse.strokeAlign = "INSIDE"; ellipse.opacity = name === "Track" ? 0.30000001192092896 : 1;
        ellipse.setBoundVariable("strokeWeight", variables["stroke-button-emphasis-width"]);
        ellipse.constraints = {horizontal: "SCALE", vertical: "SCALE"};
        component.appendChild(ellipse);
      }
      page.appendChild(component); components.push(component); sourceToTarget[frame.id] = component;
    }
    const set = combineObservedVariants("__Button/Loader/" + buttonSize, components, 6, 48, 48, 2500, 180 + Object.keys(spinnerSets).length * 290);
    set.description = "Dependencia animada privada de Button: 24 frames observados, 0.033333335 s/frame. El consumidor conserva color y tamaño por tokens. BUTTON-001.";
    spinnerSets[buttonSize] = set.id; spinnerFirst[buttonSize] = components[0].id;
  }
  for (const frame of DATA.spinnerFrames) {
    const target = sourceToTarget[frame.id];
    const reactions = frame.reactions.map(r => ({trigger: r.trigger, actions: r.actions.map(a => ({...a, destinationId: sourceToTarget[a.destinationId].id}))}));
    await target.setReactionsAsync(reactions);
  }
  return {glyphKey, glyphRemote: true, spinnerSets, spinnerFirst, sourceToTarget: Object.fromEntries(Object.entries(sourceToTarget).map(([id, node]) => [id, node.id]))};
}

async function createFamily() {
  if (page.children.some(n => n.name === "Button/" + DATA.kind)) throw new Error("Family already exists; inspect before retry");
  // Unreferenced imports need not persist between calls: import and instantiate here.
  const glyph = await figma.importComponentByKeyAsync(DATA.helpers.glyphKey);
  const spinnerNodes = Object.fromEntries(await Promise.all(Object.entries(DATA.helpers.spinnerFirst).map(async ([size, id]) => [size, await figma.getNodeByIdAsync(id)])));
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
      const instance = spinnerNodes[recipe.size].createInstance(); markTree(instance); instance.name = "Loader";
      component.appendChild(instance); instance.resize(recipe.loader.size, recipe.loader.size);
      bindVariablesToComponent(instance, {width: recipe.loader.sizeToken, height: recipe.loader.sizeToken});
      for (const child of instance.findAllWithCriteria({types: ["ELLIPSE"]})) {
        const paint = color(recipe.loader.colorToken);
        paint.opacity = child.name === "Track" ? recipe.loader.trackPaintOpacity : recipe.loader.arcPaintOpacity;
        child.opacity = child.name === "Track" ? recipe.loader.trackOpacity : recipe.loader.arcOpacity;
        child.strokes = [paint]; child.setBoundVariable("strokeWeight", variables[recipe.loader.widthToken]);
      }
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
  set.description = "Button " + DATA.kind + ". Contrato MD BUTTON-001 v2.0.0; propiedades editables Label e iconos Phosphor vinculados apagados por defecto. Usa tokens de componente y cuatro temas; no implementa servicios ni certifica accesibilidad web.";
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
