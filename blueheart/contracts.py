"""One Markdown owner per contract; JSON frontmatter, exact requirement sections."""
import re
from .io import Invalid, loads, source


def parse(raw, schemas):
    text = raw.decode("utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise Invalid("Contract needs JSON frontmatter delimited by ---")
    header, body = text[4:].split("\n---\n", 1)
    meta = loads(header)
    if not isinstance(meta, dict) or meta.get("profile") not in {"foundation", "component", "pattern", "operational"}:
        raise Invalid("Unknown contract profile")
    schemas.validate(meta, meta["profile"] + ".schema.json")
    matches = list(re.finditer(r"^### (REQ-[A-Z0-9-]+)\s*$", body, re.M))
    if meta["profile"] == "operational" and (not matches or not re.fullmatch(r"# [^\n]+\s*", body[:matches[0].start()])):
        raise Invalid("Operational rules must live in requirement sections; only a title may precede them")
    statements = {}
    for index, match in enumerate(matches):
        identity = match[1]
        if identity in statements: raise Invalid("Duplicate requirement heading: " + identity)
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        statement = body[match.end():end].strip()
        if not statement: raise Invalid("Empty requirement statement: " + identity)
        statements[identity] = statement
    ids = [q["id"] for q in meta["requirements"]]
    if len(ids) != len(set(ids)) or set(ids) != set(statements):
        raise Invalid("Requirement metadata and Markdown sections must match exactly")
    return {"metadata": meta, "requirements": statements}


def validate(contract, root, decisions):
    meta = contract["metadata"]
    sources = {s.get("id"): s for s in meta["sources"]}
    if None in sources or len(sources) != len(meta["sources"]):
        raise Invalid("Contract sources need unique explicit IDs")
    for ref in sources.values(): source(root, ref)
    if set(meta["readiness"]) != set(meta["targets"]):
        raise Invalid("Readiness must cover exactly the declared targets")
    for requirement in meta["requirements"]:
        if set(requirement["sources"]) - set(sources):
            raise Invalid("Unresolved requirement provenance: " + requirement["id"])
        if meta["status"] == "ELIGIBLE" and requirement["provenance"] in {"UNRESOLVED", "CONFLICT"}:
            raise Invalid("Eligible contract has unresolved normative requirements")
    authority = meta["authority"]
    if meta["status"] == "ELIGIBLE":
        if authority["kind"] == "PROPOSED": raise Invalid("Proposed authority cannot enable a contract")
        decision = decisions.get(authority.get("decision_id"))
        if not decision or decision["status"] != "ADOPTED" or meta["id"] not in decision["scope"]:
            raise Invalid("Eligible contract needs a scoped adopted authority decision")
        if authority["kind"] == "APPROVED" and decision.get("actor") != "human_user":
            raise Invalid("APPROVED requires a human decision")
        for requirement in meta["requirements"]:
            if requirement["provenance"] == "INFERRED":
                adoption = decisions.get(requirement.get("decision_id"))
                if not adoption or adoption["status"] != "ADOPTED" or requirement["id"] not in adoption["scope"]:
                    raise Invalid("Inferred requirement needs explicit scoped adoption")


def closure(roots, edges):
    """Deterministic transitive closure; a cycle is a conflict, never partial success."""
    done, active, order = set(), set(), []
    def visit(identity):
        if identity in active: raise Invalid("Dependency cycle: " + identity)
        if identity in done: return
        if identity not in edges: raise Invalid("Missing dependency: " + identity)
        active.add(identity)
        for dependency in sorted(edges[identity]): visit(dependency)
        active.remove(identity); done.add(identity); order.append(identity)
    for identity in sorted(roots): visit(identity)
    return order
