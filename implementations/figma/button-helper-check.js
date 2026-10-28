// Shared Loader is selected and checked by its own contract; no Button private animation.
if(figma.fileKey!==DATA.fileKey||DATA.loader.contract.id!=='LOADER-001')throw new Error('Shared Loader required');
const issues=[];for(const v of DATA.loader.variants){const n=await figma.getNodeByIdAsync(v.id);if(!n||n.type!=='COMPONENT'||n.parent.name!=='Loader')issues.push(v.id);}
return {status:issues.length?'FAIL':'PASS_SHARED_DEPENDENCY_LINKS',issues,limitation:'Animation playback belongs to Loader QA, not this link check.'};
