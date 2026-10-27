// Build a consumer matrix from actual main components, never detached copies.
if (figma.fileKey !== DATA.fileKey) throw new Error("Wrong target");
if (!DATA.contractPath) throw new Error("Missing selected contract path");
const page = await figma.getNodeByIdAsync(DATA.pageId);
await figma.setCurrentPageAsync(page);
await figma.loadFontAsync({family: "Manrope", style: "Bold"});
await figma.loadFontAsync({family: "Manrope", style: "Regular"});
if (page.children.some(n => n.name === "Button / Contract and consumption")) throw new Error("Review frame exists; inspect before retry");
const createdNodeIds = [], mark = n => { createdNodeIds.push(n.id); return n; };
function track(n) { mark(n); if ("children" in n) n.children.forEach(track); }
function layout(direction, name, gap, padding = 0) {
  const n = mark(figma.createAutoLayout(direction)); n.name = name; n.fills = [];
  n.itemSpacing = gap; n.paddingTop = n.paddingRight = n.paddingBottom = n.paddingLeft = padding;
  n.primaryAxisSizingMode = "AUTO"; n.counterAxisSizingMode = "AUTO";
  return n;
}
function text(value, size = 14, bold = false) {
  const t = mark(figma.createText()); t.name = value;
  t.fontName = {family: "Manrope", style: bold ? "Bold" : "Regular"};
  t.fontSize = size; t.characters = value; t.textAutoResize = "WIDTH_AND_HEIGHT";
  t.fills = [{type: "SOLID", color: {r: 0.05882353, g: 0.09019608, b: 0.16470589}}];
  return t;
}
function cell(width, height, name) {
  const n = layout("HORIZONTAL", name, 0); n.resize(width, height);
  n.primaryAxisSizingMode = "FIXED"; n.counterAxisSizingMode = "FIXED";
  n.primaryAxisAlignItems = "CENTER"; n.counterAxisAlignItems = "CENTER";
  return n;
}
const root = layout("VERTICAL", "Button / Contract and consumption", 24, 40);
root.fills = [{type: "SOLID", color: {r: 0.96862745, g: 0.97647059, b: 0.98431373}}];
page.appendChild(root); root.x = 80; root.y = 80;
root.appendChild(text("Button", 32, true));
root.appendChild(text("BUTTON-001 · 90 variantes · tokens de componente · cuatro temas", 16));
root.appendChild(text("Label y swaps editables. Loading y disabled no simulan servicios. Contrato MD: " + DATA.contractPath, 12));
const instances = [];
for (const size of ["large", "medium", "small"]) {
  const section = layout("VERTICAL", "Size / " + size, 8); root.appendChild(section);
  section.appendChild(text(size + " · " + ({large:48,medium:40,small:32}[size]) + " px", 20, true));
  const header = layout("HORIZONTAL", "States", 8); section.appendChild(header);
  header.appendChild(cell(120, 32, "Type"));
  for (const state of DATA.states) { const c = cell(144, 32, state); c.appendChild(text(state, 12, true)); header.appendChild(c); }
  for (const kind of DATA.types) {
    const row = layout("HORIZONTAL", kind + " / " + size, 8); section.appendChild(row);
    const title = cell(120, 68, "Type / " + kind); title.appendChild(text(kind, 14, true)); row.appendChild(title);
    for (const state of DATA.states) {
      const record = DATA.variants.find(v => v.type === kind && v.size === size && v.state === state);
      const main = await figma.getNodeByIdAsync(record.id);
      const instance = main.createInstance(); track(instance); instance.name = kind + " / " + size + " / " + state;
      const c = cell(144, 68, instance.name + " cell"); c.appendChild(instance); row.appendChild(c);
      instances.push({id: instance.id, mainId: main.id, type: kind, size, state});
    }
  }
}
const usage = layout("VERTICAL", "Functional consumption checks", 12); usage.clipsContent = false; root.appendChild(usage);
usage.appendChild(text("Consumo: etiqueta larga, iconos y estados", 20, true));
const cases = [];
for (const scenario of [{kind:"primary",state:"default",label:"Generar documento",left:true,right:false},
                        {kind:"secondary",state:"focus",label:"Ver detalle",left:false,right:true},
                        {kind:"danger",state:"disabled",label:"Eliminar registro",left:false,right:false},
                        {kind:"primary",state:"loading",label:"Generando…",left:false,right:false}]) {
  const record = DATA.variants.find(v => v.type === scenario.kind && v.size === "medium" && v.state === scenario.state);
  const main = await figma.getNodeByIdAsync(record.id); const instance = main.createInstance(); track(instance);
  const keys = DATA.properties[scenario.kind];
  instance.setProperties({[keys.labelKey]:scenario.label,[keys.showLeftKey]:scenario.left,[keys.showRightKey]:scenario.right});
  const row = layout("HORIZONTAL", scenario.kind + " / " + scenario.state, 20); row.clipsContent = false; usage.appendChild(row);
  const note = cell(240, 60, "Scenario"); note.appendChild(text(scenario.kind + " · " + scenario.state, 13));
  row.appendChild(note); row.appendChild(instance);
  cases.push({id:instance.id,mainId:main.id,...scenario});
}
root.appendChild(text("Figma valida estructura, bindings y prototipo almacenado. HTML/ARIA, confirmaciones y servicios pertenecen al consumidor.", 12));
return {status:"APPLIED",reviewFrameId:root.id,instances,cases,createdNodeIds,mutatedNodeIds:[page.id]};
