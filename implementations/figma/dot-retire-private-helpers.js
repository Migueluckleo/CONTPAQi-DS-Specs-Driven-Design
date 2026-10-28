if(figma.fileKey!=='98xEw6sK8FRVNEhopM5SSz')throw new Error('Destination only');
figma.skipInvisibleInstanceChildren=false;const old=new Set(DATA.oldComponentIds),references=[];
for(const p of figma.root.children){await p.loadAsync();for(const n of p.findAllWithCriteria({types:['INSTANCE']})){const m=await n.getMainComponentAsync();if(m&&old.has(m.id))references.push(n.id);}}
if(references.length)throw new Error('Live helper references '+JSON.stringify(references));
const deletedNodes=[];for(const id of DATA.helperIds){const n=await figma.getNodeByIdAsync(id);if(n){deletedNodes.push(n.id,...n.findAll(()=>true).map(x=>x.id));n.remove();}}
let styleUsers=[];for(const p of figma.root.children)styleUsers.push(...p.findAllWithCriteria({types:['TEXT']}).filter(n=>n.textStyleId===DATA.oldStyle).map(n=>n.id));if(styleUsers.length)throw new Error('Count style still used');const style=await figma.getStyleByIdAsync(DATA.oldStyle);if(style)style.remove();
const ids=Object.values(DATA.oldVariables),retired=new Set(ids),hits=[];
function aliases(value,out=[]){if(typeof value==='string'&&retired.has(value))out.push(value);else if(value&&typeof value==='object')for(const v of Object.values(value))aliases(v,out);return out;}
for(const p of figma.root.children)for(const n of p.findAll(()=>true))for(const id of aliases(n.boundVariables))hits.push({node:n.id,variable:id});
for(const s of await figma.getLocalTextStylesAsync())for(const id of aliases(s.boundVariables))hits.push({style:s.id,variable:id});
for(const v of await figma.variables.getLocalVariablesAsync())if(!retired.has(v.id))for(const id of aliases(v.valuesByMode))hits.push({variable:v.id,target:id});
if(hits.length)throw new Error('Retired variable users '+JSON.stringify(hits).slice(0,6000));
for(const id of ids){const v=await figma.variables.getVariableByIdAsync(id);if(v)v.remove();}
return {legacyInstanceReferences:references,deletedNodeIds:deletedNodes,deletedStyleIds:[DATA.oldStyle],deletedVariables:DATA.oldVariables,remainingCollections:(await figma.variables.getLocalVariableCollectionsAsync()).map(c=>({name:c.name,count:c.variableIds.length}))};
