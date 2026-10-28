---
{
  "schema_version": 1,
  "id": "DOT-001",
  "version": "1.0.0",
  "profile": "component",
  "status": "ELIGIBLE",
  "authority": {
    "kind": "DELEGATED",
    "decision_id": "ADR-021"
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
      "id": "SRC-USER-DOT",
      "path": "evidence/authorization/dot-dependency-request.txt",
      "sha256": "13c94305c8dc4f6dcf44311f0197de27d164716ec08ad5c6e32c58c22705e533"
    },
    {
      "id": "SRC-FIGMA",
      "path": "evidence/dot-pilot/source/variants.json",
      "sha256": "3900e1848081c6e65783d661dda5b2a69821d5130c94fd99952f545fc78d987d"
    },
    {
      "id": "SRC-VARIABLES",
      "path": "evidence/dot-pilot/source/variables.json",
      "sha256": "43b931d9d7f27c2acd940f097a653042cc638c81395fdf119c570b7eab82ba57"
    },
    {
      "id": "SRC-DESCRIPTION",
      "path": "evidence/dot-pilot/source/discovery.json",
      "sha256": "b4f436c444ed46f07fadf73e9b19a5b065d8e85408ee31ff4b3f83af7704f0b7"
    }
  ],
  "dependencies": [
    {
      "kind": "token",
      "id": "dot.color-bg-active",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "dot.color-bg-alert",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "dot.color-bg-inactive",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "dot.color-stroke-separator",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "dot.color-text-inverse",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "dot.size-presence-small",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "dot.size-presence-medium",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "dot.size-regular",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "dot.size-count-large",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "dot.radius-container",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "dot.border-width-regular",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "dot.spacing-none",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "dot.spacing-counter-inline",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "dot.font-family",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "dot.font-count-style",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "dot.font-size-large",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "dot.font-size-medium",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "dot.font-line-height",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "dot.font-letter-spacing",
      "relation": "uses"
    }
  ],
  "requirements": [
    {
      "id": "REQ-SCOPE",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER-DOT",
        "SRC-FIGMA"
      ],
      "acceptance": [
        "Página y principales dentro del destino autorizado; fuentes solo lectura."
      ]
    },
    {
      "id": "REQ-API",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-DESCRIPTION",
        "SRC-FIGMA"
      ],
      "acceptance": [
        "16 combinaciones válidas y propiedades de texto independientes."
      ]
    },
    {
      "id": "REQ-GEOMETRY",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-FIGMA",
        "SRC-VARIABLES"
      ],
      "acceptance": [
        "Métricas, ancho adaptable, padding y separación coinciden con la receta fuente."
      ]
    },
    {
      "id": "REQ-THEME",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-VARIABLES"
      ],
      "acceptance": [
        "Los cuatro temas conservan los mismos aliases y valores resueltos."
      ]
    },
    {
      "id": "REQ-TYPOGRAPHY",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-FIGMA",
        "SRC-VARIABLES"
      ],
      "acceptance": [
        "Fuentes, métricas, aliases y vínculos a estilos comprobados en instancias."
      ]
    },
    {
      "id": "REQ-TOKENS",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER-DOT",
        "SRC-VARIABLES"
      ],
      "acceptance": [
        "19 firmas únicas con scope, WEB y rutas de esta sección."
      ]
    },
    {
      "id": "REQ-BEHAVIOR",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-DESCRIPTION",
        "SRC-FIGMA"
      ],
      "acceptance": [
        "El principal no calcula ni convierte datos; controles del consumidor documentados."
      ]
    },
    {
      "id": "REQ-A11Y",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-DESCRIPTION"
      ],
      "acceptance": [
        "Semántica del host y limitaciones registradas sin certificación web."
      ]
    },
    {
      "id": "REQ-CONSUMERS",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER-DOT"
      ],
      "acceptance": [
        "Consumidores directos/transitivos migrados y sin referencias a helpers retirados."
      ]
    },
    {
      "id": "REQ-DOCUMENTATION",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER-DOT",
        "SRC-FIGMA"
      ],
      "acceptance": [
        "Overview, variantes y ejemplos editables enlazan principales reales."
      ]
    },
    {
      "id": "REQ-QA",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER-DOT",
        "SRC-FIGMA"
      ],
      "acceptance": [
        "Casos de instancias, datos, temas y preservación registrados por destino."
      ]
    }
  ],
  "profile_data": {
    "anatomy": [
      "container",
      "optional Count or Max count text"
    ],
    "composition": "fixed",
    "accessibility": "defined"
  }
}
---
# DOT-001 · Dot 1.0.0

### REQ-SCOPE

Dot es un indicador sin interacción. Crear un set en su página del destino, con maestros fuera de documentación. Mantener fuentes en solo lectura; esta alta no formaliza Icon Button.

### REQ-API

Conservar type active/busy/inactive/notification/count/count-expand y size large/medium/small. Son 16 combinaciones: presencia/notificación en los tres tamaños; count/count-expand solo large y medium. Count es TEXT con valor inicial 1; Max count es TEXT independiente, inicial 99+. No generar combinaciones small de contador ni estados hover/focus/pressed.

### REQ-GEOMETRY

Presencia y notification miden 16/12/8 px. Count usa 20/16 px, ancho HUG con mínimos 20/16; count-expand usa altura 20/16 y ancho HUG con padding horizontal 4 px, sin mínimo de ancho. Radio completo y borde blanco 1 px OUTSIDE, strokesIncludedInLayout=false. Conservar geometría y centrado. Padding 2 px no vinculado de notification medium/small con layout NONE es metadato inerte, no un uso operativo que justifique un token nuevo.

### REQ-THEME

Todos los roles Dot son invariantes. Active usa positive-default, busy/notification/count/count-expand comparten danger-default, inactive neutral-medium; texto y separador neutral-base con scopes distintos. Conservar los mismos aliases en los cuatro modos existentes de component. No heredar el color de marca ni la excepción morada de Tab.

### REQ-TYPOGRAPHY

El contador usa Manrope Bold, 12/16 px en large y 10/16 px en medium, letter-spacing 0. Crear estilos compartidos dot/count/large y dot/count/medium vinculados a los tokens, y aplicar sus IDs al finalizar. Los tipos sin texto no crean un texto invisible ni otro estilo.

### REQ-TOKENS

Aplicar BH-P07: 19 firmas directas únicas en component bajo dot/color, dot/font, dot/radius, dot/size, dot/border y dot/spacing. El tamaño 16 px se comparte entre presencia large y contador medium; alert se comparte entre cuatro tipos. Reutilizar semánticos existentes; no crear nuevas primitivas, semánticos ni colecciones.

| ID lógico | Ruta Figma |
|---|---|
| dot.color-bg-active | dot/color/bg/active |
| dot.color-bg-alert | dot/color/bg/alert |
| dot.color-bg-inactive | dot/color/bg/inactive |
| dot.color-stroke-separator | dot/color/stroke/separator |
| dot.color-text-inverse | dot/color/text/inverse |
| dot.size-presence-small | dot/size/presence-small |
| dot.size-presence-medium | dot/size/presence-medium |
| dot.size-regular | dot/size/presence-large-count-medium |
| dot.size-count-large | dot/size/count-large |
| dot.radius-container | dot/radius/container |
| dot.border-width-regular | dot/border/width-regular |
| dot.spacing-none | dot/spacing/none |
| dot.spacing-counter-inline | dot/spacing/counter-inline |
| dot.font-family | dot/font/family |
| dot.font-count-style | dot/font/count-style |
| dot.font-size-large | dot/font/size-large |
| dot.font-size-medium | dot/font/size-medium |
| dot.font-line-height | dot/font/line-height |
| dot.font-letter-spacing | dot/font/letter-spacing |

### REQ-BEHAVIOR

El cambio recomendado count/count-expand parte de un conteo numérico sin formato. La integración Tab conserva su texto ya formateado (incluido 99+) en count/medium para preservar su geometría; no aplicar esa recomendación como conversión automática.

La representación Figma no calcula, consulta ni se actualiza sola. El consumidor selecciona presencia en tiempo real cuando corresponda; count=0 debe ocultarse por el consumidor. Para 1..99 usa count y desde 100 count-expand con Max count, normalmente 99+. Count y Max count son strings independientes: cambiar uno no modifica el otro ni la visibilidad o variante. La fuente no contiene reacciones; no prometer umbral, temporizador, truncado o conversión automática en el principal.

### REQ-A11Y

El indicador no recibe foco ni ejecuta acciones. Acompañar presencia con texto/tooltip y conteos con nombre accesible; el host resuelve semántica, anuncios y actualizaciones. No usar solo color ni presentar busy como notificación. Medir contraste con colores resueltos; Figma y un test de infraestructura no certifican ARIA o accesibilidad de navegador.

### REQ-CONSUMERS

Avatar consume presencia y Tab count/medium; Avatar group y Tabs heredan esas dependencias. Aplicar BH-P01 REQ-P01-07: conservar datos, visibilidad y geometría con mapa y pruebas de reemplazo. Retirar helpers, nueve tokens y un estilo solo con cero referencias actuales; preservar historia exacta. Button no adquiere Dot.

### REQ-DOCUMENTATION

Overview y Variants & states contienen Type, Size e In context con muestras vinculadas y texto editable. Mostrar combinaciones disponibles y responsabilidades del consumidor; corregir textos ajenos de Modal/Button. Los hosts de icono son fixtures, sin crear Icon Button.

### REQ-QA

Validar 16 variantes, 19 firmas, scopes/aliases/WEB/rutas, fuentes y estilos desde instancias con 1, 12, 99+ y 999+. Verificar cuatro temas invariantes, migraciones Avatar/Tab y cero referencias retiradas. Registrar evidencia y límites del destino.
