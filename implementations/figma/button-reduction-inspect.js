if(figma.fileKey!==DATA.fileKey)throw Error('Wrong destination');
const p=await figma.getNodeByIdAsync(DATA.pageId);await figma.setCurrentPageAsync(p);figma.skipInvisibleInstanceChildren=false;
const vars=await figma.variables.getLocalVariablesAsync(),values=[],seen=new Map(),rows=[];
const intern=v=>{const key=JSON.stringify(v);if(!seen.has(key)){seen.set(key,values.length);values.push(v);}return seen.get(key);};
let count=0;const nodes=[];for(const id of DATA.rootIds){const n=await figma.getNodeByIdAsync(id);nodes.push(n,...n.findAll());}
for(const n of nodes){const bindings=[];for(const [field,value]of Object.entries(n.boundVariables??{})){if(['fills','strokes'].includes(field))continue;const refs=Array.isArray(value)?value:[value];for(const v of refs)if(DATA.idMigration[v.id])bindings.push([field,v.id]);}
 for(const field of ['fills','strokes'])if(field in n&&Array.isArray(n[field]))n[field].forEach((paint,i)=>{for(const [part,v]of Object.entries(paint.boundVariables??{}))if(DATA.idMigration[v.id])bindings.push([field,i,part,v.id]);});
 if(bindings.length){rows.push([n.id,n.type,n.width,n.height,bindings].map(intern));count+=bindings.length;}}
return{status:'CAPTURED',fields:['id','type','width','height','bindings'],values,rows,nodes:rows.length,bindings:count,rootCount:DATA.rootIds.length,variables:vars.length};
