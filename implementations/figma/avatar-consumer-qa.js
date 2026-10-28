// Native consumer tests; only new Avatars-page examples are mutated.
if(figma.fileKey!=='98xEw6sK8FRVNEhopM5SSz')throw new Error('Wrong destination');
figma.skipInvisibleInstanceChildren=false;
const page=await figma.getNodeByIdAsync(DATA.pageId);await page.loadAsync();await figma.setCurrentPageAsync(page);
for(const style of ['Regular','SemiBold','Bold'])await figma.loadFontAsync({family:'Manrope',style});
if(page.children.some(n=>n.name==='Avatar · Uso y QA'))throw new Error('QA examples already exist; inspect ledger');
const created=[],mutated=[],removed=[],controls=[],themeCases=[],slotCases=[],contentCases=[];
const mark=n=>{created.push(n.id);return n;};
function assert(id,req,condition,expected,actual){controls.push({id,requirement:req,status:condition?'PASS':'FAIL',expected,actual});}
function box(parent,name,w,h,dir='VERTICAL'){const n=mark(figma.createAutoLayout(dir));parent.appendChild(n);n.name=name;n.resize(w,h);n.primaryAxisSizingMode='FIXED';n.counterAxisSizingMode='FIXED';n.fills=[];n.clipsContent=false;return n;}
function txt(parent,str,size=14,style='Regular',width){const n=mark(figma.createText());parent.appendChild(n);n.name=str;n.fontName={family:'Manrope',style};n.fontSize=size;n.lineHeight={unit:'PIXELS',value:Math.ceil(size*1.5)};n.characters=str;n.fills=[{type:'SOLID',color:{r:.06,g:.09,b:.16}}];if(width){n.textAutoResize='HEIGHT';n.resize(width,n.height);}return n;}
function equal(a,b,tol=1e-6){return typeof a==='number'&&typeof b==='number'?Math.abs(a-b)<=tol:JSON.stringify(a)===JSON.stringify(b);}
function resolved(n){const fill=n.fills.find(p=>p.type==='SOLID');return fill?{...fill.color,a:fill.opacity??1}:null;}
function bound(n,field){const v=n.boundVariables?.[field];return Array.isArray(v)?v.map(v=>v.id):v?.id;}
const aset=await figma.getNodeByIdAsync(DATA.avatar.setId),gset=await figma.getNodeByIdAsync(DATA.group.setId),P=DATA.avatar.propertyKeys;
const avMaster=(type,size)=>aset.children.find(n=>n.variantProperties.type===type&&n.variantProperties.size===size);
const groupMaster=size=>gset.children.find(n=>n.variantProperties.size===size);
async function av(parent,type,size,initials='JA'){const n=mark(avMaster(type,size).createInstance());parent.appendChild(n);n.setProperties({[P.Initials]:initials});return n;}
const panel=box(page,'Avatar · Uso y QA',1920,1470);panel.x=80;panel.y=2800;panel.paddingTop=panel.paddingBottom=panel.paddingLeft=panel.paddingRight=40;panel.itemSpacing=24;panel.cornerRadius=24;panel.fills=[{type:'SOLID',color:{r:1,g:1,b:1}}];
txt(panel,'Avatar · temas, composición y límites',32,'Bold');
txt(panel,'22 tokens Avatar + 7 Avatar group + Dot · cuatro temas reales · anillo 1 px · Phosphor del equipo',16,'Regular',1840);
const themes=box(panel,'Cuatro temas',1840,720,'HORIZONTAL');themes.itemSpacing=20;
for(const mode of DATA.modes){
 const card=box(themes,mode,445,720);card.itemSpacing=16;card.setExplicitVariableModeForCollection(DATA.collections.component.id,DATA.collections.component.modeIds[mode]);txt(card,mode,20,'SemiBold');
 for(const type of ['image','text','icon']){
  const row=box(card,type,445,64,'HORIZONTAL');row.itemSpacing=24;row.counterAxisAlignItems='CENTER';txt(row,type,12,'Regular',66);
  for(const size of ['extra-large','large','medium','small']){
   const n=await av(row,type,size);const c=n.findOne(x=>x.type==='FRAME'&&x.name==='Avatar');const expected=type==='image'?null:DATA.primaryColors[mode];
   const actual=type==='image'?c.fills[0].imageHash:resolved(c);
   assert('theme/'+mode+'/'+type+'/'+size,'REQ-THEME',type==='image'?actual===DATA.portraitHash:Object.keys(expected).every(k=>equal(actual[k],expected[k])),type==='image'?DATA.portraitHash:expected,actual);
   themeCases.push({mode,type,size,id:n.id,contentId:c.id,paint:actual});
  }
 }
 txt(card,'Avatar group · colores fijos + marca',13,'SemiBold');
 for(const size of ['extra-large','large','medium','small']){
  const row=box(card,'Group/'+size,445,60,'HORIZONTAL');row.itemSpacing=16;row.counterAxisAlignItems='CENTER';txt(row,size,12,'Regular',90);
  const n=mark(groupMaster(size).createInstance());row.appendChild(n);const slot=n.findOne(x=>x.type==='SLOT');const paints=slot.children.map(child=>resolved(child.findOne(x=>x.type==='FRAME'&&x.name==='Avatar')));
  const expected=[DATA.primaryColors[mode],DATA.fixedColors.warning,DATA.fixedColors.positive,DATA.fixedColors.overflow];
  assert('theme/'+mode+'/group/'+size,'REQ-THEME',paints.every((p,i)=>Object.keys(expected[i]).every(k=>equal(p[k],expected[i][k]))),expected,paints);
  const overflow=slot.children[3].findOne(x=>x.type==='TEXT');assert('theme/'+mode+'/counter/'+size,'REQ-THEME',Object.keys(DATA.fixedColors.overflowText).every(k=>equal(resolved(overflow)[k],DATA.fixedColors.overflowText[k])),DATA.fixedColors.overflowText,resolved(overflow));
  themeCases.push({mode,type:'group',size,id:n.id,slotId:slot.id,paints});
 }
 const row=box(card,'Presence',445,40,'HORIZONTAL');row.itemSpacing=12;txt(row,'Presencia',12,'Regular',90);
 for(const type of ['active','busy','inactive']){const n=await av(row,'text','large');const status=n.findOne(x=>x.type==='INSTANCE'&&x.name==='Status');status.setProperties({type});const actual=resolved(status),expected=DATA.fixedColors[type];assert('theme/'+mode+'/presence/'+type,'REQ-PRESENCE',Object.keys(expected).every(k=>equal(actual[k],expected[k])),expected,actual);themeCases.push({mode,type:'presence',state:type,id:n.id,statusId:status.id,paint:actual});}
}
txt(panel,'Prueba del slot desde instancias',20,'SemiBold');
const slotsRow=box(panel,'Slots 2 y 4',1840,160,'HORIZONTAL');slotsRow.itemSpacing=32;
for(const size of ['extra-large','large','medium','small']){
 const cell=box(slotsRow,size,420,160);cell.itemSpacing=20;txt(cell,size,14,'SemiBold');
 const n=mark(groupMaster(size).createInstance());cell.appendChild(n);let slot=n.findOne(x=>x.type==='SLOT');
 const before=slot.children.map(c=>c.id);const remove=slot.children.slice(2);for(const c of remove){removed.push(c.id);c.remove();}
 assert('slot/'+size+'/remove','REQ-SLOT',slot.children.length===2&&slot.type==='SLOT',2,slot.children.length);
 const newOne=avMaster('icon',size).createInstance();slot.appendChild(newOne);created.push(newOne.id);newOne.setProperties({[P.ShowStatus]:false});
 const newTwo=avMaster('text',size).createInstance();slot.appendChild(newTwo);created.push(newTwo.id);newTwo.setProperties({[P.Initials]:'+8',[P.ShowStatus]:false});
 const last=slot.children[3];slot.insertChild(0,last);mutated.push(slot.id);
 const actual=[];for(const c of slot.children){const m=await c.getMainComponentAsync();actual.push({id:c.id,main:m?.id,linked:!!m,properties:c.componentProperties});}
 const expectedWidth=({ 'extra-large':48,large:32,medium:24,small:20})[size]*4+({'extra-large':-8,large:-6,medium:-4,small:-4})[size]*3;
 assert('slot/'+size+'/insert-reorder','REQ-SLOT',slot.children.length===4&&slot.children[0].id===newTwo.id&&actual.every(c=>c.linked),{children:4,first:newTwo.id}, {children:slot.children.length,first:slot.children[0].id,linked:actual.every(c=>c.linked)});
 assert('slot/'+size+'/layout','REQ-LAYOUT',equal(n.width,expectedWidth,.01),expectedWidth,n.width);
 slotCases.push({size,id:n.id,slotId:slot.id,before,after:actual,removed:remove.map(c=>c.id),width:n.width,height:n.height,limitViolations:slot.limitViolations});
}
txt(panel,'Contenido, iconos e imagen',20,'SemiBold');
const contentRow=box(panel,'Contenido',1840,80,'HORIZONTAL');contentRow.itemSpacing=28;contentRow.counterAxisAlignItems='CENTER';
for(const size of ['extra-large','large','medium','small'])for(const label of ['ÍÑ','WW']){
 const n=await av(contentRow,'text',size,label),text=n.findOne(x=>x.type==='TEXT'),content=n.findOne(x=>x.type==='FRAME'&&x.name==='Avatar');
 const fits=text.width<=content.width+.01&&text.height<=content.height+.01;
 contentCases.push({kind:'initials',size,label,id:n.id,textId:text.id,width:text.width,height:text.height,containerWidth:content.width,fits});
 assert('content/'+size+'/'+label,'REQ-CONTENT',fits,{maxWidth:content.width,maxHeight:content.height},{width:text.width,height:text.height});
 n.setProperties({[P.ShowStatus]:false});assert('content/'+size+'/'+label+'/hide-status','REQ-API',n.findOne(x=>x.type==='INSTANCE'&&x.name==='Status').visible===false,false,n.findOne(x=>x.type==='INSTANCE'&&x.name==='Status').visible);
}
const buildings=await figma.importComponentByKeyAsync('ac05f135edf1318580f23b4e20de17744d0453f7');
const swapped=await av(contentRow,'icon','extra-large');swapped.setProperties({[P.Icon]:buildings.id});const icon=swapped.findOne(x=>x.type==='INSTANCE'&&x.name==='Icon');
const iconColor=await figma.variables.getVariableByIdAsync(DATA.variableIds['avatar.color-icon-inverse']);
for(const v of icon.findAll(n=>n.type==='VECTOR')){v.fills=[figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:1,g:1,b:1}},'color',iconColor)];mutated.push(v.id);}
const sm=await icon.getMainComponentAsync();assert('content/icon-swap','REQ-TYPOGRAPHY',sm.remote&&sm.key==='ac05f135edf1318580f23b4e20de17744d0453f7'&&equal(icon.width,32,.01),{remote:true,key:'ac05f135edf1318580f23b4e20de17744d0453f7',width:32},{remote:sm.remote,key:sm.key,width:icon.width});
contentCases.push({kind:'icon-swap',id:swapped.id,iconId:icon.id,key:sm.key,remote:sm.remote});
const changedImage=await av(contentRow,'image','extra-large');const photo=changedImage.findOne(x=>x.type==='FRAME'&&x.name==='Avatar');const fill={...photo.fills[0],imageHash:DATA.previewHash};photo.fills=[fill];mutated.push(photo.id);const main=await changedImage.getMainComponentAsync();assert('content/image-change','REQ-IMAGE',!!main&&photo.fills[0].imageHash===DATA.previewHash,DATA.previewHash,photo.fills[0].imageHash);contentCases.push({kind:'image-change',id:changedImage.id,contentId:photo.id,mainId:main.id,imageHash:photo.fills[0].imageHash});
txt(panel,'Marca: el fondo principal sigue el tema. Presencia, alternos y contador: invariantes.',14,'SemiBold',1840);
txt(panel,'La muestra warning conserva el color fuente; el contraste medido y cualquier limitación se documentan en el comprobante. Figma no calcula +N ni ejecuta fallback de imagen, teclado o ARIA.',13,'Regular',1840);
txt(panel,'Contratos: AVATAR-001@3.0.0 / AVATAR-GROUP-001@3.0.0 · consumo: consumption/avatar y consumption/avatar-group',12,'Regular',1840);
return {panelId:panel.id,width:panel.width,height:panel.height,expectedColors:{primary:DATA.primaryColors,fixed:DATA.fixedColors},controls:controls.map(c=>c.id.startsWith('theme/')&&c.status==='PASS'?{id:c.id,requirement:c.requirement,status:c.status,expected:'expectedColors + contract recipe',actual:'themeCases; counter paint compared before recording PASS'}:c),themeCases,slotCases:slotCases.map(c=>({...c,after:c.after.map(v=>({id:v.id,main:v.main,linked:v.linked}))})),contentCases,createdNodeIds:[...new Set(created)],mutatedNodeIds:[...new Set(mutated)],removedNodeIds:removed};
