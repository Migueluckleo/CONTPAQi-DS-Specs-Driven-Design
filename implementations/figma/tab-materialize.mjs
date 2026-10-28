// Prepare bounded use_figma arguments; this script does not access Figma.
import fs from 'node:fs';
import path from 'node:path';
const root=process.cwd(), operation=process.argv[2], batch=Number(process.argv[3]||0);
if(!['foundation','family','populate'].includes(operation))throw new Error('Expected foundation, family or populate');
const read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
const plan=read('consumption/tab/build-plan.2.0.0.json');
const scripts=process.env.BLUEHEART_FIGMA_HELPERS;
if(!scripts)throw new Error('Set BLUEHEART_FIGMA_HELPERS to the scripts directory of the loaded official figma-generate-library skill');
const helper=name=>fs.readFileSync(path.join(scripts,name+'.js'),'utf8');
const builder=fs.readFileSync(path.join(root,'implementations/figma/tab-builder.js'),'utf8');
const common=builder.split('async function foundation()')[0];
const functionBody=builder.slice(builder.indexOf('async function '+operation+'()')).split(operation==='foundation'?'async function family()':operation==='family'?'async function populate()':'return await ({foundation,family,populate})')[0];
let data={operation};
if(operation==='foundation') {
  const fp=value=>{let h=2166136261;for(let i=0;i<value.length;i++)h=Math.imul(h^value.charCodeAt(i),16777619);return h>>>0;};
  const baseline=fs.readdirSync(path.join(root,'evidence/tab-pilot/destination')).filter(f=>/^variables-before-\d+\.json$/.test(f)).flatMap(f=>read('evidence/tab-pilot/destination/'+f).variables);
  const mapping=read('evidence/figma-application/application-map.json');const r=plan.variants[0].roles;
  data={...data,modes:plan.modes,tokens:plan.tokens.map(({source,...t})=>t),semanticIds:Object.fromEntries(mapping.variables.filter(v=>v.layer==='semantic').map(v=>['semantic.'+v.name,v.destination_id])),baseline:Object.fromEntries(baseline.map(v=>[v.id,fp(JSON.stringify({name:v.name,type:v.type,collectionId:v.collectionId,scopes:v.scopes,valuesByMode:v.valuesByMode,codeSyntax:v.codeSyntax,description:v.description}))])),shadowStyle:plan.shadowStyle,count:plan.nodes[r.count],countText:plan.nodes[r.countLabel]};
} else {
  const foundation=read('consumption/tab/current-native-ledger.json');
  data={...data,pageId:foundation.pageId};
  if(operation==='populate') {
    const family=read('evidence/tab-pilot/destination/family.json');
    const same=(a,b)=>['type','selected','state'].every(k=>a[k]===b[k]);
    const variants=plan.variants.slice(batch*4,batch*4+4);if(!variants.length)throw new Error('Empty batch');
    data={...data,...foundation,setId:family.setId,variantIds:Object.fromEntries(plan.variants.map(v=>[v.sourceId,family.variants.find(t=>same(v.axes,t.axes)).id])),variants,nodes:Object.fromEntries(variants.flatMap(v=>Object.entries(v.roles).filter(([role])=>!['count','countLabel'].includes(role)).map(([,id])=>[id,plan.nodes[id]])))};
    const first='evidence/tab-pilot/destination/populate-0.json';if(batch && fs.existsSync(path.join(root,first)))data.properties=read(first).properties;
  }
}
let code='const DATA='+JSON.stringify(data)+';\n'+(operation==='family'?helper('createComponentWithVariants')+'\n':helper('bindVariablesToComponent')+'\n')+common+functionBody+'\nreturn await '+operation+'();';
code=code.replace(/\/\*[\s\S]*?\*\//g,'').replace(/^\s*\/\/.*$/gm,'');
if(code.length>50000)throw new Error('Connector code exceeds 50,000 characters: '+code.length);
if(!process.env.BLUEHEART_FIGMA_SESSION)throw new Error('Set BLUEHEART_FIGMA_SESSION from the current create_session result');
const target='/tmp/tab-'+operation+'-'+batch+'.json';
fs.writeFileSync(target,JSON.stringify({fileKey:plan.destinationFileKey,sessionId:process.env.BLUEHEART_FIGMA_SESSION,link_id:'link_6aa838b2077081918681c60e737a01c6',skillNames:'figma-use,figma-generate-library',description:'Materialize registered Tab '+operation+' batch '+batch+' in Blue Heart DS only',code}));
console.log(JSON.stringify({target,codeCharacters:code.length}));
