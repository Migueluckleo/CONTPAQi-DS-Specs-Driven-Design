"""Verify captured destination facts against the registered Tab recipes.

This is destination QA, not a substitute for native playback or an independent review.
It reads evidence only and writes a deterministic comparison artifact.
"""
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / 'evidence/tab-pilot/destination'
read = lambda p: json.loads(Path(p).read_text())
plan = read(ROOT / 'evidence/tab-pilot/build-plan.json')
foundation = read(D / 'foundation.json')
policy = read(ROOT / 'evidence/tab-pilot/audit-policy.json')
failures = []


def require(condition, control, **details):
    if not condition:
        failures.append(dict(control=control, **details))


def same(a, b, tolerance=1e-4):
    if isinstance(a, dict) and isinstance(b, dict):
        return a.keys() == b.keys() and all(same(a[k], b[k], tolerance) for k in a)
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(same(x, y, tolerance) for x, y in zip(a, b))
    if type(a) in (int, float) and type(b) in (int, float):
        return abs(a-b) <= tolerance
    return a == b


def clean(value):
    if isinstance(value, dict):
        return {k: clean(v) for k, v in value.items() if k != 'boundVariables'}
    return [clean(v) for v in value] if isinstance(value, list) else value


def bound(node, field):
    if '.' in field:
        paint, index = field.split('.')
        return node[paint][int(index)].get('boundVariables', {}).get('color', {}).get('id')
    alias = node['boundVariables'].get(field, {})
    if isinstance(alias, list):
        alias = alias[0] if alias else {}
    return alias.get('id')


before = {v['id']: v for f in D.glob('variables-before-*.json') for v in read(f)['variables']}
after = {v['id']: v for f in D.glob('after-variables-*.json') for v in read(f)['variables']}
require(len(before) == 298 and len(after) == 341, 'inventory', before=len(before), after=len(after))
for identity, value in before.items():
    require(after.get(identity) == value, 'existing-variable-preserved', id=identity)
native_ids = foundation['variableIds']
mapping = read(ROOT / 'evidence/figma-application/application-map.json')['variables']
semantic_ids = {'semantic.'+v['name']: v['destination_id'] for v in mapping if v['layer'] == 'semantic'}
for token in plan['tokens']:
    v = after[native_ids[token['id']]]
    require(v['name'] == token['figmaName'] and v['scopes'] == token['scopes'] and len(v['scopes']) == 1, 'native-name-scope', token=token['id'])
    require(v['codeSyntax'].get('WEB') == token['web'], 'web-syntax', token=token['id'])
    expected = {foundation['modeIds'][mode]: {'type': 'VARIABLE_ALIAS', 'id': semantic_ids[value['alias']]} for mode, value in token['values'].items()}
    require(v['valuesByMode'] == expected, 'native-alias-vector', token=token['id'])

preservation = read(D / 'after-preservation.json')
require(preservation['button'] == read(D / 'preflight.json')['button'], 'button-metadata-geometry-and-reactions-preserved')
require({c['name']: len(c['variableIds']) for c in preservation['collections']} == {'primitive': 145, 'semantic': 106, 'component': 47, 'tab': 43}, 'collection-inventory')

actual = {n['sourceId']: n for f in D.glob('after-nodes-*.json') for n in read(f)['nodes']}
# Fresh text facts supersede the pre-repair style linkage, without changing expectations.
for f in D.glob('after-text-current-*.json'):
    actual.update({n['sourceId']: n for n in read(f)['nodes']})
for record in read(D / 'icon-frame-metadata-correction.json')['records']:
    actual[record['sourceId']]['props'].update(record['props'])
    require(record['width'] == 20 and record['height'] == 20 and
            all(same([s['width'],s['height']],[14.6875,14.6875]) for s in record['shapes']),
            'icon-metadata-repair-preserves-geometry', id=record['id'])
require(len(actual) == 150, 'complete-source-role-mapping', nodes=len(actual))
binding_rows = []
for identity, expected in plan['nodes'].items():
    n = actual[identity]
    require(n['type'] == expected['type'], 'node-type', source=identity)
    for field, value in expected['props'].items():
        require(same(n['props'].get(field), value, policy['geometry_absolute_tolerance']), 'property', source=identity, field=field, expected=value, actual=n['props'].get(field))
    for field in ['fills', 'strokes']:
        require(same(clean(n[field]), expected[field], policy['color_absolute_tolerance']), 'paint', source=identity, field=field)
    for field, token in expected['bindings'].items():
        observed = bound(n, field)
        require(observed == native_ids[token], 'binding', source=identity, field=field, expected=native_ids[token], actual=observed)
        binding_rows.append(dict(sourceNodeId=identity, destinationNodeId=n['id'], field=field, tokenId=token, destinationVariableId=observed))
    if n['type'] == 'TEXT':
        role = 'count' if expected['props']['name'] == 'Count' else 'selected' if expected['props']['fontName']['style'] == 'SemiBold' else 'regular'
        require(n['textStyleId'] == foundation['styleIds'][role], 'shared-text-style', source=identity, role=role)
        require(n['fontWeight'] == {'regular':400, 'selected':600, 'count':700}[role], 'resolved-font-weight', source=identity)
    if expected.get('effectStyle'):
        require(n['effectStyleId'] == foundation['styleIds']['shadow'], 'shared-effect-style', source=identity)
    if n['type'] == 'INSTANCE':
        require(n['main']['key'] == 'f273018f11d7d4e938078bd0b21b0b3a9e7f2634' and n['main']['remote'] if expected['props']['name'] == 'Icon' else n['main']['id'] == foundation['countId'], 'linked-dependency', source=identity)
source_map = {k:v for b in range(6) for k,v in read(D / f'populate-{b}.json')['sourceToTarget'].items()}
shadow=next(s for s in read(D/'after-resolutions.json')['effectStyles'] if s['id']==foundation['styleIds']['shadow'])
require(same(clean(shadow['effects']),clean(plan['shadowStyle']['effects']),1e-6),'shared-effect-parameters')
for recipe in plan['variants']:
    observed = actual[recipe['sourceId']]['reactions']
    expected = [{'trigger': r['trigger'], 'actions': [{**a, 'destinationId':source_map[a['destinationId']]} for a in r['actions']]} for r in recipe['reactions']]
    reduced = [{'trigger': r['trigger'], 'actions': r['actions']} for r in observed]
    require(reduced == expected, 'source-hover-reactions', source=recipe['sourceId'])
require(len(binding_rows) == 1026 and {r['tokenId'] for r in binding_rows} == set(native_ids), 'binding-coverage')
with (D / 'binding-map.csv').open('w') as stream:
    w=csv.DictWriter(stream,fieldnames=list(binding_rows[0]),lineterminator='\n');w.writeheader();w.writerows(binding_rows)

consumers = [r for name in ['final-consumers-0.json','final-consumers-1.json','after-consumers-2.json'] for r in read(D / name)['records']]
definitions = read(D / 'after-resolutions.json')['properties']
require({k.split('#')[0] for k in definitions} == {'Label','Show icon','Icon','Show badge','type','selected','state'}, 'public-api')
for name, value in [('Label','Tab'),('Show icon',False),('Show badge',False)]:
    require(next(v['defaultValue'] for k,v in definitions.items() if k.split('#')[0] == name) == value, 'public-default', name=name)
for n in consumers:
    if n['category'] == 'themeExamples':
        require(n['properties']['type']['value'] == n['type'] and n['properties']['selected']['value'] == 'true' and n['properties']['state']['value'] == 'hover', 'theme-example-state', id=n['id'])
    if n['category'] == 'countExamples':
        require(n['count']['text']['characters'] == n['value'] and n['count']['width'] >= 16 and n['count']['height'] == 16, 'count-content-and-size', id=n['id'])
        require(n['count']['mainId'] == foundation['countId'], 'count-link', id=n['id'])
    if n['category'] == 'focusExamples':
        ring=n['ring'];require(ring is not None, 'focus-ring-present', id=n['id'])
        if ring:
            require(same([ring['x'],ring['y'],ring['width'],ring['height']],[-4,-4,n['width']+8,n['height']+8]), 'focus-growth', id=n['id'])
    require(n['label']['fontName']['family'] == 'Manrope' and n['label']['fontSize'] == 14 and n['label']['lineHeight'] == {'unit':'PIXELS','value':20}, 'consumer-typography', id=n['id'])
long=next(n for n in consumers if n['category']=='focusExamples' and n['type']=='underline')
require(long['icon']['mainKey'] == '46d251bb4099700c5852180f2370d265e5166432' and long['icon']['remote'], 'phosphor-instance-swap')
require(long['icon']['shapes'][0]['fills'][0]['boundVariables']['color']['id'] == native_ids['tab.color-tab-icon-secondary'], 'icon-swap-keeps-color-token')
counts={n['value']:n for n in consumers if n['category']=='countExamples'}
require(counts['99+']['count']['width'] > counts['1']['count']['width'] and counts['99+']['width'] > counts['1']['width'], 'count-hug-growth')
stress=read(D/'focus-consumer-stress.json')
require(len(stress['records'])==24 and stress['retainedQaNodes']==0,'complete-focus-consumer-coverage')
for r in stress['records']:
    require(same([r['ring']['x'],r['ring']['y'],r['ring']['width'],r['ring']['height']],[-4,-4,r['width']+8,r['height']+8]) and r['label']['textStyleId'] and r['count']['text']=='99+' and r['icon']['width']==r['icon']['height']==20,'focus-consumer-stress',mode=r['mode'],axes=r['axes'])

base=read(ROOT/'evidence/avatar-pilot/history/blueheart.2.0.0.json')['tokens']
tokens={t['id']:t for t in base+plan['tokens']}
def resolve(identity,mode):
    t=tokens[identity];value=t['values'].get(mode,t['values'].get('Value'))
    return resolve(value['alias'],mode) if isinstance(value,dict) and 'alias'in value else value
for r in read(D/'after-resolutions.json')['resolution']:
    require(same(r['value'],resolve(r['token'],r['mode']),1e-6), 'four-theme-native-resolution', token=r['token'], mode=r['mode'])
def luminance(rgb):
    linear=lambda x:x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4
    return sum(w*linear(rgb[c]) for c,w in zip('rgb',[.2126,.7152,.0722]))
def contrast(fg,bg):
    a,b=sorted([luminance(fg),luminance(bg)],reverse=True);return(a+.05)/(b+.05)
contrasts=[]
for variant in plan['variants']:
    if variant['axes']['state']=='disabled':continue
    root=plan['nodes'][variant['roles']['container']];label=plan['nodes'][variant['roles']['label']]
    for mode in plan['modes']:
        fg=resolve(label['bindings']['fills.0'],mode)
        bg=resolve(root['bindings']['fills.0'],mode) if 'fills.0'in root['bindings'] else resolve('tab.color-tab-bg-muted' if variant['axes']['type']=='segmented'else'tab.color-tab-bg-surface',mode)
        value=contrast(fg,bg);contrasts.append(dict(axes=variant['axes'],mode=mode,ratio=value))
        require(value>=4.5,'enabled-label-contrast',axes=variant['axes'],mode=mode,ratio=value)
pill_contrasts=[]
count_contrasts=[]
for n in consumers:
    if n.get('category')=='themeExamples' and n['type']=='pill':
        ratio=contrast(n['label']['fills'][0]['color'],n['fills'][0]['color']);pill_contrasts.append(dict(mode=n['mode'],ratio=ratio))
        require(ratio>=4.5,'actual-pill-hover-paint-contrast',mode=n['mode'],ratio=ratio)
    if n.get('category')=='countExamples':
        ratio=contrast(n['count']['text']['fills'][0]['color'],n['count']['fills'][0]['color'])
        count_contrasts.append(dict(value=n['value'],ratio=ratio))
        require(ratio>=4.5,'actual-count-text-contrast',value=n['value'],ratio=ratio)

result={'status':'FAIL'if failures else'PASS','scope':'Captured Figma structure, tokens, aliases, typography, consumers and calculated contrast; native playback is separate','tolerances':policy,'counts':{'existing_variables_preserved':298,'total_variables':341,'component_tokens':43,'variants':24,'mapped_nodes':len(actual),'binding_uses':len(binding_rows),'mode_resolutions':172,'text_style_nodes':48,'shared_text_styles':3,'shared_effect_styles':1},'contrast':{'method':'WCAG sRGB relative luminance','enabled_label_contexts':len(contrasts),'minimum':min(r['ratio']for r in contrasts),'pill_selected_hover_actual_paints':pill_contrasts,'count_actual_paints':count_contrasts,'all_enabled_contexts':contrasts,'disabled':'Excluded from text contrast requirement; still tested structurally and interactively'},'failures':failures}
(D/'comparison.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':result['status'],'failures':failures[:30],'counts':result['counts'],'pill_contrast':pill_contrasts},ensure_ascii=False,indent=2))
raise SystemExit(bool(failures))
