if(figma.fileKey!==DATA.fileKey)throw Error('Wrong target');
const page=await figma.getNodeByIdAsync(DATA.pageId);await figma.setCurrentPageAsync(page);
const issues=[];const near=(a,b)=>Math.abs(a-b)<=0.00001;
function check(field,a,b){if(typeof a==='number'&&typeof b==='number'? !near(a,b):JSON.stringify(a)!==JSON.stringify(b))issues.push({field,actual:a,expected:b});}
for(const r of DATA.frames){const n=await figma.getNodeByIdAsync(DATA.helpers.sourceToTarget[r.id]);check(n.id+':width',n.width,r.width);check(n.id+':height',n.height,r.height);
 for(const [name,shape]of [['Arc',r.arc],['Track',r.track]]){const e=n.children.find(c=>c.name===name);for(const k of ['startingAngle','endingAngle','innerRadius'])check(e.id+':'+k,e.arcData[k],shape[k]);}
 check(n.id+':reaction-count',n.reactions.length,1);const reaction=n.reactions[0],expected=r.reactions[0];check(n.id+':trigger',reaction.trigger,expected.trigger);check(n.id+':next',reaction.actions[0].destinationId,DATA.helpers.sourceToTarget[expected.actions[0].destinationId]);}
const icon=await figma.getNodeByIdAsync(DATA.helpers.glyphId),vector=icon.children[0],expected=DATA.icon.children[0];check(icon.id+':size',[icon.width,icon.height],[32,32]);
check(vector.id+':path-count',vector.vectorPaths.length,expected.vectorPaths.length);let pathMaxError=0;
for(let i=0;i<expected.vectorPaths.length;i++){const a=vector.vectorPaths[i],b=expected.vectorPaths[i];check(vector.id+':winding',a.windingRule,b.windingRule);
 const parts=x=>x.match(/[A-Za-z]|[-+]?(?:\d*\.\d+|\d+\.?\d*)(?:[eE][-+]?\d+)?/g);
 const av=parts(a.data),bv=parts(b.data);check(vector.id+':path-tokens',av.length,bv.length);
 for(let j=0;j<bv.length;j++){const x=Number(av[j]),y=Number(bv[j]);if(Number.isFinite(x)&&Number.isFinite(y)){pathMaxError=Math.max(pathMaxError,Math.abs(x-y));check(vector.id+':coordinate:'+j,x,y);}else check(vector.id+':command:'+j,av[j],bv[j]);}}
for(const k of ['x','y','width','height'])check(vector.id+':'+k,vector[k],expected[k]);
return{status:issues.length?'FAIL':'PASS_HELPER_STRUCTURE',spinnerFrames:DATA.frames.length,cycles:3,iconPaths:vector.vectorPaths.length,pathMaxError,numericTolerance:0.00001,issues,limitation:'Native animation structure verified; presenter playback not exercised.'};
