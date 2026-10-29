// Read-only native verification against selected source snapshots and binding recipes.
figma.skipInvisibleInstanceChildren=false;
const page=await figma.getNodeByIdAsync(DATA.page);await page.loadAsync();
const issues=[],variants=[],counts={nodes:0,texts:0,bindings:0,icons:0,badges:0,effects:0};
const close=(a,b)=>typeof a==='number'&&typeof b==='number'?Math.abs(a-b)<.00001:JSON.stringify(a)===JSON.stringify(b);
function expect(id,field,actual,wanted){if(!close(actual,wanted))issues.push({id,field,actual,wanted})}
for(const v of DATA.variants){const root=await figma.getNodeByIdAsync(v.nativeId);const owner=root.parent;const props=owner.componentPropertyDefinitions;
 expect(root.id,'nonVariantProperties',Object.values(props).filter(p=>p.type!=='VARIANT').length,11);
 const facts={id:root.id,axes:v.axes,w:root.width,h:root.height,nodes:0,sourceId:v.id};
 for(const r of v.rows){const n=await figma.getNodeByIdAsync(r.nativeId);counts.nodes++;facts.nodes++;
  // Invisible auto-layout children retain stale source coordinates. Their active geometry is exercised by property QA.
  if(r.visible){expect(n.id,'width',n.width,r.w);expect(n.id,'height',n.height,r.h);if(r.path!=='root'){expect(n.id,'x',n.x,r.x);expect(n.id,'y',n.y,r.y)}}
  expect(n.id,'visible',n.visible,r.visible);
  for(const [field,tid]of Object.entries(r.bindings)){
   let actual;if(field.startsWith('effect.')){const [,index,key]=field.split('.');actual=n.effects?.[Number(index)]?.boundVariables?.[key]?.id;}
   else if(field==='fills'||field==='strokes')actual=n[field][0]?.boundVariables?.color?.id;
   else{let b=n.boundVariables?.[field];if(field==='strokeWeight'&&!b){const sides=['strokeTopWeight','strokeBottomWeight','strokeLeftWeight','strokeRightWeight'].map(k=>n.boundVariables?.[k]?.id);if(sides.every(x=>x===DATA.variableIds[tid]))b={id:sides[0]};}if(Array.isArray(b))b=b[0];actual=b?.id;if(!actual&&n.type==='TEXT'&&n.textStyleId){const s=await figma.getStyleByIdAsync(n.textStyleId);actual=s.boundVariables?.[field]?.id;}}
   if(n.type==='INSTANCE'&&n.name==='Badge')continue;
   expect(n.id,'binding.'+field,actual,DATA.variableIds[tid]);counts.bindings++;
  }
  if(n.type==='TEXT'){counts.texts++;expect(n.id,'characters',n.characters,r.text);expect(n.id,'fontSize',n.fontSize,r.fontSize);expect(n.id,'fontFamily',n.fontName.family,r.font.family);expect(n.id,'fontStyle',n.fontName.style,r.font.style);expect(n.id,'lineHeight',n.lineHeight,r.lineHeight);expect(n.id,'tracking.unit',n.letterSpacing.unit,'PIXELS');expect(n.id,'tracking.value',n.letterSpacing.value,r.letterSpacing.unit==='PERCENT'?r.letterSpacing.value*r.fontSize/100:r.letterSpacing.value);expect(n.id,'textStyleId',n.textStyleId,DATA.styles[r.name==='supporting-text'?'input/helper':r.name==='Label'||r.name==='textbox'?'input/label':'input/content']);if(r.name==='supporting-text')expect(n.id,'autoResize',n.textAutoResize,'HEIGHT');else{expect(n.id,'autoResize',n.textAutoResize,r.textAutoResize);expect(n.id,'truncation',n.textTruncation,r.textTruncation);expect(n.id,'maxLines',n.maxLines,r.maxLines);}}
  if(n.type==='INSTANCE'){const main=await n.getMainComponentAsync();if(n.name==='Badge'){counts.badges++;expect(n.id,'badge.main',main.id,DATA.badge.id);expect(n.id,'badge.exposed',n.isExposedInstance,true);const label=n.findOne(c=>c.type==='TEXT');expect(n.id,'badge.label',label.characters,'MXN');}else{counts.icons++;expect(n.id,'icon.key',main.key,DATA.icons[n.name].key);for(const vec of n.findAll(c=>c.type==='VECTOR'))expect(vec.id,'icon.binding',vec.fills[0]?.boundVariables?.color?.id,DATA.variableIds[r.vectorToken]);}}
  if(r.effects){counts.effects+=r.effects.length;expect(n.id,'effect.style',n.effectStyleId,DATA.styles[r.effects.length===2?'input/focus-double':'input/focus']);expect(n.id,'effect.count',n.effects.length,r.effects.length);for(let i=0;i<r.effects.length;i++){const e=n.effects[i];for(const key of ['spread','radius','offset','color','type','showShadowBehindNode'])expect(n.id,'effect.'+i+'.'+key,e[key],r.effects[i][key]);}}
 }
 expect(root.id,'reactions',root.reactions.length,0);variants.push(facts);
}
const result={status:issues.length?'FAIL':'PASS',issues,variants,counts,tolerance:.00001,sourceReadOnly:true,scope:'Native structure/typography/bindings; no HTML or keyboard certification'};if(JSON.stringify(result).length>45000)throw Error('Audit output too large: narrow batch');return result;
