---
{
  "schema_version": 1,
  "id": "TAB-001",
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
      "path": "evidence/authorization/tab-pilot-request.txt",
      "sha256": "a01ef90b7236d87a5cf1c1fa1dcc872b5924b206515a3e306aae0ae6b2d6a586"
    },
    {
      "id": "SRC-INVENTORY",
      "path": "evidence/tab-pilot/source/inventory.json",
      "sha256": "5e8671e15c5986890bb49046aac9289025604cd1c1fc127378401792611931ec"
    },
    {
      "id": "SRC-NODES",
      "path": "evidence/tab-pilot/source/nodes.json",
      "sha256": "caa420a5e998b27b9820367bd54038c8c00a16c97d309ec28384e6520bdae5c7"
    },
    {
      "id": "SRC-VARIABLES",
      "path": "evidence/tab-pilot/source/variables.json",
      "sha256": "f7549d44aca387aacbc8da7d22f48714dfbaffeeba995aee99054c0218dd21ff"
    },
    {
      "id": "SRC-DEPENDENCIES",
      "path": "evidence/tab-pilot/source/dependencies.json",
      "sha256": "abfd64ea7b6adea6e27eef0273dc8704b00da1173be3cd18cccfe358c5cc5f3d"
    },
    {
      "id": "SRC-PHOSPHOR",
      "path": "evidence/tab-pilot/source/phosphor.json",
      "sha256": "35079fecc5721acf9164d1df14990cb09546830a1596f8db5978e70805d551eb"
    },
    {
      "id": "SRC-OFFICIAL",
      "path": "evidence/tab-pilot/source/official-icon.json",
      "sha256": "538a4b89f7d09291592f1b77b1fbd9378880a73d30cb4c7375d489704dcb5945"
    },
    {
      "id": "SRC-RECIPES",
      "path": "consumption/tab/build-plan.2.0.0.json",
      "sha256": "1a1aa8ffaf6d1abde904527fb5296776aff8fb8a07bc09a71a98dafbe740fb36"
    },
    {
      "id": "SRC-OBSERVATION",
      "path": "evidence/tab-pilot/source/component-contract.yaml",
      "sha256": "c7723bdd00b6bea2a7cc7db45e2666130a11d162329b5994381ab43ccd275d6d"
    },
    {
      "id": "SRC-RECONCILIATION",
      "path": "evidence/authorization/tabs-page-reconciliation-request.txt",
      "sha256": "9bcf56c28470c2aa1fce3b3ad24a82207b58ab67af5f066a336dfe709a37843d"
    },
    {
      "id": "SRC-CONTRAST-CHOICE",
      "path": "evidence/authorization/tabs-purple-contrast-choice.txt",
      "sha256": "b891d1ceaf4dc510893900f42731341a9e4cbcc8a8c1dfa2179e6faa3cf8b497"
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
      "kind": "token",
      "id": "tab.border-tab-width-emphasis",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.border-tab-width-regular",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.color-tab-bg-brand-accent",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.color-tab-bg-brand-subtle",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.color-tab-bg-muted",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.color-tab-bg-subtle",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.color-tab-bg-surface",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.color-tab-icon-brand",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.color-tab-icon-disabled",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.color-tab-icon-primary",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.color-tab-icon-secondary",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.color-tab-stroke-brand",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.color-tab-stroke-brand-hover",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.color-tab-stroke-focus",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.color-tab-stroke-neutral",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.color-tab-text-brand",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.color-tab-text-brand-hover",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.color-tab-text-disabled",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.color-tab-text-inverse",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.color-tab-text-primary",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.color-tab-text-secondary",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.font-tab-family",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.font-tab-label-style",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.font-tab-letter-spacing",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.font-tab-line-height-label",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.font-tab-selected-style",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.font-tab-size-label",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.radius-tab-full",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.radius-tab-lg",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.radius-tab-md",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.radius-tab-sm",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.size-tab-icon",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.spacing-tab-lg",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.spacing-tab-md",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.spacing-tab-none",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.spacing-tab-sm",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.spacing-tab-xs",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.color-tab-bg-segmented-selected-default",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.color-tab-bg-segmented-selected-hover",
      "relation": "uses"
    },
    {
      "kind": "contract",
      "id": "DOT-001",
      "version": "1.0.0",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.color-tab-icon-inverse",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "tab.color-tab-icon-brand-hover",
      "relation": "uses"
    }
  ],
  "requirements": [
    {
      "id": "REQ-IDENTITY",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-USER",
        "SRC-INVENTORY",
        "SRC-USER-DOT"
      ],
      "acceptance": [
        "Un set Tab en su página Tabs, 24 variantes y ausencia de ejes o estados de Button."
      ]
    },
    {
      "id": "REQ-API",
      "force": "MUST",
      "provenance": "OBSERVED",
      "sources": [
        "SRC-INVENTORY",
        "SRC-NODES",
        "SRC-USER-DOT"
      ],
      "acceptance": [
        "Label TEXT, Show icon BOOLEAN, Icon INSTANCE_SWAP y Show badge BOOLEAN; todos operan desde instancias sin editar principales."
      ]
    },
    {
      "id": "REQ-VARIANTS",
      "force": "MUST",
      "provenance": "OBSERVED",
      "sources": [
        "SRC-INVENTORY",
        "SRC-NODES"
      ],
      "acceptance": [
        "Producto observado 3 tipos × 2 selecciones × 4 estados = 24; cada combinación es única."
      ]
    },
    {
      "id": "REQ-ANATOMY",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-NODES",
        "SRC-DEPENDENCIES",
        "SRC-USER-DOT"
      ],
      "acceptance": [
        "Orden Icon–Label–Count y Focus ring absoluto en las seis variantes focus."
      ]
    },
    {
      "id": "REQ-TYPOGRAPHY",
      "force": "MUST",
      "provenance": "OBSERVED",
      "sources": [
        "SRC-NODES",
        "SRC-VARIABLES",
        "SRC-USER-DOT"
      ],
      "acceptance": [
        "Manrope Regular/SemiBold 14/20 en Label y Bold 10/16 en Count; bindings tipográficos completos y fuentes disponibles."
      ]
    },
    {
      "id": "REQ-TOKENS",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-RECIPES",
        "SRC-VARIABLES",
        "SRC-USER-DOT"
      ],
      "acceptance": [
        "41 dependencias propias únicas más Dot; mapas de scopes, aliases y nombres vigentes en los cuatro temas."
      ]
    },
    {
      "id": "REQ-SELECTION",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-INVENTORY"
      ],
      "acceptance": [
        "El ejemplo consumidor mantiene exactamente una Tab seleccionada y muestra su panel correspondiente."
      ]
    },
    {
      "id": "REQ-INTERACTIONS",
      "force": "MUST",
      "provenance": "OBSERVED",
      "sources": [
        "SRC-NODES",
        "SRC-RECIPES"
      ],
      "acceptance": [
        "Las cuatro reacciones fuente default→hover mantienen type y selected y retornan al salir en el reproductor nativo.",
        "Las acciones de selección del ejemplo se distinguen de las reacciones del principal."
      ]
    },
    {
      "id": "REQ-FOCUS",
      "force": "MUST",
      "provenance": "OBSERVED",
      "sources": [
        "SRC-NODES",
        "SRC-RECIPES"
      ],
      "acceptance": [
        "Seis anillos visibles; ancho/alto siguen al contenedor con margen de 4 px y sobreviven a Label, icono, Count y temas."
      ]
    },
    {
      "id": "REQ-DISABLED",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-INVENTORY",
        "SRC-NODES"
      ],
      "acceptance": [
        "Seis variantes disabled sin activación ni hover; selected se conserva como estado visual independiente."
      ]
    },
    {
      "id": "REQ-ICONS",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-USER",
        "SRC-PHOSPHOR",
        "SRC-OFFICIAL"
      ],
      "acceptance": [
        "Icon es una instancia remota de Phosphor del equipo; swap real mantiene tamaño y color desde tokens, sin copias SVG."
      ]
    },
    {
      "id": "REQ-COUNT",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-NODES",
        "SRC-DEPENDENCIES",
        "SRC-USER-DOT"
      ],
      "acceptance": [
        "Show badge y Count se modifican desde instancias; 1, 12 y 99+ conservan layout, vínculo y legibilidad."
      ]
    },
    {
      "id": "REQ-LAYOUT",
      "force": "MUST",
      "provenance": "OBSERVED",
      "sources": [
        "SRC-NODES",
        "SRC-RECIPES"
      ],
      "acceptance": [
        "Auto Layout horizontal HUG, gap 8, paddings por tipo, stroke fuera de layout y ausencia de recortes con contenido largo/opcionales."
      ]
    },
    {
      "id": "REQ-ELEVATION",
      "force": "MUST",
      "provenance": "OBSERVED",
      "sources": [
        "SRC-DEPENDENCIES",
        "SRC-NODES"
      ],
      "acceptance": [
        "Un único estilo local de efecto compartido en los tres selected segmented activos, con valores iguales a la fuente."
      ]
    },
    {
      "id": "REQ-SEGMENTED",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-USER",
        "SRC-RECIPES",
        "SRC-RECONCILIATION",
        "SRC-CONTRAST-CHOICE"
      ],
      "acceptance": [
        "Morados exactos fijos en cuatro temas para selected/default y hover; focus y disabled blancos. Contraste 4.39:1 y 2.26:1 registrado sin declarar AA. Se mantiene corrección de pill hover."
      ]
    },
    {
      "id": "REQ-CONTRAST",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-USER",
        "SRC-RECIPES",
        "SRC-RECONCILIATION",
        "SRC-CONTRAST-CHOICE"
      ],
      "acceptance": [
        "Morados exactos fijos en cuatro temas para selected/default y hover; focus y disabled blancos. Contraste 4.39:1 y 2.26:1 registrado sin declarar AA. Se mantiene corrección de pill hover."
      ]
    },
    {
      "id": "REQ-CONTENT",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-INVENTORY",
        "SRC-NODES"
      ],
      "acceptance": [
        "Label conserva contenido y HUG al cambiarlo; los valores de prueba no se convierten en límites de producto."
      ]
    },
    {
      "id": "REQ-ACCESSIBILITY",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-INVENTORY",
        "SRC-DEPENDENCIES"
      ],
      "acceptance": [
        "El contrato registra role=tab, aria-selected, tablist y responsabilidad de teclado/paneles, sin atribuir pruebas DOM a Figma."
      ]
    },
    {
      "id": "REQ-CONSUMPTION",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-RECIPES",
        "SRC-USER"
      ],
      "acceptance": [
        "Contexto compacto completo dentro del presupuesto; manifiesto y dependencias actuales trazables."
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
      "optional Phosphor Icon",
      "Label",
      "optional private Count",
      "Focus ring"
    ],
    "composition": "Individual Tab with fixed anatomy and editable properties; selection/group/panels belong to its consumer.",
    "accessibility": "Declared tab/tablist semantics and consumer responsibilities; Figma does not certify executable web accessibility."
  }
}
---
# Tab · diseño y comportamiento

### REQ-IDENTITY

Tab representa una vista o sección. Crear un set local Tab en la página Tabs del destino, con maestros fuera de revisión. Button y el contenedor Tabs tienen contratos propios. Origen y proyecto anterior: solo lectura. Autoridad: ADR-016/017/021.

### REQ-API

Conservar Label (TEXT, Tab), Show icon (BOOLEAN, false), Icon (INSTANCE_SWAP, ImageSquare Outline/Light) y Show badge (BOOLEAN, false). selected es VARIANT con strings false/true, sin confundirlo con BOOLEAN. Registrar claves generadas en el destino. Badge expone Count anidado; no es un Slot.

### REQ-VARIANTS

Los ejes son type=underline|pill|segmented, selected=false|true y state=default|hover|focus|disabled. No añadir size, pressed, loading, primary o secondary por analogía con Button. selected y focus son independientes. Las 24 combinaciones están observadas, incluidas selected=true con disabled. Las alturas derivadas del contenido/padding son 44, 36 y 28 px por tipo; no constituyen un nuevo eje ni justifican variables de altura duplicadas.

### REQ-ANATOMY

Icon opcional → Label → Badge opcional; Focus ring absoluto en focus. Los opcionales inician apagados. Badge usa DOT-001@1.0.0 count/medium. Admitir contenido, visibilidad y swap de icono; sin hijos arbitrarios ni Slots.

### REQ-TYPOGRAPHY

Label: Manrope Regular no seleccionado y SemiBold seleccionado, 14/20 px, con letter-spacing porcentual y estilos locales. Badge hereda dot/count/medium de Dot. FONT_STYLE contiene nombres Figma; web traduce Regular/SemiBold/Bold a 400/600/700. Cargar fuentes antes de vincular y aplicar el estilo al finalizar.

### REQ-TOKENS

Aplicar BH-P07: 41 firmas directas únicas; Dot aporta sus tokens por dependencia. Cada propiedad referencia el token de su propietario → semántico → primitiva. Reutilizar Foundations con scopes vacíos. Manifiesto y receta identifican aliases completos, IDs, figmaName y WEB explícito. Conservar identidades lógicas, sin agrupar por RGB ni convertir roles fijos en temáticos. No recrear los seis tokens retirados de Badge.

### REQ-SELECTION

El contenedor consumidor controla qué Tab está seleccionada y qué panel/vista corresponde; Tab comunica esa selección visualmente. Una activación habilitada solicita seleccionar la vista y el consumidor actualiza el grupo y su panel. El foco por sí solo no cambia selected en esta unidad. La orientación de 2–5 vistas de segmented pertenece al contexto consumidor, no a una cardinalidad interna de Tab. El ejemplo de tres vistas solo demuestra consumo; consume el componente público Tabs de TABS-001 ni implementa servicios.

### REQ-INTERACTIONS

Conservar las cuatro reacciones ON_HOVER/CHANGE_TO observadas: underline y pill, selected=false/true, default→hover del mismo tipo y selección. No hay acciones de click de selección ni controlador de grupo en el principal fuente. Los estados sin reacción observada siguen disponibles como variantes. El ejemplo consumidor puede gestionar selección y paneles mediante navegación nativa entre frames; sus acciones pertenecen al ejemplo, no se atribuyen al principal o al origen. Validar reproducción real; una reacción almacenada no demuestra ejecución.

### REQ-FOCUS

Anillo de 2 px, offset exterior 4 px y radios según tipo. Constraints STRETCH conservan el margen al crecer HUG; los contenedores no deben recortarlo. Scopes y aliases conservan los roles independientes conforme a BH-P07.

### REQ-DISABLED

disabled impide la activación del usuario y conserva la selección recibida, incluida selected=true. El contenedor no conecta hotspots de selección sobre un ejemplo disabled. No deducir una selección alternativa ni cambiar de panel automáticamente cuando una Tab pasa a disabled: esa decisión corresponde al flujo consumidor. Mantener los colores y superficies deshabilitados observados; el contador informativo mantiene su receta propia.

### REQ-ICONS

Aplicar BH-P06. El valor inicial es ImageSquare, Format=Outline y Weight=Light, key f273018f11d7d4e938078bd0b21b0b3a9e7f2634, verificado en la biblioteca del equipo. El tamaño es 20 px y el color se vincula a SHAPE_FILL. No copiar paths vectoriales ni usar assets temporales del codegen. Desarrollo consume ImageSquareIcon weight=light desde @phosphor-icons/react (o su export SSR oficial). Con Label visible el icono es decorativo; un swap no crea otra variante. Por ADR-024, el icono sigue el alias de Label en cada estado y tema, incluido blanco en segmented selected/default y hover; conserva SHAPE_FILL.

### REQ-COUNT

Show badge controla Dot count/medium. Dot gobierna geometría, color y estilo. Count es texto ya formateado, incluidos 1, 12 y 99+; no cambia automáticamente a count-expand ni calcula, consulta o aplica topes. El consumidor decide visibilidad y nombre accesible. El mapa registra la nueva clave Count expuesta. No recrear __Tab/Count ni habilitar otros tipos Dot dentro de Badge.

### REQ-LAYOUT

Conservar Auto Layout horizontal, ancho HUG, padding horizontal 16/16/12 y vertical 12/8/4 por underline/pill/segmented, y gap 8 px. Mantener strokesIncludedInLayout=false en las unidades para no alterar las dimensiones por el indicador. El icono mide 20 px y Count no supera la línea base de 20 px de Label. El ancho depende del contenido real; los 56/48 px de los ejemplos fuente no son límites. No fijar anchos de texto por la etiqueta de muestra. El contenedor consumidor resuelve el espacio disponible y el overflow del conjunto.

### REQ-ELEVATION

segmented seleccionado en default/hover/focus usa un estilo local compartido elevation/shadow/sm con color/alpha, offset, blur y spread de la fuente. No multiplicar parámetros no variables por estado. disabled conserva ausencia de sombra. IDs y receta son derivados verificables.

### REQ-SEGMENTED

Por ADR-016 y ADR-017, igualar la raíz: selected/default usa #A146FB y selected/hover #C698FB con Label blanco, constantes en Contable, Administrativo, Servicios y Personas. Reutilizar semánticos únicos existentes mediante dos tokens FRAME_FILL dedicados al rol segmented-selected; no derivarlos de los temas. Focus conserva fondo blanco, Label oscuro, sombra y anillo; disabled conserva blanco y su foreground deshabilitado. El icono comparte el vector semántico de Label, manteniendo su token SHAPE_FILL conforme ADR-024. Esta regla sustituye la normalización blanca de 1.0.0, conservada únicamente como historia.

### REQ-CONTRAST

Segmented selected/default y hover con blanco: 4.39:1 y 2.26:1, inferiores a 4.5:1. ADR-017 conserva fidelidad con esa limitación; no declarar AA. Pill selected/hover usa el color de marca más oscuro elegido: un token TEXT_FILL con vector completo, sin semánticos ni tokens por tema. Medir colores/fondos aplicados y registrar disabled por separado como inactivo; esta comprobación no certifica WCAG global, ARIA o teclado.

### REQ-CONTENT

Label identifica la vista y requiere un nombre comprensible no vacío. La fuente recomienda 1–2 palabras; esa guía no fija un límite de caracteres. No se formaliza un modo de solo icono. Conservar wrapping/truncation observado; probar contenido largo y opcionales desde la instancia. Los textos de ejemplo y los valores 1, 12 y 99+ no son reglas de negocio ni un servicio de conteo.

### REQ-ACCESSIBILITY

La implementación web consumidora usa semántica tab con aria-selected y relación con el panel; el grupo usa tablist y gestiona flechas y orden de tabulación. El estado disabled debe reflejarse en la interacción y semántica. El consumidor define IDs, activación manual/automática y nombres accesibles del contexto, incluido el conteo; no se deducen del canvas. La selección se comunica también por peso e indicador/superficie. Figma representa estilos y transiciones, sin implementar ni certificar HTML/ARIA, teclado web o conformidad global.

### REQ-CONSUMPTION

El MD gobierna diseño y función; la inspección del origen es evidencia. Fijar contrato/hash, token set y modo al iniciar. El manifiesto enlaza recetas, IDs, propiedades y QA; usar instancias vinculadas y modo component. No presumir biblioteca publicada/importable. React/Next.js/Graphify siguen diferidos. BH-P08 gobierna envíos y versiones; esta alta no publica releases oficiales.

### REQ-COLLECTION

Seleccionar `component/tab`. [BH-P07 REQ-P07-07](../../protocols/07-COMPONENT-TOKENS.md#req-p07-07) gobierna colecciones y modos. El [mapa ADR-021](../../evidence/dot-pilot/migration-map.json) enlaza IDs y equivalencias actuales; el [índice histórico](../../evidence/dot-pilot/history/manifest.json) conserva ADR-020 y versiones previas. Consultar [QA vigente](../../evidence/qa/dot-pilot-check.json).

### REQ-SHARED-DOT

Tab 3.0.0 consume DOT-001@1.0.0 count/medium. Retira seis tokens privados y sustituye la clave Count expuesta según el mapa ADR-021, conservando texto y geometría. Su manifiesto enlaza la receta, dependencia y QA actuales.

### REQ-ICON-COLOR

Aplicar BH-P06 REQ-P06-03/04 bajo ADR-024. Icon se asocia a Label por type/selected/state. Inverse y brand-hover son las dos firmas SHAPE_FILL adicionales; secondary y brand usan los aliases completos de sus textos correspondientes, sin alterar sus colores.
