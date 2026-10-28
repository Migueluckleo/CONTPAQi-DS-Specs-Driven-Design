"""Project current native identities; retain historical creation events only as evidence."""
from pathlib import Path
import copy
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads((ROOT/path).read_text())


def ref(path):
    return {'path': path, 'sha256': hashlib.sha256((ROOT/path).read_bytes()).hexdigest()}


def write(path, value):
    (ROOT/path).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')


def refresh_manifests():
    """Refresh derived pointers only; never alter source owners or catalog hashes."""
    catalog=read('norms/catalog.json')
    current={e['id']:e for e in catalog['contracts'] if e['current']}
    qa=ref('evidence/qa/dot-pilot-check.json')
    def references(value):
        if isinstance(value,dict):
            if 'path' in value and 'sha256' in value:
                value['sha256']=ref(value['path'])['sha256']
            for item in value.values(): references(item)
        elif isinstance(value,list):
            for item in value: references(item)
    for family in ('dot','button','tab','tabs','avatar','avatar-group'):
        path='consumption/'+family+'/manifest.json'
        manifest=read(path)
        manifest['contract']=current[manifest['contract']['id']]
        if 'dependency' in manifest: manifest['dependency']=current[manifest['dependency']['id']]
        for dependency in manifest.get('dependencies',[]):
            dependency['contract']=current[dependency['contract']['id']]
        if 'sharedCount' in manifest: manifest['sharedCount']['contract']=current['DOT-001']
        if family!='button': manifest['qa']=qa
        if family=='dot': manifest.update(build_plan='current-build-plan.json',variable_map='variable-map.csv',binding_map='binding-map.csv',minimum='token-minimum.json')
        references(manifest)
        write(path,manifest)


def project():
    refresh_manifests()
    mapping = read('evidence/dot-pilot/migration-map.json')
    collection = mapping['collection']
    for family, source, prefixes in (
        ('tab', 'evidence/tab-pilot/destination/foundation.json', ('tab.',)),
        ('avatar', 'evidence/avatar-pilot/destination/foundation.json', ('avatar.', 'avatar-group.')),
    ):
        state = {k: copy.deepcopy(v) for k, v in read(source).items()
                 if not k.startswith(('created', 'mutated'))}
        state['role'] = 'DERIVED_CURRENT_NATIVE_LEDGER_NOT_RULES'
        dot = read('evidence/dot-pilot/destination/foundation.json')
        state['dotDependency'] = ref('consumption/dot/manifest.json')
        if family == 'avatar':
            state['presenceSetId'] = dot['setId']
            state['presence'] = [v for v in dot['variants'] if v['axes']['type'] in ('active','busy','inactive')]
        else:
            count = next(v for v in dot['variants'] if v['axes'] == {'type':'count','size':'medium'})
            state.update(countId=count['id'],countTextId=count['textId'],countProperty=dot['propertyKeys']['Count'])
            state['styleIds']['count'] = dot['styles']['medium']
        state['historicalBootstrap'] = ref(source)
        state['variableIds'] = {v['logicalId']: v['nativeId'] for v in mapping['variables']
                                if v['logicalId'].startswith(prefixes)}
        state['collections'] = {'component': copy.deepcopy(collection)}
        state['collectionId'] = collection['id']
        state['modeIds'] = collection['modeIds']
        if 'collection' in state:
            state['collection'] = copy.deepcopy(collection)
        path = 'consumption/'+family+'/current-native-ledger.json'
        write(path, state)
        manifest = read('consumption/'+family+'/manifest.json')
        manifest['nativeLedger'] = ref(path)
        write('consumption/'+family+'/manifest.json', manifest)

    refresh_manifests()


if __name__ == '__main__':
    project()
