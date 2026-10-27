---
{
  "base": "e7cc8ddd216ca61c497a5e8e58d33a726b09c0b3",
  "commits": [
    {
      "category": "changed",
      "sha": "81546938340f1ae1ec4b4231252ed58a1ddc2ef3",
      "subject": "test: comprobar rechazo de un envío sin notas según BH-P08"
    },
    {
      "category": "fixed",
      "sha": "498665b6635b67097ce83a5d249866efc4f8d062",
      "subject": "fix: documentar verificación de protección y retirar sonda de incumplimiento"
    }
  ],
  "components": [],
  "decisions": [
    "ADR-012"
  ],
  "evidence": [
    {
      "path": "docs/releases/verification/branch-protection-check.json",
      "sha256": "6e79347ce82dd350842890b7ea0976aac5ae01d6c66405fb1a78ab29c1553816"
    }
  ],
  "files": [
    {
      "path": "docs/releases/verification/branch-protection-check.json",
      "status": "A"
    }
  ],
  "kind": "development",
  "payload": "498665b6635b67097ce83a5d249866efc4f8d062",
  "pending": [
    "La protección exige revisión independiente; esta PR de prueba se cerrará sin integrar cambios en main."
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
      "output": "{\n  \"collections\": 3,\n  \"component_token_minimum\": {\n    \"BUTTON-001@2.0.0\": {\n      \"component_tokens\": 47,\n      \"distinct_signatures\": 47,\n      \"protocol\": \"BH-P07\",\n      \"redundancies\": 0,\n      \"status\": \"PASS\"\n    }\n  },\n  \"contracts\": 9,\n  \"deferred\": [\n    \"figma-write-adapter\",\n    \"react-library\",\n    \"graphify-adapter\",\n    \"persistent-agent-office\",\n    \"release-publication\"\n  ],\n  \"graphify_required\": false,\n  \"mode_contexts\": 4,\n  \"scope\": \"Infrastructure and registered normative content; not design or implementation QA\",\n  \"snapshot\": \"cc75cb3dccf0d3fa126807702e0de40ef3ce24085b99c3ace0036ec725380e95\",\n  \"status\": \"PASS\",\n  \"token_sets\": 1,\n  \"tokens\": 298\n}\n",
      "sha256": "5951584cc8941d822fcf166c2b93a7aeffc05023e676aae043102bcf33ccd733",
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
      "output": "----------------------------------------------------------------------\nRan 85 tests in 87.586s\n\nOK\n",
      "sha256": "67fdbe98dfd78095e37c508b4ef567a3113a9683b421eae06d4cfee3b050df70",
      "status": "PASS"
    }
  ]
}
---
# Envío 498665b6635b67097ce83a5d249866efc4f8d062

Tipo: development. Base: `e7cc8ddd216ca61c497a5e8e58d33a726b09c0b3`.

## added

Sin cambios clasificados en esta categoría.

## changed

- `81546938340f1ae1ec4b4231252ed58a1ddc2ef3` test: comprobar rechazo de un envío sin notas según BH-P08

## fixed

- `498665b6635b67097ce83a5d249866efc4f8d062` fix: documentar verificación de protección y retirar sonda de incumplimiento

## removed

Sin cambios clasificados en esta categoría.

## Trazabilidad

Los commits, archivos, pruebas, pendientes, decisiones y versiones de componentes están en el frontmatter de este único registro. El comprobante CI identifica el commit documental y el rango efectivo del push.
