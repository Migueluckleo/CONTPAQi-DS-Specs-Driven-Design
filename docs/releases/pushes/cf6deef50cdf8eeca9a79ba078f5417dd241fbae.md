---
{
  "base": "cb788b3d654e79fc6cfd50fe51cdde128374ad2f",
  "commits": [
    {
      "category": "fixed",
      "sha": "cf6deef50cdf8eeca9a79ba078f5417dd241fbae",
      "subject": "fix: depurar ledgers de consumo y verificar identidades vigentes"
    }
  ],
  "components": [],
  "decisions": [
    "ADR-012",
    "ADR-020"
  ],
  "evidence": [
    {
      "path": "evidence/collection-consolidation/ledger-reference-check.txt",
      "sha256": "5e105a5cda0925ebe4b44298d84f1f65963820d3a1b5c2464bf3254bb8cf7697"
    },
    {
      "path": "evidence/qa/component-collection-check.json",
      "sha256": "c2f042b6eb240a1fae7337b641f833a79e1781728a54bebad441b1ead044bc62"
    }
  ],
  "files": [
    {
      "path": "consumption/avatar/current-native-ledger.json",
      "status": "M"
    },
    {
      "path": "consumption/avatar/manifest.json",
      "status": "M"
    },
    {
      "path": "consumption/project-native-ledgers.py",
      "status": "A"
    },
    {
      "path": "consumption/tab/current-native-ledger.json",
      "status": "M"
    },
    {
      "path": "consumption/tab/manifest.json",
      "status": "M"
    },
    {
      "path": "evidence/collection-consolidation/README.md",
      "status": "M"
    },
    {
      "path": "evidence/collection-consolidation/ledger-reference-check.txt",
      "status": "A"
    },
    {
      "path": "tests/test_collection_layout.py",
      "status": "M"
    }
  ],
  "kind": "development",
  "payload": "cf6deef50cdf8eeca9a79ba078f5417dd241fbae",
  "pending": [],
  "references": [],
  "release_version": null,
  "schema_version": 1,
  "tests": [
    {
      "command": [
        "python3",
        "-B",
        "-m",
        "blueheart",
        "check"
      ],
      "exit_code": 0,
      "output": "{\n  \"collections\": 3,\n  \"component_token_minimum\": {\n    \"AVATAR-001@1.0.0\": {\n      \"component_tokens\": 25,\n      \"distinct_signatures\": 25,\n      \"protocol\": \"BH-P07\",\n      \"redundancies\": 0,\n      \"status\": \"PASS\"\n    },\n    \"AVATAR-001@2.0.0\": {\n      \"component_tokens\": 25,\n      \"distinct_signatures\": 25,\n      \"protocol\": \"BH-P07\",\n      \"redundancies\": 0,\n      \"status\": \"PASS\"\n    },\n    \"AVATAR-GROUP-001@1.0.0\": {\n      \"component_tokens\": 7,\n      \"distinct_signatures\": 7,\n      \"protocol\": \"BH-P07\",\n      \"redundancies\": 0,\n      \"status\": \"PASS\"\n    },\n    \"AVATAR-GROUP-001@2.0.0\": {\n      \"component_tokens\": 7,\n      \"distinct_signatures\": 7,\n      \"protocol\": \"BH-P07\",\n      \"redundancies\": 0,\n      \"status\": \"PASS\"\n    },\n    \"BUTTON-001@2.0.0\": {\n      \"component_tokens\": 47,\n      \"distinct_signatures\": 47,\n      \"protocol\": \"BH-P07\",\n      \"redundancies\": 0,\n      \"status\": \"PASS\"\n    },\n    \"BUTTON-001@2.0.1\": {\n      \"component_tokens\": 47,\n      \"distinct_signatures\": 47,\n      \"protocol\": \"BH-P07\",\n      \"redundancies\": 0,\n      \"status\": \"PASS\"\n    },\n    \"BUTTON-001@3.0.0\": {\n      \"component_tokens\": 47,\n      \"distinct_signatures\": 47,\n      \"protocol\": \"BH-P07\",\n      \"redundancies\": 0,\n      \"status\": \"PASS\"\n    },\n    \"TAB-001@1.0.0\": {\n      \"component_tokens\": 43,\n      \"distinct_signatures\": 43,\n      \"protocol\": \"BH-P07\",\n      \"redundancies\": 0,\n      \"status\": \"PASS\"\n    },\n    \"TAB-001@1.1.0\": {\n      \"component_tokens\": 45,\n      \"distinct_signatures\": 45,\n      \"protocol\": \"BH-P07\",\n      \"redundancies\": 0,\n      \"status\": \"PASS\"\n    },\n    \"TAB-001@2.0.0\": {\n      \"component_tokens\": 45,\n      \"distinct_signatures\": 45,\n      \"protocol\": \"BH-P07\",\n      \"redundancies\": 0,\n      \"status\": \"PASS\"\n    },\n    \"TABS-001@1.0.0\": {\n      \"component_tokens\": 5,\n      \"distinct_signatures\": 5,\n      \"protocol\": \"BH-P07\",\n      \"redundancies\": 0,\n      \"status\": \"PASS\"\n    },\n    \"TABS-001@2.0.0\": {\n      \"component_tokens\": 5,\n      \"distinct_signatures\": 5,\n      \"protocol\": \"BH-P07\",\n      \"redundancies\": 0,\n      \"status\": \"PASS\"\n    }\n  },\n  \"contracts\": 20,\n  \"deferred\": [\n    \"figma-write-adapter\",\n    \"react-library\",\n    \"graphify-adapter\",\n    \"persistent-agent-office\",\n    \"release-publication\"\n  ],\n  \"graphify_required\": false,\n  \"mode_contexts\": 4,\n  \"scope\": \"Infrastructure and registered normative content; not design or implementation QA\",\n  \"snapshot\": \"8c66ea2ad6da24f0444c32775277fc792133a110a87ac9e277e3f54608fdca22\",\n  \"status\": \"PASS\",\n  \"token_sets\": 1,\n  \"tokens\": 386\n}\n",
      "sha256": "b54a2bc77abd498b27e1d7b26cbbb58f9bde37b8f29a68c1ed893aece2ea64ba",
      "status": "PASS"
    },
    {
      "command": [
        "python3",
        "-B",
        "-m",
        "unittest",
        "discover",
        "-s",
        "tests",
        "-q"
      ],
      "exit_code": 0,
      "output": "----------------------------------------------------------------------\nRan 94 tests in 118.978s\n\nOK\n",
      "sha256": "cec0073c4d2d420813cb07eff07f7c2273e412c0f3db5cdb139ff0a116e3294b",
      "status": "PASS"
    }
  ]
}
---
# Envío cf6deef50cdf8eeca9a79ba078f5417dd241fbae

Tipo: development. Base: `cb788b3d654e79fc6cfd50fe51cdde128374ad2f`.

## added

Sin cambios clasificados en esta categoría.

## changed

Sin cambios clasificados en esta categoría.

## fixed

- `cf6deef50cdf8eeca9a79ba078f5417dd241fbae` fix: depurar ledgers de consumo y verificar identidades vigentes

## removed

Sin cambios clasificados en esta categoría.

## Trazabilidad

Los commits, archivos, pruebas, pendientes, decisiones y versiones de componentes están en el frontmatter de este único registro. El comprobante CI identifica el commit documental y el rango efectivo del push.
