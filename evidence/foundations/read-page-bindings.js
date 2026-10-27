const page=await figma.getNodeByIdAsync('__PAGE_ID__');
await figma.setCurrentPageAsync(page);
const nodes=page.findAll(()=>true);
const variables={},styles={},errors=[];
let textNodes=0,textRanges=0;
const seen=new Set();
function owner(n){let p=n;while(p&&p.type!=='PAGE'){if(p.type==='COMPONENT_SET'||p.type==='COMPONENT')return {id:p.id,name:p.name,type:p.type};p=p.parent;}return null;}
function record(id,field,node){
const key=node.id+'|'+field+'|'+id;if(seen.has(key))return;seen.add(key);
const row=variables[id]||(variables[id]={references:0,nodeIds:new Set(),fields:{},samples:[]});
row.references++;row.nodeIds.add(node.id);row.fields[field]=(row.fields[field]||0)+1;
if(row.samples.length<2)row.samples.push({nodeId:node.id,name:node.name,type:node.type,field,owner:owner(node)});
}
function walk(value,prefix,node){
if(!value||typeof value!=='object')return;
if(value.type==='VARIABLE_ALIAS'&&typeof value.id==='string'){record(value.id,prefix,node);return;}
if(Array.isArray(value)){for(const item of value)walk(item,prefix,node);}
else for(const [key,item]of Object.entries(value))walk(item,prefix?prefix: key,node);
}
function style(id,field,node){if(typeof id!=='string'||!id)return;const row=styles[id]||(styles[id]={references:0,fields:{},sample:{nodeId:node.id,name:node.name,field}});row.references++;row.fields[field]=(row.fields[field]||0)+1;}
for(const node of nodes){
try{
if('boundVariables'in node)walk(node.boundVariables,'',node);
for(const field of ['fills','strokes','effects','layoutGrids'])if(field in node){const values=node[field];if(Array.isArray(values))for(const value of values)walk(value.boundVariables,field,node);}
for(const field of ['fillStyleId','strokeStyleId','effectStyleId','gridStyleId'])if(field in node)style(node[field],field,node);
if(node.type==='TEXT'){
textNodes++;style(node.textStyleId,'textStyleId',node);
try{const ranges=node.getStyledTextSegments(['boundVariables','textStyleId']);textRanges+=ranges.length;for(const range of ranges){walk(range.boundVariables,'textRange:'+range.start+':'+range.end,node);style(range.textStyleId,'textRangeStyle',node);}}catch(e){if(errors.length<12)errors.push({nodeId:node.id,operation:'textRanges',message:String(e)});}
}
}catch(e){if(errors.length<12)errors.push({nodeId:node.id,operation:'node',message:String(e)});}
}
return {fileKey:figma.fileKey,page:{id:page.id,name:page.name},nodeCount:nodes.length,textNodes,textRanges,variables:Object.fromEntries(Object.entries(variables).map(([id,row])=>[id,{references:row.references,nodeCount:row.nodeIds.size,fields:row.fields,samples:row.samples}])),styles,errors,sampleLimitPerVariable:2,coverage:'All descendants; visible and hidden; node/paint/effect/grid and text-range bindings; sampled identities only; no consumer value resolution',mutations:0};
