if(figma.fileKey!==DATA.fileKey)throw Error('Wrong target');
const page=await figma.getNodeByIdAsync(DATA.pageId);await figma.setCurrentPageAsync(page);
await figma.loadFontAsync({family:'Manrope',style:'Bold'});await figma.loadFontAsync({family:'Manrope',style:'Regular'});
figma.skipInvisibleInstanceChildren=false;
const vars=await figma.variables.getLocalVariablesAsync(),cs=await figma.variables.getLocalVariableCollectionsAsync();
const nativeNames=new Map(vars.map(v=>[v.id,v]));
const component=cs.find(c=>c.id===DATA.collection.id),semantic=cs.find(c=>c.name==='semantic');
const byName=new Map(vars.map(v=>[v.variableCollectionId+':'+v.name,v]));
function componentToken(t){return nativeNames.get(t.id)??byName.get(component.id+':'+(t.figmaName??DATA.figmaNames?.[t.name]??t.name));}
const issues=[],families={},themeChecks=[];let aliases=0,paints=0;
const eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
function check(field,a,b){if(!eq(a,b))issues.push({field,actual:a,expected:b});}
check('inventory',vars.length,251+DATA.tokens.length);
for(const v of vars)if(v.variableCollectionId!==component.id)check(v.id+':scope',v.scopes,[]);
for(const t of DATA.tokens){const v=componentToken(t);if(!v)throw Error('Missing native component token '+t.name+'; supply figmaName or native ID');check(t.name+':WEB',v.codeSyntax.WEB,'var(--'+t.name+')');check(t.name+':type',v.resolvedType,t.type);check(t.name+':scopes',v.scopes,t.scopes);
 for(const [name,id]of Object.entries(DATA.collection.modeIds)){const sem=byName.get(semantic.id+':'+t.aliases[name]);check(t.name+':'+name,v.valuesByMode[id],{type:'VARIABLE_ALIAS',id:sem.id});aliases++;}}
for(const [kind,f]of Object.entries(DATA.families)){const set=await figma.getNodeByIdAsync(f.setId);families[kind]={id:set.id,key:set.key,name:set.name,properties:set.componentPropertyDefinitions};}
for(const c of [...DATA.review.instances,...DATA.review.cases]){const n=await figma.getNodeByIdAsync(c.id);check(n.id+':main',n.mainComponent.id,c.mainId);
 if(c.label){const p=DATA.families[c.kind].properties;check(n.id+':label',n.componentProperties[p.labelKey].value,c.label);check(n.id+':left',n.componentProperties[p.showLeftKey].value,c.left);check(n.id+':right',n.componentProperties[p.showRightKey].value,c.right);
 const texts=n.findAllWithCriteria({types:['TEXT']});check(n.id+':no-overflow',texts.every(t=>t.width<=n.width-n.paddingLeft-n.paddingRight),true);}}
const review=await figma.getNodeByIdAsync(DATA.review.reviewFrameId);const prior=review.explicitVariableModes[component.id];
try{for(const [theme,mode]of Object.entries(DATA.collection.modeIds)){review.setExplicitVariableModeForCollection(component,mode);let resolved=0;
 for(const t of DATA.tokens){const v=componentToken(t),sem=byName.get(semantic.id+':'+t.aliases[theme]);check(theme+':'+t.name,v.resolveForConsumer(review).value,sem.resolveForConsumer(review).value);resolved++;}
 for(const c of DATA.review.instances){const n=await figma.getNodeByIdAsync(c.id);for(const child of [n,...n.findAllWithCriteria({types:['TEXT']})])for(const field of ['fills','strokes'])for(const paint of child[field]??[]){const id=paint.boundVariables?.color?.id;if(id){const v=vars.find(v=>v.id===id);const value=v.resolveForConsumer(child).value;check(theme+':paint:'+child.id+':'+field,paint.color,{r:value.r,g:value.g,b:value.b});paints++;}}}
 themeChecks.push({theme,mode,tokensResolved:resolved});
}}finally{if(prior)review.setExplicitVariableModeForCollection(component,prior);else review.clearExplicitVariableModeForCollection(component);}
return{status:issues.length?'FAIL':'PASS_CONSUMERS_AND_THEMES',variables:vars.length,aliasesChecked:aliases,foundationalScopesChecked:251,instancesChecked:94,themeChecks,paintsChecked:paints,families,issues};
