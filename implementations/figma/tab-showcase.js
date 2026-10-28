if(figma.fileKey!=='98xEw6sK8FRVNEhopM5SSz')throw new Error('Wrong destination');
figma.skipInvisibleInstanceChildren=false;
const page=await figma.getNodeByIdAsync(DATA.pageId);await figma.setCurrentPageAsync(page);
if(page.children.some(n=>n.name==='Tab · Especificación y consumo'))throw new Error('Showcase exists; inspect before retry');
for(const style of ['Regular','SemiBold','Bold'])await figma.loadFontAsync({family:'Manrope',style});
const v=Object.fromEntries(await Promise.all(Object.entries(DATA.variableIds).map(async([k,id])=>[k,await figma.variables.getVariableByIdAsync(id)])));
const collection=await figma.variables.getVariableCollectionByIdAsync(DATA.collectionId);
const created=[],instances=[],themeExamples=[],countExamples=[],focusExamples=[],hoverExamples=[],disabledExamples=[],consumerViews=[];
function mark(n){created.push(n);return n;}
function paint(n,token='tab.color-tab-bg-surface'){n.fills=token?[figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:1,g:1,b:1}},'color',v[token])]:[];}
function box(parent,name,direction,width,height,token=null){const n=mark(figma.createAutoLayout(direction));parent.appendChild(n);n.name=name;n.resize(width,height??40);n.primaryAxisSizingMode=direction==='VERTICAL'?(height===undefined?'AUTO':'FIXED'):'FIXED';n.counterAxisSizingMode=direction==='VERTICAL'?'FIXED':(height===undefined?'AUTO':'FIXED');n.primaryAxisAlignItems='MIN';n.counterAxisAlignItems='MIN';n.clipsContent=false;n.itemSpacing=12;paint(n,token);return n;}
function text(parent,content,size=14,style='Regular',secondary=false,width){const n=mark(figma.createText());parent.appendChild(n);n.name=content;n.fontName={family:'Manrope',style};n.fontSize=size;n.lineHeight={unit:'PIXELS',value:Math.ceil(size*1.45)};n.characters=content;n.fills=[figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:0,g:0,b:0}},'color',v[secondary?'tab.color-tab-text-secondary':'tab.color-tab-text-primary'])];if(width){n.textAutoResize='HEIGHT';n.resize(width,n.height);}else n.textAutoResize='WIDTH_AND_HEIGHT';return n;}
const key=a=>[a.type,a.selected,a.state].join('/');
const masters=Object.fromEntries(await Promise.all(DATA.variants.map(async r=>[key(r.axes),await figma.getNodeByIdAsync(r.id)])));
async function instance(parent,axes,name,overrides={}){const n=mark(masters[key(axes)].createInstance());parent.appendChild(n);n.name=name;n.setProperties({...axes,...overrides});instances.push(n);return n;}
const P=DATA.properties;
const review=box(page,'Tab · Especificación y consumo','VERTICAL',1120,undefined,'tab.color-tab-bg-surface');review.x=80;review.y=80;review.paddingTop=review.paddingBottom=review.paddingLeft=review.paddingRight=40;review.itemSpacing=24;
text(review,'BLUE HEART DS  /  COMPONENTE 02',11,'SemiBold',true);
text(review,'Tabs',40,'Bold');
text(review,'3 tipos · 24 variantes · 4 temas · 43 tokens',16,'Regular',true);
text(review,'TAB-001@1.0.0  ·  Selección en el consumidor  ·  Phosphor del equipo',12,'Regular',true);
const table=box(review,'Matriz de variantes','VERTICAL',1040);table.itemSpacing=12;
const header=box(table,'Estados','HORIZONTAL',1040,28);header.itemSpacing=16;text(header,'Tipo / selección',12,'SemiBold',true,176);
for(const state of ['Default','Hover','Focus','Disabled'])text(header,state,12,'SemiBold',true,200);
for(const type of ['underline','pill','segmented'])for(const selected of ['false','true']){
 const row=box(table,type+'/'+selected,'HORIZONTAL',1040,60);row.itemSpacing=16;row.counterAxisAlignItems='CENTER';
 text(row,type.charAt(0).toUpperCase()+type.slice(1)+' · '+(selected==='true'?'selected':'normal'),12,'Regular',true,176);
 for(const state of ['default','hover','focus','disabled']){const cell=box(row,state,'HORIZONTAL',200,60,type==='segmented'?'tab.color-tab-bg-muted':null);cell.paddingLeft=16;cell.counterAxisAlignItems='CENTER';await instance(cell,{type,selected,state},'Spec/'+type+'/'+selected+'/'+state);}
}
text(review,'Cuatro temas, las mismas variables',20,'SemiBold');
const themes=box(review,'Temas','HORIZONTAL',1040);themes.itemSpacing=16;
for(const mode of DATA.modes){const card=box(themes,mode,'VERTICAL',248,undefined,'tab.color-tab-bg-surface');card.paddingTop=card.paddingBottom=card.paddingLeft=card.paddingRight=16;card.cornerRadius=12;card.strokes=[figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:0,g:0,b:0}},'color',v['tab.color-tab-stroke-neutral'])];card.strokeWeight=1;card.setExplicitVariableModeForCollection(collection,DATA.modeIds[mode]);text(card,mode,14,'SemiBold');for(const type of ['underline','pill','segmented']){const row=box(card,type,'HORIZONTAL',216);row.itemSpacing=8;row.counterAxisAlignItems='CENTER';if(type==='segmented'){paint(row,'tab.color-tab-bg-muted');row.paddingTop=row.paddingBottom=8;}text(row,type,11,'Regular',true,92);const n=await instance(row,{type,selected:'true',state:'hover'},'Theme/'+mode+'/'+type,{[P.Label]:'Ventas'});themeExamples.push({mode,type,id:n.id});}}
text(review,'Propiedades y crecimiento desde la instancia',20,'SemiBold');
const props=box(review,'Overrides','VERTICAL',1040);props.itemSpacing=20;
const swapGlyph=await figma.importComponentByKeyAsync('46d251bb4099700c5852180f2370d265e5166432');
if(!swapGlyph.remote)throw new Error('Swap icon must remain linked to Phosphor');
const long=await instance(props,{type:'underline',selected:'false',state:'focus'},'Consumer/Label-Icon-Count-focus',{[P.Label]:'Movimientos del periodo',[P.ShowIcon]:true,[P.ShowBadge]:true,[P.Icon]:swapGlyph.id});
long.findOne(n=>n.type==='INSTANCE'&&n.name==='Badge').setProperties({[DATA.countProperty]:'99+'});focusExamples.push({type:'underline',id:long.id});
const counters=box(props,'Count 1 · 12 · 99+','HORIZONTAL',1040,52);counters.itemSpacing=40;counters.counterAxisAlignItems='CENTER';
for(const value of ['1','12','99+']){const n=await instance(counters,{type:'pill',selected:'false',state:'default'},'Consumer/Count/'+value,{[P.Label]:'Tab',[P.ShowBadge]:true});const badge=n.findOne(c=>c.type==='INSTANCE'&&c.name==='Badge');badge.setProperties({[DATA.countProperty]:value});countExamples.push({value,id:n.id,badgeId:badge.id});}
const focusRow=box(props,'Focus creciendo','HORIZONTAL',1040,64);focusRow.itemSpacing=40;focusRow.counterAxisAlignItems='CENTER';
for(const type of ['pill','segmented']){const n=await instance(focusRow,{type,selected:'true',state:'focus'},'Consumer/Focus/'+type,{[P.Label]:'Contenido más extenso',[P.ShowIcon]:true});focusExamples.push({type,id:n.id});}
text(review,'Selected segmented usa blanco y texto oscuro. Pill selected/hover conserva marca con mayor contraste.',12,'Regular',true,1040);
text(review,'Contrato MD: norms/components/tab.1.0.0.md  ·  Recetas y comprobante: consumption/tab/',11,'Regular',true,1040);

const playback=box(page,'Tab · Reproducción interactiva','VERTICAL',880,440,'tab.color-tab-bg-surface');playback.x=80;playback.y=review.y+review.height+140;playback.paddingTop=playback.paddingBottom=playback.paddingLeft=playback.paddingRight=32;playback.itemSpacing=20;
text(playback,'Tab · reproducción interactiva',24,'SemiBold');
text(playback,'Hover en underline y pill; retirar el cursor debe restaurar default.',13,'Regular',true);
const hovers=box(playback,'Hover nativo','HORIZONTAL',816,88);hovers.itemSpacing=16;
for(const type of ['underline','pill'])for(const selected of ['false','true']){const cell=box(hovers,type+'/'+selected,'VERTICAL',192,88);cell.paddingTop=cell.paddingLeft=8;cell.itemSpacing=12;text(cell,type+' · '+(selected==='true'?'selected':'normal'),11,'Regular',true);const n=await instance(cell,{type,selected,state:'default'},'Playback/Hover/'+type+'/'+selected);hoverExamples.push({type,selected,id:n.id});}
text(playback,'Disabled · sin acciones',14,'SemiBold');
const disabled=box(playback,'Disabled','HORIZONTAL',816,80);disabled.itemSpacing=16;
for(const type of ['underline','pill','segmented'])for(const selected of ['false','true']){const cell=box(disabled,type+'/'+selected,'VERTICAL',122.6666667,80);text(cell,type+' / '+selected,10,'Regular',true);const n=await instance(cell,{type,selected,state:'disabled'},'Playback/Disabled/'+type+'/'+selected);disabledExamples.push({type,selected,id:n.id});}
text(playback,'Focus se inspecciona como variante explícita; este prototipo no acredita teclado o ARIA web.',11,'Regular',true,816);

const labels=['Resumen','Movimientos','Documentos'];
for(let index=0;index<labels.length;index++){
 const frame=box(page,'Tab · Consumo / '+labels[index],'VERTICAL',880,440,'tab.color-tab-bg-surface');frame.x=1100+index*1020;frame.y=playback.y;frame.paddingTop=frame.paddingBottom=frame.paddingLeft=frame.paddingRight=32;frame.itemSpacing=24;
 text(frame,'Tab / patrón de consumo',24,'SemiBold');text(frame,'La navegación pertenece a este ejemplo, separado del componente individual.',12,'Regular',true);
 const nav=box(frame,'Navegación de ejemplo','HORIZONTAL',816,52,'tab.color-tab-bg-muted');nav.paddingTop=nav.paddingBottom=8;nav.paddingLeft=nav.paddingRight=8;nav.itemSpacing=16;nav.counterAxisAlignItems='CENTER';
 const links=[];
 for(let item=0;item<labels.length;item++){const hit=box(nav,labels[item],'HORIZONTAL',160,36);hit.counterAxisAlignItems='CENTER';const n=await instance(hit,{type:'segmented',selected:item===index?'true':'false',state:'default'},'Consumer/Selection/'+labels[item],{[P.Label]:labels[item]});links.push({hitId:hit.id,instanceId:n.id,index:item});}
 const disabledHit=box(nav,'No disponible','HORIZONTAL',176,36);disabledHit.counterAxisAlignItems='CENTER';await instance(disabledHit,{type:'segmented',selected:'false',state:'disabled'},'Consumer/Disabled',{[P.Label]:'No disponible'});
 const panel=box(frame,'Panel / '+labels[index],'VERTICAL',816,196,'tab.color-tab-bg-subtle');panel.paddingTop=panel.paddingBottom=panel.paddingLeft=panel.paddingRight=24;panel.itemSpacing=16;panel.cornerRadius=12;
 text(panel,labels[index],20,'SemiBold');text(panel,'Contenido del panel '+labels[index]+'.',14);text(panel,'Una selección y un panel visible. Datos de demostración.',12,'Regular',true);
 consumerViews.push({index,label:labels[index],id:frame.id,panelId:panel.id,links,disabledHitId:disabledHit.id});
}
for(const view of consumerViews)for(const link of view.links)if(link.index!==view.index){const hit=await figma.getNodeByIdAsync(link.hitId);await hit.setReactionsAsync([{trigger:{type:'ON_CLICK'},actions:[{type:'NODE',destinationId:consumerViews[link.index].id,navigation:'NAVIGATE',transition:null,preserveScrollPosition:false}]}]);}
const bounds=n=>({x:n.absoluteBoundingBox.x,y:n.absoluteBoundingBox.y,width:n.width,height:n.height});
function allIds(n){return[n.id,...('children'in n?n.children.flatMap(allIds):[])];}
return {reviewId:review.id,reviewBounds:bounds(review),playbackId:playback.id,playbackBounds:bounds(playback),hoverExamples:hoverExamples.map(r=>({...r,bounds:bounds(instances.find(n=>n.id===r.id))})),disabledExamples:disabledExamples.map(r=>({...r,bounds:bounds(instances.find(n=>n.id===r.id))})),themeExamples,countExamples,focusExamples,consumerViews,remoteSwapGlyph:{id:swapGlyph.id,key:swapGlyph.key,remote:swapGlyph.remote},createdNodeIds:[...new Set(created.flatMap(allIds))],mutatedNodeIds:created.map(n=>n.id)};
