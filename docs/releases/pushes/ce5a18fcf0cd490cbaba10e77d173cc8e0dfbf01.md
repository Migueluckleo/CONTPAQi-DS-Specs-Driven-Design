---
{
  "base": "8ef8f7470f33db815f450cf539596ef75dd2b01a",
  "commits": [
    {
      "category": "added",
      "sha": "ce5a18fcf0cd490cbaba10e77d173cc8e0dfbf01",
      "subject": "feat: incorporar Avatar y Avatar group con contratos y tokens mínimos"
    }
  ],
  "components": [
    {
      "from": null,
      "id": "AVATAR-001",
      "impact": "minor",
      "reason": "Primera incorporación de Avatar 1.0.0 con 12 variantes, presencia privada y 25 tokens mínimos.",
      "to": {
        "fingerprint": "9ce4db305ced33362ac4ed56130c5add4fc3f22f5c9ed849e5e0e43fa1919dfa",
        "path": "norms/components/avatar.1.0.0.md",
        "sha256": "385aa42232f1241451940f479b4c1a6b31ed9bcc42f18e84200ec2d473aae83b",
        "version": "1.0.0"
      }
    },
    {
      "from": null,
      "id": "AVATAR-GROUP-001",
      "impact": "minor",
      "reason": "Primera incorporación de Avatar group 1.0.0 con slot nativo, cuatro tamaños y siete tokens propios.",
      "to": {
        "fingerprint": "930424e3791a0271665bffb9701aeb02db810721cf33d3f19858501d7dfeb60f",
        "path": "norms/components/avatar-group.1.0.0.md",
        "sha256": "29b2ceb001700063b91ed5c90b5df1e2c4098ab7703686eca3cd742ab2fba5e5",
        "version": "1.0.0"
      }
    }
  ],
  "decisions": [
    "ADR-012",
    "ADR-019"
  ],
  "evidence": [
    {
      "path": "evidence/qa/avatar-pilot-check.json",
      "sha256": "a7d7ebb5101c16b427b5bfb7261b653e61d3248727e7508fea186c0992d7b748"
    }
  ],
  "files": [
    {
      "path": "AGENTS.md",
      "status": "M"
    },
    {
      "path": "README.md",
      "status": "M"
    },
    {
      "path": "consumption/avatar-group/README.md",
      "status": "A"
    },
    {
      "path": "consumption/avatar-group/binding-map.csv",
      "status": "A"
    },
    {
      "path": "consumption/avatar-group/manifest.json",
      "status": "A"
    },
    {
      "path": "consumption/avatar-group/variable-map.csv",
      "status": "A"
    },
    {
      "path": "consumption/avatar/README.md",
      "status": "A"
    },
    {
      "path": "consumption/avatar/binding-map.csv",
      "status": "A"
    },
    {
      "path": "consumption/avatar/current-build-plan.json",
      "status": "A"
    },
    {
      "path": "consumption/avatar/manifest.json",
      "status": "A"
    },
    {
      "path": "consumption/avatar/variable-map.csv",
      "status": "A"
    },
    {
      "path": "consumption/button/manifest.json",
      "status": "M"
    },
    {
      "path": "consumption/tab/manifest.json",
      "status": "M"
    },
    {
      "path": "consumption/tabs/manifest.json",
      "status": "M"
    },
    {
      "path": "evidence/authorization/avatar-pilot-request.txt",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/assets/portrait-preview.png",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/assets/portrait.png",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/baseline-native.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/contrast.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/destination/avatar.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/destination/binding-index.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/destination/consumer-qa.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/destination/documentation.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/destination/foundation.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/destination/group.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/destination/native-audit.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/destination/portrait-upload.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/destination/preview-upload.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/destination/section-8890-846.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/destination/section-8890-860.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/destination/section-8890-874.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/destination/section-8890-888.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/destination/section-9064-29663.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/handoff.md",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/history/blueheart.2.0.0.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/history/foundations-application-map.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/presentation/section-8890-846.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/presentation/section-8890-860.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/presentation/section-8890-874.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/presentation/section-8890-888.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/presentation/section-9064-29663.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/qa-plan-contract.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/qa-plan-token.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/source/discovery.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/source/page-snapshot.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/source/phosphor.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/source/presence-and-gaps.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/source/text-layout.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/source/variables.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/targeted-tests.txt",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/token-minimum.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/token-names.json",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/visual/overview.png",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/visual/qa.png",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/visual/review.png",
      "status": "A"
    },
    {
      "path": "evidence/avatar-pilot/visual/variants.png",
      "status": "A"
    },
    {
      "path": "evidence/figma-application/application-map.json",
      "status": "M"
    },
    {
      "path": "evidence/qa/avatar-pilot-check.json",
      "status": "A"
    },
    {
      "path": "governance/decisions.json",
      "status": "M"
    },
    {
      "path": "governance/policy.json",
      "status": "M"
    },
    {
      "path": "implementations/figma/avatar-builder.js",
      "status": "A"
    },
    {
      "path": "implementations/figma/avatar-consumer-qa.js",
      "status": "A"
    },
    {
      "path": "implementations/figma/avatar-documentation-plan.py",
      "status": "A"
    },
    {
      "path": "implementations/figma/avatar-documentation.js",
      "status": "A"
    },
    {
      "path": "implementations/figma/avatar-native-audit.js",
      "status": "A"
    },
    {
      "path": "implementations/figma/avatar-plan.py",
      "status": "A"
    },
    {
      "path": "implementations/figma/tab-plan.py",
      "status": "M"
    },
    {
      "path": "implementations/figma/tab-verify.py",
      "status": "M"
    },
    {
      "path": "norms/catalog.json",
      "status": "M"
    },
    {
      "path": "norms/components/avatar-group.1.0.0.md",
      "status": "A"
    },
    {
      "path": "norms/components/avatar.1.0.0.md",
      "status": "A"
    },
    {
      "path": "norms/tokens/avatar.1.0.0.json",
      "status": "A"
    },
    {
      "path": "norms/tokens/blueheart.2.0.0.json",
      "status": "D"
    },
    {
      "path": "norms/tokens/blueheart.2.1.0.json",
      "status": "A"
    },
    {
      "path": "tests/test_button_reduction.py",
      "status": "M"
    },
    {
      "path": "tests/test_core.py",
      "status": "M"
    }
  ],
  "kind": "development",
  "payload": "ce5a18fcf0cd490cbaba10e77d173cc8e0dfbf01",
  "pending": [
    "Alterno warning conserva el binding fuente: 3.32:1 con blanco, sin declaración AA; limitación documentada.",
    "React, teclado/ARIA y revisión independiente no ejecutados en este encargo Figma/documentación."
  ],
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
      "output": "{\n  \"collections\": 7,\n  \"component_token_minimum\": {\n    \"AVATAR-001@1.0.0\": {\n      \"component_tokens\": 25,\n      \"distinct_signatures\": 25,\n      \"protocol\": \"BH-P07\",\n      \"redundancies\": 0,\n      \"status\": \"PASS\"\n    },\n    \"AVATAR-GROUP-001@1.0.0\": {\n      \"component_tokens\": 7,\n      \"distinct_signatures\": 7,\n      \"protocol\": \"BH-P07\",\n      \"redundancies\": 0,\n      \"status\": \"PASS\"\n    },\n    \"BUTTON-001@2.0.0\": {\n      \"component_tokens\": 47,\n      \"distinct_signatures\": 47,\n      \"protocol\": \"BH-P07\",\n      \"redundancies\": 0,\n      \"status\": \"PASS\"\n    },\n    \"BUTTON-001@2.0.1\": {\n      \"component_tokens\": 47,\n      \"distinct_signatures\": 47,\n      \"protocol\": \"BH-P07\",\n      \"redundancies\": 0,\n      \"status\": \"PASS\"\n    },\n    \"TAB-001@1.0.0\": {\n      \"component_tokens\": 43,\n      \"distinct_signatures\": 43,\n      \"protocol\": \"BH-P07\",\n      \"redundancies\": 0,\n      \"status\": \"PASS\"\n    },\n    \"TAB-001@1.1.0\": {\n      \"component_tokens\": 45,\n      \"distinct_signatures\": 45,\n      \"protocol\": \"BH-P07\",\n      \"redundancies\": 0,\n      \"status\": \"PASS\"\n    },\n    \"TABS-001@1.0.0\": {\n      \"component_tokens\": 5,\n      \"distinct_signatures\": 5,\n      \"protocol\": \"BH-P07\",\n      \"redundancies\": 0,\n      \"status\": \"PASS\"\n    }\n  },\n  \"contracts\": 15,\n  \"deferred\": [\n    \"figma-write-adapter\",\n    \"react-library\",\n    \"graphify-adapter\",\n    \"persistent-agent-office\",\n    \"release-publication\"\n  ],\n  \"graphify_required\": false,\n  \"mode_contexts\": 64,\n  \"scope\": \"Infrastructure and registered normative content; not design or implementation QA\",\n  \"snapshot\": \"63532a0720fdf8ec8920a790e0c9c1e8ca2f1b42e7c8c25fded0443e3b52f7d8\",\n  \"status\": \"PASS\",\n  \"token_sets\": 4,\n  \"tokens\": 386\n}\n",
      "sha256": "1578d12541b709c8c58a1fb2f7941ff90dee4ffe9c0dafbdc88b54e85d044b3f",
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
      "output": "----------------------------------------------------------------------\nRan 88 tests in 114.470s\n\nOK\n",
      "sha256": "85574094405841d6114b2f6372078aa9d30f13ec8940aa858104e68c90abcb3f",
      "status": "PASS"
    }
  ]
}
---
# Envío ce5a18fcf0cd490cbaba10e77d173cc8e0dfbf01

Tipo: development. Base: `8ef8f7470f33db815f450cf539596ef75dd2b01a`.

## added

- `ce5a18fcf0cd490cbaba10e77d173cc8e0dfbf01` feat: incorporar Avatar y Avatar group con contratos y tokens mínimos

## changed

Sin cambios clasificados en esta categoría.

## fixed

Sin cambios clasificados en esta categoría.

## removed

Sin cambios clasificados en esta categoría.

## Trazabilidad

Los commits, archivos, pruebas, pendientes, decisiones y versiones de componentes están en el frontmatter de este único registro. El comprobante CI identifica el commit documental y el rango efectivo del push.
