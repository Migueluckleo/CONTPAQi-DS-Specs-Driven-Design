// Presentation projection: source recipes are immutable; all public UI stays linked.
if(figma.fileKey!=='98xEw6sK8FRVNEhopM5SSz')throw new Error('Wrong destination');
figma.skipInvisibleInstanceChildren=false;
const page=await figma.getNodeByIdAsync('78:97');await page.loadAsync();await figma.setCurrentPageAsync(page);
const fonts=new Map();function scanFonts(d){if(d.fontName?.family&&d.fontName?.style)fonts.set(d.fontName.family+'|'+d.fontName.style,{family:d.fontName.family,style:d.fontName.style});d.kids?.forEach(scanFonts);}scanFonts(DATA.recipe);for(const font of fonts.values())await figma.loadFontAsync(font);
if(page.findOne(n=>n.getSharedPluginData('blueheart','source')===DATA.recipe.id))throw new Error('Source section already projected; inspect ledger');
const created=[],mutated=[],links=[];const P=DATA.propertyKeys;
const tabSet=await figma.getNodeByIdAsync('79:26');const tabsSet=await figma.getNodeByIdAsync('105:223');
const groupParent=DATA.parentId?await figma.getNodeByIdAsync(DATA.parentId):page;
function tag(n,d){n.setSharedPluginData('blueheart','source',d.id);links.push({sourceId:d.id,destinationId:n.id,kind:d.kind??d.t});}
function clean(x){return JSON.parse(JSON.stringify(x));}
async function paints(raw){const out=[];for(const f of raw??[]){const p=clean(f);const old=p.boundVariables?.color?.id;delete p.boundVariables;if(p.type==='IMAGE')p.imageHash=DATA.patternHash;if(old&&DATA.variableMap[old]&&p.type==='SOLID'){const v=await figma.variables.getVariableByIdAsync(DATA.variableMap[old]);out.push(figma.variables.setBoundVariableForPaint(p,'color',v));}else out.push(p);}return out;}
function tabMaster(d){const a={...d.axes,type:d.props?.type??d.axes.type,selected:d.props?.selected??d.axes.selected,state:d.props?.state??d.axes.state};const n=tabSet.children.find(v=>Object.entries(a).every(([k,x])=>v.variantProperties[k]===String(x)));if(!n)throw new Error('Unresolved Tab '+JSON.stringify(a));return n;}
function tabProps(n,d){n.setProperties({type:d.props?.type??d.axes.type,selected:String(d.props?.selected??d.axes.selected),state:d.props?.state??d.axes.state,[P.Label]:d.props?.Label??'Tab',[P.ShowIcon]:d.props?.['Show icon']??false,[P.ShowBadge]:d.props?.['Show badge']??false});}
async function build(d,parent){
 let n;
 if(d.kind==='master-tab'||d.kind==='master-tabs'){
  n=d.kind==='master-tab'?tabSet:tabsSet;parent.appendChild(n);n.layoutMode='NONE';n.resize(d.w,d.h);
  for(const s of d.variants){const v=n.children.find(c=>Object.entries(s.axes).every(([k,x])=>c.variantProperties[k]===x));if(!v)throw new Error('Missing master axes');v.x=s.x;v.y=s.y;mutated.push(v.id);}
  mutated.push(n.id);
 }else if(d.kind==='tab'){
  n=tabMaster(d).createInstance();parent.appendChild(n);created.push(n.id);tabProps(n,d);if(Math.abs((d.scale??1)-1)>.001)n.rescale(d.scale);
 }else if(d.kind==='tabs'){
  n=tabsSet.children.find(v=>v.variantProperties.type===d.type).createInstance();parent.appendChild(n);created.push(n.id);const slot=n.findOne(x=>x.type==='SLOT');if(!slot)throw new Error('Missing instance slot');
  while(slot.children.length>d.kids.length)slot.children[slot.children.length-1].remove();
  for(let i=0;i<d.kids.length;i++){const child=d.kids[i];let t=slot.children[i];if(!t){t=tabMaster(child).createInstance();slot.appendChild(t);created.push(t.id);}tabProps(t,child);tag(t,child);}
  if(Math.abs((d.scale??1)-1)>.001)n.rescale(d.scale);
 }else if(d.kind==='logo'){
  n=(await figma.getNodeByIdAsync(DATA.logoId)).clone();parent.appendChild(n);created.push(n.id);n.resize(d.w,d.h);
 }else if(d.kind==='idea'){
  n=(await figma.importComponentByKeyAsync('2414574dcd430f4362a82560f578c1eefd8e6989')).createInstance();parent.appendChild(n);created.push(n.id);n.resize(d.w,d.h);if(n.strokes.length===0)n.strokeWeight=1;
 }else if(d.kind==='bullet'){
  n=figma.createNodeFromSvg(DATA.bulletSvg);parent.appendChild(n);created.push(n.id);n.resize(d.w,d.h);
 }else{
  n=d.t==='TEXT'?figma.createText():d.t==='ELLIPSE'?figma.createEllipse():d.t==='RECTANGLE'?figma.createRectangle():figma.createFrame();parent.appendChild(n);created.push(n.id);
  if(n.type==='TEXT'){
   n.fontName={family:d.fontName.family,style:d.fontName.style};n.fontSize=d.fontSize;n.characters=d.characters;n.resize(Math.max(d.w,.01),Math.max(d.h,.01));
   for(const k of ['lineHeight','letterSpacing','textAlignHorizontal','textAlignVertical','textAutoResize'])if(d[k]!==undefined)n[k]=clean(d[k]);
  }else{
   n.resize(Math.max(d.w,.01),Math.max(d.h,.01));
   if('layoutMode'in n){n.layoutMode=['HORIZONTAL','VERTICAL'].includes(d.layoutMode)?d.layoutMode:'NONE';for(const k of ['primaryAxisAlignItems','counterAxisAlignItems','itemSpacing','paddingTop','paddingRight','paddingBottom','paddingLeft','clipsContent','strokesIncludedInLayout'])if(d[k]!==undefined&&(k!=='strokesIncludedInLayout'||n.layoutMode!=='NONE'))n[k]=d[k];}
   if(d.cornerRadius!==undefined&&'cornerRadius'in n)n.cornerRadius=d.cornerRadius;if(d.t==='GROUP')n.clipsContent=false;
  }
  if('fills'in n)n.fills=await paints(d.fills);if('strokes'in n)n.strokes=await paints(d.strokes);
  for(const k of ['strokeWeight','strokeAlign','effects'])if(d[k]!==undefined)n[k]=clean(d[k]);
  for(const [field,ref]of Object.entries(d.boundVariables??{})){if(['fills','strokes','effects'].includes(field)||!ref?.id||!DATA.variableMap[ref.id])continue;try{const v=await figma.variables.getVariableByIdAsync(DATA.variableMap[ref.id]);n.setBoundVariable(field,v);}catch(e){throw new Error('Documentation binding '+d.id+'/'+field+': '+e.message);}}
  for(const child of d.kids??[])await build(child,n);
  if(d.t==='GROUP')for(const child of n.children){child.x-=d.x;child.y-=d.y;}
  if('layoutMode'in n&&n.layoutMode!=='NONE'){n.primaryAxisSizingMode='FIXED';n.counterAxisSizingMode='FIXED';n.resize(Math.max(d.w,.01),Math.max(d.h,.01));}
 }
 if(!['master-tab','master-tabs'].includes(d.kind))n.name=d.name;n.visible=d.visible??true;n.opacity=d.opacity??1;
 if(d.x!==undefined)n.x=d.x;if(d.y!==undefined)n.y=d.y;
 if(d.layoutPositioning==='ABSOLUTE'&&parent.layoutMode&&parent.layoutMode!=='NONE')n.layoutPositioning='ABSOLUTE';
 if(d.constraints&&'constraints'in n)n.constraints=d.constraints;
 if(parent.layoutMode&&parent.layoutMode!=='NONE')for(const k of ['layoutSizingHorizontal','layoutSizingVertical'])if(d[k])n[k]=n.type==='FRAME'&&!d.kind&&d[k]!=='FILL'?'FIXED':d[k];
 tag(n,d);return n;
}
const root=await build(DATA.recipe,groupParent);
if(groupParent===page)root.setExplicitVariableModeForCollection('VariableCollectionId:78:53','78:4');
return{rootId:root.id,sourceRootId:DATA.recipe.id,width:root.width,height:root.height,createdNodeIds:created,mutatedNodeIds:mutated,links};
