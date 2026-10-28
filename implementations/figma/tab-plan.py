"""Derive Tab recipes and minimum scoped tokens from immutable Figma evidence."""
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODES = ['Contable', 'Administrativo', 'Servicios', 'Personas']
SCOPE = dict.fromkeys(['width', 'height', 'minWidth', 'minHeight'], 'WIDTH_HEIGHT')
SCOPE.update(dict.fromkeys(['itemSpacing', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft'], 'GAP'))
SCOPE.update(dict.fromkeys(['topLeftRadius', 'topRightRadius', 'bottomLeftRadius', 'bottomRightRadius'], 'CORNER_RADIUS'))
SCOPE.update(dict.fromkeys(['strokeTopWeight', 'strokeRightWeight', 'strokeBottomWeight', 'strokeLeftWeight'], 'STROKE_FLOAT'))
SCOPE.update(fontFamily='FONT_FAMILY', fontStyle='FONT_STYLE', fontSize='FONT_SIZE', lineHeight='LINE_HEIGHT', letterSpacing='LETTER_SPACING')
PREFIX = {'WIDTH_HEIGHT': 'size-', 'GAP': 'spacing-', 'CORNER_RADIUS': 'radius-', 'STROKE_FLOAT': 'stroke-',
          'FONT_FAMILY': 'font-family-', 'FONT_STYLE': 'font-weight-', 'FONT_SIZE': 'font-size-',
          'LINE_HEIGHT': 'font-line-height-', 'LETTER_SPACING': 'font-letter-spacing-'}
FIELDS = ['name', 'width', 'height', 'visible', 'clipsContent', 'opacity', 'blendMode', 'layoutMode',
          'layoutSizingHorizontal', 'layoutSizingVertical', 'primaryAxisSizingMode', 'counterAxisSizingMode',
          'primaryAxisAlignItems', 'counterAxisAlignItems', 'itemSpacing', 'paddingTop', 'paddingRight',
          'paddingBottom', 'paddingLeft', 'minWidth', 'minHeight', 'strokesIncludedInLayout', 'strokeAlign',
          'strokeTopWeight', 'strokeRightWeight', 'strokeBottomWeight', 'strokeLeftWeight',
          'topLeftRadius', 'topRightRadius', 'bottomLeftRadius', 'bottomRightRadius',
          'fontName', 'fontSize', 'lineHeight', 'letterSpacing', 'textAlignHorizontal', 'textAlignVertical',
          'textAutoResize', 'textTruncation', 'maxLines', 'textCase', 'textDecoration', 'characters']


def read(path):
    return json.loads((ROOT / path).read_text())


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def close(a, b):
    if isinstance(a, dict) and isinstance(b, dict):
        return set(a) == set(b) and all(close(a[k], b[k]) for k in a)
    if type(a) in (int, float) and type(b) in (int, float):
        return abs(a - b) <= 1e-6
    return a == b


def prepare():
    raw = read('evidence/tab-pilot/source/nodes.json')
    original = {n['id']: n for n in raw}
    nodes = copy.deepcopy(original)
    inventory = read('evidence/tab-pilot/source/inventory.json')
    source = read('evidence/tab-pilot/source/variables.json')
    variables = {v['id']: v for v in source['variables']}
    collections = {c['id']: c for c in source['collections']}
    base = read('evidence/avatar-pilot/history/blueheart.2.0.0.json')
    base_by = {t['id']: t for t in base['tokens']}
    semantics = [t for t in base['tokens'] if t['layer'] == 'semantic']

    def resolve_base(token):
        value = token['values']['Value']
        return resolve_base(base_by[value['alias']]) if isinstance(value, dict) and 'alias' in value else value

    def resolve_source(identity, mode, active=()):
        if identity in active:
            raise ValueError('Source alias cycle')
        v = variables[identity]
        collection = collections[v['collectionId']]
        mode_id = next((m['modeId'] for m in collection['modes'] if m['name'] == mode), collection['defaultModeId'])
        value = v['valuesByMode'][mode_id]
        if isinstance(value, dict) and value.get('type') == 'VARIABLE_ALIAS':
            return resolve_source(value['id'], mode, active + (identity,))
        return value

    def source_terminal(identity, mode, active=()):
        if identity in active:
            raise ValueError('Source alias cycle')
        v = variables[identity]
        collection = collections[v['collectionId']]
        mode_id = next((m['modeId'] for m in collection['modes'] if m['name'] == mode), collection['defaultModeId'])
        value = v['valuesByMode'][mode_id]
        return source_terminal(value['id'], mode, active + (identity,)) if isinstance(value, dict) and value.get('type') == 'VARIABLE_ALIAS' else identity

    def semantic(identity, scope, mode):
        v = variables[identity]
        kind = {'COLOR': 'color', 'FLOAT': 'number', 'STRING': 'string', 'BOOLEAN': 'boolean'}[v['type']]
        candidates = [t for t in semantics if t['type'] == kind and
                      (kind == 'color' or t['id'].startswith('semantic.' + PREFIX[scope])) and
                      base_by[t['values']['Value']['alias']]['source']['original_id'] == source_terminal(identity, mode) and
                      close(resolve_base(t), resolve_source(identity, mode))]
        if len(candidates) != 1:
            raise ValueError(f'Ambiguous/missing semantic for {v["name"]}, {scope}, {mode}: {[t["id"] for t in candidates]}')
        return candidates[0]['id']

    def child(variant, name):
        return next(nodes[i] for i in variant['childIds'] if nodes[i]['name'] == name)

    normalized = []
    focus = next(nodes[i] for i in inventory['variantIds'] if nodes[i]['variantProperties'] ==
                 {'type': 'segmented', 'selected': 'true', 'state': 'focus'})
    for identity in inventory['variantIds']:
        variant = nodes[identity]
        axes = variant['variantProperties']
        if axes['type'] == 'segmented' and axes['selected'] == 'true' and axes['state'] in ['default', 'hover']:
            pairs = [(variant, focus), (child(variant, 'Label'), child(focus, 'Label'))]
            icon, focus_icon = child(variant, 'Icon'), child(focus, 'Icon')
            pairs.append((nodes[icon['childIds'][0]], nodes[focus_icon['childIds'][0]]))
            for target, exemplar in pairs:
                before = copy.deepcopy(target['fills'])
                target['fills'] = copy.deepcopy(exemplar['fills'])
                target['boundVariables']['fills'] = copy.deepcopy(exemplar['boundVariables']['fills'])
                normalized.append({'sourceId': target['id'], 'field': 'fills', 'before': before,
                                   'after': target['fills'], 'exemplarSourceId': exemplar['id'], 'authority': 'ADR-015'})

    # Explicit user decision: selected pill hover uses the existing stronger brand
    # vector for text. This is one scoped token, never one token per theme/state.
    hover_source = next(v for v in source['variables'] if v['name'] == 'color/interactive/primary/hover')
    pill = next(nodes[i] for i in inventory['variantIds'] if nodes[i]['variantProperties'] ==
                {'type': 'pill', 'selected': 'true', 'state': 'hover'})
    label = child(pill, 'Label')
    before = copy.deepcopy(label['fills'])
    reference = {'type': 'VARIABLE_ALIAS', 'id': hover_source['id']}
    label['fills'][0]['boundVariables']['color'] = reference
    label['fills'][0]['color'] = {c: hover_source['resolved']['value'][c] for c in ['r', 'g', 'b']}
    label['boundVariables']['fills'] = [reference]
    normalized.append({'sourceId': label['id'], 'field': 'fills', 'before': before,
                       'after': label['fills'], 'exemplarSourceVariableId': hover_source['id'], 'authority': 'ADR-015'})

    groups, uses = {}, []

    def token_name(scope, source_id, value):
        name = variables[source_id]['name']
        if scope in ['FRAME_FILL', 'TEXT_FILL', 'SHAPE_FILL', 'STROKE_COLOR']:
            element = {'FRAME_FILL': 'bg', 'TEXT_FILL': 'text', 'SHAPE_FILL': 'icon', 'STROKE_COLOR': 'stroke'}[scope]
            if scope == 'FRAME_FILL':
                role = {'color/background/default': 'surface', 'color/background/subtle': 'subtle',
                        'color/interactive/disabled/bg': 'subtle', 'color/background/muted': 'muted',
                        'color/surface/brand': 'brand-subtle', 'color/surface/brand/accent': 'brand-accent',
                        'color/feedback/danger/icon': 'count'}[name]
            elif scope == 'STROKE_COLOR':
                role = {'color/border/default': 'neutral', 'color/border/control-disabled': 'neutral',
                        'color/border/surface': 'surface', 'color/focus/ring': 'focus',
                        'color/interactive/primary/default': 'brand', 'color/interactive/primary/hover': 'brand-hover'}[name]
            else:
                role = 'brand-hover' if name == 'color/interactive/primary/hover' else 'inverse' if name.endswith('/on-brand') else name.rsplit('/', 1)[-1]
            return f'tab/color/{element}/{role}'
        if scope == 'GAP':
            return 'tab/spacing/' + {0: 'none', 4: 'xs', 8: 'sm', 12: 'md', 16: 'lg'}[value]
        if scope == 'WIDTH_HEIGHT':
            return 'tab/size/' + {16: 'count', 20: 'icon'}[value]
        if scope == 'CORNER_RADIUS':
            return 'tab/radius/' + {4: 'sm', 8: 'md', 12: 'lg', 9999: 'full'}[value]
        if scope == 'STROKE_FLOAT':
            return 'tab/border/width-' + {1: 'regular', 2: 'emphasis'}[value]
        suffix = {'FONT_FAMILY': 'family', 'FONT_STYLE': {'Regular': 'label-style', 'Semibold': 'selected-style', 'bold': 'count-style'}.get(value),
                  'FONT_SIZE': {10: 'size-count', 14: 'size-label'}.get(value),
                  'LINE_HEIGHT': {16: 'line-height-count', 20: 'line-height-label'}.get(value),
                  'LETTER_SPACING': 'letter-spacing'}[scope]
        if suffix is None:
            raise ValueError('Unknown observed font role')
        return 'tab/font/' + suffix

    def bind(node, field, source_id, scope):
        variable = variables[source_id]
        kind = {'COLOR': 'color', 'FLOAT': 'number', 'STRING': 'string', 'BOOLEAN': 'boolean'}[variable['type']]
        aliases = {mode: {'alias': semantic(source_id, scope, mode)} for mode in MODES}
        signature = json.dumps([kind, None, scope, aliases], sort_keys=True)
        if signature not in groups:
            figma_name = token_name(scope, source_id, resolve_source(source_id, 'Contable'))
            parts = figma_name.split('/')
            logical = '--' + '-'.join([parts[1], parts[0], *parts[2:]])
            identity = 'tab.' + logical[2:]
            if any(t['id'] == identity for t in groups.values()):
                raise ValueError('Distinct vectors would collide in native naming: ' + figma_name)
            index = next(i for i, v in enumerate(source['variables']) if v['id'] == source_id)
            groups[signature] = {'id': identity, 'name': logical, 'figmaName': figma_name, 'web': f'var({logical})',
                                 'layer': 'component', 'type': kind, 'collection': 'tab', 'scopes': [scope],
                                 'description': f'Tab: {" / ".join(parts[1:])}; firma consolidada conforme a BH-P07.', 'values': aliases,
                                 'source': {'path': 'evidence/tab-pilot/source/variables.json',
                                            'sha256': digest('evidence/tab-pilot/source/variables.json'),
                                            'original_id': source_id, 'selector': f'JSON:/variables/{index}',
                                            'source_file_key': '9zs5RMR8LB5wHjW9Bd59BA'}}
        identity = groups[signature]['id']
        uses.append({'sourceNodeId': node['id'], 'field': field, 'sourceVariableId': source_id, 'scope': scope, 'tokenId': identity})
        return identity

    records = {}
    for identity in inventory['nodeIds'][1:]:
        node = nodes[identity]
        record = {'sourceId': identity, 'type': node['type'], 'props': {f: node[f] for f in FIELDS if f in node}, 'bindings': {}}
        for field, ref in node.get('boundVariables', {}).items():
            if field not in SCOPE:
                continue
            aliases = ref if isinstance(ref, list) else [ref]
            source_ids = {a['id'] for a in aliases if a.get('type') == 'VARIABLE_ALIAS'}
            if len(source_ids) != 1:
                raise ValueError('Mixed numeric/text variable binding')
            record['bindings'][field] = bind(node, field, source_ids.pop(), SCOPE[field])
        for field in ['fills', 'strokes']:
            record[field] = copy.deepcopy(node.get(field, []))
            for i, paint in enumerate(record[field]):
                ref = paint.pop('boundVariables', {}).get('color')
                if not ref:
                    # The linked Phosphor frame has an invisible, unbound white fill.
                    # Preserve that asset default; it is not a rendered component role.
                    if paint.get('visible') is False:
                        continue
                    raise ValueError(f'Unbound component paint: {identity}.{field}[{i}]')
                scope = 'STROKE_COLOR' if field == 'strokes' else 'TEXT_FILL' if node['type'] == 'TEXT' else 'SHAPE_FILL' if node['type'] == 'VECTOR' else 'FRAME_FILL'
                record['bindings'][field + '.' + str(i)] = bind(node, field + '.' + str(i), ref['id'], scope)
        if node['type'] == 'FRAME':
            record['props'].update(x=node['x'], y=node['y'], constraints=node['constraints'])
        if node.get('effectStyleId'):
            record['effectStyle'] = node['effectStyleId']
        record['childIds'] = node['childIds']
        records[identity] = record

    variants = []
    for identity in inventory['variantIds']:
        variant = nodes[identity]
        roles = {'container': identity}
        for c in variant['childIds']:
            roles[{'Label': 'label', 'Icon': 'icon', 'Badge': 'count', 'Focus ring': 'focus'}[nodes[c]['name']]] = c
        roles['iconShape'] = nodes[roles['icon']]['childIds'][0]
        roles['countLabel'] = nodes[roles['count']]['childIds'][0]
        variants.append({'sourceId': identity, 'axes': variant['variantProperties'], 'roles': roles, 'reactions': variant['reactions']})

    ordered = sorted(groups.values(), key=lambda t: t['figmaName'])
    token_set = {'schema_version': 1, 'id': 'TAB-TOKENS', 'version': '1.0.0',
                 'collections': [{'id': 'tab', 'name': 'tab', 'default_mode': MODES[0],
                                  'modes': [{'id': mode, 'name': mode} for mode in MODES]}],
                 'tokens': [{k: v for k, v in t.items() if k not in ['figmaName', 'web']} for t in ordered]}
    plan = {'id': 'TAB-001', 'version': '1.0.0', 'sourceFileKey': '9zs5RMR8LB5wHjW9Bd59BA',
            'sourceNodeId': '1183:1146', 'destinationFileKey': '98xEw6sK8FRVNEhopM5SSz', 'pageName': 'Tabs',
            'modes': MODES, 'tokens': ordered, 'variants': variants, 'nodes': records, 'uses': uses,
            'normalizations': normalized, 'shadowStyle': read('evidence/tab-pilot/source/dependencies.json')['styles'][0],
            'phosphor': read('evidence/tab-pilot/source/phosphor.json')['matches'][0],
            'statistics': {'observed_nodes': len(raw), 'observed_variants': len(variants), 'binding_uses': len(uses),
                           'source_candidates_by_scope': len({(u['sourceVariableId'], u['scope']) for u in uses}),
                           'unique_signatures': len(ordered), 'component_variables': len(ordered),
                           'primitive_identity_preserved': True,
                           'source_fields_normalized': len(normalized), 'named_effect_styles': 1}}
    return plan, token_set


if __name__ == '__main__':
    plan, tokens = prepare()
    (ROOT / 'evidence/tab-pilot/build-plan.json').write_text(json.dumps(plan, ensure_ascii=False, indent=2) + '\n')
    (ROOT / 'output/collection-consolidation/historical-tab-tokens.json').write_text(json.dumps(tokens, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(plan['statistics'], indent=2))
