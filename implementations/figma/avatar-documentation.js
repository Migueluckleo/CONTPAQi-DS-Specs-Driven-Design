// Editable presentation only. Component appearances come from linked masters.
if(figma.fileKey!=='98xEw6sK8FRVNEhopM5SSz')throw new Error('Wrong destination');
figma.skipInvisibleInstanceChildren=false;
const p=await figma.getNodeByIdAsync(DATA.pageId);await p.loadAsync();
if(DATA.operation==='scaffold')await (await figma.getNodeByIdAsync('78:97')).loadAsync();
await figma.setCurrentPageAsync(p);
for(const f of [{family:'Manrope',style:'Regular'},{family:'Manrope',style:'SemiBold'},{family:'Manrope',style:'Bold'},{family:'Figtree',style:'Regular'},{family:'Figtree',style:'SemiBold'}])await figma.loadFontAsync(f);
const created=[],mutated=[],links=[];
const mark=n=>{created.push(n.id);return n;};
function all(n){return[n.id,...('children'in n?n.children.flatMap(all):[])];}
const aSet=await figma.getNodeByIdAsync(DATA.avatar.setId),gSet=await figma.getNodeByIdAsync(DATA.group.setId);
const P=DATA.avatar.propertyKeys;
const sems=(await figma.variables.getLocalVariablesAsync()).filter(v=>v.variableCollectionId==='VariableCollectionId:6:148');
const colors=[];for(const v of sems)if(v.resolvedType==='COLOR'){const value=v.valuesByMode['6:1'];const pv=await figma.variables.getVariableByIdAsync(value.id);colors.push({v,value:Object.values(pv.valuesByMode)[0]});}
async function paints(raw){return(raw||[]).map(f=>{const q=JSON.parse(JSON.stringify(f));delete q.boundVariables;if(q.type==='SOLID'){const match=colors.find(c=>['r','g','b'].every(k=>Math.abs(c.value[k]-q.color[k])<1e-6));if(match)return figma.variables.setBoundVariableForPaint(q,'color',match.v);}return q;});}
function frame(parent,name,w,h,dir='VERTICAL'){const n=mark(figma.createAutoLayout(dir));parent.appendChild(n);n.name=name;n.resize(w,h);n.primaryAxisSizingMode='FIXED';n.counterAxisSizingMode='FIXED';n.fills=[];n.clipsContent=false;return n;}
function text(parent,str,size=14,style='Regular',width){const n=mark(figma.createText());parent.appendChild(n);n.name=str;n.fontName={family:'Manrope',style};n.fontSize=size;n.lineHeight={unit:'PIXELS',value:Math.ceil(size*1.5)};n.characters=str;n.fills=[{type:'SOLID',color:{r:.06,g:.09,b:.16}}];if(width){n.textAutoResize='HEIGHT';n.resize(width,n.height);}return n;}
async function av(parent,type,size,props={}){const m=aSet.children.find(c=>c.variantProperties.type===type&&c.variantProperties.size===size);const n=mark(m.createInstance());parent.appendChild(n);n.setProperties({[P.Initials]:props.Initials||'JA',[P.ShowStatus]:props['Show status']??true});return n;}
async function scaffold(){
 if(p.children.some(n=>n.name==='Overview'))throw new Error('Documentation exists; inspect ledger');
 const overview=mark((await figma.getNodeByIdAsync('111:461')).clone());p.appendChild(overview);overview.name='Overview';overview.x=80;overview.y=80;
 const title=overview.findOne(n=>n.type==='TEXT'&&n.name==='Title');title.characters='Avatar';
 const description=overview.findOne(n=>n.type==='TEXT'&&n.name==='Description');description.characters=DATA.overviewDescription;description.resize(940,144);description.textAlignHorizontal='CENTER';description.textAutoResize='HEIGHT';
 const content=overview.children[1].children[0];content.resize(1400,464);content.layoutSizingHorizontal='FIXED';
 const image=overview.children[2].children[0];for(const child of [...image.children])child.remove();image.layoutMode='VERTICAL';image.primaryAxisAlignItems='CENTER';image.counterAxisAlignItems='CENTER';image.primaryAxisSizingMode='FIXED';image.counterAxisSizingMode='FIXED';image.resize(1840,1046);await av(image,'image','extra-large');
 const variants=frame(p,'Variants & states',1920,2066);variants.x=2098;variants.y=80;variants.cornerRadius=32;variants.fills=await paints([{type:'SOLID',color:{r:1,g:1,b:1}}]);variants.primaryAxisSizingMode='AUTO';variants.counterAxisSizingMode='FIXED';variants.itemSpacing=104;variants.paddingBottom=104;
 const header=mark((await figma.getNodeByIdAsync('114:509')).clone());variants.appendChild(header);
 const headerText=header.findAll(n=>n.type==='TEXT');for(const n of headerText){if(n.name==='Title')n.characters='Variants & states';else if(n.name==='Description'||/Tabs|A modal comes/.test(n.characters)){n.characters='Avatar · 3 tipos, 4 tamaños y presencia opcional. Avatar group · slot nativo de 2 a 4 elementos.';n.textAutoResize='HEIGHT';}}
 const sections=frame(variants,'Variant Section Container',1920,1698);sections.itemSpacing=24;sections.primaryAxisSizingMode='AUTO';sections.counterAxisSizingMode='FIXED';
 const review=frame(p,'Avatar · matriz de referencia',972,808);review.x=4116;review.y=80;review.cornerRadius=32;review.fills=await paints([{type:'SOLID',color:{r:1,g:1,b:1}}]);review.paddingTop=64;review.paddingBottom=64;review.paddingLeft=64;review.paddingRight=64;
 const panel=frame(review,'Content',844,680);panel.primaryAxisAlignItems='CENTER';panel.counterAxisAlignItems='CENTER';panel.itemSpacing=56;panel.cornerRadius=16;panel.fills=[{type:'SOLID',color:{r:.973,g:.976,b:.98}}];panel.strokes=[{type:'SOLID',color:{r:.9,g:.92,b:.94}}];panel.strokeWeight=2;
 const matrix=frame(panel,'Avatar',450,290);matrix.primaryAxisSizingMode='AUTO';matrix.counterAxisSizingMode='FIXED';matrix.itemSpacing=26;
 const head=frame(matrix,'Size',450,20,'HORIZONTAL');head.itemSpacing=24;text(head,'',12,'Regular',100);for(const size of ['extra-large','large','medium','small'])text(head,size,size==='extra-large'?10:12,'Regular',60);
 for(const type of ['image','text','icon']){const row=frame(matrix,type,450,54,'HORIZONTAL');row.itemSpacing=24;row.counterAxisAlignItems='CENTER';text(row,type,12,'Regular',100);for(const size of ['extra-large','large','medium','small']){const cell=frame(row,size,60,54);cell.primaryAxisAlignItems='CENTER';cell.counterAxisAlignItems='CENTER';await av(cell,type,size);}}
 const groups=frame(panel,'Avatar group',450,244);groups.itemSpacing=20;groups.primaryAxisSizingMode='AUTO';groups.counterAxisSizingMode='FIXED';for(const size of ['extra-large','large','medium','small']){const row=frame(groups,size,450,48,'HORIZONTAL');row.counterAxisAlignItems='CENTER';row.itemSpacing=24;text(row,size,12,'Regular',100);const m=gSet.children.find(n=>n.variantProperties.size===size);const n=mark(m.createInstance());row.appendChild(n);}
 return {overviewId:overview.id,variantsId:variants.id,sectionsId:sections.id,reviewId:review.id,createdNodeIds:[...new Set([overview,variants,review].flatMap(all))],mutatedNodeIds:[...new Set(mutated)]};
}
async function section(){
 const parent=await figma.getNodeByIdAsync(DATA.parentId);
 async function build(d,parent){
  let n;
  if(d.kind==='avatar'){
   n=await av(parent,d.props.type,d.props.size,d.props);const status=n.findOne(c=>c.type==='INSTANCE'&&c.name==='Status');if(status&&d.statusType)status.setProperties({type:d.statusType});
  }else if(d.kind==='group'){n=mark(gSet.children.find(c=>c.variantProperties.size===d.size).createInstance());parent.appendChild(n);
  }else if(d.kind==='idea'){const m=await figma.importComponentByKeyAsync('2414574dcd430f4362a82560f578c1eefd8e6989');n=mark(m.createInstance());parent.appendChild(n);n.rescale(d.width/32);n.strokeWeight=1;
  }else{
   n=mark(d.type==='TEXT'?figma.createText():figma.createFrame());parent.appendChild(n);
   if(n.type==='TEXT'){n.fontName=d.fontName;n.fontSize=d.fontSize;n.characters=d.characters;n.lineHeight=d.lineHeight;n.letterSpacing=d.letterSpacing;n.textAlignHorizontal=d.textAlignHorizontal||'LEFT';n.textAlignVertical=d.textAlignVertical||'TOP';n.textAutoResize=d.textAutoResize||'HEIGHT';n.resize(Math.max(d.width,.01),Math.max(d.height,.01));}
   else{n.resize(Math.max(d.width,.01),Math.max(d.height,.01));n.layoutMode=['HORIZONTAL','VERTICAL'].includes(d.layoutMode)?d.layoutMode:'NONE';for(const k of ['primaryAxisAlignItems','counterAxisAlignItems','itemSpacing','paddingTop','paddingRight','paddingBottom','paddingLeft','clipsContent','strokesIncludedInLayout'])if(d[k]!==undefined&&(k!=='strokesIncludedInLayout'||n.layoutMode!=='NONE'))n[k]=d[k];if(d.cornerRadius!==undefined)n.cornerRadius=d.cornerRadius;}
   n.fills=await paints(d.fills);n.strokes=await paints(d.strokes);if(d.strokeWeight!==undefined)n.strokeWeight=d.strokeWeight;if(d.strokeAlign)n.strokeAlign=d.strokeAlign;
   for(const c of d.kids||[])await build(c,n);
   if(d.type==='GROUP')for(const c of n.children){c.x-=d.x;c.y-=d.y;}
   if(n.type==='FRAME'&&n.layoutMode!=='NONE'){n.primaryAxisSizingMode='FIXED';n.counterAxisSizingMode='FIXED';n.resize(Math.max(d.width,.01),Math.max(d.height,.01));}
  }
  n.name=d.name;n.visible=d.visible??true;n.opacity=d.opacity??1;
  if(d.layoutPositioning==='ABSOLUTE'&&parent.layoutMode&&parent.layoutMode!=='NONE')n.layoutPositioning='ABSOLUTE';
  if(d.x!==undefined)n.x=d.x;if(d.y!==undefined)n.y=d.y;
  if(d.constraints)n.constraints=d.constraints;
  links.push({sourceId:d.id,destinationId:n.id,kind:d.kind||d.type});return n;
 }
 const root=await build(DATA.recipe,parent);return {rootId:root.id,sourceRootId:DATA.recipe.id,width:root.width,height:root.height,createdNodeIds:[...new Set(all(root))],mutatedNodeIds:mutated,links};
}
return await ({scaffold,section})[DATA.operation]();
