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
    def test_component_workflows_receive_theme_criteria_and_planning_gate(self):
        workspace = Workspace(ROOT)
        for identity in ('BH-P01', 'BH-P02', 'BH-P03', 'BH-P04', 'BH-P05', 'BH-P08'):
            context = workspace.context(identity)
            self.assertEqual(context['status'], 'PASS', identity)
            tokens = next(d for d in context['documents'] if d['id'] == 'BH-P07')
            requirements = {q['id']: q for q in tokens['requirements']}
            self.assertTrue({'REQ-P07-02', 'REQ-P07-03', 'REQ-P07-06'} <= requirements.keys())
            self.assertEqual(requirements['REQ-P07-06']['force'], 'MUST')
        for change in ('contract', 'token', 'adapter'):
            plan = workspace.qa_plan(change, ['protocols/07-COMPONENT-TOKENS.md'])
            self.assertIn('component-theme-behavior', plan['required_gates'])
            self.assertFalse(plan['tests_executed'])

    def test_main_can_integrate_without_another_reviewer(self):
        ruleset = json.loads((ROOT/'docs/releases/branch-ruleset.json').read_text())
        review = next(r['parameters'] for r in ruleset['rules'] if r['type'] == 'pull_request')
        self.assertEqual(review['required_approving_review_count'], 0)
        self.assertEqual(review['required_reviewers'], [])
        for field in ('require_last_push_approval', 'require_code_owner_review',
                      'require_extra_approval_for_unattributed_changes', 'dismiss_stale_reviews_on_push'):
            self.assertFalse(review[field], field)

    def test_main_still_requires_documentation_ci_and_preserved_history(self):
        ruleset = json.loads((ROOT/'docs/releases/branch-ruleset.json').read_text())
        self.assertEqual(ruleset['enforcement'], 'active')
        self.assertEqual(ruleset['bypass_actors'], [])
        self.assertEqual(ruleset['conditions']['ref_name'], {'include': ['~DEFAULT_BRANCH'], 'exclude': []})
        rules = {r['type']: r.get('parameters', {}) for r in ruleset['rules']}
        self.assertTrue({'deletion', 'non_fast_forward', 'pull_request', 'required_status_checks'} <= rules.keys())
        checks = rules['required_status_checks']
        self.assertEqual(checks['required_status_checks'], [{'context': 'release-documentation', 'integration_id': 15368}])
        self.assertTrue(checks['strict_required_status_checks_policy'])
        self.assertFalse(checks['do_not_enforce_on_create'])
        self.assertEqual(rules['pull_request']['allowed_merge_methods'], ['merge'])
        self.assertTrue(rules['pull_request']['required_review_thread_resolution'])

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
            for name in ('norms', 'protocols', 'schemas', 'governance', 'evidence', 'consumption', 'blueheart', '.github', 'docs'):
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
