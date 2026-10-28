"""Deterministic read-only evidence projections; these are not operative rules."""
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / 'evidence/tab-pilot/source'


def load(name):
    return json.loads((DIR / name).read_text())


def generate():
    nodes = load('nodes.json'); index = load('inventory.json'); source = load('variables.json'); dependency = load('dependencies.json')
    variables = {v['id']: v for v in source['variables']}; collections = {c['id']: c for c in source['collections']}
    by = {n['id']: n for n in nodes}; root = by[index['identity']['id']]
    evidence = {'figma_direct': [], 'derived': [], 'requires_definition': []}

    def ev(path, value, layer='figma_direct', note=None):
        identity = 'E%03d' % (sum(len(v) for v in evidence.values()) + 1)
        evidence[layer].append({'id': identity, 'source': path, 'value': value, 'note': note})
        return identity

    refs = {n['id']: ev('node:' + n['id'], {'id': n['id'], 'name': n['name'], 'type': n['type']},
                       note='Complete property record: nodes.json#/' + str(i)) for i, n in enumerate(nodes)}
    desc_ref = ev('node:' + root['id'] + '.description', root['description'])
    used = defaultdict(list)

    def aliases(value, path):
        if isinstance(value, dict):
            if value.get('type') == 'VARIABLE_ALIAS': used[value['id']].append(path)
            for key, item in value.items(): aliases(item, path + '.' + key)
        elif isinstance(value, list):
            for i, item in enumerate(value): aliases(item, path + '[' + str(i) + ']')

    for n in nodes:
        for field in ['boundVariables', 'fills', 'strokes', 'effects']:
            aliases(n.get(field), 'node:' + n['id'] + '.' + field)
    for v in variables.values(): aliases(v['valuesByMode'], 'variable:' + v['id'] + '.valuesByMode')

    def variable_ref(n, field):
        raw = n.get('boundVariables', {}).get(field)
        if isinstance(raw, list): raw = raw[0] if raw else None
        return variables.get(raw['id']) if isinstance(raw, dict) and raw.get('type') == 'VARIABLE_ALIAS' else None

    def prop(n, field, unit=None, value=None):
        p = {'resolved_value': n.get(field) if value is None else value, 'unit': unit,
             'availability': 'OBSERVED' if field in n or value is not None else 'UNKNOWN', 'evidence_refs': [refs[n['id']]]}
        v = variable_ref(n, field)
        if v: p = {'token': {k: v[k] for k in ['id', 'key', 'name']}, **p}
        return p

    def layout(n):
        b = n.get('absoluteBoundingBox') or {}
        return {'node': {k: n[k] for k in ['id', 'name', 'type']},
                'position': {'x': n['x'], 'y': n['y'], 'absolute_x': b.get('x'), 'absolute_y': b.get('y'), 'unit': 'px'},
                'layout_mode': n.get('layoutMode'), 'layout_wrap': n.get('layoutWrap'), 'layout_positioning': n.get('layoutPositioning'),
                'sizing': {'horizontal': n.get('layoutSizingHorizontal'), 'vertical': n.get('layoutSizingVertical'),
                           'primary_axis_mode': n.get('primaryAxisSizingMode'), 'counter_axis_mode': n.get('counterAxisSizingMode')},
                'dimensions': {'width': prop(n, 'width', 'px'), 'height': prop(n, 'height', 'px'),
                               'min_width': n.get('minWidth'), 'max_width': n.get('maxWidth'), 'min_height': n.get('minHeight'), 'max_height': n.get('maxHeight')},
                'spacing': {'gap': prop(n, 'itemSpacing', 'px') if 'itemSpacing' in n else None,
                            'row_gap': n.get('counterAxisSpacing'), 'column_gap': None},
                'padding': {k: prop(n, f, 'px') if f in n else None for k, f in [('top', 'paddingTop'), ('right', 'paddingRight'), ('bottom', 'paddingBottom'), ('left', 'paddingLeft')]},
                'alignment': {'primary_axis': n.get('primaryAxisAlignItems'), 'counter_axis': n.get('counterAxisAlignItems'), 'self': n.get('layoutAlign')},
                'constraints': n.get('constraints'), 'overflow': None, 'clips_content': n.get('clipsContent'),
                'strokes_included_in_layout': n.get('strokesIncludedInLayout'), 'grow': n.get('layoutGrow'), 'grids': n.get('layoutGrids', []), 'evidence_refs': [refs[n['id']]]}

    def scalar(value, unit=None, evidence_refs=None):
        return {'resolved_value': value, 'unit': unit, 'availability': 'OBSERVED', 'evidence_refs': evidence_refs or []}

    def paint(p, n):
        color = scalar(p.get('color'), 'color', [refs[n['id']]]) if 'color' in p else None
        ref = p.get('boundVariables', {}).get('color')
        if color is not None and ref:
            v = variables[ref['id']]; color = {'token': {k: v[k] for k in ['id','key','name']}, **color}
        return {**{k: scalar(p.get(k), 'ratio' if k=='opacity' else None, [refs[n['id']]]) for k in ['type','visible','opacity','blendMode']},
                'color': color, 'gradient_stops': [], 'image_ref': p.get('imageHash'), 'scale_mode': p.get('scaleMode'), 'transform': p.get('imageTransform'), 'availability': 'OBSERVED', 'evidence_refs': [refs[n['id']]]}

    def effect(e, n):
        return {'type': scalar(e['type']), 'visible': scalar(e.get('visible')), 'radius': scalar(e.get('radius'), 'px'),
                'spread': scalar(e.get('spread'), 'px'), 'offset': {**e.get('offset', {'x':None,'y':None}), 'unit':'px'},
                'color': scalar(e.get('color'), 'color'), 'blend_mode': scalar(e.get('blendMode')), 'bound_variables': e.get('boundVariables', {}),
                'availability':'OBSERVED', 'evidence_refs':[refs[n['id']]]}

    def visual(n):
        effects = [effect(e, n) for e in n.get('effects', [])]
        return {'node': {k: n[k] for k in ['id', 'name', 'type']}, 'fills': [paint(p,n) for p in n.get('fills', [])], 'backgrounds': [paint(p,n) for p in n.get('backgrounds', [])], 'strokes': [paint(p,n) for p in n.get('strokes', [])],
                'stroke_width': prop(n, 'strokeWeight', 'px'),
                'stroke_widths': {k: prop(n, f, 'px') if f in n else None for k, f in [('top','strokeTopWeight'),('right','strokeRightWeight'),('bottom','strokeBottomWeight'),('left','strokeLeftWeight')]},
                'stroke_alignment': prop(n, 'strokeAlign'), 'dash_pattern': prop(n, 'dashPattern', 'px'), 'corner_radius': prop(n, 'cornerRadius', 'px'),
                'corner_radii': {k: prop(n, f, 'px') if f in n else None for k, f in [('top_left','topLeftRadius'),('top_right','topRightRadius'),('bottom_right','bottomRightRadius'),('bottom_left','bottomLeftRadius')]},
                'opacity': prop(n, 'opacity', 'ratio'), 'blend_mode': prop(n, 'blendMode'), 'effects': effects,
                'shadows': [e for e in effects if e['type']['resolved_value'] in ['DROP_SHADOW','INNER_SHADOW']], 'blur': [],
                'clips_content': prop(n, 'clipsContent'), 'is_mask': prop(n, 'isMask'), 'mask_type': prop(n, 'maskType'), 'evidence_refs': [refs[n['id']]]}

    dependencies = []
    for definition in dependency['definitions']:
        main, owner = definition['main'], definition['owner']; matching = [i for i in index['instances'] if i['main']['key'] == main['key']]
        locality = 'REMOTE' if main['remote'] else 'LOCAL'; e = ev('instance:' + definition['activeInstanceId'] + '.mainComponent', definition)
        dependencies.append({'dependency_id': main['key'], 'kind': 'COMPONENT', 'instance_ids': [i['id'] for i in matching], 'instance_count': len(matching),
                             'main_component': {k: main[k] for k in ['id','key','name']}, 'component_set': {k: owner[k] for k in ['id','key','name']},
                             'locality': locality, 'active_properties': [{'instance_id': i['id'], 'properties': by[i['id']]['componentProperties']} for i in matching],
                             'property_definitions': [{'key':k,**v} for k,v in owner['propertyDefinitions'].items()], 'variants': {'observed': [main['name']], 'available': [{'key':k,**v} for k,v in owner['propertyDefinitions'].items() if v['type']=='VARIANT'], 'unknown': []},
                             'swaps': {'active': [], 'preferred_values': [], 'preferred_candidate_count': 0, 'alternatives_deeply_resolved': False}, 'slots': [],
                             'overrides': [{'instance_id': i['id'], 'fields': by[i['id']].get('overrides', [])} for i in matching],
                             'resolution': {'status': 'RESOLVED', 'evidence': [e], 'missing_fields': [], 'reason': None},
                             'contract_ref': {'status': 'NOT_GENERATED', 'suggested_path': 'dependencies/' + owner['name'].lower() + '/component-contract.md'}})

    variable_dependencies = []
    for v in sorted(variables.values(), key=lambda x: (x['name'].lower(), x['id'])):
        assert used[v['id']], v['id']
        c = collections[v['collectionId']]; e = ev('variable:' + v['id'], v)
        variable_dependencies.append({'id': v['id'], 'key': v['key'], 'name': v['name'], 'type': v['type'],
                                     'collection': {k: c[k] for k in ['id','key','name']}, 'locality': 'REMOTE' if v['remote'] else 'LOCAL',
                                     'resolved_value': v['resolved']['value'], 'resolved_mode': {'id': root['resolvedVariableModes'][c['id']], 'name': next(m['name'] for m in c['modes'] if m['modeId']==root['resolvedVariableModes'][c['id']])},
                                     'used_by': sorted(set(used[v['id']])), 'resolution': {'status': 'RESOLVED', 'evidence': [e], 'missing_fields': [], 'reason': None}, 'evidence_refs': [e]})
    styles = []
    for s in dependency['styles']:
        uses = ['node:' + n['id'] + '.effectStyleId' for n in nodes if n.get('effectStyleId') == s['id']]
        e = ev('style:' + s['id'], s)
        styles.append({'id': s['id'], 'key': s['key'], 'name': s['name'], 'type': s['type'], 'locality': 'REMOTE' if s['remote'] else 'LOCAL', 'used_by': uses,
                       'resolution': {'status': 'RESOLVED', 'evidence': [e], 'missing_fields': [], 'reason': None}, 'evidence_refs': [e]})

    def totals(items, component=False):
        result = {'total': len(items), 'local': sum(i['locality']=='LOCAL' for i in items), 'remote': sum(i['locality']=='REMOTE' for i in items), 'unknown_locality': 0,
                  'resolved': len(items), 'partially_resolved': 0, 'unresolved': 0}
        if component: result = {'total_instances': sum(i['instance_count'] for i in items), **result}
        return result

    variants = [by[i] for i in index['variantIds']]; texts = [n for n in nodes if n['type']=='TEXT']; typography = []
    for n in texts:
        typography.append({'node': {'id': n['id'], 'name': n['name']}, 'characters': n['characters'], 'range': {'start': 0, 'end': len(n['characters'])},
                           'font_family': prop(n, 'fontFamily', value=n['fontName']['family']), 'font_style': prop(n, 'fontStyle', value=n['fontName']['style']),
                           'font_weight': prop(n, 'fontWeight'), 'font_size': prop(n, 'fontSize', 'px'), 'line_height': prop(n, 'lineHeight'),
                           'letter_spacing': prop(n, 'letterSpacing'), 'paragraph_spacing': n.get('paragraphSpacing'), 'paragraph_indent': n.get('paragraphIndent'),
                           'text_align_horizontal': n['textAlignHorizontal'], 'text_align_vertical': n['textAlignVertical'], 'text_case': n['textCase'], 'text_decoration': n['textDecoration'],
                           'text_style': {'id': n.get('textStyleId') or None, 'key': None, 'name': None, 'locality': 'UNKNOWN'},
                           'auto_resize': n['textAutoResize'], 'truncation': n['textTruncation'], 'max_lines': n['maxLines'], 'bound_variables': n['boundVariables'],
                           'mixed_fields': [], 'styled_segments': [], 'hyperlinks': [], 'evidence_refs': [refs[n['id']]]})
    interactions = [{'source_id': n['id'], 'reaction': r, 'evidence_refs': [refs[n['id']]]} for n in variants for r in n.get('reactions', [])]
    categories = defaultdict(list)
    tokens = []
    for v in variable_dependencies:
        category = 'Color' if v['type']=='COLOR' else 'Typography' if v['name'].startswith('font/') else 'Spacing' if v['name'].startswith('spacing/') else 'Radius' if v['name'].startswith('radius/') else 'Size' if v['name'].startswith('size/') else 'Border' if v['name'].startswith('stroke/') else 'Other'
        token = {'name': v['name'], 'id': v['id'], 'key': v['key'], 'type': v['type'], 'category': category,
                                                          'collection': v['collection'], 'remote': v['locality']=='REMOTE', 'resolved_value': v['resolved_value'],
                                                          'resolved_mode': v['resolved_mode'], 'used_by': v['used_by'], 'evidence_refs': v['evidence_refs']}
        categories[category].append(token); tokens.append(token)
    ext = []
    for d in dependencies:
        if d['locality'] != 'REMOTE': continue
        ext.append({'kind': 'COMPONENT', **d['main_component'], 'remote': True, 'collection': None, 'component_set': d['component_set'],
                    **{k: 'NOT_EXPOSED_BY_FIGMA_MCP' for k in ['library_name','source_file','source_url','project','organization','library_version']}, 'resolution': d['resolution']})
    model = {'schema_version': '0.1.0', 'generated_at': json.loads((DIR.parent/'state.json').read_text())['generated_at'],
             'generator': {'skill': 'figma-component-contract', 'skill_version': '0.1.0', 'serialization': 'JSON subset of YAML 1.2, consistent with the Button evidence format'},
             'inspection': {'status': 'COMPLETE', 'read_only': True, 'traversal': {'discovered_nodes': 151, 'inspected_nodes': 151, 'pending_nodes': 0, 'invisible_nodes_inspected': 48, 'truncated': False, 'limit': None},
                            'mcp_limitations': ['Direct ID getter missed one hidden Count text; explicit traversal through parent 9058:307 recovered it completely.', 'No executable web accessibility or group controller is exposed by this design node.']},
             'component': {'id': root['id'], 'key': root['key'], 'name': root['name'], 'type': root['type'], 'description': root['description'], 'parent': index['identity']['parent'], 'page': index['identity']['page'],
                           'source': {'url': 'https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=1183-1146', 'file_key': '9zs5RMR8LB5wHjW9Bd59BA', 'node_id': root['id']}},
             'classification': {'kind': 'component', 'reusable': True, 'composition': False, 'evidence_refs': [refs[root['id']]]},
             'identity': {'position': {'x': root['x'], 'y': root['y']}, 'dimensions': {'width': root['width'], 'height': root['height']}, 'visible': root['visible'], 'clips_content': root['clipsContent'], 'opacity': root['opacity'], 'blend_mode': root['blendMode']},
             'direct_children': [{'id': n['id'], 'name': n['name'], 'type': n['type'], 'sibling_index': i, 'dimensions': {'width': n['width'], 'height': n['height']}, 'evidence_refs': [refs[n['id']]]} for i, n in enumerate(variants)],
             'anatomy': {'functional_tree': [{'id': n['id'], 'parent_id': n['parentId'], 'name': n['name'], 'type': n['type'], 'visible': n['visible'], 'children': n['childIds'], 'evidence_refs': [refs[n['id']]]} for n in nodes if n['type']!='VECTOR'],
                         'graphical_details_omitted': [{'id': n['id'], 'parent_id': n['parentId'], 'reason': 'Linked Phosphor geometry, not a standalone component; paint references retained in nodes.json.', 'evidence_refs': [refs[n['id']]]} for n in nodes if n['type']=='VECTOR']},
             'dependency_inventory': {'components': totals(dependencies, True), 'variables': totals(variable_dependencies), 'styles': totals(styles)},
             'dependencies': dependencies, 'variable_dependencies': variable_dependencies, 'style_dependencies': styles,
             'properties': {'definitions': [{'key':k,**v} for k,v in root['componentPropertyDefinitions'].items()], 'observed': [n['variantProperties'] for n in variants], 'available': [{'key':k,**v} for k,v in root['componentPropertyDefinitions'].items()], 'unknown': []},
             'variants': {'observed_combinations': [{'source_id': n['id'], **n['variantProperties']} for n in variants], 'available_values': [{'property':k,'values':v['variantOptions']} for k, v in root['componentPropertyDefinitions'].items() if v['type']=='VARIANT'], 'unknown': []},
             'states': {'observed': ['default','hover','focus','disabled'], 'available': ['default','hover','focus','disabled'], 'unknown': []},
             'layout': {'node': layout(root), 'children': [layout(n) for n in variants], 'relationships': [{'parent_id': root['id'], 'child_id': n['id'], 'relationship': 'OBSERVED_VARIANT', 'parent_layout_mode': root['layoutMode'], 'child_layout_positioning': n['layoutPositioning'], 'child_sizing': {'horizontal': n['layoutSizingHorizontal'], 'vertical': n['layoutSizingVertical']}, 'evidence_refs': [refs[n['id']]]} for n in variants]},
             'visual': {'node': visual(root), 'descendants': [visual(n) for n in nodes if n['type'] in ['COMPONENT','FRAME']], 'icons': [{'node': {'id': n['id'], 'name': n['name'], 'type': n['type']}, 'dimensions': {'width': n['width'], 'height': n['height'], 'unit': 'px'}, 'format': 'Outline', 'weight': 'Light', 'vector_descendant_count': 1, 'fills': n['fills'], 'strokes': n['strokes'], 'evidence_refs': [refs[n['id']]]} for n in nodes if n['type']=='INSTANCE' and n['name']=='Icon']},
             'typography': {'styles': [], 'text_runs': typography}, 'tokens': {'summary': {'total': len(tokens), 'local': sum(not v['remote'] for v in tokens), 'remote': sum(v['remote'] for v in tokens)}, 'categories': dict(categories), 'source': 'variable_dependencies'},
             'content': {'example_content': {'observed_strings': sorted({n['characters'] for n in texts})}, 'component_rules': [{'source': 'componentPropertyDefinitions', 'value': root['componentPropertyDefinitions']}], 'truncation_and_wrapping': [{'source_id': n['id'], 'auto_resize': n['textAutoResize'], 'truncation': n['textTruncation'], 'max_lines': n['maxLines']} for n in texts]},
             'interactions': {'status': 'FIGMA_DEFINED', 'reason': 'Four observed ON_HOVER / CHANGE_TO reactions; click selection, tablist controller and executable keyboard behavior are not authored on this individual node.', 'rules': interactions},
             'semantic_contract': {'explicit_descriptions': [{'source_id': root['id'], 'description': root['description'], 'evidence_refs': [desc_ref]}], 'purpose': {'status': 'DEFINED', 'evidence_refs': [desc_ref]}, 'usage_rules': {'status': 'DEFINED', 'evidence_refs': [desc_ref]}},
             'accessibility': {'status': 'REQUIRES_DEFINITION', 'observed': [{'value': 'Description declares role=tab, aria-selected, tablist and arrow navigation; visual focus and selected states exist.', 'evidence_refs': [desc_ref]}], 'undefined': ['Executable DOM/ARIA and keyboard management', 'Consumer panel IDs, activation policy and product-specific accessible names', 'Whole-flow accessibility certification']},
             'external_dependencies': ext,
             'unresolved': [{'id': 'U-SEGMENTED', 'category': 'SOURCE_CONFLICT', 'subject': 'segmented selected', 'reason': 'Description says white; source default/hover use accent purple with white text.', 'missing_fields': [], 'evidence_refs': [desc_ref, refs['9058:244'], refs['9058:249']], 'impact': 'Resolved for Blue Heart DS through explicit user decision ADR-015; original evidence remains unchanged.'},
                            {'id': 'U-CONTRAST', 'category': 'SOURCE_QUALITY', 'subject': 'pill selected hover', 'reason': 'Original text falls below 4.5:1 in three themes on its accent background.', 'missing_fields': [], 'evidence_refs': [refs['1334:8380']], 'impact': 'User adopted the existing stronger brand vector for text; applies only in the operative destination contract.'}],
             'implementation_notes': ['Read-only source evidence, not operative Blue Heart DS rules.', 'No production code, imported original components, SVG copies or source mutations.', 'The native Tab contract is separate from the tablist/container and its product-specific panels.'],
             'evidence': {**evidence, 'confidence': {'level': 'HIGH', 'reason': 'Full 151-node traversal, hidden nodes included; 97 used/alias variables, two active component definitions and one named style resolved.'}}}
    assert model['dependency_inventory']['components']['total_instances'] == 48
    assert model['tokens']['summary']['total'] == len(model['variable_dependencies']) == 97
    assert len(model['variants']['observed_combinations']) == 24
    (DIR/'component-contract.yaml').write_text(json.dumps(model, ensure_ascii=False, indent=2)+'\n')
    md = ['# Tab — contrato de inspección del origen', '', '**Evidencia Figma de solo lectura.** No gobierna la implementación de Blue Heart DS; el contrato operativo es `norms/components/tab.1.0.0.md`.', '',
          'Fuente: '+model['component']['source']['url'], 'Inspección: COMPLETE; '+model['generated_at']+'; 151/151 nodos, 48 invisibles, 0 pendientes.', '']
    sections = [
        ('Component Identity', f"**Observed from Figma:** `{root['name']}` / `{root['type']}` / `{root['id']}`. Página `{index['identity']['page']['name']}`. Es una Tab individual reusable, no un Button ni el contenedor de Tabs."),
        ('Anatomy', '**Derived structure:** set → 24 variantes → Icon (oculto), Label, Badge Count (oculto), Focus ring (solo focus). Los 24 vectores se conservan como geometría referenciada de Phosphor, sin copias vectoriales.'),
        ('Dependencies', '**Observed from Figma:** 48 instancias; 2 componentes únicos resueltos (ImageSquare remoto y Count medium local al origen); 97 variables usadas directa o transitivamente, todas resueltas; 1 estilo de efecto nombrado resuelto. El contador expuesto conserva Count y Max count del origen; solo Count está conectado al tipo activo.'),
        ('Properties', '\n'.join(['| Propiedad | Tipo | Predeterminado |','|---|---|---|']+[f"| {k} | {v['type']} | `{v['defaultValue']}` |" for k,v in root['componentPropertyDefinitions'].items()])),
        ('Variants', '\n'.join(['**Observed from Figma:** 24 combinaciones; no eje size.', '', '| ID | Combinación | Dimensiones observadas |','|---|---|---|']+[f"| {n['id']} | {n['name']} | {n['width']} × {n['height']} |" for n in variants])),
        ('States', '**Observed from Figma:** default, hover, focus y disabled; selected=true/false es un eje independiente.'),
        ('Layout', '**Observed from Figma:** Auto Layout horizontal y ancho HUG. Alturas de ejemplo 44/36/28 px para underline/pill/segmented; padding vertical 12/8/4, horizontal 16/16/12 y gap 8. Icono 20 px; contador con mínimo 16 px. Focus ring con offset −4 y constraints STRETCH. La geometría completa está en `nodes.json` y en la proyección estructurada.'),
        ('Visual Styles', '**Observed from Figma:** indicador inferior de 2 px en los estados definidos de underline; superficies de pill y segmented; anillo de foco de 2 px. Tres selected segmented activos usan elevation/shadow/sm. **Requires definition / source conflict:** el blanco descrito y los morados observados no coinciden; ADR-015 define la adaptación, sin alterar este snapshot.'),
        ('Typography', '**Observed from Figma:** Manrope Regular 14/20 en no seleccionado; SemiBold 14/20 en seleccionado; Count Bold 10/16. Variables de estilo usan los strings originales; Figma expone los nombres de fuente resueltos. No hay estilos de texto nombrados en el origen inspeccionado.'),
        ('Tokens', '**Observed from Figma:** 47 variables referenciadas directamente y 50 adicionales en el cierre de aliases; inventario total 97. El YAML conserva IDs, nombres, claves, colecciones, modos, valores y used_by. No son los tokens normalizados de Blue Heart DS.'),
        ('Content', '**Observed from Figma:** textos de ejemplo “Tab” y “1”; Label editable. La descripción recomienda etiquetas cortas de 1–2 palabras. El texto de ejemplo no es una regla de negocio.'),
        ('Interactions', '**Observed from Figma:** cuatro ON_HOVER/CHANGE_TO: underline y pill, con selected=false y true, default→hover. No se observan acciones de selección por click, gestión de grupo o paneles en este nodo. Los estados restantes existen como variantes seleccionables.'),
        ('Accessibility', '**Observed from Figma:** descripción con role=tab, aria-selected, tablist y flechas; anillo visible. **Requires definition:** DOM/ARIA ejecutable, activación del grupo, paneles y nombres accesibles del contexto. No se acredita conformidad WCAG.'),
        ('External Dependencies', '**Observed from Figma:** ImageSquare Outline Light remoto, key `f273018f11d7d4e938078bd0b21b0b3a9e7f2634`. La coincidencia con la biblioteca del equipo fue verificada separadamente en `phosphor.json`. Campos remotos no expuestos permanecen NOT_EXPOSED_BY_FIGMA_MCP.'),
        ('Unresolved Information', 'Se conserva la contradicción visual de segmented y el contraste original de pill hover como hechos del origen; ambos tienen resolución autorizada en el destino. Un hijo invisible requirió lectura por su padre y quedó recuperado. No hay nodos ni dependencias pendientes de inspección.'),
        ('Implementation Notes', 'Este par MD/YAML describe evidencia original, no crea componentes, código de aplicación o reglas productivas. El modelo estructurado usa el subconjunto JSON de YAML 1.2, como el snapshot anterior de Button. Las definiciones hijas son referencias, sin importar la familia Dot completa.'),
        ('Evidence / Confidence', '**HIGH por cobertura**, no por certificación funcional: `inventory.json`, `nodes.json`, `variables.json`, `dependencies.json`, `phosphor.json` y `overview.png`. MD y YAML proceden del mismo modelo. Cada nodo y variable tiene selector y referencia de evidencia.')]
    for title, text in sections: md += ['## '+title, '', text, '']
    (DIR/'component-contract.md').write_text('\n'.join(md))
    return model


if __name__ == '__main__':
    m = generate()
    print(json.dumps({'status': 'PASS_SOURCE_PROJECTIONS', 'nodes': m['inspection']['traversal'], 'dependencies': m['dependency_inventory']}, ensure_ascii=False))
