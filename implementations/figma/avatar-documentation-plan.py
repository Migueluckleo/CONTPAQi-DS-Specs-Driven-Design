"""Prepare presentation recipes from the read-only page snapshot, not another contract."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[2]
def read(p):return json.loads((R/p).read_text())
ns=read('evidence/avatar-pilot/source/page-snapshot.json')['nodes'];ix={n['id']:n for n in ns}
tl={n['id']:n for n in read('evidence/avatar-pilot/source/text-layout.json')['texts']}
children={}
for n in ns:children.setdefault(n['parent'],[]).append(n)
replacements={
 '8890:851':'Representa una identidad con fotografía, iniciales o icono. Prioridad de contenido: image → text → icon.',
 '8890:865':'Cuatro tamaños de Avatar: extra-large 48 px, large 32 px, medium 24 px y small 20 px. Usa size; no escales manualmente.',
 '8890:879':'Show status controla la presencia opcional. Los tipos active, busy e inactive son fijos y requieren texto o tooltip.',
 '8890:893':'Máximo dos letras en mayúsculas. Conserva Ñ y acentos; omite partículas y régimen societario.',
 '9064:29668':'Grupo traslapado con slot nativo de 2 a 4 elementos. Anillo real 1 px; colores alternos fijos y primer Avatar temático.'
}
def recipe(n):
 d={k:v for k,v in n.items() if k not in ['main','properties','boundVariables','reactions','effectStyleId','textStyleId','segments','componentPropertyReferences']}
 if n['type']=='INSTANCE' and n.get('main'):
  p=n['main'].get('parent') or {}
  if p.get('id')=='1132:21344':
   props={k.split('#')[0]:v['value'] for k,v in n['properties'].items()};d.update(kind='avatar',props=props)
   status=next((c for c in children.get(n['id'],[]) if c['name']=='Status'),None)
   if status:d['statusType']=status['properties']['type']['value']
   return d
  if p.get('id')=='9064:477':d.update(kind='group',size=n['properties']['size']['value']);return d
  if n['main']['name']=='Icon / Platform / Idea':d['kind']='idea';return d
 if n['type']=='TEXT':
  seg=n['segments'][0];d.update({k:v for k,v in seg.items() if k not in ['characters','start','end']});d.update(tl.get(n['id'],{}));d['characters']=replacements.get(n['id'],n['characters']);d['fontName']={k:seg['fontName'][k] for k in ['family','style']}
 d['kids']=[recipe(c) for c in children.get(n['id'],[]) if c['type']!='VECTOR']
 return d
for id in ['8890:846','8890:860','8890:874','8890:888','9064:29663']:
 p=R/'evidence/avatar-pilot/presentation'/('section-'+id.replace(':','-')+'.json');p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(recipe(ix[id]),ensure_ascii=False,indent=2)+'\n')
print('Five presentation sections prepared; original text retained in source snapshot.')
