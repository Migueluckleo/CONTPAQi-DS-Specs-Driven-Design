// Rebind before deletion. Only exact IDs from the migration ledger may retire.
if(figma.fileKey!==DATA.fileKey)throw Error('Wrong destination');
const page=await figma.getNodeByIdAsync(DATA.pageId);await figma.setCurrentPageAsync(page);figma.skipInvisibleInstanceChildren=false;
const all=await figma.variables.getLocalVariablesAsync(),vars=new Map(all.map(v=>[v.id,v]));
const retired=new Set(DATA.tokens.flatMap(t=>t.retireIds));
for(const [from,to]of Object.entries(DATA.idMigration)){const a=vars.get(from),b=vars.get(to);if(!a||!b||a.variableCollectionId!==DATA.collection.id||b.variableCollectionId!==DATA.collection.id)throw Error('Missing/moved token');
 if(a.resolvedType!==b.resolvedType||JSON.stringify(a.scopes)!==JSON.stringify(b.scopes)||JSON.stringify(a.valuesByMode)!==JSON.stringify(b.valuesByMode))throw Error('Non-equivalent tokens '+from+' '+to);}
const nodes=[];for(const id of DATA.rootIds){const n=await figma.getNodeByIdAsync(id);nodes.push(n,...n.findAll());}
const fonts=new Map();for(const n of nodes)if(n.type==='TEXT')for(const s of n.getStyledTextSegments(['fontName']))fonts.set(JSON.stringify(s.fontName),s.fontName);
for(const f of fonts.values())await figma.loadFontAsync(f);
const mutatedNodeIds=[],removedVariableIds=[],retainedVariables=[];let changedBindings=0;
try{
for(const n of nodes){let changed=false;
 for(const [field,value]of Object.entries(n.boundVariables??{})){
  if(['fills','strokes'].includes(field))continue;
  const refs=Array.isArray(value)?value:[value];const ids=[...new Set(refs.map(v=>v.id))];
  if(ids.some(id=>retired.has(id))){if(ids.length!==1)throw Error('Mixed binding requires range-aware migration '+n.id+':'+field);
   n.setBoundVariable(field,vars.get(DATA.idMigration[ids[0]]));changed=true;changedBindings++;}
 }
 for(const field of ['fills','strokes'])if(field in n&&Array.isArray(n[field])){
  let paintChanged=false;const paints=n[field].map(paint=>{let next=paint;for(const [part,v]of Object.entries(paint.boundVariables??{}))if(retired.has(v.id)){next=figma.variables.setBoundVariableForPaint(next,part,vars.get(DATA.idMigration[v.id]));paintChanged=true;changedBindings++;}return next;});
  if(paintChanged){n[field]=paints;changed=true;}
 }
 if(changed)mutatedNodeIds.push(n.id);
}
// Inspect all page consumers, including inherited instance bindings and overrides.
const residual=[];function visit(value,path){if(!value||typeof value!=='object')return;if(value.type==='VARIABLE_ALIAS'&&retired.has(value.id))residual.push({path,id:value.id});for(const [k,v]of Object.entries(value))visit(v,path+'.'+k);}
for(const n of page.findAll()){visit(n.boundVariables,n.id+':bindings');for(const field of ['fills','strokes'])if(field in n&&Array.isArray(n[field]))visit(n[field],n.id+':'+field);}
for(const v of all)if(!retired.has(v.id))visit(v.valuesByMode,v.id+':aliases');
if(residual.length)return{status:'BLOCKED_RESIDUAL_REFERENCES',residual,mutatedNodeIds,removedVariableIds,changedBindings};
for(const t of DATA.tokens){const v=vars.get(t.id);v.name=t.name;v.scopes=t.scopes;v.description='Button: token compartido por propiedad y aliases idénticos en los cuatro temas. Estados y variantes se resuelven en la receta, sin duplicar variables.';v.setVariableCodeSyntax('WEB','var(--'+t.name+')');retainedVariables.push({id:v.id,key:v.key,name:v.name,scopes:v.scopes});}
for(const id of retired){vars.get(id).remove();removedVariableIds.push(id);}
return{status:'APPLIED_TOKEN_REDUCTION',before:125,after:retainedVariables.length,changedBindings,mutatedNodeIds,removedVariableIds,retainedVariables,residualReferences:0};
}catch(e){return{status:'PARTIAL_FAILURE',error:String(e),mutatedNodeIds,removedVariableIds,retainedVariables,changedBindings};}
