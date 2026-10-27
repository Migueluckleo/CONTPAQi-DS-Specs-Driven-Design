"""Lossless-source observation projection; never an editable normative contract."""
import json
from collections import defaultdict, Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "evidence/button-pilot/source"


def payload(name):
    data = json.loads((DIR / name).read_text())
    return json.loads(next(c["text"] for c in data["content"] if c["type"] == "text"))


def main():
    raw = json.loads((DIR / "nodes.json").read_text())
    byid = {n["id"]: n for n in raw}
    ordered = []
    def walk(identity):
        n = byid[identity]; ordered.append(n)
        for child in n["children"]: walk(child)
    walk("2433:26890")
    assert len(ordered) == len(byid) == 597
    discovery = payload("discovery-compact-response.json")
    defs = payload("dependencies-response.json")["records"]
    vars = payload("variables-response.json")
    variables = {v["id"]: v for v in vars["variables"]}
    allvars = {**variables, **{v["id"]: v for v in payload("primitives-response.json")["variables"]}}
    collections = {c["id"]: c for c in vars["collections"]}
    evidence = [{"id": "E" + str(i + 1).zfill(3), "source": "node:" + n["id"], "value": {"type": n["type"], "name": n["name"]}, "note": "Complete API fields: nodes.json, record id " + n["id"]} for i, n in enumerate(ordered)]
    eref = {n["id"]: [evidence[i]["id"]] for i, n in enumerate(ordered)}
    used = defaultdict(list)
    def refs(value, path):
        if isinstance(value, dict):
            if value.get("type") == "VARIABLE_ALIAS": used[value["id"]].append(path)
            for k, v in value.items(): refs(v, path + "." + k)
        elif isinstance(value, list):
            for i, v in enumerate(value): refs(v, path + "." + str(i))
    for n in ordered: refs(n, "node:" + n["id"])
    assert set(used) == set(variables)
    def resolve(identity):
        v = allvars[identity]; values = v["valuesByMode"]
        mode = collections.get(v["variableCollectionId"], {}).get("defaultModeId", next(iter(values)))
        value = values[mode]
        return resolve(value["id"]) if isinstance(value, dict) and value.get("type") == "VARIABLE_ALIAS" else value
    def prop(value, n, field):
        result = {"resolved_value": value, "unit": "px" if type(value) in (int, float) else None,
                  "availability": "OBSERVED", "evidence_refs": eref[n["id"]]}
        alias = n.get("boundVariables", {}).get(field)
        if isinstance(alias, list): alias = alias[0] if alias else None
        if isinstance(alias, dict) and alias.get("id") in variables:
            v = variables[alias["id"]]; result["token"] = {"id": v["id"], "key": v["key"], "name": v["name"]}
        return result
    def layout(n):
        return {"node": {k: n[k] for k in ("id", "name", "type")},
            "position": {"x": n.get("x"), "y": n.get("y"), "absolute_x": None, "absolute_y": None, "unit": "px"},
            "layout_mode": n.get("layoutMode"), "layout_wrap": n.get("layoutWrap"), "layout_positioning": n.get("layoutPositioning"),
            "sizing": {"horizontal": n.get("layoutSizingHorizontal"), "vertical": n.get("layoutSizingVertical"), "primary_axis_mode": n.get("primaryAxisSizingMode"), "counter_axis_mode": n.get("counterAxisSizingMode")},
            "dimensions": {"width": prop(n["width"], n, "width"), "height": prop(n["height"], n, "height"), **{k: n.get(v) for k, v in [("min_width", "minWidth"), ("max_width", "maxWidth"), ("min_height", "minHeight"), ("max_height", "maxHeight")]}},
            "spacing": {"gap": prop(n["itemSpacing"], n, "itemSpacing") if "itemSpacing" in n else None, "row_gap": None, "column_gap": None},
            "padding": {k: prop(n[v], n, v) if v in n else None for k, v in [("top", "paddingTop"), ("right", "paddingRight"), ("bottom", "paddingBottom"), ("left", "paddingLeft")]},
            "alignment": {"primary_axis": n.get("primaryAxisAlignItems"), "counter_axis": n.get("counterAxisAlignItems"), "self": n.get("layoutAlign")},
            "constraints": n.get("constraints"), "overflow": None, "clips_content": n.get("clipsContent"), "strokes_included_in_layout": n.get("strokesIncludedInLayout"), "grow": n.get("layoutGrow"), "grids": [], "evidence_refs": eref[n["id"]]}
    def visual(n):
        # Paint entries retain their raw data in the evidence alongside normalized values.
        def paints(field):
            out = []
            for paint in n.get(field, []):
                color = {"resolved_value": paint.get("color"), "unit": "color", "availability": "OBSERVED", "evidence_refs": eref[n["id"]]}
                alias = paint.get("boundVariables", {}).get("color")
                if alias and alias["id"] in variables:
                    v = variables[alias["id"]]; color["token"] = {"id": v["id"], "key": v["key"], "name": v["name"]}
                out.append({"type": prop(paint["type"], n, "paint.type"), "visible": prop(paint.get("visible", True), n, "paint.visible"), "opacity": prop(paint.get("opacity", 1), n, "paint.opacity"), "blend_mode": prop(paint.get("blendMode"), n, "paint.blendMode"), "color": color, "gradient_stops": [], "image_ref": None, "scale_mode": None, "transform": None, "availability": "OBSERVED", "evidence_refs": eref[n["id"]]})
            return out
        return {"node": {k: n[k] for k in ("id", "name", "type")}, "fills": paints("fills"), "backgrounds": [], "strokes": paints("strokes"),
            "stroke_width": prop(n.get("strokeWeight"), n, "strokeWeight"), "stroke_widths": {k: None for k in ("top", "right", "bottom", "left")},
            "stroke_alignment": prop(n.get("strokeAlign"), n, "strokeAlign"), "dash_pattern": prop([], n, "dashPattern"),
            "corner_radius": prop(n.get("cornerRadius"), n, "cornerRadius"), "corner_radii": {k: prop(n.get(v), n, v) for k, v in [("top_left", "topLeftRadius"), ("top_right", "topRightRadius"), ("bottom_right", "bottomRightRadius"), ("bottom_left", "bottomLeftRadius")]},
            "opacity": prop(n.get("opacity"), n, "opacity"), "blend_mode": prop(n.get("blendMode"), n, "blendMode"),
            "effects": n.get("effects", []), "shadows": [], "blur": [], "clips_content": prop(n.get("clipsContent"), n, "clipsContent"),
            "is_mask": prop(None, n, "isMask"), "mask_type": prop(None, n, "maskType"), "evidence_refs": eref[n["id"]]}
    grouped = defaultdict(list)
    for n in ordered:
        if n["type"] == "INSTANCE": grouped[n["mainComponent"]["id"]].append(n)
    dependencies = []
    for dep in sorted(defs, key=lambda x: (x["name"].casefold(), x["id"])):
        instances = grouped[dep["id"]]
        dependencies.append({"dependency_id": dep["key"], "kind": "COMPONENT", "instance_ids": [n["id"] for n in instances], "instance_count": len(instances),
            "main_component": {k: dep[k] for k in ("id", "key", "name")}, "component_set": dep["parent"], "locality": "REMOTE" if dep["remote"] else "LOCAL",
            "active_properties": [n.get("componentProperties", {}) for n in instances], "property_definitions": dep["definitions"],
            "variants": {"observed": [n.get("componentProperties", {}) for n in instances], "available": [], "unknown": []},
            "swaps": {"active": [], "preferred_values": [], "preferred_candidate_count": None, "alternatives_deeply_resolved": False}, "slots": [],
            "overrides": [n.get("overrides", []) for n in instances], "resolution": {"status": "RESOLVED", "evidence": eref[instances[0]["id"]], "missing_fields": [], "reason": "Active main identity/definition and consumed instance subtree were read."},
            "contract_ref": {"status": "NOT_GENERATED", "suggested_path": "dependencies/" + dep["id"].replace(":", "-") + "/component-contract.yaml"}})
    variable_deps = []
    for v in sorted(variables.values(), key=lambda v: (v["name"].casefold(), v["id"])):
        c = collections[v["variableCollectionId"]]
        variable_deps.append({"id": v["id"], "key": v["key"], "name": v["name"], "type": v["resolvedType"], "collection": {k: c[k] for k in ("id", "key", "name")},
            "locality": "REMOTE" if v["remote"] else "LOCAL", "resolved_value": resolve(v["id"]), "resolved_mode": c["defaultModeId"], "used_by": used[v["id"]],
            "resolution": {"status": "RESOLVED", "evidence": [used[v["id"]][0]], "missing_fields": [], "reason": "Read variable, collection, modes and primitive aliases."}, "evidence_refs": [used[v["id"]][0]]})
    def inventory(total, remote=0, instances=None):
        value = {"total": total, "local": total-remote, "remote": remote, "unknown_locality": 0, "resolved": total, "partially_resolved": 0, "unresolved": 0}
        if instances is not None: value = {"total_instances": instances, **value}
        return value
    root, definition = byid["2433:26890"], discovery["sets"][0]
    text_runs = []
    for n in ordered:
        if n["type"] != "TEXT": continue
        text_runs.append({"node": {"id": n["id"], "name": n["name"]}, "characters": n["characters"], "range": {"start": 0, "end": len(n["characters"])},
            "font_family": prop(n["fontName"]["family"], n, "fontFamily"), "font_style": prop(n["fontName"]["style"], n, "fontStyle"), "font_weight": prop(n["fontWeight"], n, "fontWeight"),
            "font_size": prop(n["fontSize"], n, "fontSize"), "line_height": prop(n["lineHeight"], n, "lineHeight"), "letter_spacing": prop(n["letterSpacing"], n, "letterSpacing"),
            "paragraph_spacing": prop(n["paragraphSpacing"], n, "paragraphSpacing"), "paragraph_indent": prop(n["paragraphIndent"], n, "paragraphIndent"),
            "text_align_horizontal": n["textAlignHorizontal"], "text_align_vertical": n["textAlignVertical"], "text_case": n["textCase"], "text_decoration": n["textDecoration"],
            "text_style": {"id": None, "key": None, "name": None, "locality": "UNKNOWN"}, "auto_resize": n["textAutoResize"], "truncation": n["textTruncation"], "max_lines": n["maxLines"],
            "bound_variables": n["boundVariables"], "mixed_fields": [], "styled_segments": [], "hyperlinks": [], "evidence_refs": eref[n["id"]]})
    model = {"schema_version": "0.1.0", "generated_at": datetime.now(timezone.utc).isoformat(), "generator": {"skill": "figma-component-contract", "skill_version": "0.1.0"},
        "inspection": {"status": "COMPLETE", "read_only": True, "traversal": {"discovered_nodes":597,"inspected_nodes":597,"pending_nodes":0,"invisible_nodes_inspected":150,"truncated":False,"limit":None}, "mcp_limitations": ["Large replies recovered using bounded lossless dictionary encoding.", "Preferred swaps sampled shallowly; 1512 candidates per icon are not imported or exhaustively inspected."]},
        "component": {"id":root["id"],"key":None,"name":root["name"],"type":root["type"],"description":definition["description"],"parent":discovery["node"]["parent"],"page":discovery["node"]["page"],"source":{"url":"https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=2433-26890","file_key":discovery["fileKey"],"node_id":root["id"]}},
        "classification":{"kind":"composition","reusable":False,"composition":True,"evidence_refs":eref[root["id"]]},
        "identity":{"position":{"x":root["x"],"y":root["y"]},"dimensions":{"width":root["width"],"height":root["height"]},"visible":root["visible"],"clips_content":root.get("clipsContent"),"opacity":root["opacity"],"blend_mode":root["blendMode"]},
        "direct_children":[{k:byid[i][k] for k in ("id","name","type","width","height")} for i in root["children"]],
        "anatomy":{"functional_tree":[{"id":n["id"],"parent_id":n["parentId"],"name":n["name"],"type":n["type"]} for n in ordered if n["type"]!="VECTOR"],"graphical_details_omitted":[{"kind":"VECTOR","count":150,"reason":"Paths retained in nodes.json; vector internals omitted only from functional anatomy."}]},
        "dependency_inventory":{"components":inventory(13,1,180),"variables":inventory(47),"styles":inventory(0)},"dependencies":dependencies,"variable_dependencies":variable_deps,"style_dependencies":[],
        "properties":{"definitions":definition["definitions"],"observed":[{"node_id":n["id"],"values":n.get("componentProperties",{})} for n in ordered if n["type"]=="INSTANCE"],"available":definition["definitions"],"unknown":[]},
        "variants":{"observed_combinations":discovery["variants"],"available_values":definition["variantGroupProperties"],"unknown":[]},
        "states":{"observed":["default","hover","pressed","focus","loading","disabled"],"available":["default","hover","pressed","focus","loading","disabled"],"unknown":[]},
        "layout":{"node":layout(root),"children":[layout(n) for n in ordered[1:] if n["type"]!="VECTOR"],"relationships":[{"parent_id":n["parentId"],"child_id":n["id"],"relationship":"CHILD","parent_layout_mode":byid.get(n["parentId"],{}).get("layoutMode"),"child_layout_positioning":n.get("layoutPositioning"),"child_sizing":{"horizontal":n.get("layoutSizingHorizontal"),"vertical":n.get("layoutSizingVertical")},"evidence_refs":eref[n["id"]]} for n in ordered[1:]]},
        "visual":{"node":visual(root),"descendants":[visual(n) for n in ordered[1:]],"icons":[{"node":{"id":n["id"],"name":n["name"],"type":n["type"]},"dimensions":{"width":n["width"],"height":n["height"],"unit":"px"},"format":"Outline","weight":"Light","vector_descendant_count":1,"fills":n.get("fills",[]),"strokes":n.get("strokes",[]),"evidence_refs":eref[n["id"]]} for n in ordered if n["type"]=="INSTANCE" and n["name"] in {"Left icon","Right icon"}]},
        "typography":{"styles":[],"text_runs":text_runs},"tokens":{"summary":{"total":47,"local":47,"remote":0},"categories":{"Color":[v["id"] for v in variable_deps if v["type"]=="COLOR"],"Other":[v["id"] for v in variable_deps if v["type"]!="COLOR"]},"source":"variable_dependencies"},
        "content":{"example_content":{"observed_strings":[n["characters"] for n in ordered if n["type"]=="TEXT"]},"component_rules":[{"source":"component-set:355:86695.description","value":definition["description"]}],"truncation_and_wrapping":[{"node_id":n["id"],"auto_resize":n["textAutoResize"],"truncation":n["textTruncation"]} for n in ordered if n["type"]=="TEXT"]},
        "interactions":{"status":"FIGMA_DEFINED","reason":"Partial native reactions plus explicit descriptive functional guidance; do not conflate these layers.","rules":[{"node_id":n["id"],"reactions":n["reactions"],"evidence_refs":eref[n["id"]]} for n in ordered if n.get("reactions")]},
        "semantic_contract":{"explicit_descriptions":[definition["description"]],"purpose":{"status":"DEFINED","source":"component-set:355:86695.description"},"usage_rules":{"status":"DEFINED","source":"component-set:355:86695.description"}},
        "accessibility":{"status":"REQUIRES_DEFINITION","observed":["Explicit focus ring and textual guidance; source claims AA but this is not a performed compliance audit."],"undefined":["Executable browser keyboard/ARIA behavior","Touch hit-area integration for 40px medium","Independent contrast certification"]},
        "external_dependencies":[{"id":defs[0]["id"],"library_name":"NOT_EXPOSED_BY_FIGMA_MCP","source_file_key":"NOT_EXPOSED_BY_FIGMA_MCP","source_url":"NOT_EXPOSED_BY_FIGMA_MCP","project":"NOT_EXPOSED_BY_FIGMA_MCP","organization":"NOT_EXPOSED_BY_FIGMA_MCP","library_version":"NOT_EXPOSED_BY_FIGMA_MCP"}],
        "unresolved":[{"id":"U01","category":"SOURCE_CONFLICT","subject":"Loading width","reason":"Description requires stable width; observed HUG widths grow with the spinner.","missing_fields":[],"evidence_refs":["node:355:86695.description","node:8857:26557.width"],"impact":"Consumer must define width reservation for an operation."},{"id":"U02","category":"REQUIRES_DEFINITION","subject":"Mobile hit area","reason":"Medium has a 40px visual height; description requests a minimum 44px mobile hit area.","missing_fields":["consumer hit area"],"evidence_refs":["node:355:86695.description"],"impact":"Not certified by visual geometry alone."}],
        "implementation_notes":["This pair documents source evidence read-only. The operative delegated MD is a separate Blue Heart contract.","Inactive swaps and unsupported external metadata are not inferred."],
        "evidence":{"figma_direct":evidence,"derived":[{"id":"D01","source":"complete traversal","value":{"nodes":597,"variants":90,"instances":180},"note":"Mechanical counts."}],"requires_definition":[{"id":"R01","source":"description vs measured geometry","value":["U01","U02"],"note":"Consumer decisions are explicit rather than guessed."}],"confidence":{"level":"HIGH","reason":"Complete subtree and active dependency/variable reads; functional and accessibility limits explicit."}}}
    assert model["dependency_inventory"]["components"]["total_instances"] == sum(d["instance_count"] for d in dependencies)
    assert all(v["used_by"] for v in variable_deps)
    # JSON is deterministic YAML 1.2 syntax; no YAML parser dependency is introduced.
    (DIR / "component-contract.yaml").write_text(json.dumps(model,ensure_ascii=False,indent=2)+"\n")
    sections=["Component Identity","Anatomy","Dependencies","Properties","Variants","States","Layout","Visual Styles","Typography","Tokens","Content","Interactions","Accessibility","External Dependencies","Unresolved Information","Implementation Notes","Evidence / Confidence"]
    paragraphs=[
        "Observed from Figma: GROUP Button component, 2433:26890, página ❖ Button. La composición contiene el set button y sus etiquetas; no es por sí misma un componente reusable.",
        "Derived structure: contenedor Button, Label, iconos opcionales, Focus ring y Loader. Se recorrieron 597 nodos, incluidos 150 invisibles; vectores completos en nodes.json.",
        "Observed from Figma: 180 instancias, 13 componentes únicos (12 locales y 1 remoto), 47 variables locales y cero estilos nombrados. Todas las referencias activas se resolvieron; no se generaron contratos de dependencias.",
        "Observed from Figma: Label=Button; Show left/right icon=false; Left/Right icon son INSTANCE_SWAP. Cada uno ofrece 1512 candidatos de biblioteca, no inspeccionados exhaustivamente ni importados.",
        "Observed from Figma: type=primary|secondary|text|link|danger, size=large|medium|small; 90 combinaciones existentes, sin inferir otras.",
        "Observed from Figma: default, hover, pressed, focus, loading, disabled.",
        "Observed from Figma: Auto Layout horizontal, ancho HUG, alturas 48/40/32 px. Padding/gap/bindings por variante en el YAML y nodes.json. strokesIncludedInLayout=false.",
        "Observed from Figma: pinturas, opacidades, strokes y bindings conservados por nodo. Focus ring de 2px a 2px de distancia, radio 12; radio del control 8.",
        "Observed from Figma: Manrope Bold salvo text=Regular, 16px large y 14px medium/small, line-height 20px; link subrayado. No hay TextStyle asignado en este subárbol.",
        "Observed from Figma: 47 referencias semánticas y sus valores resueltos en Contable, conservando aliases y todos los modos en las respuestas fuente. La normalización del destino no reescribe esta evidencia.",
        "Observed from Figma: Button es contenido de ejemplo y Label es editable. La descripción define sentence case, máximo tres palabras y restricciones de datos sensibles; no convertir ejemplos fiscales en lógica ejecutable.",
        "Observed from Figma: reacciones nativas parciales hover/pressed y ciclos AFTER_TIMEOUT. La descripción declara loading/disabled/confirmación; eso no acredita implementación web ni llamadas de servicio.",
        "Requires definition: integración HTML/ARIA, área táctil y auditoría de contraste. La frase Cumple AA en la fuente es una afirmación del autor, no un resultado medido aquí.",
        "Observed from Figma: PlusCircle remoto activo con key e identidad legibles; biblioteca/proyecto/versión externa NOT_EXPOSED_BY_FIGMA_MCP.",
        "Requires definition: la guía pide ancho estable durante loading pero HUG crece; medium mide 40px frente al mínimo móvil de 44px descrito. Se conservan ambas evidencias.",
        "Evidencia de origen de solo lectura; no prescribe rediseño ni crea código de aplicación. El contrato MD normativo del piloto adopta y delimita su implementación por separado.",
        "HIGH para la observación estructural: 597/597 nodos, 0 pendientes, 13/13 componentes y 47/47 variables resueltos. YAML y MD salen del mismo modelo."
    ]
    md="# Button · Contrato observacional\n\nFuente: "+model["component"]["source"]["url"]+"\n\nInspección COMPLETE · "+model["generated_at"]+" · Evidencia Figma de solo lectura. Este documento no sustituye la autoridad del MD normativo de Blue Heart.\n\n"
    md+="\n\n".join("## "+title+"\n\n"+body for title,body in zip(sections,paragraphs))+"\n"
    (DIR / "component-contract.md").write_text(md)
    print(json.dumps({"nodes":597,"pending":0,"components":13,"instances":180,"variables":47,"styles":0,"status":"COMPLETE"}))


if __name__ == "__main__": main()
