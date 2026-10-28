---
{
  "schema_version": 1,
  "id": "LOADER-001",
  "version": "1.0.0",
  "profile": "component",
  "status": "ELIGIBLE",
  "authority": {
    "kind": "DELEGATED",
    "decision_id": "ADR-022"
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
      "path": "evidence/authorization/loader-dependency-request.txt",
      "sha256": "def9511ea1100631f7cccceb26f7f6e69a4813792abe882f05aa27b5b6865d33"
    },
    {
      "id": "SRC-FIGMA",
      "path": "evidence/loader-pilot/source/public.json",
      "sha256": "193d4c82c28dfafbf01b2e14e92628d7cdcad691fe13070a115a27cb3e8203ef"
    },
    {
      "id": "SRC-ANIMATION",
      "path": "evidence/loader-pilot/source/animation.json",
      "sha256": "009559f1416e56b6b0ccf5bb830dba5c4cf272c488a599b761c4c197d763b2e0"
    },
    {
      "id": "SRC-BUTTON",
      "path": "evidence/loader-pilot/source/button-loading.json",
      "sha256": "da728dfa7e7d48706e15d6261247ea787f1afd6ffb22426afb3a2987882aa925"
    }
  ],
  "dependencies": [
    {
      "kind": "token",
      "id": "loader.color-stroke-primary-default",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "loader.color-stroke-secondary",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "loader.color-stroke-strong",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "loader.color-stroke-inverse",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "loader.color-stroke-track",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "loader.size-extra-small",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "loader.size-small",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "loader.size-medium",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "loader.size-large",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "loader.size-extra-large",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "loader.size-2x-large",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "loader.border-width-regular",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "loader.border-width-large",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "loader.border-width-extra-large",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "loader.border-width-2x-large",
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
        "SRC-FIGMA",
        "SRC-ANIMATION"
      ],
      "acceptance": [
        "Comprobar el requisito contra su receta, evidencia fuente y destino; registrar límites y resultado del alcance."
      ]
    },
    {
      "id": "REQ-API",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-FIGMA",
        "SRC-ANIMATION"
      ],
      "acceptance": [
        "Comprobar el requisito contra su receta, evidencia fuente y destino; registrar límites y resultado del alcance."
      ]
    },
    {
      "id": "REQ-GEOMETRY",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-FIGMA",
        "SRC-ANIMATION"
      ],
      "acceptance": [
        "Comprobar el requisito contra su receta, evidencia fuente y destino; registrar límites y resultado del alcance."
      ]
    },
    {
      "id": "REQ-THEME",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-FIGMA",
        "SRC-ANIMATION"
      ],
      "acceptance": [
        "Comprobar el requisito contra su receta, evidencia fuente y destino; registrar límites y resultado del alcance."
      ]
    },
    {
      "id": "REQ-TOKENS",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-FIGMA",
        "SRC-ANIMATION"
      ],
      "acceptance": [
        "Comprobar el requisito contra su receta, evidencia fuente y destino; registrar límites y resultado del alcance."
      ]
    },
    {
      "id": "REQ-ANIMATION",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-FIGMA",
        "SRC-ANIMATION"
      ],
      "acceptance": [
        "Comprobar el requisito contra su receta, evidencia fuente y destino; registrar límites y resultado del alcance."
      ]
    },
    {
      "id": "REQ-BEHAVIOR",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-FIGMA",
        "SRC-ANIMATION"
      ],
      "acceptance": [
        "Comprobar el requisito contra su receta, evidencia fuente y destino; registrar límites y resultado del alcance."
      ]
    },
    {
      "id": "REQ-A11Y",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-FIGMA",
        "SRC-ANIMATION"
      ],
      "acceptance": [
        "Comprobar el requisito contra su receta, evidencia fuente y destino; registrar límites y resultado del alcance."
      ]
    },
    {
      "id": "REQ-CONSUMERS",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-FIGMA",
        "SRC-ANIMATION"
      ],
      "acceptance": [
        "Comprobar el requisito contra su receta, evidencia fuente y destino; registrar límites y resultado del alcance."
      ]
    },
    {
      "id": "REQ-DOCUMENTATION",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-FIGMA",
        "SRC-ANIMATION"
      ],
      "acceptance": [
        "Comprobar el requisito contra su receta, evidencia fuente y destino; registrar límites y resultado del alcance."
      ]
    },
    {
      "id": "REQ-QA",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-FIGMA",
        "SRC-ANIMATION"
      ],
      "acceptance": [
        "Comprobar el requisito contra su receta, evidencia fuente y destino; registrar límites y resultado del alcance."
      ]
    }
  ],
  "profile_data": {
    "anatomy": [
      "container",
      "Spinner instance",
      "Track ellipse",
      "Arc ellipse"
    ],
    "composition": "fixed",
    "accessibility": "defined"
  }
}
---
# LOADER-001 · Loader 1.0.0

### REQ-SCOPE

Crear Loader en su propia página del destino Blue Heart DS; fuente 3917:1263 y proyecto anterior en solo lectura. No habilita componentes ajenos, React ni publicación de biblioteca.

### REQ-API

Conservar size extra-small/small/medium/large/extra-large/2x-large y color brand/neutral/strong/on-color: 24 variantes. No añadir hover, focus, pressed o disabled. No recibe texto ni Slots arbitrarios; el mensaje pertenece al host. Los nombres públicos color conservan la API fuente; los tokens expresan función, no nombre de paleta.

### REQ-GEOMETRY

Dimensiones cuadradas 16/20/24/40/64/88 px; trazos 2/2/2/4/6/8 px INSIDE. Track circular completo sin relleno ni remate; Arc de 90° con remates ROUND. Superponer las dos elipses dentro del cuadro fijo: geometría de arco y posición son constantes nativas, no padding/radius ficticios. El wrapper usa centrado auto-layout sin padding ni gap operativo. No crear tipografía oculta.

### REQ-THEME

Solo primary-default (arco de color brand) sigue el vector de marca de los cuatro modos existentes. Secondary, strong, inverse, track, dimensiones y grosores son invariantes. Brand/neutral/strong usan track neutral-muted opaco; on-color comparte el token inverse entre arco y track, con opacidad de nodo 0.3 solo en el track. Conservar ese alpha fuente sin crear un color semántico duplicado, tema artificial ni excepción morada de Tab. Los vectores exactos pertenecen al token set seleccionado.

### REQ-TOKENS

Aplicar BH-P07: 15 firmas únicas, cinco STROKE_COLOR, seis WIDTH_HEIGHT y cuatro STROKE_FLOAT. Compartir 2 px entre los primeros tres tamaños; compartir inverse entre arco y riel on-color. Component → semantic → primitive; exactamente tres colecciones. Añadir únicamente primitive.size-88 y semantic.size-8xl, scopes vacíos, porque la dimensión fuente 88 carecía de alias compatible. No reutilizar font-size para una dimensión ni crear variables por cuadro o por combinación.

| ID lógico | Ruta Figma |
|---|---|
| loader.color-stroke-primary-default | loader/color/stroke/primary-default |
| loader.color-stroke-secondary | loader/color/stroke/secondary |
| loader.color-stroke-strong | loader/color/stroke/strong |
| loader.color-stroke-inverse | loader/color/stroke/inverse |
| loader.color-stroke-track | loader/color/stroke/track |
| loader.size-extra-small | loader/size/extra-small |
| loader.size-small | loader/size/small |
| loader.size-medium | loader/size/medium |
| loader.size-large | loader/size/large |
| loader.size-extra-large | loader/size/extra-large |
| loader.size-2x-large | loader/size/2x-large |
| loader.border-width-regular | loader/border/width-regular |
| loader.border-width-large | loader/border/width-large |
| loader.border-width-extra-large | loader/border/width-extra-large |
| loader.border-width-2x-large | loader/border/width-2x-large |

### REQ-ANIMATION

24 fases por tamaño; cada fase cambia a la siguiente con AFTER_TIMEOUT 0.03333333507180214 s y CHANGE_TO sin transición; fase 24 vuelve a 1. Arco avanza 15° por cuadro en sentido horario, vuelta nominal 0.8 s. Conservar arcData exacta del snapshot, no Smart Animate. Seis sets internos de 24 variantes quedan fuera de la documentación y no son API de consumo. Color/opacity de cada instancia pública debe persistir durante todo el ciclo y el retorno; una conexión almacenada no demuestra reproducción real ni 30 fps medidos.

### REQ-BEHAVIOR

Indicador de espera indeterminada, sin acciones ni foco. Mostrarlo al superar aproximadamente 300 ms para evitar parpadeo; conservar el contenido previo en actualizaciones parciales. Si supera 2 s, acompañar con mensaje de proceso en gerundio y elipsis, nombrando al tercero cuando corresponda. Si supera 10 s y existe avance conocido, preferir un progreso determinado, sin construir esa otra familia aquí. No programar temporizadores o servicios en Figma. Evitar cargas simultáneas innecesarias; no usarlo como único indicador de error.

### REQ-A11Y

El host funcional debe proporcionar role=status, aria-live=polite y nombre accesible Cargando… o el proceso; Button anuncia aria-busy y bloquea activaciones. Con prefers-reduced-motion debe ofrecer vuelta de 1.6 s o mensaje estático: obligación futura web, no capacidad demostrada del prototipo Figma. Medir contraste del arco con su fondo real, objetivo 3:1; los ratios de la descripción no son certificación WCAG. No usar on-color sobre blanco.

### REQ-CONSUMERS

Auditar todas las páginas con hijos invisibles incluidos conforme BH-P01 REQ-P01-07. Button es consumidor directo existente: small→extra-small, medium→small, large→medium; primary/danger→on-color, secondary/link→brand, text→strong. Sustituir maestros primero y releer consumidores heredados sin resetear overrides ajenos. Retirar los tres helpers Button y dos colores exclusivos solo con cero referencias, conservando historia y mapa. Corregir el riel y remate desviados de Button conforme a su fuente real. No incorporar Loader a Tab, Tabs, Avatar, Avatar group o Dot por recomendaciones textuales.

### REQ-DOCUMENTATION

Overview, matriz de 24 variantes y ejemplos en contexto con instancias vinculadas editables; maestros y fases fuera del frame de revisión. Mostrar tamaños, función del color, dependencia Button, cuatro temas y límites de ejecución. MD es autoridad; recetas/ledger/CSV derivan de él y del token set por hash.

### REQ-QA

Validar 24 combinaciones, 144 fases/cierre por ID, colores/opacity durante reproducción, cuatro temas desde instancias, scopes/aliases/WEB/rutas, 15 firmas y cero referencias retiradas. Tolerancia geométrica 0.00001 por representación float Figma, identidades/aliases exactos. Contrastar los 90 principales Button y sus consumidores: geometría, etiquetas, iconos, visibilidad y reacciones ajenas intactas. Separar QA nativo de pruebas del núcleo y de revisión independiente no ejecutada.
