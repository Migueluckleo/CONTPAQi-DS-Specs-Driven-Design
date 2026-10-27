"""Verify the delivered normalization against the preserved Figma inventory."""
import csv
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def read_csv(name):
    with (ROOT / "auditoria/fase-1" / name).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def normalized(name):
    return (name[6:] if name.startswith("color/") else name).replace("/", "-")


class NormalizationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inventory = json.loads((ROOT / "evidence/foundations/observed-inventory.json").read_text())
        cls.originals = {v["id"]: v for v in cls.inventory["variables"]}
        cls.collections = {c["id"]: c for c in cls.inventory["collections"]}
        cls.catalog = read_csv("semanticos-color.csv")
        cls.rows = read_csv("variables-normalizadas.csv")

    def test_one_color_semantic_per_referenced_primitive(self):
        self.assertEqual(len(self.catalog), len({r["semantico"] for r in self.catalog}))
        self.assertEqual(len(self.catalog), len({r["id_primitiva"] for r in self.catalog}))
        self.assertEqual(len(self.catalog), len({r["primitiva"] for r in self.catalog}))
        expected = {alias["id"] for v in self.originals.values()
                    if self.collections[v["variableCollectionId"]]["name"] == "semantic"
                    and v["resolvedType"] == "COLOR" for alias in v["valuesByMode"].values()}
        self.assertEqual({r["id_primitiva"] for r in self.catalog}, expected)
        for row in self.catalog:
            target = self.originals[row["id_primitiva"]]
            self.assertEqual(target["resolvedType"], "COLOR")
            self.assertEqual(self.collections[target["variableCollectionId"]]["name"], "primitive")
            self.assertEqual(row["primitiva"], normalized(target["name"]))

    def test_semantics_have_no_application_scopes(self):
        for row in self.catalog + self.rows:
            self.assertEqual(json.loads(row["scopes"]), [])
        forbidden = {"frame", "shape", "fill", "bg", "stroke", "border", "text", "icon",
                     "surface", "background", "button", "input", "hover", "active", "disabled"}
        for row in self.catalog:
            self.assertFalse(set(row["semantico"].split("-")) & forbidden)

    def test_complete_original_identity_coverage(self):
        self.assertEqual(len(self.rows), len(self.originals))
        self.assertEqual({r["id_original"] for r in self.rows}, set(self.originals))
        for row in self.rows:
            original = self.originals[row["id_original"]]
            self.assertEqual(row["nombre_original"], original["name"])
            self.assertEqual(row["tipo"], original["resolvedType"])

    def test_every_theme_preserves_its_original_alias_target(self):
        catalog = {r["semantico"]: r for r in self.catalog}
        for row in self.rows:
            original = self.originals[row["id_original"]]
            collection = self.collections[original["variableCollectionId"]]
            for mode in collection["modes"]:
                value = original["valuesByMode"][mode["modeId"]]
                if isinstance(value, dict) and value.get("type") == "VARIABLE_ALIAS":
                    if original["resolvedType"] == "COLOR":
                        self.assertEqual(catalog[row[mode["name"]]]["id_primitiva"], value["id"])
                    else:
                        self.assertEqual(row[mode["name"]], normalized(self.originals[value["id"]]["name"]))
                elif not isinstance(value, dict):
                    self.assertEqual(row[mode["name"]], str(value))
                else:
                    channels = [round(value[k] * 255) for k in ("r", "g", "b", "a")]
                    display = "#" + "".join("{:02X}".format(c) for c in
                                             (channels[:3] if channels[3] == 255 else channels))
                    self.assertEqual(row[mode["name"]], display)

    def test_blue_200_has_only_brand_accent(self):
        matching = [r for r in self.catalog if r["primitiva"] == "blue-200"]
        self.assertEqual(len(matching), 1)
        self.assertEqual(matching[0]["semantico"], "brand-accent")
