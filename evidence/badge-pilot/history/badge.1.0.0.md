---
{
  "schema_version": 1,
  "id": "BADGE-001",
  "version": "1.0.0",
  "profile": "component",
  "status": "ELIGIBLE",
  "authority": {
    "kind": "DELEGATED",
    "decision_id": "ADR-023"
  },
  "targets": [
    "figma",
    "documentation"
  ],
  "readiness": {
    "figma": "READY",
    "documentation": "READY"
  },
  "sources": [
    {
      "id": "SRC-USER",
      "path": "evidence/authorization/input-pilot-request.txt",
      "sha256": "1cf0d2f9edea79434932186fe0eaa7fc7556fc012999eca0bc14e7afbca855f3"
    },
    {
      "id": "SRC-BADGE-CHOICE",
      "path": "evidence/authorization/input-badge-scope-choice.txt",
      "sha256": "741bf5277e05f621df9afc3ed5f78f0fd37209c13dc8bd16a991195cc967c6cd"
    },
    {
      "id": "SRC-API",
      "path": "evidence/input-pilot/source/api.json",
      "sha256": "1656540b6bdc0989b57ca87f7f7016e58ce5801bda93fbb575f2fff21ad4b0fc"
    },
    {
      "id": "SRC-VARIABLES",
      "path": "evidence/input-pilot/source/variables.json",
      "sha256": "f9b7b0db34c69e855570d13876717239ad7111d9d0d94491a1b7a69d916f5750"
    },
    {
      "id": "SRC-TEXT",
      "path": "evidence/input-pilot/source/text-limits.json",
      "sha256": "6332d7c5a5e2a7a2176e94fe957e1b3d59a17c04c87183ab8df2c70e737832a3"
    },
    {
      "id": "SRC-BADGE",
      "path": "evidence/input-pilot/source/text-and-badge.json",
      "sha256": "5a4e0fd6835b0d06dda782c659bc4dff62ae702c72c7d31f97b15e81f8292479"
    },
    {
      "id": "SRC-PHOSPHOR",
      "path": "evidence/input-pilot/source/phosphor.json",
      "sha256": "398f21e086e03bfaf9d08c69dbb084c3b810916aff6c6eca952bdc26fb2d628d"
    },
    {
      "id": "SRC-DEFAULT-FALSE",
      "path": "evidence/input-pilot/source/default-false.json",
      "sha256": "983270c53add66d4fddb74a6855dbce04c6d2fb5ddbd8f495494b2fceb87873a"
    },
    {
      "id": "SRC-HOVER-FALSE",
      "path": "evidence/input-pilot/source/hover-false.json",
      "sha256": "8fb60d8b8f1ec6d150bb369613f85fcb5fbda0c5dc4555e78727d64ad9cab4fd"
    },
    {
      "id": "SRC-FOCUS-FALSE",
      "path": "evidence/input-pilot/source/focus-false.json",
      "sha256": "26e5b20eea4aadc5cbf521a7fb105aab65cdcab9c1c98487ab286049e89c7541"
    },
    {
      "id": "SRC-SUCCESS-FALSE",
      "path": "evidence/input-pilot/source/success-false.json",
      "sha256": "a8222ec0bc1a5e6cac94253944e1161f4b68881e615200ed1a36c563d4eb155d"
    },
    {
      "id": "SRC-ERROR-FALSE",
      "path": "evidence/input-pilot/source/error-false.json",
      "sha256": "6343da11f7c8c826833fd0dccfe6c62255ab30cb5377e815ad87f87b32ee80e4"
    },
    {
      "id": "SRC-READ-ONLY-FALSE",
      "path": "evidence/input-pilot/source/read-only-false.json",
      "sha256": "c3893aa81e314e3f44e7d5048639482d882d16ee1f65022ccf18126561ae742d"
    },
    {
      "id": "SRC-DISABLED-FALSE",
      "path": "evidence/input-pilot/source/disabled-false.json",
      "sha256": "1383c00e9f4234daf40158e55ae0ac39c6c346d14e93bfb460a74376aa79b5de"
    },
    {
      "id": "SRC-DEFAULT-TRUE",
      "path": "evidence/input-pilot/source/default-true.json",
      "sha256": "16f9544705e9e94672064b9958303257d62a92e8314756c2017d0109d8dc1961"
    },
    {
      "id": "SRC-HOVER-TRUE",
      "path": "evidence/input-pilot/source/hover-true.json",
      "sha256": "a8b12cf56fb51b18cac95396e523589bd20ce8ca4a54ad5a3755a43b15e4818b"
    },
    {
      "id": "SRC-FOCUS-TRUE",
      "path": "evidence/input-pilot/source/focus-true.json",
      "sha256": "42cf1eb838c4e8eb078bb148b66af228c3da6a6fcda1cdc15eaef2aceab41e5f"
    },
    {
      "id": "SRC-SUCCESS-TRUE",
      "path": "evidence/input-pilot/source/success-true.json",
      "sha256": "4ff3c110533ea379a8fc9efe5765de6f5ae18f836f4fc16e4f4ce8ee3b707416"
    },
    {
      "id": "SRC-ERROR-TRUE",
      "path": "evidence/input-pilot/source/error-true.json",
      "sha256": "be45f01a6f71c8371998d5ab3ccb452a1421e001851d0427a4c3ade07b192144"
    },
    {
      "id": "SRC-READ-ONLY-TRUE",
      "path": "evidence/input-pilot/source/read-only-true.json",
      "sha256": "57affb8e3a5c94bc8fe376ef99976691f7e575c0e3fdc821a096a3560e870d29"
    },
    {
      "id": "SRC-DISABLED-TRUE",
      "path": "evidence/input-pilot/source/disabled-true.json",
      "sha256": "05984d0d14ffa806a53b7bfb3a328648475f68e6fdb18c59937c4ef73b6cc681"
    }
  ],
  "dependencies": [
    {
      "kind": "token",
      "id": "badge.color-bg-subtle",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.color-stroke-subtle",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.spacing-none",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.spacing-inline",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.radius-container",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.border-width-regular",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.color-text-primary",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.font-family",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.font-label-style",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.font-size",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.font-line-height",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.font-letter-spacing",
      "relation": "uses"
    }
  ],
  "requirements": [
    {
      "id": "REQ-SCOPE",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-API",
        "SRC-BADGE-CHOICE"
      ],
      "acceptance": [
        "Verificar la regla completa contra sus fuentes seleccionadas, receta y consumidor del destino; registrar resultado y límites."
      ]
    },
    {
      "id": "REQ-API",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-API",
        "SRC-BADGE-CHOICE"
      ],
      "acceptance": [
        "Verificar la regla completa contra sus fuentes seleccionadas, receta y consumidor del destino; registrar resultado y límites."
      ]
    },
    {
      "id": "REQ-GEOMETRY",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-API",
        "SRC-BADGE-CHOICE"
      ],
      "acceptance": [
        "Verificar la regla completa contra sus fuentes seleccionadas, receta y consumidor del destino; registrar resultado y límites."
      ]
    },
    {
      "id": "REQ-TYPOGRAPHY",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-API",
        "SRC-BADGE-CHOICE"
      ],
      "acceptance": [
        "Verificar la regla completa contra sus fuentes seleccionadas, receta y consumidor del destino; registrar resultado y límites."
      ]
    },
    {
      "id": "REQ-THEME",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-API",
        "SRC-BADGE-CHOICE"
      ],
      "acceptance": [
        "Verificar la regla completa contra sus fuentes seleccionadas, receta y consumidor del destino; registrar resultado y límites."
      ]
    },
    {
      "id": "REQ-TOKENS",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-API",
        "SRC-BADGE-CHOICE"
      ],
      "acceptance": [
        "Verificar la regla completa contra sus fuentes seleccionadas, receta y consumidor del destino; registrar resultado y límites."
      ]
    },
    {
      "id": "REQ-CONSUMERS",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-API",
        "SRC-BADGE-CHOICE"
      ],
      "acceptance": [
        "Verificar la regla completa contra sus fuentes seleccionadas, receta y consumidor del destino; registrar resultado y límites."
      ]
    },
    {
      "id": "REQ-A11Y",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-API",
        "SRC-BADGE-CHOICE"
      ],
      "acceptance": [
        "Verificar la regla completa contra sus fuentes seleccionadas, receta y consumidor del destino; registrar resultado y límites."
      ]
    },
    {
      "id": "REQ-QA",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-API",
        "SRC-BADGE-CHOICE"
      ],
      "acceptance": [
        "Verificar la regla completa contra sus fuentes seleccionadas, receta y consumidor del destino; registrar resultado y límites."
      ]
    }
  ],
  "profile_data": {
    "anatomy": [
      "container",
      "Label"
    ],
    "composition": "fixed",
    "accessibility": "defined"
  }
}
---
# BADGE-001 · Badge 1.0.0

### REQ-SCOPE

BADGE-001@1.0.0 cubre solo subtle/small necesario para Input por elección expresa. Principal compartido en página Badge; no reconstruir las otras 17 variantes ni iconos opcionales no consumidos. No sustituye Dot ni sus contadores.

### REQ-API

Un set Badge con type=subtle y size=small, una combinación y Label TEXT inicialmente Label. Los consumidores pueden editarlo como MXN/USD. No es botón, chip removible ni indicador con acción; no hay Slots arbitrarios, iconos o reacciones en este alcance.

### REQ-GEOMETRY

Auto Layout horizontal HUG, texto de una línea sin truncado, alto 20 px derivado del line-height 20 y padding vertical 0; padding horizontal 8, radio 4, borde interior 1 con strokesIncludedInLayout=false. Width depende del texto: ejemplo Label mide 46 y MXN 42. Un gap 4 con un único hijo visible no justifica otra variable. El consumidor evita montos/datos sensibles y mantiene una etiqueta breve.

### REQ-TYPOGRAPHY

Manrope Regular 12/20 px, letter-spacing 0 PIXELS. Crear y aplicar badge/subtle-small al texto; aliases de familia, estilo, tamaño, line-height y tracking permanecen vinculados. No heredar el tracking porcentual de Input ni escalar la tipografía.

### REQ-THEME

Todos sus roles son invariantes: fondo neutral-subtle, borde neutral-muted y texto neutral-maximum, mismos aliases en los cuatro modos de component. No usar color de marca para metadatos de moneda.

### REQ-TOKENS

12 firmas propias en component/badge: tres paints con scopes separados, padding 0/8, radio, borde y cinco campos tipográficos. Altura HUG deriva del estilo, no crear un token height adicional ni tokens para iconos ausentes. No fusionar sus responsabilidades con Input por igualdad de valor.

| ID lógico | Ruta Figma |
|---|---|
| badge.color-bg-subtle | badge/color/bg/subtle |
| badge.color-stroke-subtle | badge/color/stroke/subtle |
| badge.spacing-none | badge/spacing/none |
| badge.spacing-inline | badge/spacing/inline |
| badge.radius-container | badge/radius/container |
| badge.border-width-regular | badge/border/width-regular |
| badge.color-text-primary | badge/color/text/primary |
| badge.font-family | badge/font/family |
| badge.font-label-style | badge/font/label-style |
| badge.font-size | badge/font/size |
| badge.font-line-height | badge/font/line-height |
| badge.font-letter-spacing | badge/font/letter-spacing |

### REQ-CONSUMERS

Input crea 42 instancias anidadas, expuestas e inicialmente ocultas; el contrato Input fija el pin exacto. Mantener vínculo al principal y Label independiente. La auditoría previa no detectó consumidores de este Badge; los nodos de Tab con ese nombre son Dot.

### REQ-A11Y

Etiqueta de metadato sin interacción ni foco. El host conserva texto explícito y contexto, ocultando iconos decorativos si se amplía en otro encargo; no certificar accesibilidad web desde Figma. No se adopta la excepción de contraste warning de las variantes fuera del alcance.

### REQ-QA

Verificar texto Label/MXN/USD/EUR y contenido largo, tamaño HUG, estilos/bindings y cuatro temas desde Input. Comprobar que no se crearon las otras variantes ni controles de icono y que no se alteraron los consumidores actuales de Dot.
