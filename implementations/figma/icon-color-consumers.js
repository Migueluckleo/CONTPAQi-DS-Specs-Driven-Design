// Scoped override audit/repair. DATA is a derived pairing and native identity projection.
if(figma.fileKey!=='98xEw6sK8FRVNEhopM5SSz')throw Error('Blue Heart destination only');
figma.skipInvisibleInstanceChildren=false;
await figma.loadFontAsync({family:'Manrope',style:'Regular'});await figma.loadFontAsync({family:'Manrope',style:'Bold'});
const page=await figma.getNodeByIdAsync(DATA.page);await figma.setCurrentPageAsync(page);
const cache={};async function variable(id){if(!cache[id])cache[id]=await figma.variables.getVariableByIdAsync(id);return cache[id]}
const selected=new Set(DATA.pairs.map(p=>p.variantId)),changes=[],issues=[],controls=[],mutatedNodeIds=[];let pairCount=0;
for(const control of page.findAllWithCriteria({types:['INSTANCE']})){
 const main=await control.getMainComponentAsync();if(!selected.has(main.id))continue;
 let count=0;for(const pair of DATA.pairs.filter(p=>p.variantId===main.id)){
  const icon=control.findOne(n=>n.type==='INSTANCE'&&n.id.endsWith(';'+pair.iconId));
  const text=control.findOne(n=>n.type==='TEXT'&&n.id.endsWith(';'+pair.textId));
  if(!icon||!text){issues.push({control:control.id,part:pair.iconId,reason:'missing paired part'});continue;}
  const expected=await variable(DATA.nativeIds[pair.targetToken]);const textId=text.fills[0]?.boundVariables?.color?.id;const tv=textId?await variable(textId):null;
  if(!tv||JSON.stringify(tv.valuesByMode)!==JSON.stringify(expected.valuesByMode)){issues.push({control:control.id,text:text.id,reason:'text override needs an adopted counterpart',textId,target:expected.id});continue;}
  const vectors=icon.findAll(n=>n.type==='VECTOR'||n.type==='BOOLEAN_OPERATION'||n.type==='ELLIPSE'||n.type==='RECTANGLE');
  for(const vector of vectors){for(const field of ['fills','strokes']){if(!vector[field]?.some(p=>p.visible!==false))continue;
   const paints=vector[field].map(p=>({...p}));let changed=false;for(let i=0;i<paints.length;i++){if(paints[i].visible===false)continue;const before=paints[i].boundVariables?.color?.id;if(before!==expected.id&&DATA.repair){paints[i]=figma.variables.setBoundVariableForPaint(paints[i],'color',expected);changes.push({control:control.id,icon:icon.id,id:vector.id,field,index:i,before,after:expected.id});changed=true;}}
   if(changed){vector[field]=paints;mutatedNodeIds.push(vector.id);}
   for(const p of vector[field].filter(p=>p.visible!==false)){const iv=p.boundVariables?.color?.id?await variable(p.boundVariables.color.id):null;const equal=!!iv&&JSON.stringify(iv.valuesByMode)===JSON.stringify(tv.valuesByMode);const a=p.color,b=text.fills[0].color;const resolved=['r','g','b'].every(k=>Math.abs(a[k]-b[k])<.00001);if(!equal||!resolved)issues.push({control:control.id,icon:icon.id,id:vector.id,text:text.id,field,reason:'alias or resolved color differs',equal,resolved,iconColor:a,textColor:b});}
  }}count++;pairCount++;
 }controls.push({id:control.id,mainId:main.id,pairs:count});
}
const result={status:issues.length?'FAIL':'PASS',family:DATA.family,controls,pairCount,changes,issues,createdNodeIds:[],mutatedNodeIds:[...new Set(mutatedNodeIds)]};if(JSON.stringify(result).length>45000)throw Error('Narrow consumer audit');return result;
