import copy
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from blueheart.contracts import closure, parse
from blueheart.io import Invalid, canonical, loads, path, sha, source
from blueheart.schema import Schemas
from blueheart.tokens import Tokens
from blueheart.workspace import Workspace

ROOT = Path(__file__).resolve().parents[1]


class CoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for directory in ("schemas", "governance", "evidence/authorization"):
            shutil.copytree(ROOT / directory, self.root / directory)
        # Synthetic fixtures exercise arbitrary collections, outside the DS layout.
        policy = json.loads((self.root / "governance/policy.json").read_text())
        policy.pop("token_collections", None)
        self.write("governance/policy.json", policy)
        (self.root / "norms").mkdir()
        self.write("norms/catalog.json", {"schema_version": 1, "contracts": [], "token_sets": []})
        shutil.copyfile(ROOT / "blueheart.json", self.root / "blueheart.json")
        self.write("evidence/sample.json", {"value": 7, "rows": ["proof"], "variable": {"id": "fixture"}})
        self.ref = {"id": "SRC-ONE", "path": "evidence/sample.json", "sha256": sha((self.root / "evidence/sample.json").read_bytes()), "selector": "JSON:/rows/0"}

    def write(self, name, value):
        target = self.root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(canonical(value) + b"\n")

    def foundation(self, identity="FND-ONE", version="1.0.0", dependencies=None, current=True):
        meta = {"schema_version": 1, "id": identity, "version": version, "profile": "foundation", "status": "ELIGIBLE",
                "authority": {"kind": "DELEGATED", "decision_id": "TEST-DECISION"}, "targets": ["documentation"],
                "readiness": {"documentation": "READY"}, "sources": [self.ref], "dependencies": dependencies or [],
                "requirements": [{"id": "REQ-ONE", "force": "MUST", "provenance": "EXPLICIT", "sources": ["SRC-ONE"], "acceptance": ["Verify sample bytes"]}],
                "profile_data": {"domains": ["color"]}}
        decisions = json.loads((self.root / "governance/decisions.json").read_text())
        existing = next((d for d in decisions["decisions"] if d["id"] == "TEST-DECISION"), None)
        if existing:
            if identity not in existing["scope"]: existing["scope"].append(identity)
        else:
            decisions["decisions"].append({"id": "TEST-DECISION", "status": "ADOPTED", "actor": "implementing_agent",
                "statement": "Synthetic scoped authority for infrastructure testing", "scope": [identity], "source": self.ref})
        self.write("governance/decisions.json", decisions)
        name = "norms/" + identity + "-" + version + ".md"
        raw = b"---\n" + canonical(meta) + b"\n---\n# Synthetic foundation\n\n### REQ-ONE\nPreserve the exact observed value.\n"
        (self.root / name).write_bytes(raw)
        self.register("contracts", meta, name, current)
        return meta, name

    def register(self, group, meta, name, current=True):
        catalog = json.loads((self.root / "norms/catalog.json").read_text())
        catalog[group].append({"id": meta["id"], "version": meta["version"], "path": name,
                               "sha256": sha((self.root / name).read_bytes()), "current": current})
        self.write("norms/catalog.json", catalog)

    def token_document(self):
        token_source = {**self.ref, "selector": "JSON:/variable", "original_id": "fixture"}
        return {"schema_version": 1, "id": "TOKENS-ONE", "version": "1.0.0",
                "collections": [{"id": "palette", "name": "Palette", "default_mode": "light",
                                 "modes": [{"id": "light", "name": "Light"}, {"id": "dark", "name": "Dark"}]}],
                "tokens": [{"id": "scale.one", "name": "scale/one", "layer": "primitive", "type": "number", "unit": "px",
                            "description": "Synthetic scale datum", "collection": "palette", "values": {"light": 1, "dark": 2}, "source": token_source},
                           {"id": "space.intent", "name": "space/intent", "layer": "semantic", "type": "number", "unit": "px",
                            "description": "Synthetic spacing intent", "collection": "palette", "values": {"light": {"alias": "scale.one"}, "dark": {"alias": "scale.one"}}, "source": token_source}]}

    def token_store(self, document=None):
        doc = document or self.token_document()
        Schemas(self.root).validate(doc, "token-set.schema.json")
        policy = json.loads((self.root / "governance/policy.json").read_text())
        return Tokens([doc], self.root, policy)

    def component_fixture(self, identity, dependencies):
        meta, name = self.foundation(identity, dependencies=dependencies)
        meta.update(profile="component", profile_data={"anatomy": ["content"], "composition": "fixed", "accessibility": "defined"})
        (self.root / name).write_bytes(b"---\n" + canonical(meta) + b"\n---\n# Synthetic component\n\n### REQ-ONE\nPreserve the fixture.\n")
        catalog = json.loads((self.root / "norms/catalog.json").read_text())
        next(e for e in catalog["contracts"] if e["id"] == identity)["sha256"] = sha((self.root / name).read_bytes())
        self.write("norms/catalog.json", catalog)

    def component_tokens_fixture(self):
        d = self.token_document()
        for name in ("control.one", "control.two"):
            t = copy.deepcopy(d["tokens"][1])
            t.update(id=name, name=name, layer="component", scopes=["WIDTH_HEIGHT"],
                     values={m: {"alias": "space.intent"} for m in ("light", "dark")})
            d["tokens"].append(t)
        return d

    def test_registered_families_keep_unrequested_destinations_deferred(self):
        w = Workspace(ROOT)
        self.assertEqual(set(w.current), {"BUTTON-001", "TAB-001", "TABS-001", "BLUEHEART-TOKENS", "AVATAR-001", "AVATAR-GROUP-001", "DOT-001", "LOADER-001"} | {"BH-P%02d" % i for i in range(1, 9)})
        report = w.check()["component_token_minimum"]["BUTTON-001@4.0.0"]
        self.assertEqual(report["component_tokens"], 45)
        self.assertEqual(report["redundancies"], 0)
        self.assertEqual(w.check()["component_token_minimum"]["TAB-001@3.0.0"]["component_tokens"], 39)
        self.assertEqual(w.check()["component_token_minimum"]["TAB-001@3.0.0"]["redundancies"], 0)
        self.assertTrue(all(t["id"].startswith(("button.", "tab.", "tabs.", "avatar.", "avatar-group.", "dot.", "loader.")) for t in w.tokens.tokens.values() if t["layer"] == "component"))
        self.assertEqual(w.check()["component_token_minimum"]["TAB-001@3.0.0"]["component_tokens"], 39)
        self.assertEqual(w.check()["component_token_minimum"]["TABS-001@3.0.0"]["component_tokens"], 5)
        self.assertFalse((ROOT / "implementations/react").exists())
        self.assertFalse((ROOT / "implementations/web").exists())
        self.assertFalse((ROOT / "graphify-out").exists())

    def test_empty_workspace_is_functional_and_deterministic(self):
        a = Workspace(self.root); b = Workspace(self.root)
        self.assertEqual(a.check()["status"], "PASS")
        self.assertEqual(a.snapshot(), b.snapshot())
        with self.assertRaises(Invalid): a.context("ABSENT")

    def test_duplicate_keys_and_nonfinite_numbers_rejected(self):
        for value in ['{"a":1,"a":2}', '{"a":NaN}', '{"a":1e10000}']:
            with self.assertRaises(Invalid): loads(value)

    def test_traversal_and_symlink_rejected(self):
        for value in ["../file", "/tmp/file", "evidence//file", "evidence\\file"]:
            with self.assertRaises(Invalid): path(self.root, value)
        (self.root / "evidence/link").symlink_to(self.root / "evidence/sample.json")
        with self.assertRaises(Invalid): path(self.root, "evidence/link")

    def test_source_hash_and_pointer_must_match(self):
        source(self.root, self.ref)
        with self.assertRaises(Invalid): source(self.root, {**self.ref, "selector": "JSON:/rows/1"})
        with self.assertRaises(Invalid): source(self.root, {**self.ref, "selector": "JSON:/rows/-1"})
        with self.assertRaises(Invalid): source(self.root, {**self.ref, "selector": "JSON:/variable", "original_id": "other"})
        self.write("evidence/sample.json", {"value": 8})
        with self.assertRaises(Invalid): source(self.root, self.ref)

    def test_unsupported_schema_keyword_is_not_ignored(self):
        self.write("schemas/unknown.schema.json", {"type": "string", "format": "email"})
        with self.assertRaises(Invalid): Schemas(self.root).validate("x", "unknown.schema.json")

    def test_distinct_profiles_validated_in_memory(self):
        meta, name = self.foundation()
        for profile, data in [("foundation", {"domains": ["color"]}),
                              ("component", {"anatomy": ["content"], "composition": "fixed", "accessibility": "defined"}),
                              ("pattern", {"contexts": ["synthetic"], "behavior": "defined", "accessibility": "defined"})]:
            candidate = {**meta, "profile": profile, "profile_data": data}
            Schemas(self.root).validate(candidate, profile + ".schema.json")
            with self.assertRaises(Invalid): Schemas(self.root).validate({**candidate, "profile_data": {}}, profile + ".schema.json")

    def test_frontmatter_is_json_subset_not_an_unverified_yaml_parser(self):
        with self.assertRaises(Invalid): parse(b"---\nid: X\n---\n# Text", Schemas(self.root))

    def test_missing_requirement_statement_rejected(self):
        meta, name = self.foundation()
        raw = b"---\n" + canonical(meta) + b"\n---\n# Missing statement\n"
        with self.assertRaises(Invalid): parse(raw, Schemas(self.root))

    def test_hash_drift_and_unregistered_norms_rejected(self):
        _, name = self.foundation()
        Workspace(self.root)
        (self.root / name).write_text("Changed")
        with self.assertRaises(Invalid): Workspace(self.root)
        (self.root / name).unlink()
        self.write("norms/catalog.json", {"schema_version": 1, "contracts": [], "token_sets": []})
        (self.root / "norms/unregistered.md").write_text("not registered")
        with self.assertRaises(Invalid): Workspace(self.root)

    def test_explicit_selection_never_highest_version_wins(self):
        self.foundation(version="1.0.0")
        self.foundation(version="9.0.0", current=False)
        self.assertEqual(Workspace(self.root).context("FND-ONE")["root"], "contract:FND-ONE@1.0.0")

    def test_ambiguous_current_versions_fail(self):
        self.foundation(version="1.0.0")
        self.foundation(version="2.0.0")
        with self.assertRaises(Invalid): Workspace(self.root)

    def test_scoped_authority_cannot_approve_another_contract(self):
        self.foundation()
        d = json.loads((self.root / "governance/decisions.json").read_text())
        d["decisions"][-1]["scope"] = ["OTHER"]
        self.write("governance/decisions.json", d)
        with self.assertRaises(Invalid): Workspace(self.root)

    def test_dependency_closure_is_transitive_and_cycle_safe(self):
        self.assertEqual(closure(["c"], {"a": set(), "b": {"a"}, "c": {"b"}}), ["a", "b", "c"])
        with self.assertRaises(Invalid): closure(["a"], {"a": {"b"}, "b": {"a"}})
        with self.assertRaises(Invalid): closure(["a"], {"a": {"missing"}})

    def test_contract_dependencies_require_pinned_versions(self):
        self.foundation("FND-TWO")
        self.foundation(dependencies=[{"kind": "contract", "id": "FND-TWO", "relation": "uses"}])
        with self.assertRaises(Invalid): Workspace(self.root)

    def test_context_covers_transitive_dependencies_without_partial_success(self):
        self.foundation("FND-TWO")
        self.foundation(dependencies=[{"kind": "contract", "id": "FND-TWO", "version": "1.0.0", "relation": "uses"}])
        w = Workspace(self.root)
        self.assertEqual(len(w.context("FND-ONE")["documents"]), 2)
        exact = w.context("FND-ONE")
        self.assertEqual(exact["context_bytes"], len(canonical(exact)))
        self.assertEqual(w.context("FND-ONE", budget=exact["context_bytes"])["status"], "PASS")
        self.assertEqual(w.context("FND-ONE", budget=exact["context_bytes"]-1)["status"], "BLOCKED")
        with self.assertRaises(Invalid): w.context("FND-ONE", intent="unknown")
        blocked = w.context("FND-ONE", budget=1)
        self.assertEqual(blocked["status"], "BLOCKED")
        self.assertEqual(blocked["documents"], [])
        self.assertNotIn("sources", w.context("FND-ONE")["documents"][0])
        self.assertIn("sources", w.context("FND-ONE", intent="evidence")["documents"][0])

    def test_compact_context_preserves_explicit_alias_mode_and_rejects_unknown_modes(self):
        d = self.token_document()
        d["tokens"][1]["values"]["light"]["mode"] = "dark"
        self.write("norms/tokens.json", d)
        self.register("token_sets", d, "norms/tokens.json")
        self.foundation(dependencies=[{"kind": "token", "id": "space.intent", "relation": "uses"}])
        w = Workspace(self.root)
        result = w.context("FND-ONE", compact=True, modes={"palette": "light"})
        projected = {t["id"]: t for t in result["tokens"]}
        self.assertEqual(projected["scale.one"]["values"], {"dark": 2})
        self.assertEqual(projected["space.intent"]["values"], {"light": {"alias": "scale.one", "mode": "dark"}})
        self.assertEqual(len(result["token_sets"]), 1)
        self.assertEqual(result["context_bytes"], len(canonical(result)))
        self.assertEqual(w.context("FND-ONE", compact=True, budget=1)["status"], "BLOCKED")
        for mode in [{"palette": "unknown"}, {"unknown": "light"}, []]:
            with self.assertRaises(Invalid): w.context("FND-ONE", compact=True, modes=mode)
        with self.assertRaises(Invalid): w.context("FND-ONE", modes={"palette": "dark"})

    def test_pilot_consumption_retains_every_rule_within_budget_in_all_themes(self):
        w = Workspace(ROOT)
        self.assertEqual(w.context("BUTTON-001")["status"], "BLOCKED")
        for mode in ("Contable", "Administrativo", "Servicios", "Personas"):
            result = w.context("BUTTON-001", compact=True, modes={"component": mode})
            self.assertEqual(result["status"], "PASS")
            self.assertLessEqual(result["context_bytes"], w.policy["default_context_bytes"])
            self.assertEqual({r["id"] for r in result["documents"][0]["requirements"]},
                             set(w.contracts[w.current["BUTTON-001"]]["requirements"]))
            self.assertIn("REQ-COLLECTION", {r["id"] for r in result["documents"][0]["requirements"]})
            self.assertEqual(len([t for t in result["tokens"] if t["layer"] == "component"]), 60)
            for t in result["tokens"]:
                for selected, value in t["values"].items(): self.assertEqual(value, w.tokens.tokens[t["id"]]["values"][selected])
        self.assertEqual(w.tokens.resolve("button.color-button-primary-bg-hover", {"component": "Contable"})["chain"][-1]["id"], "primitive.blue-500")

    def test_semantic_scope_and_component_scope_type_fail_closed(self):
        d = self.token_document(); d["tokens"][1]["scopes"] = ["WIDTH_HEIGHT"]
        with self.assertRaisesRegex(Invalid, "empty scopes"): self.token_store(d).validate()
        d = self.token_document(); component = copy.deepcopy(d["tokens"][1])
        component.update(id="control.size", name="control/size", layer="component", scopes=["TEXT_FILL"],
                         values={m: {"alias": "space.intent"} for m in ("light", "dark")})
        d["tokens"].append(component)
        with self.assertRaisesRegex(Invalid, "scope/type"): self.token_store(d).validate()
        component["scopes"] = ["WIDTH_HEIGHT"]
        self.assertEqual(self.token_store(d).validate()["tokens"], 3)
        component["scopes"] = []
        with self.assertRaisesRegex(Invalid, "explicit property scope"): self.token_store(d).validate()
        component["scopes"] = ["WIDTH_HEIGHT", "GAP"]
        with self.assertRaisesRegex(Invalid, "exactly one property scope"): self.token_store(d).validate()

    def test_component_duplicates_block_workspace_before_consumption(self):
        d = self.component_tokens_fixture()
        self.write("norms/tokens.json", d); self.register("token_sets", d, "norms/tokens.json")
        self.component_fixture("CMP-ONE", [{"kind": "token", "id": name, "relation": "uses"} for name in ("control.one", "control.two")])
        with self.assertRaisesRegex(Invalid, "BH-P07 redundant component tokens"): Workspace(self.root)

    def test_minimum_preserves_distinct_scopes_and_semantic_identities(self):
        d = self.component_tokens_fixture(); d["tokens"][-1]["scopes"] = ["GAP"]
        store = self.token_store(d); store.validate()
        self.assertEqual(store.component_minimum(["control.one", "control.two"])["distinct_signatures"], 2)
        d = self.component_tokens_fixture()
        other = copy.deepcopy(d["tokens"][1]); other.update(id="space.other", name="space/other")
        d["tokens"].append(other)
        d["tokens"][3]["values"] = {m: {"alias": "space.other"} for m in ("light", "dark")}
        store = self.token_store(d); store.validate()
        self.assertEqual(store.resolve("control.one")["value"], store.resolve("control.two")["value"])
        self.assertEqual(store.component_minimum(["control.one", "control.two"])["distinct_signatures"], 2)

    def test_minimum_compares_every_mode_and_explicit_alias_mode(self):
        d = self.component_tokens_fixture()
        d["tokens"][-1]["values"]["dark"]["mode"] = "light"
        store = self.token_store(d); store.validate()
        self.assertEqual(store.component_minimum(["control.one", "control.two"])["distinct_signatures"], 2)
        d["tokens"][-1]["values"]["dark"].pop("mode")
        store = self.token_store(d); store.validate()
        with self.assertRaisesRegex(Invalid, "BH-P07 redundant"): store.component_minimum(["control.one", "control.two"])

    def test_minimum_does_not_equate_different_collection_contexts(self):
        d = self.component_tokens_fixture(); c = copy.deepcopy(d["collections"][0]); c["id"] = "another"; d["collections"].append(c)
        d["tokens"][-1]["collection"] = "another"
        store = self.token_store(d); store.validate()
        self.assertEqual(store.component_minimum(["control.one", "control.two"])["distinct_signatures"], 2)

    def test_minimum_is_per_component_not_a_global_merge_of_families(self):
        d = self.component_tokens_fixture()
        self.write("norms/tokens.json", d); self.register("token_sets", d, "norms/tokens.json")
        for identity, token in [("CMP-ONE", "control.one"), ("CMP-TWO", "control.two")]:
            self.component_fixture(identity, [{"kind": "token", "id": token, "relation": "uses"}])
        w = Workspace(self.root)
        self.assertEqual({k: r["component_tokens"] for k, r in w.check()["component_token_minimum"].items()},
                         {"CMP-ONE@1.0.0": 1, "CMP-TWO@1.0.0": 1})

    def test_duplicate_color_semantic_primitive_is_rejected(self):
        d = self.token_document()
        for t in d["tokens"]:
            t["type"] = "color"; t.pop("unit")
        d["tokens"][0]["values"] = {m: {"r": 0, "g": 0, "b": 0, "a": 1} for m in ("light", "dark")}
        other = copy.deepcopy(d["tokens"][1]); other.update(id="color.copy", name="color/copy"); d["tokens"].append(other)
        with self.assertRaisesRegex(Invalid, "Duplicate color semantic primitive"): self.token_store(d).validate()

    def test_impact_is_transitive_and_unknown_paths_require_review(self):
        self.foundation("FND-TWO")
        self.foundation(dependencies=[{"kind": "contract", "id": "FND-TWO", "version": "1.0.0", "relation": "uses"}])
        w = Workspace(self.root)
        self.assertEqual(len(w.impact(["evidence/sample.json"])["affected"]), 2)
        self.assertEqual(w.impact(["unmapped.json"])["status"], "REVIEW_REQUIRED")
        self.assertFalse(w.qa_plan("token", ["evidence/sample.json"])["tests_executed"])

    def test_modes_resolve_without_implicit_name_mapping(self):
        store = self.token_store(); self.assertEqual(store.validate()["mode_contexts"], 2)
        self.assertEqual(store.resolve("space.intent")["value"], 1)
        self.assertEqual(store.resolve("space.intent", {"palette": "dark"})["value"], 2)
        with self.assertRaises(Invalid): store.resolve("space.intent", {"palette": "Dark"})
        with self.assertRaises(Invalid): store.resolve("space.intent", {"unknown": "light"})

    def test_cross_collection_alias_has_explicit_mode_trace(self):
        d = self.token_document()
        d["collections"].append({"id": "intent", "name": "Intent", "default_mode": "only", "modes": [{"id": "only", "name": "Only"}]})
        d["tokens"][1].update(collection="intent", values={"only": {"alias": "scale.one", "mode": "dark"}})
        result = self.token_store(d).resolve("space.intent")
        self.assertEqual(result["value"], 2)
        self.assertEqual(result["chain"][-1]["mode_selection"], "alias-explicit")

    def test_missing_modes_and_alias_target_rejected(self):
        for alter in [lambda d: d["tokens"][0]["values"].pop("dark"),
                      lambda d: d["tokens"][1]["values"]["light"].update(alias="absent")]:
            d = self.token_document(); alter(d)
            with self.assertRaises(Invalid): self.token_store(d).validate()

    def test_type_unit_and_layer_violations_rejected(self):
        for field, value in [("type", "string"), ("unit", "rem"), ("layer", "primitive")]:
            d = self.token_document(); d["tokens"][1][field] = value
            with self.assertRaises(Invalid): self.token_store(d).validate()

    def test_same_value_does_not_merge_identities(self):
        d = self.token_document(); other = copy.deepcopy(d["tokens"][1]); other.update(id="space.other", name="space/other", description="Another intention")
        d["tokens"].append(other); store = self.token_store(d)
        self.assertEqual(len(store.tokens), 3)
        self.assertEqual(store.resolve("space.intent")["value"], store.resolve("space.other")["value"])

    def test_literals_are_typed_and_finite(self):
        for kind, value in [("number", True), ("number", float("inf")), ("color", {"r": 2, "g": 0, "b": 0, "a": 1})]:
            with self.assertRaises(Invalid): Tokens.literal(kind, value)

    def test_mode_budget_blocks_instead_of_claiming_partial_coverage(self):
        store = self.token_store(); store.policy["max_mode_combinations"] = 1
        with self.assertRaises(Invalid): store.validate()

    def test_cli_check_and_context_missing_are_read_only(self):
        before = {p.relative_to(self.root).as_posix(): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        for arguments, expected in [(["check"], 0), (["context", "ABSENT"], 2)]:
            result = subprocess.run([sys.executable, "-B", "-m", "blueheart", "--root", str(self.root), *arguments], cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        after = {p.relative_to(self.root).as_posix(): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
