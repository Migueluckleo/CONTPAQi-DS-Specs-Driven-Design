"""Print the current Button recipes; never rewrite historical source evidence."""
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def verified(entry):
    content = (ROOT / entry['path']).read_bytes()
    if hashlib.sha256(content).hexdigest() != entry['sha256']:
        raise ValueError('Hash mismatch: ' + entry['path'])
    return content


def materialize():
    manifest = json.loads((ROOT / 'consumption/button/manifest.json').read_text())
    verified(manifest['contract'])
    correction = json.loads(verified(manifest['prototypeCorrections']))
    if correction['contract'] != {k: manifest['contract'][k] for k in ('id', 'version')}:
        raise ValueError('Correction does not match the selected contract')
    baseline = json.loads(verified(correction['baseline']))
    plan = copy.deepcopy(baseline)
    variants = {v['sourceId']: v for v in plan['variants']}
    for rule in correction['rules']:
        source, target = variants[rule['sourceId']], variants[rule['destinationId']]
        if any(source[k] != rule[k] for k in ('type', 'size', 'state')):
            raise ValueError('Unexpected source identity')
        if (target['type'], target['size'], target['state']) != (source['type'], source['size'], 'hover'):
            raise ValueError('Destination does not preserve type and size')
        reactions = [r for r in source['reactions'] if r['trigger']['type'] == rule['trigger']]
        if len(reactions) != 1:
            raise ValueError('Expected exactly one reaction')
        actions = reactions[0].get('actions', [reactions[0].get('action')])
        if len(actions) != 1 or actions[0]['destinationId'] != rule['oldDestinationId']:
            raise ValueError('Historical destination changed unexpectedly')
        if (actions[0]['type'], actions[0]['navigation']) != ('NODE', 'CHANGE_TO'):
            raise ValueError('Unexpected action')
        actions[0]['destinationId'] = rule['destinationId']
        if reactions[0].get('action'):
            reactions[0]['action']['destinationId'] = rule['destinationId']
    plan['version'] = correction['contract']['version']
    return plan


if __name__ == '__main__':
    print(json.dumps(materialize(), ensure_ascii=False, indent=2))
