---
{
  "schema_version": 1,
  "id": "TABS-001",
  "version": "3.1.0",
  "profile": "component",
  "status": "ELIGIBLE",
  "authority": {
    "kind": "DELEGATED",
    "decision_id": "ADR-024"
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
      "path": "evidence/authorization/tabs-page-reconciliation-request.txt",
      "sha256": "9bcf56c28470c2aa1fce3b3ad24a82207b58ab67af5f066a336dfe709a37843d"
    },
    {
      "id": "SRC-GROUP",
      "path": "evidence/tabs-page-reconciliation/source/groups.json",
      "sha256": "96464f0a61e0bffebde03ec1f3cc28118fa3e6724b3df194f9417a259d45e2b8"
    },
    {
      "id": "SRC-INVENTORY",
      "path": "evidence/tabs-page-reconciliation/source/inventory.json",
      "sha256": "8dbf33ed1cb57448983423f5f51ac59397204187f5fab4200e8bef195828aa89"
    },
    {
      "id": "SRC-COLLECTION",
      "path": "evidence/authorization/component-collection-request.txt",
      "sha256": "041814c7ca461cddd8d809a5ae3e9f179fdd096b92832c95f57efae3fb2eb11e"
    },
    {
      "id": "SRC-USER-DOT",
      "path": "evidence/authorization/dot-dependency-request.txt",
      "sha256": "13c94305c8dc4f6dcf44311f0197de27d164716ec08ad5c6e32c58c22705e533"
    },
    {
      "id": "SRC-ICON-ALIGNMENT",
      "path": "evidence/authorization/icon-color-alignment-request.txt",
      "sha256": "35568ec00f70dd642e02b342c165506315874951b932afd9c6c298fbae93a59f"
    }
  ],
  "dependencies": [
    {
      "kind": "contract",
      "id": "TAB-001",
      "version": "3.1.0",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tabs.color-tabs-divider-default",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tabs.size-tabs-divider",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tabs.spacing-tabs-container",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tabs.radius-tabs-container",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tabs.color-tabs-bg-segmented-default",
      "relation": "uses"
    }
  ],
  "requirements": [
    {
      "id": "REQ-IDENTITY",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-GROUP",
        "SRC-INVENTORY",
        "SRC-USER-DOT"
      ],
      "acceptance": [
        "Tres variantes de grupo en el destino; fuentes solo lectura."
      ]
    },
    {
      "id": "REQ-SLOT",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-GROUP",
        "SRC-INVENTORY"
      ],
      "acceptance": [
        "Slot nativo con límites, preferredValues y operaciones desde instancias comprobados."
      ]
    },
    {
      "id": "REQ-TYPE",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-GROUP",
        "SRC-INVENTORY"
      ],
      "acceptance": [
        "Tipos coherentes entre grupo e hijos; coordinación del consumidor documentada."
      ]
    },
    {
      "id": "REQ-SELECTION",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-GROUP",
        "SRC-INVENTORY"
      ],
      "acceptance": [
        "Una selección y panel correspondiente; sin automatismos atribuidos al slot."
      ]
    },
    {
      "id": "REQ-LAYOUT",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-GROUP",
        "SRC-INVENTORY"
      ],
      "acceptance": [
        "Geometría por tipo, Divider estirado y foco sin recorte."
      ]
    },
    {
      "id": "REQ-TOKENS",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-GROUP",
        "SRC-INVENTORY",
        "SRC-USER-DOT"
      ],
      "acceptance": [
        "Cinco firmas propias invariantes; herencia de tokens del hijo sin duplicados."
      ]
    },
    {
      "id": "REQ-CONTENT",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-GROUP",
        "SRC-INVENTORY"
      ],
      "acceptance": [
        "Ejemplos de cardinalidad, contenido largo y reordenamiento probados."
      ]
    },
    {
      "id": "REQ-DOCUMENTATION",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-GROUP",
        "SRC-INVENTORY"
      ],
      "acceptance": [
        "Overview y variantes editables con todas las secciones y muestras vinculadas."
      ]
    },
    {
      "id": "REQ-ACCESSIBILITY",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-GROUP",
        "SRC-INVENTORY"
      ],
      "acceptance": [
        "Semántica web y responsabilidades del consumidor sin certificación de Figma."
      ]
    },
    {
      "id": "REQ-QA",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-GROUP",
        "SRC-INVENTORY",
        "SRC-USER-DOT"
      ],
      "acceptance": [
        "Casos de consumidor, cardinalidad, vínculos, modos y foco registrados en BH-P04."
      ]
    },
    {
      "id": "REQ-COLLECTION",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-COLLECTION",
        "SRC-USER-DOT"
      ],
      "acceptance": [
        "Colección component y grupo propio; regla única BH-P07, equivalencias actuales ADR-021."
      ]
    },
    {
      "id": "REQ-SHARED-DOT",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-USER-DOT"
      ],
      "acceptance": [
        "Consumir DOT-001@1.0.0 mediante el contrato hijo vigente y el mapa de migración; no reconstruir el helper privado anterior."
      ]
    },
    {
      "id": "REQ-ICON-COLOR",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-ICON-ALIGNMENT"
      ],
      "acceptance": [
        "Comparar aliases completos y colores resueltos con el texto correspondiente en cuatro temas, estados, opcionales visibles, swaps y consumidores; conservar identidad, geometría y reacciones."
      ]
    }
  ],
  "profile_data": {
    "anatomy": [
      "container",
      "editable Tabs slot",
      "linked Tab instances",
      "underline Divider"
    ],
    "composition": "Native slot: four default linked Tab instances, minimum two, no hard maximum. Same type; one selected.",
    "accessibility": "Tablist and keyboard/panel behavior belong to the consuming implementation; Figma slot is not executable HTML/ARIA."
  }
}
---
# Tabs · contrato de grupo

### REQ-IDENTITY

Tabs es el grupo, distinto de Tab individual. Reproducir las tres variantes fuente type=underline/pill/segmented en la página Tabs de Blue Heart DS. Las fuentes permanecen en solo lectura.

### REQ-SLOT

Conservar un slot nativo Tabs con cuatro instancias por defecto, mínimo 2, sin máximo técnico. stretchChildOnInsert=false, displayEmptyByDefault=false y allowPreferredValuesOnly=false; preferredValues referencia el set Tab del destino. Agregar, quitar y reordenar desde una instancia del grupo, conservando vínculos. No reemplazar el slot por cuatro propiedades fijas o por un frame inmutable.

### REQ-TYPE

Las Tabs del slot deben tener el mismo type que el grupo. El consumidor coordina ese dato al cambiar una composición personalizada; no prometer sincronización automática no probada. Cada Tab conserva sus propiedades Label, selected, state, Icon y Show badge.

### REQ-SELECTION

La primera Tab viene seleccionada y las demás no. El consumidor conserva exactamente una selección y el panel correspondiente; no atribuir selección automática a un slot editable. La receta de grupo no agrega lógica de negocio a los principales.

### REQ-LAYOUT

underline: slot horizontal con gap 0 y Divider absoluto inferior de 1 px, ancho que sigue al grupo y color de borde observado. pill: slot horizontal con gap 4 sin contenedor pintado. segmented: padding 4, radio 8, fondo neutral sutil y slot con gap 4. Grupo y slot HUG, centrado vertical y clipsContent=false; el foco del hijo puede sobresalir. El ancho de cuatro etiquetas fuente no es un límite.

### REQ-TOKENS

Cinco tokens directos propios: color del Divider (SHAPE_FILL por ser un rectángulo), altura del Divider (WIDTH_HEIGHT), gap/padding (GAP), radio (CORNER_RADIUS) y fondo segmented (FRAME_FILL). Alias a semánticos existentes, un scope cada uno y nombres funcionales. No duplicar los tokens del hijo ni fusionar familias por igualdad de valor. Los cinco tokens viven bajo tab en component y son invariantes en sus cuatro modos. El modo component del contenedor controla también los hijos, conforme a BH-P07 REQ-P07-07.

### REQ-CONTENT

Cuatro elementos son la muestra inicial, mínimo 2 es el límite del slot. Recomendado máximo 6; segmented ideal 2–5 opciones similares. Son recomendaciones, no maxChildren. Probar 2 y 6, contenido largo, reordenamiento, opcionales y cambio de selección desde la instancia.

### REQ-DOCUMENTATION

La página incluye los dos sets, Overview con ejemplos Facturas/Pagos/Notas de crédito/Complementos, Todos/Vigentes/Cancelados/Por timbrar y Lista/Tarjetas/Calendario; Variants & states contiene Type, Selected, State e Icon & badge y sus notas. Todas las muestras usan instancias vinculadas. La documentación es editable; no aplanar la página como imagen.

### REQ-ACCESSIBILITY

En web, el grupo usa tablist, coordina aria-selected, aria-controls, IDs, foco y activación manual/automática con sus paneles. La representación Figma no certifica HTML/ARIA o teclado web. El contrato del hijo gobierna tipografía, estados e iconografía Phosphor.

### REQ-QA

Verificar desde una instancia, no solo en principales: cardinalidad menor y mayor que cuatro, orden y etiqueta, vínculos, único selected, tipos coherentes, Divider estirado, foco sin clip y scopes/aliases/nombres reales. Registrar límites del slot y conservar los resultados en un comprobante único BH-P04. Las pruebas del núcleo no sustituyen QA de Figma.

### REQ-COLLECTION

Seleccionar `component/tab`. [BH-P07 REQ-P07-07](../../protocols/07-COMPONENT-TOKENS.md#req-p07-07) gobierna colecciones y modos. El [mapa ADR-021](../../evidence/dot-pilot/migration-map.json) enlaza IDs y equivalencias actuales; el [índice histórico](../../evidence/dot-pilot/history/manifest.json) conserva ADR-020 y versiones previas. Consultar [QA vigente](../../evidence/qa/dot-pilot-check.json).

### REQ-SHARED-DOT

Tabs 3.0.0 fija TAB-001@3.0.0. Dot se consume transitivamente por Badge; los cinco tokens propios y el slot permanecen. El mapa ADR-021 y el QA actual conservan la trazabilidad de hijos y overrides.

La dependencia Tab 3.1.0 propaga los colores de sus iconos. Verificar los tres principales del grupo, slots y consumidores sin modificar sus IDs o su composición.

### REQ-ICON-COLOR

Aplicar BH-P06 REQ-P06-03/04 bajo ADR-024. Los hijos mantienen su contrato Tab; el grupo no crea otra paleta de iconos. Validar la herencia y los overrides en las instancias anidadas.
