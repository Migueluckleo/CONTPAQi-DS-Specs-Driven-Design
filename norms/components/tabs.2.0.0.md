---
{
  "schema_version": 1,
  "id": "TABS-001",
  "version": "2.0.0",
  "profile": "component",
  "status": "ELIGIBLE",
  "authority": {
    "kind": "DELEGATED",
    "decision_id": "ADR-020"
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
    }
  ],
  "dependencies": [
    {
      "kind": "contract",
      "id": "TAB-001",
      "version": "2.0.0",
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
        "SRC-INVENTORY"
      ],
      "acceptance": [
        "Tabs es el grupo, distinto de Tab individual. Reproducir las tres variantes fuente type=underline/pill/segmented en la página Tabs de Blue Heart DS. Las fuentes permanecen en solo lectura."
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
        "Conservar un slot nativo Tabs con cuatro instancias por defecto, mínimo 2, sin máximo técnico. stretchChildOnInsert=false, displayEmptyByDefault=false y allowPreferredValuesOnly=false; preferredValues referencia el set Tab del destino. Agregar, quitar y reordenar desde una instancia del grupo, conservando vínculos. No reemplazar el slot por cuatro propiedades fijas o por un frame inmutable."
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
        "Las Tabs del slot deben tener el mismo type que el grupo. El consumidor coordina ese dato al cambiar una composición personalizada; no prometer sincronización automática no probada. Cada Tab conserva sus propiedades Label, selected, state, Icon y Show badge."
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
        "La primera Tab viene seleccionada y las demás no. El consumidor conserva exactamente una selección y el panel correspondiente; no atribuir selección automática a un slot editable. La receta de grupo no agrega lógica de negocio a los principales."
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
        "underline: slot horizontal con gap 0 y Divider absoluto inferior de 1 px, ancho que sigue al grupo y color de borde observado. pill: slot horizontal con gap 4 sin contenedor pintado. segmented: padding 4, radio 8, fondo neutral sutil y slot con gap 4. Grupo y slot HUG, centrado vertical y clipsContent=false; el foco del hijo puede sobresalir. El ancho de cuatro etiquetas fuente no es un límite."
      ]
    },
    {
      "id": "REQ-TOKENS",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-GROUP",
        "SRC-INVENTORY"
      ],
      "acceptance": [
        "Cinco tokens directos propios: color del Divider (SHAPE_FILL por ser un rectángulo), altura del Divider (WIDTH_HEIGHT), gap/padding (GAP), radio (CORNER_RADIUS) y fondo segmented (FRAME_FILL). Alias a semánticos existentes, un scope cada uno y nombres funcionales. No duplicar los tokens del hijo ni fusionar familias por igualdad de valor. Los cinco tokens viven bajo tab en component y son invariantes en sus cuatro modos. El modo component del contenedor controla también los hijos, conforme a BH-P07 REQ-P07-07."
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
        "Cuatro elementos son la muestra inicial, mínimo 2 es el límite del slot. Recomendado máximo 6; segmented ideal 2–5 opciones similares. Son recomendaciones, no maxChildren. Probar 2 y 6, contenido largo, reordenamiento, opcionales y cambio de selección desde la instancia."
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
        "La página incluye los dos sets, Overview con ejemplos Facturas/Pagos/Notas de crédito/Complementos, Todos/Vigentes/Cancelados/Por timbrar y Lista/Tarjetas/Calendario; Variants & states contiene Type, Selected, State e Icon & badge y sus notas. Todas las muestras usan instancias vinculadas. La documentación es editable; no aplanar la página como imagen."
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
        "En web, el grupo usa tablist, coordina aria-selected, aria-controls, IDs, foco y activación manual/automática con sus paneles. La representación Figma no certifica HTML/ARIA o teclado web. El contrato del hijo gobierna tipografía, estados e iconografía Phosphor."
      ]
    },
    {
      "id": "REQ-QA",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-GROUP",
        "SRC-INVENTORY"
      ],
      "acceptance": [
        "Verificar desde una instancia, no solo en principales: cardinalidad menor y mayor que cuatro, orden y etiqueta, vínculos, único selected, tipos coherentes, Divider estirado, foco sin clip y scopes/aliases/nombres reales. Registrar límites del slot y conservar los resultados en un comprobante único BH-P04. Las pruebas del núcleo no sustituyen QA de Figma."
      ]
    },
    {
      "id": "REQ-COLLECTION",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-COLLECTION"
      ],
      "acceptance": [
        "Consumir la colección component y el grupo tab; aplicar BH-P07 REQ-P07-07 y el mapa de migración ADR-020."
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

ADR-020 cambia la API de colección: seleccionar `component` y el grupo `tab`. Los tokens mantienen identidad lógica, nombre WEB, scope, aliases y función; las rutas y los IDs nativos afectados se consultan en [el mapa de migración](../../evidence/collection-consolidation/migration-map.json). La colección y sus cuatro temas se gobiernan únicamente por [BH-P07 REQ-P07-07](../../protocols/07-COMPONENT-TOKENS.md#req-p07-07). Los roles fijos repiten el mismo alias en los cuatro modos.

El cambio mayor corresponde al contexto de modo y ubicación consumidos desde Figma/CLI; no añade variantes, propiedades, tokens ni comportamiento de aplicación. Las pruebas anteriores acreditan sus cortes históricos; la preservación del destino tras esta migración se acredita en [el comprobante actual](../../evidence/qa/component-collection-check.json).
