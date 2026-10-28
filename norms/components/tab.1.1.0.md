---
{
  "schema_version": 1,
  "id": "TAB-001",
  "version": "1.1.0",
  "profile": "component",
  "status": "ELIGIBLE",
  "authority": {
    "kind": "DELEGATED",
    "decision_id": "ADR-016"
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
      "path": "consumption/tab/current-build-plan.json",
      "sha256": "0335a0b29170030689623f322bb2fd534df3e054e41e31592bc2c0a3bf2e75c8"
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
      "id": "tab.color-tab-bg-count",
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
      "id": "tab.color-tab-stroke-surface",
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
      "id": "tab.font-tab-count-style",
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
      "id": "tab.font-tab-line-height-count",
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
      "id": "tab.font-tab-size-count",
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
      "id": "tab.size-tab-count",
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
    }
  ],
  "requirements": [
    {
      "id": "REQ-IDENTITY",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-USER",
        "SRC-INVENTORY"
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
        "SRC-NODES"
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
        "SRC-DEPENDENCIES"
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
        "SRC-VARIABLES"
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
        "SRC-VARIABLES"
      ],
      "acceptance": [
        "45 dependencias directas, 45 firmas únicas, cero redundancias y 1.026 bindings fuente cubiertos por la proyección vigente.",
        "Todos los tokens aliasan semánticos existentes en cuatro modos, con un solo scope y nombres tab/categoría/propiedad."
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
        "SRC-DEPENDENCIES"
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
        "context TAB-001 compacto conserva todos los requisitos y 43 tokens en los cuatro temas; manifiesto enlaza hashes/IDs/keys/properties/QA."
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

Tab es la pestaña individual que representa una vista o sección relacionada dentro de un contexto. Este contrato no es Button ni formaliza la familia contenedora Tabs. Crear un único set local `Tab` en la página dedicada `Tabs` del destino autorizado; los maestros y dependencias privadas quedan fuera del frame final de revisión. El origen Figma y el proyecto anterior permanecen en solo lectura. La autoridad vigente es ADR-016 y ADR-017, no los permisos históricos de la biblioteca fuente.

### REQ-API

Conservar las propiedades públicas Label (TEXT, predeterminado Tab), Show icon (BOOLEAN, false), Icon (INSTANCE_SWAP, Phosphor ImageSquare Outline Light) y Show badge (BOOLEAN, false). El eje selected es VARIANT con strings `false`/`true` en Figma; no confundirlo con una propiedad BOOLEAN. Capturar las claves generadas por Figma, sin reutilizar sufijos del origen. El contador expone su instancia anidada y Count editable; no presentar esa exposición como un Slot nativo.

### REQ-VARIANTS

Los ejes son type=underline|pill|segmented, selected=false|true y state=default|hover|focus|disabled. No añadir size, pressed, loading, primary o secondary por analogía con Button. selected y focus son independientes. Las 24 combinaciones están observadas, incluidas selected=true con disabled. Las alturas derivadas del contenido/padding son 44, 36 y 28 px por tipo; no constituyen un nuevo eje ni justifican variables de altura duplicadas.

### REQ-ANATOMY

La anatomía fija es Icon opcional antes de Label, Count opcional después de Label y Focus ring absoluto cuando state=focus. Los dos opcionales están apagados por defecto. El contador es una dependencia privada de esta familia, limitada a la representación activa Count medium; no importar ni recrear toda la familia Dot. La personalización admitida es contenido, visibilidad y swap de icono; no se ofrece inserción arbitraria de hijos o Slots.

### REQ-TYPOGRAPHY

Label usa Manrope Regular no seleccionado y SemiBold seleccionado, 14 px con línea de 20 px. Count usa Bold 10 px con línea de 16 px. Mantener el letter-spacing porcentual observado y sus bindings. Las variables FONT_STYLE son strings de estilo Figma, no un valor CSS font-style; el consumidor web traduce Regular/SemiBold/Bold a 400/600/700 conforme al peso observado. Cargar las fuentes reales antes de asignarlas o vincular variables. Aplicar estilos de texto locales compartidos por estos tres roles, derivados de las mismas recetas.

### REQ-TOKENS

Aplicar BH-P07 antes de crear variables. La receta seleccionada consolida 1.026 usos en 45 firmas de tipo, unidad, scope y aliases completos. Cada token se declara una vez como dependencia. La cadena es propiedad → token Tab → semántico → primitiva. Las 145 primitivas y 106 semánticos existentes se reutilizan con scopes vacíos; no crear duplicados. La colección de Tab tiene Contable (predeterminado), Administrativo, Servicios y Personas. Usar `figmaName` de la receta y `web` explícito con var(); el nombre lógico conserva su identidad. Las referencias de primitivas originales se preservan, no se agrupan por RGB. Un alias fijo de foco que no cambia de tema no se convierte en un alias de marca por intuición.

### REQ-SELECTION

El contenedor consumidor controla qué Tab está seleccionada y qué panel/vista corresponde; Tab comunica esa selección visualmente. Una activación habilitada solicita seleccionar la vista y el consumidor actualiza el grupo y su panel. El foco por sí solo no cambia selected en esta unidad. La orientación de 2–5 vistas de segmented pertenece al contexto consumidor, no a una cardinalidad interna de Tab. El ejemplo de tres vistas solo demuestra consumo; consume el componente público Tabs de TABS-001 ni implementa servicios.

### REQ-INTERACTIONS

Conservar las cuatro reacciones ON_HOVER/CHANGE_TO observadas: underline y pill, selected=false/true, default→hover del mismo tipo y selección. No hay acciones de click de selección ni controlador de grupo en el principal fuente. Los estados sin reacción observada siguen disponibles como variantes. El ejemplo consumidor puede gestionar selección y paneles mediante navegación nativa entre frames; sus acciones pertenecen al ejemplo, no se atribuyen al principal o al origen. Validar reproducción real; una reacción almacenada no demuestra ejecución.

### REQ-FOCUS

Conservar el anillo de 2 px, offset exterior de 4 px y radios observados por tipo. Las constraints STRETCH mantienen el margen al crecer el contenido HUG. El anillo no puede quedar recortado por contenedores de revisión o consumo. Mantener independientes color del anillo, indicador, texto e icono cuando sus scopes o vectores de aliases difieran.

### REQ-DISABLED

disabled impide la activación del usuario y conserva la selección recibida, incluida selected=true. El contenedor no conecta hotspots de selección sobre un ejemplo disabled. No deducir una selección alternativa ni cambiar de panel automáticamente cuando una Tab pasa a disabled: esa decisión corresponde al flujo consumidor. Mantener los colores y superficies deshabilitados observados; el contador informativo mantiene su receta propia.

### REQ-ICONS

Aplicar BH-P06. El valor inicial es ImageSquare, Format=Outline y Weight=Light, key f273018f11d7d4e938078bd0b21b0b3a9e7f2634, verificado en la biblioteca del equipo. El tamaño es 20 px y el color se vincula a SHAPE_FILL. No copiar paths vectoriales ni usar assets temporales del codegen. Desarrollo consume ImageSquareIcon weight=light desde @phosphor-icons/react (o su export SSR oficial). Con Label visible el icono es decorativo; un swap no crea otra variante. Segmented conserva el icono oscuro observado y su scope SHAPE_FILL; Label usa blanco en default/hover seleccionados.

### REQ-COUNT

Show badge controla el contador opcional. La dependencia privada conserva alto y mínimo de ancho de 16 px, ancho HUG, radio completo, borde blanco de 1 px, relleno de aviso y texto blanco. Count es texto formateado por el consumidor; la representación no realiza cálculos, topes ni consultas. El consumidor controla su visibilidad y nombre accesible según el significado del conteo. No prometer los tipos de presencia, notificación o count-expand ni la lógica de Max count de la familia Dot completa. El helper es propiedad de este contrato, no una segunda familia pública.

### REQ-LAYOUT

Conservar Auto Layout horizontal, ancho HUG, padding horizontal 16/16/12 y vertical 12/8/4 por underline/pill/segmented, y gap 8 px. Mantener strokesIncludedInLayout=false en las unidades para no alterar las dimensiones por el indicador. El icono mide 20 px y Count no supera la línea base de 20 px de Label. El ancho depende del contenido real; los 56/48 px de los ejemplos fuente no son límites. No fijar anchos de texto por la etiqueta de muestra. El contenedor consumidor resuelve el espacio disponible y el overflow del conjunto.

### REQ-ELEVATION

segmented seleccionado en default/hover/focus conserva elevation/shadow/sm mediante un estilo de efecto local compartido. Su definición deriva del único estilo de efecto observado; sus parámetros no eran variables de origen y no se multiplican como tokens por estado. La receta y el estilo conservan color/alpha, offset, blur y spread exactos con la tolerancia numérica declarada. disabled conserva ausencia de sombra. El estilo y sus IDs son derivados verificables, no otra paleta o regla editable paralela.

### REQ-SEGMENTED

Por ADR-016 y ADR-017, igualar la raíz: selected/default usa #A146FB y selected/hover #C698FB con Label blanco, constantes en Contable, Administrativo, Servicios y Personas. Reutilizar semánticos únicos existentes mediante dos tokens FRAME_FILL dedicados al rol segmented-selected; no derivarlos de los temas. Focus conserva fondo blanco, Label oscuro, sombra y anillo; disabled conserva blanco y su foreground deshabilitado. El icono mantiene su receta oscura observada. Esta regla sustituye la normalización blanca de 1.0.0, conservada únicamente como historia.

### REQ-CONTRAST

Segmented selected/default y hover con texto blanco ofrecen respectivamente 4.39:1 y 2.26:1: están por debajo de 4.5:1. El responsable conserva fidelidad visual según ADR-017; no declarar AA ni ocultar la limitación. El usuario mantiene el color de marca más oscuro existente para el texto de pill selected/hover. Se registra un único token adicional de TEXT_FILL con el vector completo de aliases; no se crea un semántico o un token por tema. La elección corrige los contrastes de texto insuficientes heredados. La verificación cromática puntual usa los valores aplicados y sus fondos demostrados; no equivale a certificar WCAG general, teclado, ARIA o un flujo web. disabled se registra separadamente como control inactivo.

### REQ-CONTENT

Label identifica la vista y requiere un nombre comprensible no vacío. La fuente recomienda 1–2 palabras; esa guía no fija un límite de caracteres. No se formaliza un modo de solo icono. Conservar wrapping/truncation observado; probar contenido largo y opcionales desde la instancia. Los textos de ejemplo y los valores 1, 12 y 99+ no son reglas de negocio ni un servicio de conteo.

### REQ-ACCESSIBILITY

La implementación web consumidora usa semántica tab con aria-selected y relación con el panel; el grupo usa tablist y gestiona flechas y orden de tabulación. El estado disabled debe reflejarse en la interacción y semántica. El consumidor define IDs, activación manual/automática y nombres accesibles del contexto, incluido el conteo; no se deducen del canvas. La selección se comunica también por peso e indicador/superficie. Figma representa estilos y transiciones, sin implementar ni certificar HTML/ARIA, teclado web o conformidad global.

### REQ-CONSUMPTION

El MD es la fuente operativa de diseño y función; YAML/MD de inspección son evidencia original. La Skill fija contrato/hash, ambos token sets y contexto de modos al iniciar. El manifiesto derivado enlaza la familia, helpers, variables, estilos, claves de propiedades y QA; no duplica requisitos editables. Crear instancias vinculadas y aplicar el modo de tab al contenedor. Los componentes locales no se presumen publicados/importables en otro archivo. React, Next.js y Graphify siguen sin implementarse por este encargo. Aplicar BH-P08 para notas, CI y versiones; no publicar releases oficiales por esta alta de componente.
