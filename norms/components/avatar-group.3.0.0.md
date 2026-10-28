---
{
  "schema_version": 1,
  "id": "AVATAR-GROUP-001",
  "version": "3.0.0",
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
      "id": "SRC-USER",
      "path": "evidence/authorization/avatar-pilot-request.txt",
      "sha256": "5c384535b5e34ef6bea2c91253bc592dbd46106062612094fab96870237608d6"
    },
    {
      "id": "SRC-PAGE",
      "path": "evidence/avatar-pilot/source/page-snapshot.json",
      "sha256": "84264381b8a2fc19117a07c9d3d188205b57a070c6c6f6122aa07cb3b11c010d"
    },
    {
      "id": "SRC-API",
      "path": "evidence/avatar-pilot/source/discovery.json",
      "sha256": "d0e645762915047442e6c7168241f25c86b2e4989fc07473139725780c545fee"
    },
    {
      "id": "SRC-PRESENCE",
      "path": "evidence/avatar-pilot/source/presence-and-gaps.json",
      "sha256": "1dadf1360f8a9927cb9b54cb27d5c72ae3eb9b674030ef60f1914831598f7304"
    },
    {
      "id": "SRC-PHOSPHOR",
      "path": "evidence/avatar-pilot/source/phosphor.json",
      "sha256": "47bd8e5371eaae376a6a48d9bed9e47ae5b38bfce4da15c1eab2482d3fcf9588"
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
    }
  ],
  "dependencies": [
    {
      "kind": "contract",
      "id": "AVATAR-001",
      "version": "3.0.0",
      "relation": "composition"
    },
    {
      "kind": "token",
      "id": "avatar-group.color-bg-alternate-warning",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar-group.color-bg-alternate-positive",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar-group.color-bg-overflow-default",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar-group.color-text-overflow-default",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar-group.spacing-overlap-extra-large",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar-group.spacing-overlap-large",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar-group.spacing-overlap-compact",
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
        "SRC-PAGE",
        "SRC-API",
        "SRC-PRESENCE",
        "SRC-PHOSPHOR",
        "SRC-USER-DOT"
      ],
      "acceptance": [
        "Cuatro variantes de grupo y dependencia exacta Avatar vinculada."
      ]
    },
    {
      "id": "REQ-SLOT",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-PAGE",
        "SRC-API",
        "SRC-PRESENCE",
        "SRC-PHOSPHOR"
      ],
      "acceptance": [
        "Slot nativo, límites y operaciones desde consumidor comprobados."
      ]
    },
    {
      "id": "REQ-LAYOUT",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-PAGE",
        "SRC-API",
        "SRC-PRESENCE",
        "SRC-PHOSPHOR"
      ],
      "acceptance": [
        "Traslape, anillo real y geometría por tamaño coinciden con receta."
      ]
    },
    {
      "id": "REQ-CONTENT",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-PAGE",
        "SRC-API",
        "SRC-PRESENCE",
        "SRC-PHOSPHOR"
      ],
      "acceptance": [
        "Cardinalidad y contador documentados sin cálculo automático ficticio."
      ]
    },
    {
      "id": "REQ-THEME",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-PAGE",
        "SRC-API",
        "SRC-PRESENCE",
        "SRC-PHOSPHOR"
      ],
      "acceptance": [
        "Grupo invariante y contexto de tema del hijo comprobados en los cuatro temas."
      ]
    },
    {
      "id": "REQ-TOKENS",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-PAGE",
        "SRC-API",
        "SRC-PRESENCE",
        "SRC-PHOSPHOR",
        "SRC-USER-DOT"
      ],
      "acceptance": [
        "Siete firmas propias; herencia y extensión mínima de Foundations trazables."
      ]
    },
    {
      "id": "REQ-ACCESSIBILITY",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-PAGE",
        "SRC-API",
        "SRC-PRESENCE",
        "SRC-PHOSPHOR"
      ],
      "acceptance": [
        "Contraste y nombres accesibles documentados; warning no se declara AA."
      ]
    },
    {
      "id": "REQ-DOCUMENTATION",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-PAGE",
        "SRC-API",
        "SRC-PRESENCE",
        "SRC-PHOSPHOR"
      ],
      "acceptance": [
        "Tres bloques editables completos; textos ajenos y descripciones obsoletas corregidos."
      ]
    },
    {
      "id": "REQ-QA",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-PAGE",
        "SRC-API",
        "SRC-PRESENCE",
        "SRC-PHOSPHOR",
        "SRC-USER-DOT"
      ],
      "acceptance": [
        "Operaciones y vínculos del slot, contenido y modos probados según tolerancias."
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
    }
  ],
  "profile_data": {
    "anatomy": [
      "Group",
      "Avatars SLOT",
      "Avatar instances",
      "Overflow"
    ],
    "composition": "Slot nativo 2..4 con Avatar vinculados; tres identidades y contador si total >4.",
    "accessibility": "Responsabilidades del consumidor y medidas en REQ-ACCESSIBILITY; Figma no certifica accesibilidad web."
  }
}
---
# AVATAR-GROUP-001 · avatar-group 3.0.0

### REQ-IDENTITY

Avatar group es otra familia con cuatro variantes size, en la misma página Avatars. Usa Avatar 3.0.0 mediante instancias vinculadas; no duplicar la anatomía ni publicar toda la familia Dot.

### REQ-SLOT

Un slot nativo Avatars por tamaño, mínimo 2 y máximo 4; stretchChildOnInsert=false, displayEmptyByDefault=false, allowPreferredValuesOnly=true, preferredValues referencia el set Avatar. Por defecto tres avatares y un contador +4. Probar 2 y 4, reordenar y sustituir desde el consumidor sin detach. Un elemento o vacío quedan fuera del contrato del grupo; usar Avatar individual.

### REQ-LAYOUT

Grupo y slot Auto Layout horizontal HUG, alineado al centro, sin clipping. Traslape por itemSpacing −8/−6/−4/−4 px, siguiente hijo delante del anterior (itemReverseZIndex=false). Ancho inicial 168/110/84/68 px. Conservar el anillo real blanco INSIDE de 1 px del hijo: se descartan los 3/2 px de la descripción obsoleta por decisión del responsable. Todos los hijos tienen size del grupo y Show status=false; el consumidor coordina esas propiedades al personalizar el slot.

### REQ-CONTENT

Para más de 4 identidades: tres avatares y contador +N, N=total−3. El texto +4 de muestra representa siete identidades; no convertirlo en constante de producto. Figma permite edición manual y no calcula N automáticamente. Para 2–4 identidades, eliminar/sustituir el contador según la lista real. El límite de dos letras de Avatar no aplica al contador +N. No truncar silenciosamente un contador largo: registrar su ajuste pendiente al formato/espacio disponible y usar el listado accesible del consumidor.

### REQ-THEME

El primer avatar mantiene el fondo temático propio de Avatar. Las muestras alternas warning-default y positive-default son fijas, para distinguir identidades y no comunicar presencia/categorías; el contador usa neutral-muted/neutral-strong, fijo. Los siete tokens directos del grupo son invariantes, dentro del grupo avatar de component. El modo component del contenedor controla el hijo temático; los aliases del grupo se conservan fijos conforme a BH-P07 REQ-P07-07.

### REQ-TOKENS

Siete firmas directas únicas: tres GAP negativos compartiendo medium/small, dos fondos alternos FRAME_FILL, fondo del contador FRAME_FILL y texto de contador TEXT_FILL. Anillo y tipografía se heredan del contrato Avatar sin recrearlos en el grupo. Tres valores de traslape ausentes en Foundations se incorporan como primitivas numéricas y aliases spacing-overlap sin scope en BLUEHEART-TOKENS 2.1.0, conservados en el registro vigente; aquel corte se mantiene como historia. No usar literals para ocultar variables necesarias.

### REQ-ACCESSIBILITY

Cada identidad necesita nombre accesible/tooltip y el contador describe las personas ocultas, por ejemplo y 4 más. La composición visual Figma no genera esos atributos ni el tooltip. Medir contraste real de alternos y contador y registrar diferencias; no recolorear por iniciativa ni certificar AA global. La medición derivada está en evidence/avatar-pilot/contrast.json: el alterno warning queda por debajo del umbral normal de texto. Se conserva por fidelidad a los bindings adoptados, con limitación explícita; no se declara AA.

### REQ-DOCUMENTATION

Reconstruir Overview, Variants & states y maestros del contenido de la página fuente mediante documentación editable y ejemplos vinculados de Type, Size, Show status, Initials y Avatar group. Corregir los textos copiados de Button y Modal. Documentar los cuatro temas reales, el anillo real, excepciones fijas, dependencia Phosphor, contador manual y límites de accesibilidad, sin prometer siete modos inexistentes.

### REQ-QA

Validar cada tamaño con 2 y 4 hijos, inserción/retirada/reordenación, types image/icon/text, iniciales y contador modificados; verificar límites nativos y ausencia de detach. Probar cuatro temas sobre el primer hijo y todos los colores fijos de grupo y presencia. Reutilizar tolerancias de Avatar y registrar resultado por caso, no solo existencia de IDs.

### REQ-COLLECTION

Seleccionar `component/avatar`. [BH-P07 REQ-P07-07](../../protocols/07-COMPONENT-TOKENS.md#req-p07-07) gobierna colecciones y modos. El [mapa ADR-021](../../evidence/dot-pilot/migration-map.json) enlaza IDs y equivalencias actuales; el [índice histórico](../../evidence/dot-pilot/history/manifest.json) conserva ADR-020 y versiones previas. Consultar [QA vigente](../../evidence/qa/dot-pilot-check.json).

### REQ-SHARED-DOT

Avatar group 3.0.0 fija AVATAR-001@3.0.0. Dot es transitivo; los siete tokens propios y el slot permanecen. Los hijos conservan Show status=false; el mapa ADR-021 y el QA actual acreditan la preservación.
