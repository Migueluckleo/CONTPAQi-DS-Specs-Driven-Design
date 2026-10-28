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


def project():
    mapping = read('evidence/collection-consolidation/migration-map.json')
    collection = mapping['collection']
    for family, source, prefixes in (
        ('tab', 'evidence/tab-pilot/destination/foundation.json', ('tab.',)),
        ('avatar', 'evidence/avatar-pilot/destination/foundation.json', ('avatar.', 'avatar-group.')),
    ):
        state = {k: copy.deepcopy(v) for k, v in read(source).items()
                 if not k.startswith(('created', 'mutated'))}
        state['role'] = 'DERIVED_CURRENT_NATIVE_LEDGER_NOT_RULES'
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


if __name__ == '__main__':
    project()
