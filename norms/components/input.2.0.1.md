---
{
  "schema_version": 1,
  "id": "INPUT-001",
  "version": "2.0.1",
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
    },
    {
      "id": "SRC-ICON-ALIGNMENT",
      "path": "evidence/authorization/icon-color-alignment-request.txt",
      "sha256": "35568ec00f70dd642e02b342c165506315874951b932afd9c6c298fbae93a59f"
    },
    {
      "id": "SRC-BADGE-FULL",
      "path": "evidence/authorization/badge-full-request.txt",
      "sha256": "e330c5190cc3518dc0f1085283ce58d206729c52cb5e17889159d463567a895e"
    }
  ],
  "dependencies": [
    {
      "kind": "token",
      "id": "input.spacing-sm",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.spacing-none",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.spacing-xs",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.color-text-primary",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.font-size",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.font-label-style",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.font-family",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.font-label-line-height",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.font-letter-spacing-label",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.color-text-error",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.size-icon",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.color-icon-secondary",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.spacing-lg",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.radius-container",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.border-width-regular",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.color-bg-surface",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.color-stroke-default",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.spacing-md",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.size-height-large",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.color-text-secondary",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.font-content-style",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.font-letter-spacing-normal",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.color-icon-default",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.font-helper-size",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.size-height-medium",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.size-height-small",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.color-stroke-hover",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.color-effect-focus",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.size-focus-spread",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.spacing-effect-none",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.color-indicator-focus",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.color-stroke-success",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.color-text-success",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.color-stroke-error",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.color-bg-read-only-disabled",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.color-stroke-read-only",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.color-text-disabled",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.color-icon-disabled",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.color-stroke-value",
      "relation": "uses"
    },
    {
      "kind": "contract",
      "id": "BADGE-001",
      "version": "1.1.0",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.size-focus-outer-spread",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "input.color-effect-separation",
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
      "id": "REQ-FOCUS",
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
      "id": "REQ-BEHAVIOR",
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
      "id": "REQ-CONTENT",
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
      "id": "REQ-DEPENDENCIES",
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
    },
    {
      "id": "REQ-BADGE-FULL",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-BADGE-FULL"
      ],
      "acceptance": [
        "Consumir Badge 1.1.0 subtle/small en las mismas instancias, conservando contenido, visibilidad, geometría, identidad y Show badge; sin helper temporal."
      ]
    }
  ],
  "profile_data": {
    "anatomy": [
      "label row",
      "Label",
      "Required",
      "Question",
      "field",
      "focus indicator when focus",
      "value or placeholder",
      "Badge optional",
      "CaretDown",
      "helper"
    ],
    "composition": "fixed with optional child components",
    "accessibility": "defined"
  }
}
---
# INPUT-001 · Input 2.0.1

### REQ-SCOPE

Construir Input en su página dedicada de Blue Heart DS, a partir de la página 20:3. Origen y proyecto anterior siguen en solo lectura. Se incorpora únicamente Badge subtle/small como dependencia autorizada; no construir dropdown-menu, tooltip de producto, otras variantes Badge ni React.

### REQ-API

Conservar las 42 combinaciones observadas: size large/medium/small, status default/hover/focus/success/error/read-only/disabled y value false/true. El destino separa value en Input/empty e Input/filled, 21 variantes por set con size y status. La receta mantiene las tres dimensiones lógicas; no usar sets mayores de 30 combinaciones. Label, Placeholder y Helper text son TEXT; Show label/helper/placeholder/tooltip/icon/badge y Required son BOOLEAN. Icon es INSTANCE_SWAP; CaretDown Light es el valor inicial. Defaults: etiqueta, asterisco, contenido, ayuda e icono visibles; tooltip y Badge ocultos. Value elige tratamiento visual, no captura ni valida datos automáticamente. Placeholder conserva su nombre de API también en filled.

### REQ-GEOMETRY

Conservar 464 px como ancho de ejemplo adaptable; no es un token de ancho fijo. Área de captura 48/40/32 px y alturas cortas totales 96/88/80 con etiqueta/ayuda. Padding horizontal 16, vertical 12/8/8, gap de raíz 8, etiqueta-asterisco 4 y ayuda superior 4; radio 8 y borde interior 1 px con strokesIncludedInLayout=false. Conservar el layout y geometría por variante del snapshot. El contenido crece horizontalmente y trunca a una línea con elipsis; helper adopta HEIGHT/HUG para mensajes de varias líneas y crece el componente, manteniendo el baseline corto. La etiqueta debe seguir siendo breve y visible: probar texto representativo, no usar el placeholder como sustituto. Las propiedades sin paint o con un único hijo de flujo pueden conservar métricas inertes sin generar otro token.

### REQ-TYPOGRAPHY

Manrope Bold 14/20 px para etiqueta y asterisco, tracking 0.10000000149011612 %. Manrope Regular 14 con line-height AUTO y tracking 0 % para contenido; helper Regular 12/AUTO, tracking 0 %. Crear y aplicar estilos compartidos input/label, input/content e input/helper con aliases y unidades correctas. AUTO es un estado tipográfico nativo sin alias numérico compatible, no convertirlo a una altura fija ni inventar una variable string LINE_HEIGHT. La API Figma convierte el tracking enlazado a PIXELS. El adaptador conserva la apariencia con 0.10000000149011612 % × 14 px / 100 = 0.014000000208616256 px para Label/Required, y reutiliza el tracking normal 0 px para contenido/helper. Conservar el porcentaje original en evidencia y verificar la equivalencia a tamaño 14; un cambio futuro de tamaño debe recalcular su métrica.

### REQ-TOKENS

Aplicar BH-P07 antes de escribir: 41 firmas propias de Input en component/input; valores y aliases completos pertenecen al conjunto registrado. Color de texto error se comparte con Required; default stroke se comparte con disabled cuando sus firmas coinciden. Reutilizar dimensiones, espaciados y estilos entre tamaños/estados; Badge conserva 12 tokens en su propio contrato. Añadir cuatro Foundations sin scopes: dos del tracking label normalizado a px y dos del neutral F8FAFC observado en el halo de separación; el resto reutiliza los semánticos existentes. Width/height, GAP, radios, trazo, tipografía, paints y efectos usan scopes nativos específicos. Los contenedores de iconos tienen paints fuente desactivados: no crear un fondo operativo para esa metadata inerte.

| ID lógico | Ruta Figma |
|---|---|
| input.spacing-sm | input/spacing/sm |
| input.spacing-none | input/spacing/none |
| input.spacing-xs | input/spacing/xs |
| input.color-text-primary | input/color/text/primary |
| input.font-size | input/font/size |
| input.font-label-style | input/font/label-style |
| input.font-family | input/font/family |
| input.font-label-line-height | input/font/label-line-height |
| input.font-letter-spacing-label | input/font/letter-spacing-label |
| input.color-text-error | input/color/text/error |
| input.size-icon | input/size/icon |
| input.color-icon-secondary | input/color/icon/secondary |
| input.spacing-lg | input/spacing/lg |
| input.radius-container | input/radius/container |
| input.border-width-regular | input/border/width-regular |
| input.color-bg-surface | input/color/bg/surface |
| input.color-stroke-default | input/color/stroke/default |
| input.spacing-md | input/spacing/md |
| input.size-height-large | input/size/height-large |
| input.color-text-secondary | input/color/text/secondary |
| input.font-content-style | input/font/content-style |
| input.font-letter-spacing-normal | input/font/letter-spacing-normal |
| input.color-icon-default | input/color/icon/default |
| input.font-helper-size | input/font/helper-size |
| input.size-height-medium | input/size/height-medium |
| input.size-height-small | input/size/height-small |
| input.color-stroke-hover | input/color/stroke/hover |
| input.color-effect-focus | input/color/effect/focus |
| input.size-focus-spread | input/size/focus-spread |
| input.spacing-effect-none | input/spacing/effect-none |
| input.color-indicator-focus | input/color/indicator/focus |
| input.color-stroke-success | input/color/stroke/success |
| input.color-text-success | input/color/text/success |
| input.color-stroke-error | input/color/stroke/error |
| input.color-bg-read-only-disabled | input/color/bg/read-only-disabled |
| input.color-stroke-read-only | input/color/stroke/read-only |
| input.color-text-disabled | input/color/text/disabled |
| input.color-icon-disabled | input/color/icon/disabled |
| input.color-stroke-value | input/color/stroke/value |
| input.size-focus-outer-spread | input/size/focus-outer-spread |
| input.color-effect-separation | input/color/effect/separation |

### REQ-THEME

Solo stroke hover sigue el tema. Question sigue el color de Label y CaretDown el de contenido/placeholder, con aliases invariantes según el texto de cada variante, incluidos disabled y value. Foco, Required/error, success, read-only y disabled mantienen sus roles. Conservar cuatro modos y las excepciones fijas de foco. ADR-024 sustituye únicamente las recetas anteriores de iconos; no cambia la tipografía ni los fondos.

### REQ-FOCUS

Preservar la composición fuente de focus: wrapper y rectángulo absoluto btn, radio 8, halo DROP_SHADOW de spread 2, blur/offset 0, azul fijo y sin recorte. En empty large hay halo simple en wrapper y btn; en empty medium/small el wrapper es HUG y no lleva efecto, btn conserva halo simple y el campo lleva dos halos: exterior brand-deep de 4 px e interior F8FAFC de 2 px. En filled solo btn lleva halo simple. Aplicar input/focus al halo simple e input/focus-double al compuesto; conservar todos los efectos y aliases por índice. El wrapper HUG deriva su altura del campo y no recibe binding de altura fijo. No sustituir el halo por un stroke ni perder su presencia al estrechar el campo. No cambiar el gris del borde vacío por conveniencia.

### REQ-BEHAVIOR

Campo de una línea. Success requiere validación concluida; error aparece tras intentar enviar con mensaje en Helper text. La guía recomienda validar al salir, no mientras se escribe; no interpreta esto como validación de negocio en Figma. Read-only permite copiar pero no editar; disabled no aplica y exige motivo cercano. Con CaretDown puede ser disparador de dropdown-menu con separación 4 px, cuya implementación queda fuera de esta familia. Show tooltip muestra el icono de ayuda; no hay un tooltip funcional anidado en la fuente. Las 42 variantes fuente no tienen reacciones; no inventar hover/foco automático, teclado, captura de texto o servicios. Los estados se seleccionan mediante propiedades y la pantalla futura implementa los eventos.

### REQ-CONTENT

Label en sentence case y sustantivo, placeholder como ejemplo. Usar formatos regionales e identificadores cuando correspondan al flujo, sin inventar validadores fiscales universales. Badge subtle/small describe moneda ISO o unidad y conserva Label propio editable, por ejemplo MXN/USD; no almacena montos. Minimizar exposición de datos personales; las políticas y reglas del producto las aporta el host. No duplicar el texto del Badge en una propiedad paralela de Input.

### REQ-DEPENDENCIES

Consumir BADGE-001@1.1.0 como instancia expuesta, inicialmente oculta, con Label MXN. Puede editarse desde la instancia anidada sin desacoplarse. CaretDown y Question consumen las keys Outline/Light de la biblioteca Phosphor del equipo, con WIDTH_HEIGHT y vectores SHAPE_FILL de Input; desarrollo futuro usa CaretDownIcon/QuestionIcon weight=light del paquete oficial. No copiar vectores ni importar inventarios masivos de preferencias. La auditoría inversa no encontró inputs existentes; los nodos Badge de Tab apuntan a Dot y no adquieren esta dependencia por el nombre. No reemplazar componentes ajenos.

### REQ-A11Y

El host web debe asociar label for/id, Required/aria-required, error/aria-invalid y mensaje mediante aria-describedby; exponer significado sin depender del color. Iconos decorativos no reciben foco; una ayuda interactiva necesita nombre y manejo accesible en su host. Mantener label aunque la API permita ocultarlo para composiciones que ya lo proporcionen. Medir contraste de texto/borde con fondos reales: el borde vacío heredado puede quedar por debajo de 3:1; registrar la limitación sin proclamar AA ni recolorear la raíz. Figma y pruebas de infraestructura no acreditan HTML/ARIA o navegación por teclado.

### REQ-QA

Comprobar 42 variantes/11 propiedades no variantes, 41 firmas propias, cuatro temas, fonts/unidades/estilos y efecto compartido desde instancias. Probar visibilidad, Required, Label/Placeholder/Helper, Badge con MXN/USD y etiqueta larga, swap Phosphor, ancho 280 y valores largos con elipsis; helper largo debe crecer sin solaparse. Mantener geometría corta con tolerancia float 0.00001, identidad/alias exactos. Separar edición nativa, vista del presentador sin reacciones, QA web no ejecutada y revisión independiente NOT_RUN.

### REQ-ICON-COLOR

Aplicar BH-P06 REQ-P06-03/04 bajo ADR-024. Question se asocia a Label; CaretDown al contenido o placeholder, incluso cuando el texto de filled/disabled conserve color primary. Helper y Required no son su referencia cromática. El retiro de input.color-icon-tooltip se migra a default/disabled para ayuda y a secondary para placeholder; el ID/key Figma anterior se conserva bajo input/color/icon/secondary, pero cambia la API lógica/CSS.

### REQ-BADGE-FULL

Consumir el Badge completo BADGE-001@1.1.0 por composición. Input sigue usando solo subtle/small con Label de moneda; los nuevos iconos del Badge permanecen ocultos por defecto. La ampliación del principal existente elimina el alcance temporal y conserva todos los usos actuales sin sustituir IDs ni alterar la API de Input. La receta y el ledger actuales fijan el componente compartido; QA del encargo verifica los 113 usos y la reproducción de Show badge desde cada combinación de Input. No crear un helper privado ni otro grupo de tokens en Input para Badge.
