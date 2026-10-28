"""Portable identities and explicit mode contexts. No color/unit conversions or writes."""
import itertools
import math
from .io import Invalid, canonical, source


class Tokens:
    def __init__(self, documents, root, policy):
        self.policy = policy
        self.tokens, self.collections, self.source_sets = {}, {}, {}
        names = set()
        for document in documents:
            for collection in document["collections"]:
                identity = collection["id"]
                if identity in self.collections: raise Invalid("Duplicate collection ID: " + identity)
                modes = [m["id"] for m in collection["modes"]]
                if len(modes) != len(set(modes)) or collection["default_mode"] not in modes:
                    raise Invalid("Duplicate or missing default mode: " + identity)
                self.collections[identity] = collection
            for token in document["tokens"]:
                identity = token["id"]
                if identity in self.tokens or token["name"] in names:
                    raise Invalid("Duplicate token ID or name: " + identity)
                if token["layer"] not in policy["allowed_token_layers"]:
                    raise Invalid("Token layer is forbidden in this phase: " + token["layer"])
                source(root, token["source"])
                self.tokens[identity] = token; names.add(token["name"])
                self.source_sets[identity] = document["id"] + "@" + document["version"]

    def mode(self, token, context):
        collection = self.collections.get(token["collection"])
        if not collection: raise Invalid("Unresolved collection: " + token["collection"])
        selected = context.get(collection["id"], collection["default_mode"])
        if selected not in {m["id"] for m in collection["modes"]}:
            raise Invalid("Unknown mode: " + str(selected))
        return selected

    def resolve(self, identity, context=None):
        context = dict(context or {})
        for collection, selected in context.items():
            if collection not in self.collections or selected not in {m["id"] for m in self.collections[collection]["modes"]}:
                raise Invalid("Invalid mode context")
        def visit(key, active, explicit_mode=None):
            if key not in self.tokens: raise Invalid("Unresolved alias/token: " + key)
            token = self.tokens[key]
            selected = explicit_mode if explicit_mode is not None else self.mode(token, context)
            if selected not in token["values"]: raise Invalid("Missing token mode: " + key)
            state = (key, selected)
            if state in active: raise Invalid("Token alias cycle: " + key)
            value = token["values"][selected]
            trace = {"id": key, "mode": selected, "collection": token["collection"],
                     "mode_selection": "alias-explicit" if explicit_mode is not None else "context" if token["collection"] in context else "collection-default"}
            if isinstance(value, dict) and "alias" in value:
                if (set(value) - {"alias", "mode"} or not isinstance(value["alias"], str)
                        or ("mode" in value and not isinstance(value["mode"], str))):
                    raise Invalid("Invalid alias value")
                other = self.tokens.get(value["alias"])
                if not other: raise Invalid("Unresolved alias: " + value["alias"])
                if other["layer"] not in self.policy["layer_edges"][token["layer"]]:
                    raise Invalid("Invalid layer edge: " + key + " -> " + other["id"])
                if token["type"] != other["type"] or token.get("unit") != other.get("unit"):
                    raise Invalid("Alias type/unit mismatch: " + key)
                result, chain = visit(other["id"], active | {state}, value.get("mode"))
                return result, [trace] + chain
            if token["layer"] != "primitive": raise Invalid("Non-primitive token needs an alias: " + key)
            self.literal(token["type"], value)
            return value, [trace]
        value, chain = visit(identity, set())
        return {"id": identity, "value": value, "type": self.tokens[identity]["type"],
                "unit": self.tokens[identity].get("unit"), "chain": chain}

    @staticmethod
    def literal(kind, value):
        valid = ((kind == "string" and isinstance(value, str)) or
                 (kind == "boolean" and type(value) is bool) or
                 (kind == "number" and type(value) in (int, float) and math.isfinite(value)))
        if kind == "color":
            valid = (isinstance(value, dict) and set(value) == {"r", "g", "b", "a"}
                     and all(type(v) in (int, float) and math.isfinite(v) and 0 <= v <= 1 for v in value.values()))
        if not valid: raise Invalid("Invalid literal for token type " + kind)

    def validate(self):
        layout = self.policy.get("token_collections")
        if layout is not None:
            expected = set(layout.values())
            if len(expected) != len(layout) or set(self.collections) != expected:
                raise Invalid("BH-P07 collection layout requires exactly: " + ", ".join(sorted(expected)))
            for identity, collection in self.collections.items():
                if collection.get("name") != identity:
                    raise Invalid("BH-P07 logical/native collection names must match: " + identity)
        color_targets = {}
        for identity, token in self.tokens.items():
            if layout is not None and token["collection"] != layout[token["layer"]]:
                raise Invalid("BH-P07 token is in the wrong layer collection: " + identity)
            scopes = token.get("scopes", [])
            if token["layer"] in {"primitive", "semantic"} and scopes:
                raise Invalid("Primitives and semantics require empty scopes: " + identity)
            if token["layer"] == "component" and not scopes:
                raise Invalid("Component token requires an explicit property scope: " + identity)
            if token["layer"] == "component" and len(scopes) != 1:
                raise Invalid("Component token requires exactly one property scope: " + identity)
            scope_types = {
                "color": {"FRAME_FILL", "SHAPE_FILL", "TEXT_FILL", "STROKE_COLOR", "EFFECT_COLOR"},
                "number": {"STROKE_FLOAT", "EFFECT_FLOAT", "WIDTH_HEIGHT", "GAP", "CORNER_RADIUS", "OPACITY", "FONT_WEIGHT", "FONT_SIZE", "LINE_HEIGHT", "LETTER_SPACING", "PARAGRAPH_SPACING", "PARAGRAPH_INDENT"},
                "string": {"FONT_FAMILY", "FONT_STYLE", "TEXT_CONTENT"}, "boolean": set()}
            if set(scopes) - scope_types[token["type"]]:
                raise Invalid("Token scope/type mismatch: " + identity)
            if token["layer"] == "semantic" and token["type"] == "color":
                targets = {v.get("alias") for v in token["values"].values() if isinstance(v, dict)}
                if len(targets) != 1:
                    raise Invalid("Color semantic must have a fixed primitive alias: " + identity)
                target = next(iter(targets))
                if target in color_targets:
                    raise Invalid("Duplicate color semantic primitive: " + identity + " / " + color_targets[target])
                color_targets[target] = identity
        collections = sorted(self.collections)
        combinations = 1
        for key in collections: combinations *= len(self.collections[key]["modes"])
        if combinations > self.policy["max_mode_combinations"]:
            raise Invalid("Mode coverage exceeds explicit validation budget; no partial PASS")
        contexts = [dict(zip(collections, modes)) for modes in itertools.product(
            *[[m["id"] for m in self.collections[key]["modes"]] for key in collections])]
        for identity, token in sorted(self.tokens.items()):
            collection = self.collections.get(token["collection"])
            if not collection or set(token["values"]) != {m["id"] for m in collection["modes"]}:
                raise Invalid("Token must define exactly all collection modes: " + identity)
            for context in contexts: self.resolve(identity, context)
        return {"tokens": len(self.tokens), "collections": len(collections), "mode_contexts": len(contexts)}

    def edges(self):
        return {"token:" + identity: {"token:" + value["alias"] for value in token["values"].values()
                if isinstance(value, dict) and "alias" in value} for identity, token in self.tokens.items()}

    def component_minimum(self, identities):
        """BH-P07: compare direct component dependencies, never merge separate families.

        Collection identity retains mode context; direct aliases and alias-explicit
        modes retain intent even when resolved numeric/color values coincide.
        """
        signatures = {}
        for identity in sorted(set(identities)):
            token = self.tokens.get(identity)
            if token is None: raise Invalid("Unresolved component token: " + identity)
            if token["layer"] != "component": continue
            signature = canonical({k: token.get(k) for k in ("type", "unit", "collection", "scopes", "values")})
            if signature in signatures:
                raise Invalid("BH-P07 redundant component tokens: " + signatures[signature] + " / " + identity)
            signatures[signature] = identity
        return {"status": "PASS", "protocol": "BH-P07", "component_tokens": len(signatures),
                "distinct_signatures": len(signatures), "redundancies": 0}
