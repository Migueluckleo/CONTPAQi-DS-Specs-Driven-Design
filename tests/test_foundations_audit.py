import copy
import unittest
import json
from pathlib import Path
import tempfile
from blueheart.foundations_audit import analyze, referenced_inventory
from blueheart.io import Invalid


class AuditTests(unittest.TestCase):
    def inventory(self):
        def v(identity, name, collection, values, description="Intent"):
            return {"id": identity, "key": "key-" + identity, "name": name, "variableCollectionId": collection,
                    "valuesByMode": values, "resolvedType": "FLOAT", "description": description, "codeSyntax": {}}
        return {"fileKey": "synthetic",
                "collections": [{"id": "p", "name": "primitive", "variableIds": ["a"], "defaultModeId": "one", "modes": [{"modeId": "one", "name": "Value"}]},
                                {"id": "s", "name": "semantic", "variableIds": ["b", "c"], "defaultModeId": "theme", "modes": [{"modeId": "theme", "name": "Theme"}]}],
                "variables": [v("a", "scale/one", "p", {"one": 12}),
                              v("b", "spacing/md", "s", {"theme": {"type": "VARIABLE_ALIAS", "id": "a"}}, "Espaciado md — 16px"),
                              v("c", "another/intent", "s", {"theme": {"type": "VARIABLE_ALIAS", "id": "a"}}, "Different intent")]}

    def test_membership_compares_ids_not_dictionary_values(self):
        result = analyze(self.inventory(), [])
        self.assertEqual(result["summary"]["structural_issues"], [])
        self.assertEqual(result["summary"]["unique_alias_targets"], 1)

    def test_equal_aliases_do_not_merge_identities(self):
        result = analyze(self.inventory(), [])
        self.assertEqual(len(result["matrix"]), 3)
        self.assertEqual(result["summary"]["equal_alias_semantic_groups"], 1)
        self.assertIn("not proof", result["equal_alias_groups"][0]["interpretation"])

    def test_description_is_compared_to_all_resolved_contexts(self):
        result = analyze(self.inventory(), [])
        mismatch = result["summary"]["numeric_description_mismatches"][0]
        self.assertEqual(mismatch["resolved"], [12])
        self.assertEqual(mismatch["name"], "spacing/md")

    def test_missing_alias_and_cycle_block_observed_scope(self):
        missing = self.inventory(); missing["variables"][1]["valuesByMode"]["theme"]["id"] = "absent"
        self.assertEqual(analyze(missing, [])["summary"]["status"], "BLOCKED")
        cycle = self.inventory(); cycle["variables"][1]["valuesByMode"]["theme"]["id"] = "c"
        cycle["variables"][2]["valuesByMode"]["theme"]["id"] = "b"
        self.assertEqual(analyze(cycle, [])["summary"]["status"], "BLOCKED")

    def test_consumer_impact_distinguishes_discard_and_upper_bound(self):
        pages = [{"page": {"id": "p", "name": "Descarte"}, "nodeCount": 2, "textNodes": 0, "errors": [],
                  "variables": {"b": {"references": 2, "nodeCount": 1, "samples": []}}}]
        result = analyze(self.inventory(), pages)
        primitive = next(r for r in result["matrix"] if r["original_id"] == "a")
        semantic = next(r for r in result["matrix"] if r["original_id"] == "b")
        self.assertEqual(primitive["direct_node_count"], 0)
        self.assertEqual(primitive["potential_node_uses_upper_bound"], 1)
        self.assertEqual(semantic["discard_direct_nodes"], 1)

    def test_incomplete_page_read_does_not_pass(self):
        pages = [{"page": {"id": "p", "name": "Page"}, "nodeCount": 1, "textNodes": 0,
                  "variables": {}, "errors": [{"operation": "read"}]}]
        self.assertEqual(analyze(self.inventory(), pages)["summary"]["status"], "BLOCKED")

    def test_non_enumerated_local_records_are_quarantined_and_coverage_checked(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            def save(name, value):
                (root / name).write_text(json.dumps({"content": [{"type": "text", "text": json.dumps(value)}]}))
            record = {"id": "z", "key": "z-key", "name": "legacy/intent", "remote": False, "variableCollectionId": "q"}
            save("referenced-000-response.json", {"variables": [record]})
            save("discard-external-ids-response.json", {"externalReferences": []})
            save("referenced-collections-response.json", {"referencedCollections": [{"id": "q", "name": "Unlisted", "remote": False}]})
            pages = [{"page": {"id": "p", "name": "Page"}, "variables": {"z": {"nodeCount": 1, "samples": []}}}]
            result = referenced_inventory(root, self.inventory(), pages)
            self.assertEqual(result["local_not_enumerated"], 1)
            self.assertEqual(result["status"], "RECONCILIATION_REQUIRED")
            self.assertEqual(result["matrix"][0]["proposal"], "QUARANTINE_EVIDENCE_RECONCILE_BEFORE_MIGRATION")
            save("referenced-000-response.json", {"variables": [{**record, "id": "different"}]})
            with self.assertRaises(Invalid): referenced_inventory(root, self.inventory(), pages)
