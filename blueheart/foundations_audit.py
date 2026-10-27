"""Recompute a read-only Foundations audit from current-task MCP evidence, never norms."""
import argparse
from collections import Counter, defaultdict
import csv
import io
import json
from pathlib import Path
import re
from .io import Invalid, canonical, loads, sha


def payload(file):
    response = loads(file.read_bytes())
    if response.get("isError"): raise Invalid("Failed MCP response: " + file.name)
    return loads(next(c["text"] for c in response["content"] if c["type"] == "text"))


def assemble(directory):
    directory = Path(directory)
    discovery = payload(directory / "discovery-response.json")
    variables = []
    for start in range(0, discovery["variableCount"], 50):
        batch = payload(directory / ("variables-%03d-response.json" % start))
        if batch["total"] != discovery["variableCount"] or batch["start"] != start:
            raise Invalid("Inconsistent inventory batches")
        variables.extend(batch["variables"])
    inventory = {"fileKey": discovery["fileKey"], "requestedNode": discovery["requestedNode"],
                 "collections": discovery["collections"], "variables": variables,
                 "provenance": "LIVE_FIGMA_READ_ONLY", "normative_status": "OBSERVED_NOT_ADOPTED"}
    pages = []
    for page in discovery["pages"]:
        name = "page-" + page["id"].replace(":", "-")
        file = directory / (name + "-compact-response.json")
        if not file.exists(): file = directory / (name + "-response.json")
        result = payload(file)
        if result["page"]["id"] != page["id"] or result["fileKey"] != inventory["fileKey"]:
            raise Invalid("Page identity mismatch")
        pages.append(result)
    return inventory, pages, payload(directory / "styles-response.json")


def referenced_inventory(directory, inventory, pages):
    """Do not silently promote ID-readable records missing from local enumeration."""
    directory = Path(directory)
    rows = []
    for file in sorted(directory.glob("referenced-*-response.json")):
        if file.name == "referenced-collections-response.json": continue
        rows.extend(payload(file)["variables"])
    if not rows: return {"status": "NOT_RUN", "variables": [], "matrix": []}
    by_id = {v["id"]: v for v in rows}
    if len(rows) != len(by_id): raise Invalid("Duplicate referenced variable lookup")
    declared = {v["id"] for v in inventory["variables"]}
    expected = {identity for page in pages if page["page"]["name"] != "Descarte"
                for identity in page["variables"] if identity not in declared}
    discard = payload(directory / "discard-external-ids-response.json")
    discarded_counts = dict(discard["externalReferences"])
    expected.update(discarded_counts)
    if expected != set(by_id): raise Invalid("Referenced variable lookup coverage differs from bindings")
    collections = payload(directory / "referenced-collections-response.json")
    names = {c["id"]: c.get("name", "UNKNOWN") for c in collections["referencedCollections"]}
    declared_collections = {c["id"] for c in inventory["collections"]}
    known = {v["id"]: v for v in inventory["variables"]}
    known.update(by_id)
    alias_edges = [{"source": v["id"], "mode": mode, "target": value["id"],
                    "target_read": value["id"] in known}
                   for v in rows for mode, value in v.get("valuesByMode", {}).items()
                   if isinstance(value, dict) and value.get("type") == "VARIABLE_ALIAS"]
    matrix = []
    for identity, variable in sorted(by_id.items()):
        uses = [(p, p["variables"][identity]) for p in pages if p["page"]["name"] != "Descarte" and identity in p["variables"]]
        matrix.append({"original_id": identity, "original_key": variable.get("key"), "original_name": variable.get("name"),
                       "remote": variable.get("remote"), "collection_id": variable.get("variableCollectionId"),
                       "collection_name": names.get(variable.get("variableCollectionId"), "UNKNOWN"),
                       "classification": "REFERENCED_REMOTE" if variable.get("remote") else "READABLE_LOCAL_NOT_ENUMERATED",
                       "proposal": "QUARANTINE_EVIDENCE_RECONCILE_BEFORE_MIGRATION", "proposal_status": "PENDING_REVIEW",
                       "non_discard_direct_nodes": sum(row["nodeCount"] for _, row in uses),
                       "discard_binding_observations_not_unique_nodes": discarded_counts.get(identity, 0),
                       "pages": [p["page"] for p, _ in uses],
                       "samples": [{"page_id": p["page"]["id"], **s} for p, row in uses for s in row["samples"]],
                       "lookup_status": variable.get("status", "READABLE")})
    return {"status": "RECONCILIATION_REQUIRED", "total": len(rows),
            "local_not_enumerated": sum(v.get("remote") is False for v in rows),
            "remote": sum(v.get("remote") is True for v in rows),
            "readable": sum("status" not in v for v in rows),
            "additional_local_collections": [c for c in collections["referencedCollections"]
                if c.get("remote") is False and c["id"] not in declared_collections],
            "variables": rows, "collections": collections, "matrix": matrix, "alias_edges": alias_edges,
            "further_alias_targets_not_read": sorted({edge["target"] for edge in alias_edges if not edge["target_read"]}),
            "scope": "All IDs observed outside local enumeration across 53 pages; no imports, no inference of current publication or deletion state"}


def analyze(inventory, pages, styles=None):
    variables = {v["id"]: v for v in inventory["variables"]}
    collections = {c["id"]: c for c in inventory["collections"]}
    issues, alias_rows = [], []
    if len(variables) != len(inventory["variables"]): issues.append("Duplicate variable IDs")
    if len(collections) != len(inventory["collections"]): issues.append("Duplicate collection IDs")
    membership = [v for c in collections.values() for v in c["variableIds"]]
    if Counter(membership) != Counter(variables.keys()): issues.append("Collection membership does not match inventory")
    incoming = defaultdict(set)
    def alias(value): return isinstance(value, dict) and value.get("type") == "VARIABLE_ALIAS"
    for variable in variables.values():
        collection = collections.get(variable["variableCollectionId"])
        if not collection:
            issues.append("Missing collection: " + variable["id"]); continue
        modes = {m["modeId"] for m in collection["modes"]}
        if collection["defaultModeId"] not in modes or set(variable["valuesByMode"]) != modes:
            issues.append("Mode coverage: " + variable["id"])
        if variable["id"] not in collection["variableIds"]: issues.append("Wrong collection owner: " + variable["id"])
        for mode, value in variable["valuesByMode"].items():
            if alias(value):
                target = variables.get(value["id"])
                alias_rows.append({"source": variable["id"], "mode": mode, "target": value["id"]})
                incoming[value["id"]].add(variable["id"])
                if not target: issues.append("Unresolved alias: " + value["id"])
                elif target["resolvedType"] != variable["resolvedType"]: issues.append("Alias type mismatch: " + variable["id"])
            else:
                kind = variable["resolvedType"]
                valid = ((kind == "FLOAT" and type(value) in (int, float)) or
                         (kind == "STRING" and isinstance(value, str)) or
                         (kind == "BOOLEAN" and type(value) is bool) or
                         (kind == "COLOR" and isinstance(value, dict) and set(value) == {"r", "g", "b", "a"}
                          and all(type(x) in (int, float) and 0 <= x <= 1 for x in value.values())))
                if not valid: issues.append("Invalid literal: " + variable["id"])

    def resolve(identity, context, active=()):
        variable = variables[identity]; collection = collections[variable["variableCollectionId"]]
        mode = context.get(collection["id"], collection["defaultModeId"])
        state = (identity, mode)
        if state in active: raise Invalid("Observed alias cycle: " + identity)
        value = variable["valuesByMode"][mode]
        return resolve(value["id"], context, active + (state,)) if alias(value) else value

    # The observed source has one primitive mode and four semantic modes.
    # Enumerate the actual collection Cartesian product; do not infer mode equivalence by name.
    import itertools
    keys = sorted(collections)
    contexts = [dict(zip(keys, values)) for values in itertools.product(*[
        [m["modeId"] for m in collections[key]["modes"]] for key in keys])]
    resolved = {}
    for identity in variables:
        try: resolved[identity] = [resolve(identity, context) for context in contexts]
        except (Invalid, KeyError) as error: issues.append(str(error))
    by_alias, by_value = defaultdict(list), defaultdict(list)
    for identity, variable in variables.items():
        level = collections[variable["variableCollectionId"]]["name"]
        by_alias[(level, variable["resolvedType"], canonical(variable["valuesByMode"]))].append(identity)
        if identity in resolved:
            by_value[(level, variable["resolvedType"], canonical(resolved[identity]))].append(identity)
    groups = [{"ids": sorted(ids), "names": sorted(variables[i]["name"] for i in ids),
               "interpretation": ("Observed color aliases; normalize to one semantic per primitive with empty scopes."
                                  if variables[ids[0]]["resolvedType"] == "COLOR" else
                                  "Equal non-color aliases in every observed mode; not proof of equal intention")}
              for (level, _, _), ids in by_alias.items() if level == "semantic" and len(ids) > 1]
    groups.sort(key=lambda group: group["ids"])

    use = defaultdict(lambda: {"node_count": 0, "discard_node_count": 0, "references": 0, "pages": [], "samples": []})
    for page in pages:
        for identity, row in page["variables"].items():
            if identity not in variables: continue
            item = use[identity]; item["node_count"] += row["nodeCount"]
            item["references"] += row["references"]
            if page["page"]["name"] == "Descarte": item["discard_node_count"] += row["nodeCount"]
            item["pages"].append(page["page"])
            item["samples"].extend({"page_id": page["page"]["id"], **sample} for sample in row["samples"])
    matrix = []
    for identity, variable in sorted(variables.items()):
        reached, pending = set(), list(incoming[identity])
        while pending:
            item = pending.pop()
            if item not in reached: reached.add(item); pending.extend(incoming[item])
        direct = use[identity]
        affected_pages = {p["id"]: p for item in reached | {identity} for p in use[item]["pages"]}
        recommendations = ["RETAIN_SOURCE_EVIDENCE"]
        reason = "Observed source record; normalized correspondence is maintained separately."
        if variable["resolvedType"] == "COLOR" and collections[variable["variableCollectionId"]]["name"] == "semantic":
            recommendations.append("MAP_TO_UNIQUE_COLOR_SEMANTIC_WITH_EMPTY_SCOPES")
            reason = "One fixed semantic alias per primitive; property and state belong to future consumer tokens."
        if variable["name"] in {"size/md", "spacing/md", "font/size/1xs"} and collections[variable["variableCollectionId"]]["name"] == "semantic":
            recommendations.append("CORRECT_DESCRIPTION_ONLY_PENDING_APPROVAL")
            reason = "Description differs from observed resolved numeric value; preserve that value."
        if not variable["description"].strip(): recommendations.append("DOCUMENT_INTENTION_OR_DATA_KIND")
        if variable["name"] == "logo/categoria":
            recommendations.append("REVIEW_THEME_METADATA_OR_PRIMITIVE_STRING_REFERENCE")
        row = {"source_file_key": inventory["fileKey"], "original_id": identity, "original_key": variable["key"],
               "collection": collections[variable["variableCollectionId"]]["name"], "original_name": variable["name"],
               "normalization_reference": "auditoria/fase-1/variables-normalizadas.csv",
               "actions": recommendations, "rationale": reason,
               "direct_node_count": direct["node_count"], "discard_direct_nodes": direct["discard_node_count"],
               "direct_alias_consumer_ids": sorted(incoming[identity]), "transitive_alias_consumer_ids": sorted(reached),
               "potential_node_uses_upper_bound": sum(use[i]["node_count"] for i in reached | {identity}),
               "affected_pages": [affected_pages[p] for p in sorted(affected_pages)], "samples": direct["samples"],
               "sample_scope": "At most two identities per variable per page; complete local binding counts, not all node IDs",
               "source_selector": "JSON:/variables/" + str(next(j for j, v in enumerate(inventory["variables"]) if v["id"] == identity))}
        matrix.append(row)
    numeric_mismatches = []
    for identity, variable in variables.items():
        match = re.search(r"—\s*([0-9]+(?:\.[0-9]+)?)px", variable["description"])
        if match and identity in resolved and any(type(v) in (int, float) and v != float(match[1]) for v in resolved[identity]):
            numeric_mismatches.append({"id": identity, "name": variable["name"], "description": variable["description"], "resolved": resolved[identity]})
    page_errors = [{"page": p["page"], "errors": p["errors"]} for p in pages if p["errors"]]
    summary = {"status": "PASS_OBSERVED_SCOPE" if not issues and not page_errors else "BLOCKED",
               "file_key": inventory["fileKey"], "variables": len(variables), "collections": len(collections),
               "by_collection": dict(Counter(collections[v["variableCollectionId"]]["name"] for v in variables.values())),
               "by_type": dict(Counter(v["resolvedType"] for v in variables.values())), "mode_contexts": len(contexts),
               "alias_assignments": len(alias_rows), "unique_alias_targets": sum(bool(ids) for ids in incoming.values()),
               "pages_scanned": len(pages), "nodes_scanned": sum(p["nodeCount"] for p in pages),
               "text_nodes_scanned": sum(p["textNodes"] for p in pages),
               "variables_with_direct_bindings": sum(bool(use[i]["node_count"]) for i in variables),
               "variables_without_direct_bindings": sum(not use[i]["node_count"] for i in variables),
               "equal_alias_semantic_groups": len(groups), "empty_descriptions": sum(not v["description"].strip() for v in variables.values()),
               "code_syntax_defined": sum(bool(v["codeSyntax"]) for v in variables.values()),
               "numeric_description_mismatches": numeric_mismatches, "structural_issues": sorted(set(issues)), "page_errors": page_errors,
               "styles": {kind: len(items) for kind, items in (styles or {}).get("styles", {}).items()},
               "limitations": ["Observed local variables only; no complete external-library or downstream-file consumer census.",
                               "Bindings counted; identities sampled. Transitive node-use sums are upper bounds, not unique-node counts.",
                               "No visual, accessibility or interaction certification; no authority granted by this audit.",
                               "Remote styles, inherited presentation and arbitrary unbound literals are not fully resolved."]}
    return {"summary": summary, "inventory_canonical_sha256": sha(canonical(inventory)), "aliases": alias_rows,
            "equal_alias_groups": groups, "matrix": matrix}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path(__file__).resolve().parents[1] / "evidence/foundations")
    parser.add_argument("--view", choices=["summary", "analysis", "matrix-csv", "inventory", "referenced", "referenced-csv"], default="summary")
    args = parser.parse_args()
    try:
        inventory, pages, styles = assemble(args.input)
        result = analyze(inventory, pages, styles)
        referenced = referenced_inventory(args.input, inventory, pages)
        result["summary"]["referenced_record_reconciliation"] = {k: referenced[k] for k in
            ("status", "total", "local_not_enumerated", "remote", "readable") if k in referenced}
        if args.view in {"matrix-csv", "referenced-csv"}:
            columns = ["original_id", "original_key", "collection", "original_name", "normalization_reference", "actions",
                       "direct_node_count", "discard_direct_nodes", "direct_alias_consumer_ids", "transitive_alias_consumer_ids",
                       "potential_node_uses_upper_bound", "affected_pages", "samples", "rationale", "source_selector"]
            matrix = result["matrix"]
            if args.view == "referenced-csv":
                matrix = referenced["matrix"]
                columns = list(matrix[0]) if matrix else ["original_id", "lookup_status"]
            stream = io.StringIO(); writer = csv.DictWriter(stream, fieldnames=columns); writer.writeheader()
            for row in matrix:
                writer.writerow({key: json.dumps(row[key], ensure_ascii=False, sort_keys=True) if isinstance(row[key], (dict, list)) else row[key] for key in columns})
            print(stream.getvalue(), end="")
        else:
            value = inventory if args.view == "inventory" else referenced if args.view == "referenced" else result if args.view == "analysis" else result["summary"]
            print(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False))
        return 0 if result["summary"]["status"] == "PASS_OBSERVED_SCOPE" else 2
    except (Invalid, OSError, KeyError, ValueError, TypeError) as error:
        print(json.dumps({"status": "BLOCKED", "reason": str(error)}, ensure_ascii=False)); return 2


if __name__ == "__main__":
    raise SystemExit(main())
