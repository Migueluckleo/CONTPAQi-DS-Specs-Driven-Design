// Read only. Text bindings may be arrays over text ranges; all ranges must agree.
figma.skipInvisibleInstanceChildren=false;
const p=await figma.getNodeByIdAsync('78:97');await p.loadAsync();
const all={};function visit(n){all[n.id]=n;if('children'in n)n.children.forEach(visit);}
visit(await figma.getNodeByIdAsync('79:26'));visit(await figma.getNodeByIdAsync('78:102'));
let checked=0;const errors=[];
for(const[id,fields]of DATA){const n=all[id];if(!n){errors.push({id,error:'MISSING_NODE'});continue;}for(const[field,expected]of Object.entries(fields)){
 let values;if(field.startsWith('fills.'))values=[n.fills[Number(field.split('.')[1])]?.boundVariables?.color];else if(field.startsWith('strokes.'))values=[n.strokes[Number(field.split('.')[1])]?.boundVariables?.color];else{const b=n.boundVariables?.[field];values=Array.isArray(b)?b:[b];}
 const actual=values.filter(Boolean).map(b=>b.id);checked++;if(!actual.length||actual.some(v=>v!==expected))errors.push({id,field,expected,actual});
}}
return{checked,nodes:DATA.length,errors,status:errors.length?'FAIL':'PASS',method:'Actual paints and numeric bindings; every text-range alias; descendants traversed including hidden Count'};
