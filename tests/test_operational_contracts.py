import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from blueheart.contracts import parse
from blueheart.io import Invalid, canonical, sha
from blueheart.workspace import Workspace

ROOT = Path(__file__).resolve().parents[1]


class OperationalContractTests(unittest.TestCase):
    def test_all_eight_have_one_registered_owner_and_complete_context(self):
        workspace = Workspace(ROOT)
        files = []
        for number in range(1, 9):
            identity = 'BH-P%02d' % number
            key = workspace.current[identity]
            contract = workspace.contracts[key]
            self.assertEqual(contract['metadata']['profile'], 'operational')
            files.append(workspace.entries[key]['path'])
            result = workspace.context(identity)
            self.assertEqual(result['status'], 'PASS', identity)
            selected = next(d for d in result['documents'] if d['id'] == identity)
            self.assertEqual({q['id'] for q in selected['requirements']}, set(contract['requirements']))
            self.assertEqual(result['context_bytes'], len(canonical(result)))
        self.assertEqual(len(files), len(set(files)))
        self.assertEqual(set(files), {p.relative_to(ROOT).as_posix() for p in (ROOT/'protocols').glob('0*.md')})
        self.assertEqual(workspace.context('BH-P08')['tokens'], [])

    def test_operational_profile_requires_inputs_outputs_responsibility_and_failure(self):
        workspace = Workspace(ROOT)
        entry = workspace.entries[workspace.current['BH-P08']]
        contract = parse((ROOT/entry['path']).read_bytes(), workspace.schemas)
        for field in contract['metadata']['profile_data']:
            meta = copy.deepcopy(contract['metadata'])
            del meta['profile_data'][field]
            with self.assertRaises(Invalid):
                workspace.schemas.validate(meta, 'operational.schema.json')

    def test_protocol_sources_and_catalog_hashes_fail_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for name in ('blueheart.json',):
                shutil.copy(ROOT/name, root/name)
            for name in ('norms', 'protocols', 'schemas', 'governance', 'evidence', 'blueheart', '.github', 'docs'):
                shutil.copytree(ROOT/name, root/name, ignore=shutil.ignore_patterns('.DS_Store'))
            Workspace(root)
            p = root/'protocols/08-GITHUB-RELEASE-DOCUMENTATION.md'
            p.write_text(p.read_text()+'drift\n')
            with self.assertRaisesRegex(Invalid, 'hash mismatch'):
                Workspace(root)

    def test_unregistered_protocol_and_component_in_protocol_directory_rejected(self):
        # Use the core fixture to exercise path validation without copying large evidence.
        from test_core import CoreTests
        fixture = CoreTests(); fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        root = fixture.root
        (root/'protocols').mkdir()
        (root/'protocols/09-UNKNOWN.md').write_text('not registered')
        with self.assertRaisesRegex(Invalid, 'Unregistered'):
            Workspace(root)
        (root/'protocols/09-UNKNOWN.md').unlink()
        meta, name = fixture.foundation()
        destination = 'protocols/01-WRONG.md'
        (root/name).rename(root/destination)
        cat = json.loads((root/'norms/catalog.json').read_text())
        cat['contracts'][0]['path'] = destination
        fixture.write('norms/catalog.json', cat)
        with self.assertRaisesRegex(Invalid, 'Operational contracts'):
            Workspace(root)
