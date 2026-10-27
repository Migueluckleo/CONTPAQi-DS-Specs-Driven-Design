"""Closed JSON Schema vocabulary used by this repository, not a general implementation.

Reject unsupported keywords instead of silently pretending full draft conformance.
Schemas remain the single owner of structural rules; domain invariants live in domain modules.
"""
import re
from .io import Invalid, canonical, read

KEYWORDS = {"$schema", "$id", "$ref", "$defs", "title", "description", "type", "enum", "const",
            "required", "properties", "additionalProperties", "items", "minItems", "uniqueItems",
            "minLength", "pattern", "minimum", "maximum", "allOf"}


class Schemas:
    def __init__(self, root):
        self.root = root
        self.cache = {}

    def load(self, name):
        if not re.fullmatch(r"[a-z][a-z0-9-]*\.schema\.json", name):
            raise Invalid("Schema reference must name a local schema")
        if name not in self.cache:
            value = read(self.root, "schemas/" + name)
            self._vocabulary(value)
            self.cache[name] = value
        return self.cache[name]

    def _vocabulary(self, schema):
        if not isinstance(schema, dict):
            raise Invalid("Schemas must be objects")
        unknown = set(schema) - KEYWORDS
        if unknown:
            raise Invalid("Unsupported schema keywords: " + ", ".join(sorted(unknown)))
        for key in ("properties", "$defs"):
            for sub in schema.get(key, {}).values(): self._vocabulary(sub)
        if isinstance(schema.get("additionalProperties"), dict): self._vocabulary(schema["additionalProperties"])
        if "items" in schema: self._vocabulary(schema["items"])
        for sub in schema.get("allOf", []): self._vocabulary(sub)

    def validate(self, value, name):
        self._check(value, self.load(name), name, "$", ())
        return value

    def _check(self, value, schema, name, location, refs):
        if "$ref" in schema:
            ref = schema["$ref"]
            target_name, _, fragment = ref.partition("#")
            target_name = target_name or name
            key = (target_name, fragment)
            if key in refs: raise Invalid("Recursive schema references are not supported")
            target = self.load(target_name)
            if fragment:
                if not fragment.startswith("/"): raise Invalid("Invalid schema fragment")
                for part in fragment[1:].split("/"):
                    target = target[part.replace("~1", "/").replace("~0", "~")]
            self._check(value, target, target_name, location, refs + (key,))
        for sub in schema.get("allOf", []): self._check(value, sub, name, location, refs)
        checks = {"object": isinstance(value, dict), "array": isinstance(value, list),
                  "string": isinstance(value, str), "boolean": type(value) is bool,
                  "number": type(value) in (int, float), "integer": type(value) is int, "null": value is None}
        if "type" in schema and not checks.get(schema["type"], False):
            raise Invalid(location + ": expected " + str(schema["type"]))
        if "enum" in schema and not any(canonical(value) == canonical(x) for x in schema["enum"]):
            raise Invalid(location + ": value outside enum")
        if "const" in schema and canonical(value) != canonical(schema["const"]):
            raise Invalid(location + ": value differs from const")
        if isinstance(value, dict):
            if set(schema.get("required", [])) - set(value): raise Invalid(location + ": required fields missing")
            props = schema.get("properties", {})
            for key, item in value.items():
                if key in props: self._check(item, props[key], name, location + "/" + key, refs)
                elif schema.get("additionalProperties") is False: raise Invalid(location + ": unknown field " + key)
                elif isinstance(schema.get("additionalProperties"), dict):
                    self._check(item, schema["additionalProperties"], name, location + "/" + key, refs)
        if isinstance(value, list):
            if len(value) < schema.get("minItems", 0): raise Invalid(location + ": too few items")
            if schema.get("uniqueItems") and len({canonical(x) for x in value}) != len(value):
                raise Invalid(location + ": duplicate items")
            if "items" in schema:
                for i, item in enumerate(value): self._check(item, schema["items"], name, location + "/" + str(i), refs)
        if isinstance(value, str):
            if len(value) < schema.get("minLength", 0): raise Invalid(location + ": string too short")
            if "pattern" in schema and not re.search(schema["pattern"], value): raise Invalid(location + ": pattern mismatch")
        if type(value) in (int, float):
            if "minimum" in schema and value < schema["minimum"]: raise Invalid(location + ": below minimum")
            if "maximum" in schema and value > schema["maximum"]: raise Invalid(location + ": above maximum")
