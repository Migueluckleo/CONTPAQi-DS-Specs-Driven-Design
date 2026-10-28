// Current Button owns 45 tokens. Historical 47-token bootstrap is archived, never executed.
if(figma.fileKey!==DATA.fileKey)throw new Error('Wrong destination');
if(DATA.tokens.length!==45)throw new Error('Resolve BUTTON-001@4.0.0 before consumption');
const variables=[];for(const t of DATA.tokens){const v=await figma.variables.getVariableByIdAsync(t.nativeId);if(!v||v.name!==t.figmaName)throw new Error('Registered Button variable drift');variables.push({id:v.id,key:v.key,name:v.name});}
return {variables,createdNodeIds:[],mutatedNodeIds:[]};
