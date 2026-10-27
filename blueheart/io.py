"""Project-confined IO. No writes, network, imports from the legacy repository or eval."""
import hashlib
import json
import math
from pathlib import Path, PurePosixPath


class Invalid(ValueError):
    pass


def path(root, name):
    if not isinstance(name, str) or not name or "\\" in name:
        raise Invalid("Invalid project path")
    pure = PurePosixPath(name)
    if pure.is_absolute() or ".." in pure.parts or str(pure) != name:
        raise Invalid("Path must be canonical and relative: " + name)
    root = Path(root).resolve()
    candidate = root / name
    for part in (candidate, *candidate.parents):
        if part == root:
            break
        if part.is_symlink():
            raise Invalid("Symlink rejected: " + name)
    if not candidate.resolve().is_relative_to(root):
        raise Invalid("Path escapes project")
    return candidate


def sha(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def loads(raw):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise Invalid("Duplicate JSON key: " + key)
            result[key] = value
        return result
    def constant(value):
        raise Invalid("Non-finite JSON number: " + value)
    try:
        result = json.loads(raw, object_pairs_hook=pairs, parse_constant=constant)
        def finite(v):
            if isinstance(v, float) and not math.isfinite(v):
                raise Invalid("Non-finite JSON number")
            if isinstance(v, dict):
                for item in v.values(): finite(item)
            if isinstance(v, list):
                for item in v: finite(item)
        finite(result)
        return result
    except (json.JSONDecodeError, UnicodeError) as error:
        raise Invalid(str(error)) from error


def read(root, name):
    return loads(path(root, name).read_bytes())


def source(root, reference):
    """Return verified bytes; a digest is integrity evidence, not approval."""
    raw = path(root, reference["path"]).read_bytes()
    if sha(raw) != reference["sha256"]:
        raise Invalid("Source hash mismatch: " + reference["path"])
    selector = reference.get("selector")
    if selector is not None:
        if not selector.startswith("JSON:/"):
            raise Invalid("Only explicit JSON Pointer selectors are supported")
        value = loads(raw)
        try:
            for part in selector[6:].split("/"):
                part = part.replace("~1", "/").replace("~0", "~")
                if isinstance(value, list):
                    if not part.isdecimal() or (len(part) > 1 and part.startswith("0")):
                        raise Invalid("Invalid JSON array index")
                    value = value[int(part)]
                else:
                    value = value[part]
        except (KeyError, IndexError, TypeError, ValueError) as error:
            raise Invalid("Unresolved source selector: " + selector) from error
        if "original_id" in reference and (not isinstance(value, dict) or value.get("id") != reference["original_id"]):
            raise Invalid("Original source identity differs from selected record")
    elif "original_id" in reference:
        raise Invalid("Original source identity requires an explicit selector")
    return raw
