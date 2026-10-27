"""Generate the Button pilot recipes and token map from preserved read-only evidence."""
import json
import hashlib
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "evidence/button-pilot/source"
MODES = ["Contable", "Administrativo", "Servicios", "Personas"]


def read(path):
    return json.loads((ROOT / path).read_text())


def payload(name):
    reply = json.loads((SOURCE / name).read_text())
    if reply.get("isError"):
        raise ValueError(name)
    return json.loads(next(c["text"] for c in reply["content"] if c["type"] == "text"))


def save(path, value):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def consolidate(tokens, recipes):
    """One token per type, exact property scope and four-mode alias vector.

    Never merge by RGB, today's theme, or numeric coincidence. Recipes retain
    the mapping of component type/state/part to the shared property token.
    """
    anchors = {
        "color-button-danger-bg": "color-button-danger-bg-default",
        "color-button-bg-disabled": "color-button-primary-bg-disabled",
        "color-button-danger-bg-hover": "color-button-danger-bg-hover",
        "color-button-danger-bg-pressed": "color-button-danger-bg-pressed",
        "color-button-icon-inverse": "color-button-primary-icon-default",
        "color-button-icon-disabled": "color-button-primary-icon-disabled",
        "color-button-loader-inverse": "color-button-primary-loader-stroke-loading",
        "color-button-text-inverse": "color-button-primary-text-default",
        "color-button-text-disabled": "color-button-primary-text-disabled",
        "color-button-focus-stroke": "color-button-focus-stroke",
        "color-button-bg-soft": "color-button-secondary-bg-hover",
        "color-button-icon-brand": "color-button-secondary-icon-default",
        "color-button-icon-brand-hover": "color-button-secondary-icon-hover",
        "color-button-stroke-brand": "color-button-secondary-stroke-default",
        "color-button-text-brand": "color-button-secondary-text-default",
        "color-button-text-brand-emphasis": "color-button-secondary-text-hover",
        "color-button-primary-bg": "color-button-primary-bg-default",
        "color-button-primary-bg-hover": "color-button-primary-bg-hover",
        "color-button-primary-bg-pressed": "color-button-primary-bg-pressed",
        "color-button-bg-surface": "color-button-secondary-bg-default",
        "color-button-bg-accent": "color-button-secondary-bg-pressed",
        "color-button-stroke-disabled": "color-button-secondary-stroke-disabled",
        "color-button-stroke-brand-emphasis": "color-button-secondary-stroke-hover",
        "color-button-icon-neutral": "color-button-text-icon-default",
        "color-button-loader-neutral": "color-button-text-loader-stroke-loading",
        "color-button-text-neutral": "color-button-text-text-default",
        "font-button-label-family": "font-button-label-family",
        "font-button-label-letter-spacing": "font-button-label-letter-spacing",
        "font-button-label-line-height": "font-button-label-line-height",
        "font-button-label-style": "font-button-label-style",
        "font-button-large-label-size": "font-button-large-label-size",
        "font-button-compact-label-size": "font-button-medium-label-size",
        "font-button-text-label-style": "font-button-text-label-style",
        "radius-button-container": "radius-button-container",
        "radius-button-focus": "radius-button-focus",
        "size-button-large-height": "size-button-large-height",
        "size-button-large-content": "size-button-large-icon",
        "size-button-medium-height": "size-button-medium-height",
        "size-button-medium-content": "size-button-medium-icon",
        "size-button-small-height": "size-button-small-height",
        "size-button-small-content": "size-button-small-icon",
        "spacing-button-sm": "spacing-button-large-gap",
        "spacing-button-xs": "spacing-button-link-large-padding-x",
        "spacing-button-lg": "spacing-button-standard-large-padding-x",
        "spacing-button-md": "spacing-button-standard-small-padding-x",
        "stroke-button-border-width": "stroke-button-border-width",
        "stroke-button-emphasis-width": "stroke-button-focus-width",
    }
    def signature(t):
        return (t["type"], tuple(sorted(t["scopes"])), tuple(sorted(t["aliases"].items())))
    groups = defaultdict(list)
    for name, t in tokens.items(): groups[signature(t)].append(name)
    chosen = {signature(tokens[old]): (new, old) for new, old in anchors.items()}
    assert len(chosen) == len(anchors) == len(groups) == 47
    assert set(chosen) == set(groups)
    replacements, reduced = {}, {}
    for sig, names in groups.items():
        new, old = chosen[sig]
        reduced[new] = {**tokens[old], "name": new, "sourceVariableIds": sorted({tokens[n]["sourceVariableId"] for n in names}), "replaces": sorted(names), "retainedFrom": old}
        replacements.update({n: new for n in names})
    def replace(value):
        if isinstance(value, str): return replacements.get(value, value)
        if isinstance(value, list): return [replace(v) for v in value]
        if isinstance(value, dict): return {k: replace(v) for k, v in value.items()}
        return value
    return reduced, replace(recipes), replacements


def generate():
    captured = []
    for file in sorted(SOURCE.glob("variants-???-response.json")) + [SOURCE / "container-response.json", SOURCE / "component-set-response.json"]:
        table = payload(file.name)
        assert not table["errors"]
        captured.extend({field: table["values"][row[i]] for i, field in enumerate(table["fields"]) if row[i] != -1} for row in table["rows"])
    assert len(captured) == len({n["id"] for n in captured}) == 597
    layout_flags = {n["id"]: n for n in payload("stroke-layout-response.json")["variants"]}
    for node in captured:
        if node["id"] in layout_flags:
            node.update({k: v for k, v in layout_flags[node["id"]].items() if k != "id"})
    save("evidence/button-pilot/source/nodes.json", captured)
    nodes = read("evidence/button-pilot/source/nodes.json")
    byid = {n["id"]: n for n in nodes}
    variables = {v["id"]: v for v in payload("variables-response.json")["variables"]}
    primitives = {v["id"]: v for v in payload("primitives-response.json")["variables"]}
    all_variables = {**primitives, **variables}
    mode_ids = {m["name"]: m["modeId"] for m in payload("variables-response.json")["collections"][0]["modes"]}
    baseline = read("evidence/figma-application/plan.json")
    primitive_plan, semantic_plan = [c["variables"] for c in baseline["collections"]]
    dest_map = read("evidence/figma-application/application-map.json")["variables"]
    target_names = {(x["layer"], x["name"]): x for x in dest_map}
    p_by_source = {p["sourceIds"][0]: p for p in primitive_plan}
    s_by_primitive = {s["aliasName"]: s for s in semantic_plan if s["type"] == "COLOR"}
    s_by_source = {i: s for s in semantic_plan if s["type"] != "COLOR" for i in s["sourceIds"]}
    tokens = {}

    def resolved(identity, mode):
        v = all_variables[identity]
        values = v["valuesByMode"]
        value = values[mode_ids[mode]] if mode_ids[mode] in values else next(iter(values.values()))
        if isinstance(value, dict) and value.get("type") == "VARIABLE_ALIAS":
            return resolved(value["id"], mode)
        return value

    def aliases(identity):
        v = variables[identity]
        if v["resolvedType"] != "COLOR":
            return {mode: s_by_source[identity]["name"] for mode in MODES}
        result = {}
        for mode in MODES:
            primitive_id = v["valuesByMode"][mode_ids[mode]]["id"]
            result[mode] = s_by_primitive[p_by_source[primitive_id]["name"]]["name"]
        return result

    def token(name, identity, scope):
        value = {"name": name, "type": variables[identity]["resolvedType"], "scopes": [scope],
                 "aliases": aliases(identity), "sourceVariableId": identity}
        if name in tokens:
            assert tokens[name] == value, (name, tokens[name], value)
        tokens[name] = value
        return name

    # Source typography and geometry are retained; only their variable references change.
    recipes = []
    for n in nodes:
        if n["type"] != "COMPONENT":
            continue
        kind, size, state = [n["variantProperties"][k] for k in ("type", "size", "state")]
        children = [byid[i] for i in n["children"]]
        label = next(c for c in children if c["type"] == "TEXT")
        recipe = {"sourceId": n["id"], "type": kind, "size": size, "state": state,
                  "sourceWidth": n["width"], "height": n["height"],
                  "padding": [n[k] for k in ("paddingTop", "paddingRight", "paddingBottom", "paddingLeft")],
                  "gap": n["itemSpacing"], "radius": n["cornerRadius"], "strokeWeight": n["strokeWeight"],
                  "strokesIncludedInLayout": n["strokesIncludedInLayout"],
                  "bindings": {}, "paints": {}, "label": {k: label[k] for k in
                  ("characters", "fontName", "fontSize", "lineHeight", "letterSpacing", "textDecoration", "width", "height")},
                  "labelBindings": {}, "reactions": n["reactions"], "icons": [], "focus": None, "loader": None}
        for field, scope, label_name in [("paddingTop", "GAP", "padding-y"), ("paddingBottom", "GAP", "padding-y"),
                                         ("paddingLeft", "GAP", "padding-x"), ("paddingRight", "GAP", "padding-x"),
                                         ("itemSpacing", "GAP", "gap"), ("height", "WIDTH_HEIGHT", "height"),
                                         ("topLeftRadius", "CORNER_RADIUS", "radius"), ("topRightRadius", "CORNER_RADIUS", "radius"),
                                         ("bottomLeftRadius", "CORNER_RADIUS", "radius"), ("bottomRightRadius", "CORNER_RADIUS", "radius")]:
            alias = n.get("boundVariables", {}).get(field)
            if alias:
                # text/link use different horizontal padding; preserve each actual recipe.
                padding_kind = kind if kind in {"text", "link"} else "standard"
                name = ("radius-button-container" if label_name == "radius" else
                        "size-button-" + size + "-height" if label_name == "height" else
                        "spacing-button-" + padding_kind + "-" + size + "-padding-x" if label_name == "padding-x" else
                        "spacing-button-" + size + "-" + label_name)
                recipe["bindings"][field] = token(name, alias["id"], scope)
        for field, part, scope in [("fills", "bg", "FRAME_FILL"), ("strokes", "stroke", "STROKE_COLOR")]:
            paints = n[field]
            if paints:
                identity = paints[0]["boundVariables"]["color"]["id"]
                recipe["paints"][field] = token("color-button-" + kind + "-" + part + "-" + state, identity, scope)
                if field == "strokes":
                    recipe["bindings"]["strokeWeight"] = token("stroke-button-border-width", "VariableID:559:7", "STROKE_FLOAT")
        recipe["labelBindings"]["fills"] = token("color-button-" + kind + "-text-" + state,
                                                  label["fills"][0]["boundVariables"]["color"]["id"], "TEXT_FILL")
        for field, scope, suffix in [("fontFamily", "FONT_FAMILY", "family"), ("fontStyle", "FONT_STYLE", "style"),
                                      ("fontSize", "FONT_SIZE", "size"), ("lineHeight", "LINE_HEIGHT", "line-height"),
                                      ("letterSpacing", "LETTER_SPACING", "letter-spacing")]:
            alias = label["boundVariables"].get(field)
            if isinstance(alias, list): alias = alias[0]
            if alias:
                name = ("font-button-" + size + "-label-size" if field == "fontSize" else
                        "font-button-text-label-style" if field == "fontStyle" and kind == "text" else
                        "font-button-label-" + suffix)
                recipe["labelBindings"][field] = token(name, alias["id"], scope)
        for child in children:
            if child["name"] in {"Left icon", "Right icon"}:
                vector = byid[child["children"][0]]
                alias = vector["fills"][0]["boundVariables"]["color"]["id"]
                dimensions = child["boundVariables"]["width"]["id"]
                recipe["icons"].append({"side": "left" if child["name"] == "Left icon" else "right", "visible": child["visible"],
                    "size": child["width"], "colorToken": token("color-button-" + kind + "-icon-" + state, alias, "SHAPE_FILL"),
                    "sizeToken": token("size-button-" + size + "-icon", dimensions, "WIDTH_HEIGHT")})
            if child["name"] == "Focus ring":
                recipe["focus"] = {k: child[k] for k in ("x", "y", "width", "height", "cornerRadius", "strokeWeight")}
                recipe["focus"].update(colorToken=token("color-button-focus-stroke", child["strokes"][0]["boundVariables"]["color"]["id"], "STROKE_COLOR"),
                    radiusToken=token("radius-button-focus", "VariableID:562:5", "CORNER_RADIUS"),
                    widthToken=token("stroke-button-focus-width", "VariableID:559:9", "STROKE_FLOAT"))
            if state == "loading" and child["type"] == "INSTANCE":
                descendants = []
                def visit(x):
                    descendants.append(x)
                    for i in x["children"]: visit(byid[i])
                visit(child)
                track = next(x for x in descendants if x["name"] == "Track")
                arc = next(x for x in descendants if x["name"] == "Arc")
                identity = arc["strokes"][0]["boundVariables"]["color"]["id"]
                size_id = {"large": "VariableID:562:20", "medium": "VariableID:8871:11", "small": "VariableID:562:19"}[size]
                recipe["loader"] = {"size": child["width"], "trackOpacity": track["opacity"],
                    "trackPaintOpacity": track["strokes"][0].get("opacity", 1), "arcOpacity": arc["opacity"],
                    "arcPaintOpacity": arc["strokes"][0].get("opacity", 1), "strokeWeight": arc["strokeWeight"],
                    "colorToken": token("color-button-" + kind + "-loader-stroke-loading", identity, "STROKE_COLOR"),
                    "sizeToken": token("size-button-" + size + "-loader", size_id, "WIDTH_HEIGHT"),
                    "widthToken": token("stroke-button-loader-width", "VariableID:559:9", "STROKE_FLOAT")}
        recipes.append(recipe)
    assert len(recipes) == 90 and len(byid) == 597
    tokens, recipes, replacements = consolidate(tokens, recipes)
    for t in tokens.values():
        assert all(("semantic", alias) in target_names for alias in t["aliases"].values())
    plan = {"id": "BUTTON-001", "version": "2.0.0", "sourceFileKey": "9zs5RMR8LB5wHjW9Bd59BA",
            "sourceNodeId": "2433:26890", "destinationFileKey": "98xEw6sK8FRVNEhopM5SSz", "pageName": "Buttons",
            "modes": MODES, "tokens": sorted(tokens.values(), key=lambda t: t["name"]), "variants": recipes,
            "tokenMigration": replacements,
            "icon": payload("helper-discovery-response.json")["icon"],
            "spinnerFrames": payload("spinner-frames-compact-response.json")["frames"],
            "sourceNodesSha256": digest("evidence/button-pilot/source/nodes.json"),
            "sourceVariablesSha256": digest("evidence/button-pilot/source/variables-response.json"),
            "implementationDecisions": {"variantSets": "Five sets by type, 18 variants each; type is selected by set, preserving all 90 observed combinations.",
                "loadingWidth": "Keep source HUG geometry; document stable-width requirement as consumer responsibility, not as an implemented web guarantee.",
                "scope": "Figma and contract/consumption only; React implementation and service-backed actions are outside this pilot."}}
    save("evidence/button-pilot/build-plan.json", plan)
    save("evidence/button-pilot/source/variables.json", payload("variables-response.json"))
    original = read("evidence/foundations/observed-inventory.json")
    original_indices = {v["id"]: i for i, v in enumerate(original["variables"])}
    variable_list = payload("variables-response.json")["variables"]
    variable_indices = {v["id"]: i for i, v in enumerate(variable_list)}
    portable = []
    type_map = {"FLOAT": "number", "COLOR": "color", "STRING": "string", "BOOLEAN": "boolean"}
    for layer, entries in [("primitive", primitive_plan), ("semantic", semantic_plan)]:
        for entry in entries:
            identity = layer + "." + entry["name"]
            source_id = (entry["sourceIds"][0] if layer == "primitive" or entry["type"] != "COLOR" else
                         next(p["sourceIds"][0] for p in primitive_plan if p["name"] == entry["aliasName"]))
            portable.append({"id": identity, "name": "--primitive-" + entry["name"] if layer == "primitive" else "--" + entry["name"],
                "layer": layer, "type": type_map[entry["type"]], "collection": layer, "scopes": [],
                "description": ("Primitiva normalizada " if layer == "primitive" else "Semántico compartido ") + entry["name"],
                "values": {"Value": entry["value"] if layer == "primitive" else {"alias": "primitive." + entry["aliasName"]}},
                "source": {"path": "evidence/foundations/observed-inventory.json", "sha256": digest("evidence/foundations/observed-inventory.json"),
                           "original_id": source_id, "selector": "JSON:/variables/" + str(original_indices[source_id]),
                           "source_file_key": "9zs5RMR8LB5wHjW9Bd59BA"}})
    for entry in plan["tokens"]:
        source_id = entry["sourceVariableId"]
        portable.append({"id": "button." + entry["name"], "name": "--" + entry["name"], "layer": "component",
            "type": type_map[entry["type"]], "collection": "button", "scopes": entry["scopes"],
            "description": "Token de Button para " + entry["name"].replace("-", " "),
            "values": {mode: {"alias": "semantic." + alias} for mode, alias in entry["aliases"].items()},
            "source": {"path": "evidence/button-pilot/source/variables.json", "sha256": digest("evidence/button-pilot/source/variables.json"),
                       "original_id": source_id, "selector": "JSON:/variables/" + str(variable_indices[source_id]),
                       "source_file_key": "9zs5RMR8LB5wHjW9Bd59BA"}})
    save("norms/tokens/blueheart.2.0.0.json", {"schema_version": 1, "id": "BLUEHEART-TOKENS", "version": "2.0.0",
        "collections": [{"id": layer, "name": layer, "default_mode": "Value", "modes": [{"id": "Value", "name": "Value"}]} for layer in ("primitive", "semantic")] +
                       [{"id": "button", "name": "component", "default_mode": MODES[0], "modes": [{"id": m, "name": m} for m in MODES]}],
        "tokens": portable})
    print(json.dumps({"variants": len(recipes), "componentTokens": len(tokens), "spinnerFrames": len(plan["spinnerFrames"]),
                      "allAliasesResolveToExistingSemantics": True}))


if __name__ == "__main__":
    generate()
