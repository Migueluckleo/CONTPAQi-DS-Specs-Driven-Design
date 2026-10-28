---
{
  "schema_version": 1,
  "id": "BUTTON-001",
  "version": "3.0.0",
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
      "id": "SRC-NODES",
      "path": "evidence/button-pilot/source/nodes.json",
      "sha256": "026da4ed94157b68f5c186330a7f69628cb478b9203f068c0b929b5a4dcb712e"
    },
    {
      "id": "SRC-DESCRIPTION",
      "path": "evidence/button-pilot/source/description.json",
      "sha256": "3f78bd2d4f911f91e95ea284546b6343c3b23360d3191fb7871cd6372ba9b5df"
    },
    {
      "id": "SRC-RECIPES",
      "path": "evidence/button-pilot/build-plan.json",
      "sha256": "39e2d4c0f15cc729d3aff286c355456ca0cd338e12d52daa696d32de9409189c"
    },
    {
      "id": "SRC-USER",
      "path": "evidence/authorization/button-pilot-request.txt",
      "sha256": "ad9199e0b2241c52be0161d966dc3057bae284e4df9e16607ace9bec93de3233"
    },
    {
      "id": "SRC-PHOSPHOR",
      "path": "evidence/phosphor/mapping.json",
      "sha256": "145dda152dfb79e01b25836bbdf001faad56e90626c9501063b888a82d04ce7c"
    },
    {
      "id": "SRC-PHOSPHOR-USER",
      "path": "evidence/authorization/phosphor-request.txt",
      "sha256": "d15413a34395f25035e31a4a07fbbe2ea029e2ea4a8edb8d558d25386fb70aa6"
    },
    {
      "id": "SRC-REDUCTION",
      "path": "evidence/button-reduction/migration-plan.json",
      "sha256": "ff3f4244723aa147bb704656c15456362909e6901212e7150adbf5a9a1d45608"
    },
    {
      "id": "SRC-REDUCTION-USER",
      "path": "evidence/authorization/button-reduction-request.txt",
      "sha256": "45c7ea5859315f89a51b95c1d7666456b000017280cf7148e1e10d9311c57398"
    },
    {
      "id": "SRC-FOCUS-USER",
      "path": "evidence/authorization/secondary-focus-size-request.txt",
      "sha256": "008dc71c861dc7696d54809e7d70b4b46472919fbef04b1e7e909f06ac09a1c9"
    },
    {
      "id": "SRC-PROTOTYPE-CORRECTIONS",
      "path": "consumption/button/prototype-corrections.2.0.1.json",
      "sha256": "4a0aa5eb9d3e13fb504f9712dd6707560993cf3f25c672ff8240a4fdba5490cb"
    },
    {
      "id": "SRC-COLLECTION",
      "path": "evidence/authorization/component-collection-request.txt",
      "sha256": "041814c7ca461cddd8d809a5ae3e9f179fdd096b92832c95f57efae3fb2eb11e"
    }
  ],
  "dependencies": [
    {
      "kind": "token",
      "id": "button.color-button-bg-accent",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-bg-disabled",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-bg-soft",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-bg-surface",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-danger-bg",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-danger-bg-hover",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-danger-bg-pressed",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-focus-stroke",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-icon-brand",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-icon-brand-hover",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-icon-disabled",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-icon-inverse",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-icon-neutral",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-loader-inverse",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-loader-neutral",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-primary-bg",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-primary-bg-hover",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-primary-bg-pressed",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-stroke-brand",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-stroke-brand-emphasis",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-stroke-disabled",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-text-brand",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-text-brand-emphasis",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-text-disabled",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-text-inverse",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.color-button-text-neutral",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.font-button-compact-label-size",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.font-button-label-family",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.font-button-label-letter-spacing",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.font-button-label-line-height",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.font-button-label-style",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.font-button-large-label-size",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.font-button-text-label-style",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.radius-button-container",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.radius-button-focus",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.size-button-large-content",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.size-button-large-height",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.size-button-medium-content",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.size-button-medium-height",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.size-button-small-content",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.size-button-small-height",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.spacing-button-lg",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.spacing-button-md",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.spacing-button-sm",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.spacing-button-xs",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.stroke-button-border-width",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "button.stroke-button-emphasis-width",
      "relation": "uses"
    }
  ],
  "requirements": [
    {
      "id": "REQ-IDENTITY",
      "force": "MUST",
      "provenance": "OBSERVED",
      "sources": [
        "SRC-NODES"
      ],
      "acceptance": [
        "Verificar contra la fuente exacta y el resultado de destino en el alcance descrito; registrar por separado límites funcionales del consumidor."
      ]
    },
    {
      "id": "REQ-API",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-DESCRIPTION"
      ],
      "acceptance": [
        "Verificar contra la fuente exacta y el resultado de destino en el alcance descrito; registrar por separado límites funcionales del consumidor."
      ]
    },
    {
      "id": "REQ-GEOMETRY",
      "force": "MUST",
      "provenance": "OBSERVED",
      "sources": [
        "SRC-RECIPES"
      ],
      "acceptance": [
        "Verificar contra la fuente exacta y el resultado de destino en el alcance descrito; registrar por separado límites funcionales del consumidor."
      ]
    },
    {
      "id": "REQ-TYPOGRAPHY",
      "force": "MUST",
      "provenance": "OBSERVED",
      "sources": [
        "SRC-NODES"
      ],
      "acceptance": [
        "Verificar contra la fuente exacta y el resultado de destino en el alcance descrito; registrar por separado límites funcionales del consumidor."
      ]
    },
    {
      "id": "REQ-TOKENS",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-REDUCTION",
        "SRC-REDUCTION-USER"
      ],
      "acceptance": [
        "47 tokens de componente, sin firmas duplicadas por tipo/scope/vector de aliases en los cuatro temas; 251 variables base intactas.",
        "90 recetas conservan estados y propiedades; todos los bindings sustituyen variables retiradas por su token compartido con aliases equivalentes."
      ]
    },
    {
      "id": "REQ-SCOPES",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-USER"
      ],
      "acceptance": [
        "Verificar contra la fuente exacta y el resultado de destino en el alcance descrito; registrar por separado límites funcionales del consumidor."
      ]
    },
    {
      "id": "REQ-THEMES",
      "force": "MUST",
      "provenance": "OBSERVED",
      "sources": [
        "SRC-RECIPES"
      ],
      "acceptance": [
        "Verificar contra la fuente exacta y el resultado de destino en el alcance descrito; registrar por separado límites funcionales del consumidor."
      ]
    },
    {
      "id": "REQ-FOCUS",
      "force": "MUST",
      "provenance": "OBSERVED",
      "sources": [
        "SRC-NODES"
      ],
      "acceptance": [
        "Verificar contra la fuente exacta y el resultado de destino en el alcance descrito; registrar por separado límites funcionales del consumidor."
      ]
    },
    {
      "id": "REQ-LOADING",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-DESCRIPTION"
      ],
      "acceptance": [
        "Verificar contra la fuente exacta y el resultado de destino en el alcance descrito; registrar por separado límites funcionales del consumidor."
      ]
    },
    {
      "id": "REQ-DISABLED",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-DESCRIPTION"
      ],
      "acceptance": [
        "Verificar contra la fuente exacta y el resultado de destino en el alcance descrito; registrar por separado límites funcionales del consumidor."
      ]
    },
    {
      "id": "REQ-USAGE",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-DESCRIPTION"
      ],
      "acceptance": [
        "Verificar contra la fuente exacta y el resultado de destino en el alcance descrito; registrar por separado límites funcionales del consumidor."
      ]
    },
    {
      "id": "REQ-CONTENT",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-DESCRIPTION"
      ],
      "acceptance": [
        "Verificar contra la fuente exacta y el resultado de destino en el alcance descrito; registrar por separado límites funcionales del consumidor."
      ]
    },
    {
      "id": "REQ-COMPOSITION",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-DESCRIPTION"
      ],
      "acceptance": [
        "Verificar contra la fuente exacta y el resultado de destino en el alcance descrito; registrar por separado límites funcionales del consumidor."
      ]
    },
    {
      "id": "REQ-PROTOTYPE",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-NODES",
        "SRC-FOCUS-USER",
        "SRC-PROTOTYPE-CORRECTIONS"
      ],
      "acceptance": [
        "Verificar contra la fuente exacta y el resultado de destino en el alcance descrito; registrar por separado límites funcionales del consumidor.",
        "Secondary focus medium cambia a hover medium (40 px) y small a hover small (32 px), con retorno al salir y conservación de tamaño; verificar en el reproductor nativo y por IDs.",
        "Aplicar la proyección vigente de recetas y comprobar que solo cambien los dos destinos autorizados; conservar las demás reacciones, geometría, propiedades y 47 tokens."
      ]
    },
    {
      "id": "REQ-ASSETS",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-NODES",
        "SRC-PHOSPHOR",
        "SRC-PHOSPHOR-USER"
      ],
      "acceptance": [
        "Verificar que las instancias y defaults de swap apunten a PlusCircle/Outline/Light de Phosphor por key y remote=true, con tamaño y color ligados a tokens.",
        "Verificar la correspondencia de desarrollo PlusCircleIcon weight=light desde @phosphor-icons/react oficial, sin generar una copia JSX desde Figma."
      ]
    },
    {
      "id": "REQ-ACCESSIBILITY",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-DESCRIPTION"
      ],
      "acceptance": [
        "Verificar contra la fuente exacta y el resultado de destino en el alcance descrito; registrar por separado límites funcionales del consumidor."
      ]
    },
    {
      "id": "REQ-FIDELITY",
      "force": "MUST",
      "provenance": "OBSERVED",
      "sources": [
        "SRC-NODES"
      ],
      "acceptance": [
        "Verificar contra la fuente exacta y el resultado de destino en el alcance descrito; registrar por separado límites funcionales del consumidor."
      ]
    },
    {
      "id": "REQ-CONSUMPTION",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-USER"
      ],
      "acceptance": [
        "Verificar contra la fuente exacta y el resultado de destino en el alcance descrito; registrar por separado límites funcionales del consumidor."
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
        "Consumir la colección component y el grupo button; aplicar BH-P07 REQ-P07-07 y el mapa de migración ADR-020."
      ]
    }
  ],
  "profile_data": {
    "anatomy": [
      "Button container",
      "Label",
      "Left icon (optional)",
      "Right icon (optional)",
      "Focus ring (focus state)",
      "Loader (loading state)"
    ],
    "composition": "Bounded label plus optional icon swaps; no arbitrary-content Slot required. Screen grouping is documented separately.",
    "accessibility": "Visible focus and label evidence; functional HTML/ARIA and touch-target rules belong to the consumer, not certified by Figma alone."
  }
}
---
# Button · Contrato de diseño y función

Fuente: nodo `2433:26890`, Librería v1.1.0. Destino: página **Buttons** de Blue Heart DS. Autoridad delegada para el piloto por ADR-006 y actualización Phosphor por ADR-007 y consolidación por ADR-008 y corrección de destinos por ADR-014; no se atribuye aprobación humana a cada dato extraído. React y backend están fuera de esta implementación.

El MD es fuente de verdad para las reglas. Los datos numéricos, matrices y bindings seleccionados se delegan a los tokens registrados y al snapshot de recetas identificado por hash en `sources`. Cambiar esos datos exige revisar este contrato y su selección en el catálogo. La evidencia observacional se conserva separada; no se importó ningún contrato histórico.

| Dimensión | Spec seleccionada |
|---|---|
| Tipos | primary, secondary, text, link, danger |
| Tamaños | large 48 px, medium 40 px, small 32 px |
| Estados | default, hover, pressed, focus, loading, disabled |
| Combinaciones | 90 observadas; 5 sets de 18 variantes en destino |
| Label | Texto editable, ejemplo `Button`; no ancho de producto fijo |
| Iconos | PlusCircle activo, swaps y visibilidad opcional apagada por defecto |
| Foco | 2 px, gap 2 px, expansión 4 px y radio 12 px |
| Carga | Loader 24/20/16 px; 24 frames a 0.033333335 s/frame |
| Temas | Contable, Administrativo, Servicios, Personas |

## Alcance funcional y límites explícitos

Las reglas de uso, contenido, loading y disabled provienen de la descripción del set, no de inferencia visual. Las reacciones realmente leídas se mantienen distintas de esas reglas. Confirmación destructiva, causa de disabled, anuncio accesible y reserva de ancho son obligaciones de la pantalla/PoC que consuma el componente; este piloto Figma no implementa un servicio ni certifica HTML/ARIA.

Hay dos discrepancias relevantes: loading aumenta el ancho del ejemplo porque el layout es HUG aunque la guía pide estabilidad; medium mide 40 px aunque la descripción menciona un target móvil mínimo de 44 px. Se conserva la geometría fuente y se exige a la composición resolver la reserva de ancho o hit area cuando corresponda. No se anuncia cumplimiento AA por la frase de la descripción.

La revisión 2.0.0 retira 78 tokens redundantes y cambia nombres públicos de tokens; el [mapa de migración](../../evidence/button-reduction/variable-map.csv) permite actualizar consumidores. Las variantes, geometría, colores y propiedades públicas de Button se conservan. No se unifican propiedades de scopes distintos ni se crean modos para ocultar duplicados.

La revisión 2.0.1 corrige únicamente los dos destinos de Secondary focus autorizados por ADR-014. La [proyección de consumo](../../consumption/button/README.md) conserva el baseline histórico y aplica un parche mínimo; no duplica los valores ni las reglas del contrato.

## Requisitos y aceptación

### REQ-IDENTITY

Conservar las 90 combinaciones observadas, sin inventar estados ni variantes. El destino agrupa los cinco tipos en sets separados de 18 variantes; cada set mantiene size y state.

### REQ-API

Exponer Label y los controles Show left icon, Show right icon, Left icon y Right icon donde la anatomía los admite. Ambos iconos están apagados por defecto; loading los sustituye por el indicador observado.

### REQ-GEOMETRY

Conservar alturas large=48, medium=40 y small=32 px, geometría HUG, padding, gap y radio de las recetas seleccionadas. Los anchos del ejemplo no son anchos fijos de producto.

### REQ-TYPOGRAPHY

Conservar Manrope Bold para primary, secondary, link y danger, y Manrope Regular para text; 16 px en large y 14 px en medium/small, line-height 20 px y tracking 0 px. Link conserva UNDERLINE.

### REQ-TOKENS

Mantener 47 tokens de componente (26 colores y 21 métricas/tipografía), con un único scope de propiedad por token. Compartir un token cuando coincidan tipo, scope y aliases semánticos en los cuatro temas. Tipo, tamaño y estado seleccionan el token desde las recetas; no exigen una variable nueva por cada combinación. Cada binding de la familia debe usar un token de componente con alias directo a un semántico existente. El semántico aliasa una primitiva. Los colores semánticos no se duplican por uso; los scopes permanecen vacíos en primitive y semantic.

### REQ-SCOPES

Los tokens de componente declaran scopes específicos: bg=FRAME_FILL, texto=TEXT_FILL, icono vectorial=SHAPE_FILL, bordes/foco/loader=STROKE_COLOR; dimensiones=WIDTH_HEIGHT, gap/padding=GAP, radios=CORNER_RADIUS, ancho de trazo=STROKE_FLOAT y tipografía según FONT_FAMILY/FONT_STYLE/FONT_SIZE/LINE_HEIGHT/LETTER_SPACING.

### REQ-THEMES

Conservar el mapa original en Contable, Administrativo, Servicios y Personas mediante los modos del conjunto de tokens de componente. No variar ni renombrar las primitivas/semánticos existentes.

### REQ-FOCUS

Conservar Focus ring: expansión de 4 px por lado, stroke interior de 2 px, separación visual de 2 px y radio de 12 px, con alias de color de foco y constraints STRETCH.

### REQ-LOADING

Loading representa operación en curso, bloquea activaciones duplicadas y usa el loader observado de 24/20/16 px según tamaño. En un consumidor funcional, anunciar ocupado/aria-busy y mantener estable el ancho del control durante la operación. El maestro Figma mantiene su HUG observado; la reserva de ancho es responsabilidad del consumidor y no está demostrada por la matriz fuente.

### REQ-DISABLED

Disabled representa información insuficiente para continuar; el consumidor debe explicar el motivo de forma accesible y no activar la acción. Ocultar una acción que no aplica es una regla de la pantalla, no una variante nueva.

### REQ-USAGE

Primary es la acción principal, como máximo una por vista/modal; secondary acompaña acciones alternativas; text es terciario; link navega y debe representarse como enlace cuando cambie de página; danger se reserva para acciones destructivas/irreversibles y requiere confirmación explícita del objeto y consecuencia en la pantalla consumidora.

### REQ-CONTENT

Usar etiqueta específica en sentence case, verbo en infinitivo y objeto si aclara, con máximo tres palabras según la guía fuente. Loading usa gerundio y elipsis. No incluir datos sensibles ni usar ejemplos fiscales como lógica o llamadas remotas de este componente.

### REQ-COMPOSITION

Mantener tamaño uniforme en un grupo de acciones. La guía ubica primary a la derecha de secondary en escritorio y arriba en una pila de ancho completo en móvil. Es una regla de composición de pantallas: el botón no impone breakpoints ni un contenedor global. No usar dos iconos meramente decorativos a la vez.

### REQ-PROTOTYPE

Reproducir las reacciones nativas leídas por ID y los ciclos AFTER_TIMEOUT del spinner de 24 frames por tamaño. ADR-014 corrige expresamente Secondary: focus medium debe cambiar a hover medium y focus small a hover small; conservar 40 px y 32 px, respectivamente, y el retorno al estado focus al salir. Esta corrección prevalece sobre los dos destinos large de la referencia histórica. Aplicar la proyección de recetas indicada en consumo, que combina el baseline inmutable con SRC-PROTOTYPE-CORRECTIONS; no reconstruir directamente desde el baseline sin esa corrección. Estados sin reacción observada siguen seleccionables como variantes; no inventar navegación, confirmación o servicios remotos para completar el ejemplo.

### REQ-ASSETS

Usar PlusCircle de la biblioteca Phosphor del equipo (file xZSksKpcQTp5H3C4dZApBL, variante Outline/Light, key 46d251bb4099700c5852180f2370d265e5166432) como instancia vinculada remota con instance swap; no mantener una copia local del dibujo. Desarrollo debe consumir PlusCircleIcon con weight="light" desde la distribución oficial @phosphor-icons/react (o su entrada /ssr para RSC), conservando tamaño y color mediante tokens del consumidor. No exportar el dibujo Figma a JSX ni importar masivamente los candidatos de swap. Conservar geometría/opacity y animación del loader, que es un indicador de progreso específico y no un icono Phosphor.

### REQ-ACCESSIBILITY

Documentar foco, etiqueta, semántica botón/enlace y estados ocupados/disabled como obligaciones del consumidor funcional. La afirmación de contraste AA de la descripción no acredita una auditoría WCAG. Medium=40 px no demuestra por sí solo un target táctil de 44 px; no aumentar silenciosamente la geometría de fuente.

### REQ-FIDELITY

Preservar los valores y bindings observados; no aproximar colores, redibujar assets ni aplicar doble escala tipográfica. Literales geométricos y alpha efectivo de 0.3 del track se conservan como hechos fuente donde no existe variable compatible; no crean primitivas o semánticos nuevos.

### REQ-CONSUMPTION

El MD es el propietario normativo de reglas de diseño y función. Los YAML/JSON de inspección y recetas son evidencia o proyecciones con hash; no una especificación editable paralela. Cada consumidor debe poder recuperar requisitos, tokens, propiedades e IDs reales sin depender del proyecto original o de esta conversación.

### REQ-COLLECTION

ADR-020 cambia la API de colección: seleccionar `component` y el grupo `button`. Los tokens mantienen identidad lógica, nombre WEB, scope, aliases y función; las rutas y los IDs nativos afectados se consultan en [el mapa de migración](../../evidence/collection-consolidation/migration-map.json). La colección y sus cuatro temas se gobiernan únicamente por [BH-P07 REQ-P07-07](../../protocols/07-COMPONENT-TOKENS.md#req-p07-07). Los roles fijos repiten el mismo alias en los cuatro modos.

El cambio mayor corresponde al contexto de modo y ubicación consumidos desde Figma/CLI; no añade variantes, propiedades, tokens ni comportamiento de aplicación. Las pruebas anteriores acreditan sus cortes históricos; la preservación del destino tras esta migración se acredita en [el comprobante actual](../../evidence/qa/component-collection-check.json).
