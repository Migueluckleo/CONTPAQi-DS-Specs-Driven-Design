---
{
  "schema_version": 1,
  "id": "BADGE-001",
  "version": "1.1.0",
  "profile": "component",
  "status": "ELIGIBLE",
  "authority": {
    "kind": "DELEGATED",
    "decision_id": "ADR-025"
  },
  "targets": [
    "figma",
    "documentation"
  ],
  "readiness": {
    "figma": "READY",
    "documentation": "READY"
  },
  "profile_data": {
    "anatomy": [
      "container",
      "Left icon (optional Phosphor instance)",
      "Label",
      "Right icon (optional Phosphor instance)"
    ],
    "composition": "fixed-with-optional-instance-swaps",
    "accessibility": "defined-with-warning-contrast-exception"
  },
  "sources": [
    {
      "id": "SRC-USER",
      "path": "evidence/authorization/badge-full-request.txt",
      "sha256": "e330c5190cc3518dc0f1085283ce58d206729c52cb5e17889159d463567a895e"
    },
    {
      "id": "SRC-IDENTITY",
      "path": "evidence/badge-pilot/source/identity.json",
      "sha256": "7f07f4e70ceb8ff4fc4dedc2ef7dd6db50d1fb5047f5498ace1d4897dd93e8e9"
    },
    {
      "id": "SRC-SMALL",
      "path": "evidence/badge-pilot/source/small.json",
      "sha256": "58b6b89453bf3ae2e01870c56442878a2c2a25068659c0f2eb934931b62f5236"
    },
    {
      "id": "SRC-MEDIUM",
      "path": "evidence/badge-pilot/source/medium.json",
      "sha256": "7ac82eb8114f0768101f516258a54c9defb0edfee91ff451d5deee99de085732"
    },
    {
      "id": "SRC-LARGE",
      "path": "evidence/badge-pilot/source/large.json",
      "sha256": "db67a4d3c16affe23b6f2526e862df1a817392494063eeb3bc76e57bfc37e8a5"
    },
    {
      "id": "SRC-VARIABLES_AND_NOTES",
      "path": "evidence/badge-pilot/source/variables-and-notes.json",
      "sha256": "cc46e423fb350730e7941e6e234b00faf9f20ac649f9c2ab7650bb2afc51b170"
    },
    {
      "id": "SRC-VARIABLES_REMAINING",
      "path": "evidence/badge-pilot/source/variables-remaining.json",
      "sha256": "0247f9939e908937a5f8174e80d7d74a2b2fd301d745971417f51cb3bd802bcc"
    },
    {
      "id": "SRC-EXAMPLES",
      "path": "evidence/badge-pilot/source/examples.json",
      "sha256": "5e2a504323e6986be30cf316adcb2fceb875e5d61e2ad28e3ee50ed933b6ccf2"
    },
    {
      "id": "SRC-EXAMPLE_ICONS",
      "path": "evidence/badge-pilot/source/example-icons.json",
      "sha256": "5b8dc83f7d5c215a4b304f81b13db43c2a64909c27e071cb1001c601163b2b63"
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
    },
    {
      "kind": "token",
      "id": "badge.color-bg-error",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.spacing-compact",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.color-text-error",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.size-icon-small",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.color-icon-error",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.color-bg-warning",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.color-text-warning",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.color-icon-warning",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.color-bg-success",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.color-text-success",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.color-icon-success",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.color-bg-info",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.color-text-info",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.color-icon-info",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.color-icon-subtle",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.color-bg-neutral",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.size-height-medium",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.font-line-height-medium",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.size-icon-regular",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.spacing-large",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.size-height-large",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.font-size-large",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "badge.font-line-height-large",
      "relation": "uses"
    }
  ],
  "requirements": [
    {
      "id": "REQ-SCOPE",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-SMALL",
        "SRC-MEDIUM",
        "SRC-LARGE"
      ],
      "acceptance": [
        "Un único set compartido cubre las 18 combinaciones sin modificar el origen."
      ]
    },
    {
      "id": "REQ-API",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-SMALL",
        "SRC-MEDIUM",
        "SRC-LARGE"
      ],
      "acceptance": [
        "Comprobar ejes, defaults y cinco controles de contenido/iconos desde instancias."
      ]
    },
    {
      "id": "REQ-GEOMETRY",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-SMALL",
        "SRC-MEDIUM",
        "SRC-LARGE"
      ],
      "acceptance": [
        "Comparar métricas observadas con tolerancia 0.01 px y contenido HUG."
      ]
    },
    {
      "id": "REQ-TYPOGRAPHY",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-SMALL",
        "SRC-MEDIUM",
        "SRC-LARGE"
      ],
      "acceptance": [
        "Tres estilos aplicados conservan Manrope Regular, unidades y bindings."
      ]
    },
    {
      "id": "REQ-THEME",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-SMALL",
        "SRC-MEDIUM",
        "SRC-LARGE"
      ],
      "acceptance": [
        "Los cuatro modos conservan los mismos aliases y paints por rol."
      ]
    },
    {
      "id": "REQ-TOKENS",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-SMALL",
        "SRC-MEDIUM",
        "SRC-LARGE"
      ],
      "acceptance": [
        "35 firmas únicas; doce IDs conservados y veintitrés adiciones."
      ]
    },
    {
      "id": "REQ-CONSUMERS",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-SMALL",
        "SRC-MEDIUM",
        "SRC-LARGE"
      ],
      "acceptance": [
        "113 usos de Input y tres ejemplos previos conservan identidad, contenido y geometría."
      ]
    },
    {
      "id": "REQ-ICONS",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-SMALL",
        "SRC-MEDIUM",
        "SRC-LARGE"
      ],
      "acceptance": [
        "Comparar key, tamaño, bindings y color con Label tras swaps en cuatro temas."
      ]
    },
    {
      "id": "REQ-CONTENT",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-SMALL",
        "SRC-MEDIUM",
        "SRC-LARGE"
      ],
      "acceptance": [
        "Ejemplos de estados y monedas mantienen función no interactiva y etiqueta legible."
      ]
    },
    {
      "id": "REQ-A11Y",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-SMALL",
        "SRC-MEDIUM",
        "SRC-LARGE"
      ],
      "acceptance": [
        "Registrar warning insuficiente y separar contraste de implementación accesible web."
      ]
    },
    {
      "id": "REQ-QA",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-SMALL",
        "SRC-MEDIUM",
        "SRC-LARGE"
      ],
      "acceptance": [
        "Comprobante nativo cubre matriz, swaps y consumidores; revisión independiente explícita."
      ]
    }
  ]
}
---
# BADGE-001 · Badge 1.1.0

### REQ-SCOPE

Badge 1.1.0 sustituye el alcance temporal con las 18 combinaciones observadas en 1234:65377, página 1234:53606. Un único set compartido en Blue Heart DS; Dot conserva su función. Origen y proyecto anterior siguen en solo lectura. Este MD gobierna diseño/función; consumption/badge/current-build-plan.json es su receta derivada.

### REQ-API

type = neutral | subtle | info | success | warning | error; size = small | medium | large. Label TEXT editable, inicialmente Label. Show left icon y Show right icon BOOLEAN independientes, false por defecto; Left icon y Right icon INSTANCE_SWAP de Phosphor. Anatomy: Left icon → Label → Right icon. Sin Slots arbitrarios. No hay eje state, hover, focus, pressed, selected ni disabled; no crear variantes o tokens para ellos. Para compatibilidad se conserva el default existente subtle/small; las 18 combinaciones quedan disponibles. La raíz parte de neutral/large, diferencia explícita limitada al valor inicial del set local, sin alterar la apariencia de ninguna variante.

### REQ-GEOMETRY

Auto Layout horizontal HUG en ambos ejes, alineación vertical CENTER y horizontal MIN. Radio 4, gap 4, strokeAlign INSIDE y strokesIncludedInLayout=false. Small: padding 0 vertical /8 horizontal, Label 12/20, iconos 12; altura natural 20. Medium: padding 4/8, Label 12/16, iconos 16; altura natural y maxHeight 24. Large: padding 4/12, Label 14/24, iconos 16; altura natural y maxHeight 32. Conservar estas diferencias reales aunque la descripción raíz sugiera otra talla de icono. Solo subtle tiene borde de 1 px. Los anchos 46 (small/medium) y 59 (large) corresponden al ejemplo Label sin iconos, no son anchos fijos. Ancho HUG con texto o iconos visibles; sin truncado ni saltos automáticos. El contenedor host resuelve etiquetas que no caben sin escalar Badge ni recortarlo.

### REQ-TYPOGRAPHY

Manrope Regular, tracking 0 PIXELS, sin escala. Aplicar estilos compartidos según REQ-GEOMETRY: conservar ID de badge/subtle-small para todos los small; añadir badge/label-medium y badge/label-large. Verificar textStyleId y bindings de familia, estilo, tamaño, line-height y tracking.

### REQ-THEME

Todos los roles son INVARIANT: mismo alias en los cuatro modos de component. Neutral/subtle comparten texto/icono primary; neutral usa surface sin borde sobre superficies de color, subtle fondo tenue con borde. Info/success/warning/error usan los semánticos existentes de información/éxito/atención/fallo. No cambiar por tema de producto ni crear modos por tipo. Valores y aliases pertenecen al token set. La excepción humana que conserva warning se limita a Badge.

### REQ-TOKENS

BH-P07 gobierna minimización, capas, colecciones, scopes y nombres. Resultado: 360 usos y 35 firmas; doce variables conservadas y veintitrés adiciones, sin retirar IDs ni cambiar APIs. Neutral/subtle comparten texto e icono; TEXT_FILL/SHAPE_FILL requieren tokens separados. Gap y padding de 4 comparten spacing/compact; ambos iconos comparten ancho/alto por talla. HUG no requiere height-small; medium/large vinculan solo maxHeight. Todas las variables viven en component/badge, sin nuevos primitivos o semánticos. La tabla fija rutas Figma; CSS pertenece al token set.

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
| badge.color-bg-error | badge/color/bg/error |
| badge.spacing-compact | badge/spacing/compact |
| badge.color-text-error | badge/color/text/error |
| badge.size-icon-small | badge/size/icon-small |
| badge.color-icon-error | badge/color/icon/error |
| badge.color-bg-warning | badge/color/bg/warning |
| badge.color-text-warning | badge/color/text/warning |
| badge.color-icon-warning | badge/color/icon/warning |
| badge.color-bg-success | badge/color/bg/success |
| badge.color-text-success | badge/color/text/success |
| badge.color-icon-success | badge/color/icon/success |
| badge.color-bg-info | badge/color/bg/info |
| badge.color-text-info | badge/color/text/info |
| badge.color-icon-info | badge/color/icon/info |
| badge.color-icon-subtle | badge/color/icon/subtle |
| badge.color-bg-neutral | badge/color/bg/neutral |
| badge.size-height-medium | badge/size/height-medium |
| badge.font-line-height-medium | badge/font/line-height-medium |
| badge.size-icon-regular | badge/size/icon-regular |
| badge.spacing-large | badge/spacing/large |
| badge.size-height-large | badge/size/height-large |
| badge.font-size-large | badge/font/size-large |
| badge.font-line-height-large | badge/font/line-height-large |

### REQ-CONSUMERS

Input usa solo subtle/small para monedas ISO (MXN/USD), con Label editable, instancia expuesta inicialmente oculta y pin BADGE-001@1.1.0. Ampliar set/variante existentes conserva instancias, sin swaps destructivos. Auditar todas las páginas y preservar IDs, texto, visibilidad, vínculo, geometría y overrides legítimos de los 113 usos de Input y los tres ejemplos de Badge. No dejar otro Badge privado/temporal. Tab mantiene Dot; no sustituir sus contadores. Conservar corte previo y mapa de migración.

### REQ-ICONS

Aplicar BH-P06: Phosphor del equipo en Figma y paquete oficial en desarrollo futuro. Default: Presentation Outline/Fill, key 3f0d7ae9a02577d4fb4e615737d09fa1b49ec230; placeholder intercambiable de la raíz, sin significado de estado. Los ejemplos usan CheckCircle, WarningCircle e Info Light. Ambos lados son decorativos y opcionales; su token SHAPE_FILL comparte todos los aliases de Label, con tamaño WIDTH_HEIGHT. Mantener vínculo remoto, sin copiar paths ni editar maestros. Verificar swaps visibles en cuatro temas. El icono derecho informa; nunca cierra.

### REQ-CONTENT

Etiqueta no interactiva para estado o atributo. Success: concluido; warning: atención sin bloquear; error: fallo/negativo; info: en curso/informativo; subtle/neutral: metadatos. Un mismo estado mantiene tipo entre productos. Small: tablas/listas densas; medium: estándar; large: detalle. Un tamaño por lista/tabla. Sentence case; recomendar 1–3 palabras y ≤20 caracteres, sin imponer un máximo del API. No truncar: el host abrevia o usa una notificación cuando no cabe. Mantener concordancia, término fiscal correcto, fecha día-mes y moneda ISO; excluir montos y datos sensibles. No apilar estados ni usar Badge como botón o chip removible.

### REQ-A11Y

El texto describe el estado; color e icono no son el único medio. Sin foco, interacción ni reacciones de prototipo. En web futura los iconos son decorativos aria-hidden y el host aporta contexto y aria-live cuando cambie un estado en tiempo real. La fuente reconoce warning alrededor de 3:1, inferior a 4.5:1 para texto pequeño; la elección humana conserva esos colores. Registrar cálculo desde los valores reales, no redondear a cumplimiento AA. Las demás mediciones se documentan como contraste de color, sin certificar accesibilidad funcional web desde Figma. El host mantiene texto claro y puede reforzar warning crítico con icono izquierdo.

### REQ-QA

Validar 18 variantes, API/defaults, tres estilos aplicados y métricas contra fuente: tolerancia 0.01 px y color 1e-6; identidades/aliases/scopes/WEB/nombres exactos. Desde instancias cubrir 18×4 temas×4 combinaciones de iconos (ninguno/izquierdo/derecho/ambos), texto corto/largo, swaps Phosphor, invariancia y contraste con warning exceptuado. Activar Show badge desde cada combinación de Input y conservar consumidores anteriores. Separar infraestructura, QA visual y revisión independiente en el comprobante.
