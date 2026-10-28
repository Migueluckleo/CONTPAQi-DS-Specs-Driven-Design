"""ADR-020: fail closed for collection drift, preserve values and consumption."""
import copy
import hashlib
import json
from pathlib import Path
import runpy
import unittest

from blueheart.io import Invalid
from blueheart.tokens import Tokens
from blueheart.workspace import Workspace

ROOT = Path(__file__).resolve().parents[1]


class CollectionLayoutTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workspace = Workspace(ROOT)
        cls.policy = cls.workspace.policy
        cls.document = json.loads((ROOT/'norms/tokens/blueheart.4.0.0.json').read_text())

    def validate(self, document):
        return Tokens([document], ROOT, self.policy).validate()

    def test_only_three_homonymous_collections_and_four_contexts(self):
        self.assertEqual(self.validate(self.document), {'tokens': 396, 'collections': 3, 'mode_contexts': 4})
        counts = {c: sum(t['collection'] == c for t in self.document['tokens']) for c in ('primitive', 'semantic', 'component')}
        self.assertEqual(counts, {'primitive': 148, 'semantic': 109, 'component': 139})

    def test_extra_unused_family_collection_is_rejected(self):
        doc = copy.deepcopy(self.document)
        doc['collections'].append({'id': 'avatar', 'name': 'avatar', 'default_mode': 'Value', 'modes': [{'id': 'Value', 'name': 'Value'}]})
        with self.assertRaisesRegex(Invalid, 'exactly'):
            self.validate(doc)

    def test_component_in_semantic_collection_is_rejected(self):
        doc = copy.deepcopy(self.document)
        token = next(t for t in doc['tokens'] if t['layer'] == 'component')
        token['collection'] = 'semantic'
        with self.assertRaisesRegex(Invalid, 'wrong layer collection'):
            self.validate(doc)

    def test_family_named_native_collection_is_rejected(self):
        doc = copy.deepcopy(self.document)
        doc['collections'][2]['name'] = 'Buttons'
        with self.assertRaisesRegex(Invalid, 'names must match'):
            self.validate(doc)

    def test_every_identity_scope_and_alias_vector_is_preserved(self):
        historical_cut=json.loads((ROOT/'evidence/dot-pilot/history/blueheart.3.0.0.json').read_text())
        current = {t['id']: t for t in historical_cut['tokens']}
        historic = []
        for name in ('blueheart.2.1.0.json', 'tab.1.1.0.json', 'tabs.1.0.0.json', 'avatar.1.0.0.json'):
            historic.extend(json.loads((ROOT/'evidence/collection-consolidation/history'/name).read_text())['tokens'])
        self.assertEqual(set(current), {t['id'] for t in historic})
        for old in historic:
            expected = copy.deepcopy(old)
            if old['layer'] == 'component':
                expected['collection'] = 'component'
                expected['values'] = {m: old['values'].get(m, old['values'].get('Value')) for m in ('Contable', 'Administrativo', 'Servicios', 'Personas')}
            self.assertEqual(current[old['id']], expected)

    def test_current_component_manifests_and_recipes_select_registered_cut(self):
        mapping = json.loads((ROOT/'evidence/dot-pilot/migration-map.json').read_text())
        live = {v['nativeId'] for v in mapping['variables']}
        live.update(v['destination_id'] for v in json.loads(
            (ROOT/'evidence/figma-application/application-map.json').read_text())['variables'])
        def verify_references(value):
            if isinstance(value, dict):
                if 'path' in value and 'sha256' in value:
                    self.assertEqual(hashlib.sha256((ROOT/value['path']).read_bytes()).hexdigest(),
                                     value['sha256'], value['path'])
                for item in value.values():
                    verify_references(item)
            elif isinstance(value, list):
                for item in value:
                    verify_references(item)
        for family in ('button', 'tab', 'tabs', 'avatar', 'avatar-group','dot'):
            m = json.loads((ROOT/'consumption'/family/'manifest.json').read_text())
            verify_references(m)
            if 'nativeLedger' in m:
                ledger = json.loads((ROOT/m['nativeLedger']['path']).read_text())
                self.assertTrue(set(ledger['variableIds'].values()) <= live)
                self.assertEqual(ledger['role'], 'DERIVED_CURRENT_NATIVE_LEDGER_NOT_RULES')
                self.assertFalse(any(k.startswith(('created', 'mutated')) for k in ledger))
                self.assertEqual(len(ledger['variableIds']), {'tab':39,'avatar':29,'dot':19}[family])
            self.assertEqual(m['contract'], self.workspace.entries[self.workspace.current[m['contract']['id']]])
            collection = m.get('collection', m.get('native_collection'))
            self.assertEqual(collection['id'], 'VariableCollectionId:11:2')
            self.assertEqual(collection['name'], 'component')
            self.assertEqual(set(collection['modeIds']), {'Contable', 'Administrativo', 'Servicios', 'Personas'})
        module = runpy.run_path(str(ROOT/'consumption/button/materialize-plan.py'))
        self.assertEqual(module['materialize']()['version'], '3.0.0')
        plan = json.loads((ROOT/'consumption/tab/build-plan.3.0.0.json').read_text())
        self.assertTrue(all(t['collection'] == 'component' for t in plan['tokens']))
        avatar = json.loads((ROOT/'consumption/avatar/current-build-plan.json').read_text())
        self.assertTrue(all(t['collection'] == 'component' for t in avatar['tokens']))
        mapping = json.loads((ROOT/'evidence/collection-consolidation/migration-map.json').read_text())
        self.assertEqual({v['figmaName'].split('/')[0] for v in mapping['variables']}, {'button', 'avatar', 'tab'})
