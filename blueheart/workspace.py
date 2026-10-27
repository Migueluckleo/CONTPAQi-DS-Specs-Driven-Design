"""Catalog-driven norms, transitive dependencies, source impact and selective context."""
from pathlib import Path
from .io import Invalid, canonical, path, read, sha, source
from .schema import Schemas
from .contracts import parse, validate, closure
from .tokens import Tokens


class Workspace:
    def __init__(self, root):
        root = Path(root).resolve()
        self.root = root
        self.schemas = Schemas(root)
        config = read(root, "blueheart.json")
        if set(config) != {"schema_version", "catalog", "policy", "decisions"} or config["schema_version"] != 1:
            raise Invalid("Unsupported workspace configuration")
        self.config = config
        for schema_path in sorted(path(root, "schemas").glob("*.schema.json")):
            self.schemas.load(schema_path.name)
        self.policy = self.schemas.validate(read(root, config["policy"]), "policy.schema.json")
        if self.policy["layer_edges"] != {"primitive": [], "semantic": ["primitive"], "component": ["semantic"]}:
            raise Invalid("Token architecture requires primitive -> semantic -> component consumption")
        self.catalog = self.schemas.validate(read(root, config["catalog"]), "catalog.schema.json")
        data = self.schemas.validate(read(root, config["decisions"]), "decisions.schema.json")
        self.decisions = {d["id"]: d for d in data["decisions"]}
        if len(self.decisions) != len(data["decisions"]): raise Invalid("Duplicate decision ID")
        for d in self.decisions.values(): source(root, d["source"])
        self.contracts, self.current, self.entries, self.sources = {}, {}, {}, {}
        documents = []
        protocol_ids = set()
        for group in ("contracts", "token_sets"):
            for entry in self.catalog[group]:
                key = (entry["id"], entry["version"])
                if key in self.entries: raise Invalid("Duplicate catalog identity/version")
                protocol_path = entry["path"].startswith("protocols/") and entry["path"].endswith(".md") and entry["path"] != "protocols/README.md"
                if (not entry["path"].startswith("norms/") and not (group == "contracts" and protocol_path)) or entry["path"] == config["catalog"]:
                    raise Invalid("Norms must reside under norms/; operational contracts under protocols/")
                if entry["current"]:
                    if entry["id"] in self.current: raise Invalid("Ambiguous current version: " + entry["id"])
                    self.current[entry["id"]] = key
                self.entries[key] = entry
                raw = source(root, entry)
                if group == "contracts":
                    contract = parse(raw, self.schemas); meta = contract["metadata"]
                    if (meta["profile"] == "operational") != protocol_path:
                        raise Invalid("Operational contracts have one owner under protocols/ only")
                    if protocol_path:
                        if entry["id"] in protocol_ids:
                            raise Invalid("Operational contracts require one file per protocol; history belongs in Git/evidence")
                        protocol_ids.add(entry["id"])
                    if meta["profile"] not in self.policy["allowed_contract_profiles"]:
                        raise Invalid("Contract profile forbidden in this phase")
                    if entry["current"] and meta["status"] != "ELIGIBLE":
                        raise Invalid("Only an eligible contract can be current")
                    validate(contract, root, self.decisions)
                    self.contracts[key] = contract
                    for ref in meta["sources"]:
                        self.sources.setdefault(ref["path"], set()).add("contract:" + entry["id"] + "@" + entry["version"])
                else:
                    if not entry["current"]: raise Invalid("Historical token sets belong in evidence, not the active token registry")
                    meta = self.schemas.validate(read(root, entry["path"]), "token-set.schema.json")
                    documents.append(meta)
                if (meta["id"], meta["version"]) != key: raise Invalid("Catalog identity differs from file")
        registered = {e["path"] for e in self.entries.values()} | {config["catalog"]}
        actual = {p.relative_to(root).as_posix() for p in path(root, "norms").rglob("*") if p.is_file() and p.name != ".DS_Store"}
        actual.update(p.relative_to(root).as_posix() for p in path(root, "protocols").rglob("*")
                      if p.is_file() and p.name != ".DS_Store" and p.relative_to(root).as_posix() != "protocols/README.md")
        if actual != registered: raise Invalid("Unregistered or missing normative files: " + str(sorted(actual ^ registered)))
        self.tokens = Tokens(documents, root, self.policy)
        self.token_coverage = self.tokens.validate()
        self.edges = self.tokens.edges()
        for identity, token in self.tokens.tokens.items():
            self.sources.setdefault(token["source"]["path"], set()).add("token:" + identity)
        for key, contract in sorted(self.contracts.items()):
            name = "contract:" + key[0] + "@" + key[1]; self.edges[name] = set()
            evidence = {s["id"] for s in contract["metadata"]["sources"]}
            for dep in contract["metadata"]["dependencies"]:
                if dep["kind"] == "contract":
                    target = (dep["id"], dep.get("version"))
                    if target not in self.contracts: raise Invalid("Contract dependency needs an exact registered version")
                    if contract["metadata"]["status"] == "ELIGIBLE" and self.contracts[target]["metadata"]["status"] != "ELIGIBLE":
                        raise Invalid("Eligible contract depends on an ineligible contract")
                    self.edges[name].add("contract:" + target[0] + "@" + target[1])
                elif dep["kind"] == "token":
                    if "version" in dep: raise Invalid("Token versions are locked by their catalog set")
                    self.edges[name].add("token:" + dep["id"])
                elif dep["id"] not in evidence: raise Invalid("Unresolved evidence dependency")
        closure(self.edges, self.edges)
        self.component_token_minimum = {}
        for key, contract in sorted(self.contracts.items()):
            if contract["metadata"]["profile"] == "component":
                direct = [d["id"] for d in contract["metadata"]["dependencies"] if d["kind"] == "token"]
                self.component_token_minimum[key[0] + "@" + key[1]] = self.tokens.component_minimum(direct)

    def snapshot(self):
        for entry in self.entries.values(): source(self.root, entry)
        for contract in self.contracts.values():
            for ref in contract["metadata"]["sources"]: source(self.root, ref)
        for token in self.tokens.tokens.values(): source(self.root, token["source"])
        for decision in self.decisions.values(): source(self.root, decision["source"])
        names = {"blueheart.json", self.config["catalog"], self.config["policy"], self.config["decisions"]}
        names.update(entry["path"] for entry in self.entries.values())
        names.update(self.sources)
        names.update(d["source"]["path"] for d in self.decisions.values())
        names.update(p.relative_to(self.root).as_posix() for directory in ("schemas", "blueheart")
                     for p in path(self.root, directory).glob("*") if p.is_file())
        hashes = {name: sha(path(self.root, name).read_bytes()) for name in sorted(names)}
        return {"digest": sha(canonical(hashes)), "files": hashes}

    def check(self):
        return {"status": "PASS", "scope": "Infrastructure and registered normative content; not design or implementation QA",
                "contracts": len(self.contracts), "token_sets": len(self.catalog["token_sets"]), **self.token_coverage,
                "component_token_minimum": self.component_token_minimum,
                "graphify_required": False, "deferred": self.policy["deferred"], "snapshot": self.snapshot()["digest"]}

    def context(self, identity, version=None, intent="rules", budget=None, compact=False, modes=None):
        if intent not in {"rules", "dependencies", "evidence"}: raise Invalid("Unknown context intent")
        key = (identity, version) if version else self.current.get(identity)
        if key not in self.contracts: raise Invalid("No selected contract/version: " + identity)
        root = "contract:" + key[0] + "@" + key[1]
        if modes is not None and not isinstance(modes, dict): raise Invalid("Mode context must be an object")
        modes = modes or {}
        if modes and not compact: raise Invalid("Mode selection requires compact context")
        token_modes = {}
        if compact:
            for collection, mode in modes.items():
                if collection not in self.tokens.collections or mode not in {m["id"] for m in self.tokens.collections[collection]["modes"]}:
                    raise Invalid("Invalid mode context")
            # Resolve every declared token dependency. Trace states preserve alias-explicit
            # mode overrides, including two consumers needing different modes of one token.
            contract_edges = {n: {d for d in deps if d.startswith("contract:")}
                              for n, deps in self.edges.items() if n.startswith("contract:")}
            selected = set(closure([root], contract_edges))
            for name in list(selected):
                for dep in self.edges[name]:
                    if dep.startswith("token:"):
                        for state in self.tokens.resolve(dep[6:], modes)["chain"]:
                            token_modes.setdefault(state["id"], set()).add(state["mode"])
            selected = sorted(selected | {"token:" + i for i in token_modes})
        else:
            selected = closure([root], self.edges)
        result = {"status": "PASS", "scope": "Declared transitive dependencies", "intent": intent,
                  "snapshot": self.snapshot()["digest"], "root": root, "dependencies": selected, "documents": [], "tokens": []}
        for name in selected:
            if name.startswith("contract:"):
                contract_id, version_id = name[9:].rsplit("@", 1)
                contract = self.contracts[(contract_id, version_id)]
                entry = self.entries[(contract_id, version_id)]
                meta = contract["metadata"]
                document = {"id": contract_id, "version": version_id, "path": entry["path"], "sha256": entry["sha256"],
                            "status": meta["status"], "authority": meta["authority"], "targets": meta["targets"],
                            "readiness": meta["readiness"], "profile_data": meta["profile_data"]}
                if contract_id + "@" + version_id in self.component_token_minimum:
                    document["token_minimum"] = self.component_token_minimum[contract_id + "@" + version_id]
                if intent == "rules":
                    document["requirements"] = [{**r, "statement": contract["requirements"][r["id"]]}
                                                for r in contract["metadata"]["requirements"]]
                elif intent == "evidence": document["sources"] = contract["metadata"]["sources"]
                result["documents"].append(document)
            elif intent == "rules":
                token = self.tokens.tokens[name[6:]]
                if compact:
                    token = {k: v for k, v in token.items() if k in {"id", "name", "layer", "type", "unit", "collection", "scopes"}}
                    token["values"] = {m: self.tokens.tokens[name[6:]]["values"][m] for m in sorted(token_modes[name[6:]])}
                result["tokens"].append(token)
        if compact:
            result["projection"] = "selected-modes; provenance is retained in the referenced token sets"
            result["mode_context"] = {c: modes.get(c, v["default_mode"]) for c, v in sorted(self.tokens.collections.items())}
            sets = {self.tokens.source_sets[i] for i in token_modes}
            result["token_sets"] = [{"id": e["id"], "version": e["version"], "path": e["path"], "sha256": e["sha256"]}
                                    for e in self.catalog["token_sets"] if e["id"] + "@" + e["version"] in sets]
        limit = self.policy["default_context_bytes"] if budget is None else budget
        if type(limit) is not int or limit <= 0: raise Invalid("Context budget must be positive")
        result["context_bytes"] = 0
        while True:
            size = len(canonical(result))
            if result["context_bytes"] == size: break
            result["context_bytes"] = size
        if size > limit:
            return {"status": "BLOCKED", "reason": "CONTEXT_LIMIT", "required_bytes": size, "budget_bytes": limit,
                    "root": root, "snapshot": result["snapshot"], "documents": [], "tokens": []}
        return result

    def impact(self, changed):
        start = set()
        known_paths = set(self.sources)
        for key, entry in self.entries.items():
            known_paths.add(entry["path"])
            if entry["path"] in changed:
                if key in self.contracts: start.add("contract:" + key[0] + "@" + key[1])
                else: start.update("token:" + i for i, s in self.tokens.source_sets.items() if s == key[0] + "@" + key[1])
        for name in changed:
            path(self.root, name)  # Reject traversal even when the file no longer exists.
            start.update(self.sources.get(name, set()))
        reverse = {key: set() for key in self.edges}
        for consumer, dependencies in self.edges.items():
            for dep in dependencies: reverse[dep].add(consumer)
        affected, pending = set(start), list(start)
        while pending:
            for consumer in reverse[pending.pop()]:
                if consumer not in affected: affected.add(consumer); pending.append(consumer)
        unknown = sorted(set(changed) - known_paths)
        return {"status": "REVIEW_REQUIRED" if unknown else "PASS", "changed": sorted(changed),
                "affected": sorted(affected), "unmapped_paths": unknown,
                "scope": "Current declared dependencies; removed/unmapped paths require review against the previous snapshot"}

    def qa_plan(self, change, paths):
        return {"status": "PLAN_ONLY", "change": change, "required_gates": self.policy["gates"][change],
                "impact": self.impact(paths), "tests_executed": False,
                "independent_review": change in {"contract", "adapter", "tooling"}}
