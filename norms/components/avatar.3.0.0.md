---
{
  "schema_version": 1,
  "id": "AVATAR-001",
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
      "kind": "token",
      "id": "avatar.color-bg-primary-default",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar.color-stroke-separator",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar.color-text-inverse",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar.color-icon-inverse",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar.border-width-regular",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar.radius-container",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar.spacing-none",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar.size-extra-large",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar.size-large",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar.size-medium",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar.size-small",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar.size-content-regular",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar.size-content-compact",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar.size-content-small",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar.font-family",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar.font-initials-style",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar.font-size-extra-large",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar.font-size-large",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar.font-size-compact",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar.font-line-height-extra-large",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar.font-line-height-compact",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "avatar.font-letter-spacing",
      "relation": "uses"
    },
    {
      "kind": "contract",
      "id": "DOT-001",
      "version": "1.0.0",
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
        "12 combinaciones reales, página y destinos autorizados; ningún estado inventado."
      ]
    },
    {
      "id": "REQ-API",
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
        "Propiedades y presencia expuesta responden desde instancias vinculadas."
      ]
    },
    {
      "id": "REQ-ANATOMY",
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
        "Anatomía, tamaños, clipping, separador y anclaje coinciden con la receta fuente."
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
        "Fallback e iniciales quedan definidos sin automatismos ficticios ni identificadores fiscales."
      ]
    },
    {
      "id": "REQ-TYPOGRAPHY",
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
        "Métricas, estilos y Phosphor coinciden con fuente y mapa de binding."
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
        "Los cuatro temas cambian solo los roles adoptados; los roles fijos permanecen invariantes."
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
        "22 firmas únicas; dependencias, scopes, nombres y receta cubren todos los usos."
      ]
    },
    {
      "id": "REQ-PRESENCE",
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
        "Tres significados de presencia editables; sin atribuir comportamiento en tiempo real a Figma."
      ]
    },
    {
      "id": "REQ-IMAGE",
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
        "Bytes/hash y recorte fuente preservados; sustitución desde instancia sin detach."
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
        "Mediciones y obligaciones del consumidor visibles, sin certificaciones no ejecutadas."
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
        "Controles pertinentes documentados con tolerancias previas y preservación de contenido anterior."
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
      "Container",
      "Image | Initials | Icon",
      "Status"
    ],
    "composition": "Contenido alternativo único más presencia opcional; sin lista variable ni Slot en Avatar individual.",
    "accessibility": "Responsabilidades del consumidor y medidas en REQ-ACCESSIBILITY; Figma no certifica accesibilidad web."
  }
}
---
# AVATAR-001 · avatar 3.0.0

### REQ-IDENTITY

Crear Avatar en una página Avatars de Blue Heart DS, con type=image/icon/text y size=extra-large/large/medium/small: 12 combinaciones reales. No agregar hover, pressed, loading ni foco como variantes inexistentes. Mantener origen y proyecto anterior en solo lectura.

### REQ-API

Conservar Initials (TEXT, JA de muestra), Icon (INSTANCE_SWAP, Phosphor User Outline/Light) y Show status (BOOLEAN, true). Status es instancia anidada expuesta con type=active/busy/inactive y size=large/medium/small. Status consume DOT-001@1.0.0 y solo admite ese subconjunto de presencia; el contrato Avatar no habilita notificaciones ni contadores.

### REQ-ANATOMY

Raíz con Auto Layout vertical HUG y sin clipping. Contenedor Avatar circular fijo de 48/32/24/20 px, radio full, borde blanco de 1 px INSIDE y contenido centrado. Contenedor clipsContent=true para recorte; Status es hermano absoluto anclado abajo/derecha, de 16/12/8/8 px, borde blanco de 1 px OUTSIDE. No aplicar dos veces escalas históricas ni modificar grosor de metadatos de texto sin pintura.

### REQ-CONTENT

Prioridad foto → iniciales → icono, gestionada por el consumidor; Figma no ejecuta carga ni fallback. Iniciales: primera letra del primer nombre y primer apellido, máximo dos letras en mayúsculas, conservando Ñ/acentos y omitiendo partículas y régimen societario según descripción fuente. Nunca usar identificadores fiscales como iniciales o nombre accesible. Si no hay nombre fiable usar icono. El contador +N del grupo es una excepción delimitada de contenido del grupo, no una inicial personal.

### REQ-TYPOGRAPHY

Manrope SemiBold observado: extra-large 20 px/20 px; large 14 px/16 px; medium y small 10 px/16 px. Tracking 0 px. Alias FONT_STYLE conserva el STRING semántico Semibold; la fuente instalada resuelve a SemiBold. Tres estilos locales avatar/initials/extra-large, large y compact, con bindings sobre el estilo y vínculo de estilo aplicado al texto al finalizar. Iconos 32/20/16/12 px, instancias remotas Phosphor sin copia vectorial local.

### REQ-THEME

El fondo primary-default de text/icon es temático con el vector real de cuatro temas de la fuente. Texto/icono inversos, separador blanco, presencia y métricas son invariantes. No crear los siete modos blue/purple/red/amber/emerald/cyan/brand prometidos por una descripción obsoleta: no existen en las variables fuente. La decisión del responsable adopta bindings/geometría reales; no extrapolar la excepción morada de Tab. La fotografía es un asset fijo de muestra y no se recolorea con el tema.

### REQ-TOKENS

Consumir los 22 tokens propios del conjunto BLUEHEART-TOKENS vigente. Compartir tamaños por firma completa entre Avatar e iconos; Dot posee las métricas de presencia; compartir radio y borde dentro de la familia. Mantener scopes distintos para FRAME_FILL, SHAPE_FILL, TEXT_FILL y STROKE_COLOR aun si el alias blanco coincide. La receta y mapa generados identifican todos los consumidores, modos, rutas Figma, IDs y WEB; no duplicar variables por tamaño/estado si su firma coincide. BH-P07 gobierna minimización y nombres.

### REQ-PRESENCE

Status es una instancia vinculada de Dot y conserva type/size expuestos. Avatar extra-large usa Dot large; large usa medium; medium/small usan small. active/busy/inactive son significados de presencia fijos independientes de marca. Mostrar solo cuando la presencia sea relevante; acompañar con texto o tooltip. No usar en listados de nómina, clientes o proveedores. Mostrar/ocultar desde la propiedad y cambiar tipo desde la instancia expuesta. No atribuir actualizaciones en tiempo real ni navegación a Figma: no hay reacciones almacenadas en los maestros fuente.

### REQ-IMAGE

Conservar bytes y hash de la fotografía fuente 33f6b019db4382817513e4485e94d3a7dd5a6ca2, transform y recorte FILL. Es contenido de muestra, no una identidad requerida. Cambiar el fill desde la instancia conserva su componente. El consumidor obtiene autorización de uso de fotografías, carga y tratamiento de datos; el contrato no certifica cumplimiento legal ni implementa almacenamiento. La guía fuente de 96×96 px es recomendación de entrega web, no describe este asset original de 800×1200 px.

### REQ-ACCESSIBILITY

Nombre accesible con nombre completo o razón social; decorativo si el nombre ya está al lado. Color de presencia acompañado de texto. Si el contexto es interactivo, el consumidor aporta foco visible y target mínimo 44×44 px sin escalar los tamaños visuales. Medir contraste de textos/iconos por tema en el comprobante; no repetir AA de la descripción como certificación. No hay implementación ni prueba de teclado, ARIA o privacidad web en este encargo.

### REQ-QA

Verificar 12 variantes, el subconjunto de 9 variantes de presencia de Dot, cuatro temas desde instancias reales, cambios de Initials, visibilidad/status, User→Buildings con bindings del consumidor y cambio de imagen. Tolerancia geométrica 0.01 px, colores 1e-6 por canal; identidades, scopes y aliases exactos. Probar Ñ/acentos y dos letras anchas, registrar clipping si aparece. Contraste según medición, nunca inferido del nombre del token. Acreditar la migración trazable de consumidores sin pérdida de contenido, posición, tamaño ni visibilidad; Button y Foundations conservan sus identidades y valores.

### REQ-COLLECTION

Seleccionar `component/avatar`. [BH-P07 REQ-P07-07](../../protocols/07-COMPONENT-TOKENS.md#req-p07-07) gobierna colecciones y modos. El [mapa ADR-021](../../evidence/dot-pilot/migration-map.json) enlaza IDs y equivalencias actuales; el [índice histórico](../../evidence/dot-pilot/history/manifest.json) conserva ADR-020 y versiones previas. Consultar [QA vigente](../../evidence/qa/dot-pilot-check.json).

### REQ-SHARED-DOT

Avatar 3.0.0 consume el subconjunto de presencia de DOT-001@1.0.0. Retira tres tokens privados y conserva Show status, type/size, posición y tamaño según el mapa ADR-021. Su manifiesto enlaza la receta, dependencia y QA actuales.
