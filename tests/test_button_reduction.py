"""Regression coverage for consolidation without changing source recipes or foundations."""
import copy
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def read(name):
    return json.loads((ROOT / name).read_text())


class ButtonReductionTests(unittest.TestCase):
    def test_minimum_preserves_exact_scope_and_all_theme_aliases(self):
        before = read('evidence/button-reduction/before/build-plan.json')
        after = read('evidence/button-pilot/build-plan.json')
        def signature(t):
            return t['type'], tuple(t['scopes']), tuple(sorted(t['aliases'].items()))
        signatures = {signature(t) for t in before['tokens']}
        self.assertEqual(len(before['tokens']), 125)
        self.assertEqual(len(signatures), 47)
        self.assertEqual(len(after['tokens']), 47)
        self.assertEqual({signature(t) for t in after['tokens']}, signatures)
        self.assertTrue(all(len(t['scopes']) == 1 for t in after['tokens']))
        self.assertEqual(sum(t['type'] == 'COLOR' for t in after['tokens']), 26)
        self.assertEqual(set(after['tokenMigration']), {t['name'] for t in before['tokens']})
        # The creation adapter must not silently recreate the retired 125-token set.
        script = (ROOT / 'implementations/figma/button-tokens.js').read_text()
        data = json.loads(script.split('const data=', 1)[1].split(';\n', 1)[0])
        self.assertEqual(len(data['tokens']), 47)
        self.assertEqual({t['name']: signature(t) for t in data['tokens']},
                         {t['name']: signature(t) for t in after['tokens']})

    def test_recipes_only_change_token_names(self):
        before = read('evidence/button-reduction/before/build-plan.json')
        after = read('evidence/button-pilot/build-plan.json')
        mapping = after['tokenMigration']
        def remap(value):
            if isinstance(value, str): return mapping.get(value, value)
            if isinstance(value, dict): return {k: remap(v) for k, v in value.items()}
            if isinstance(value, list): return [remap(v) for v in value]
            return value
        self.assertEqual(remap(before['variants']), after['variants'])
        self.assertEqual(before['spinnerFrames'], after['spinnerFrames'])
        self.assertEqual(before['icon'], after['icon'])
        # The different text/icon aliases in Servicios must remain distinct.
        tokens = {t['name']: t for t in after['tokens']}
        self.assertNotEqual(tokens['color-button-icon-brand']['aliases']['Servicios'],
                            tokens['color-button-text-brand']['aliases']['Servicios'])

    def test_foundations_are_unchanged_and_retained_ids_still_exist(self):
        before = read('evidence/button-reduction/before/blueheart.1.0.0.json')
        after = read('norms/tokens/blueheart.4.0.0.json')
        historical = read('evidence/avatar-pilot/history/blueheart.2.0.0.json')
        previous_ids = {t['id'] for t in historical['tokens']}
        expected = copy.deepcopy(historical['tokens'])
        for token in expected:
            if token['layer'] == 'component':
                token['collection'] = 'component'
        self.assertEqual([t for t in after['tokens'] if t['id'] in previous_ids], expected)
        self.assertEqual({t['id'] for t in after['tokens'] if t['layer'] != 'component'} - previous_ids,
                         {'primitive.spacing-negative-' + str(n) for n in (4, 6, 8)} |
                         {'semantic.spacing-overlap-' + r for r in ('xs', 'sm', 'md')})
        self.assertEqual([t for t in before['tokens'] if t['layer'] != 'component'],
                         [t for t in after['tokens'] if t['layer'] != 'component' and t['id'] in previous_ids])
        before_ids = {v['id'] for v in read('evidence/button-reduction/before/state.json')['createdVariables']}
        state = read('evidence/button-pilot/destination/state.json')
        retained = {v['id'] for v in state['createdVariables']}
        retired = set(state['retiredVariableIds'])
        self.assertEqual(len(retained), 47)
        self.assertEqual(len(retired), 78)
        self.assertEqual(retained | retired, before_ids)
        self.assertFalse(retained & retired)


if __name__ == '__main__':
    unittest.main()
