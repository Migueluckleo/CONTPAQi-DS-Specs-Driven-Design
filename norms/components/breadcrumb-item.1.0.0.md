---
{
  "schema_version": 1,
  "id": "BREADCRUMB-ITEM-001",
  "version": "1.0.0",
  "profile": "component",
  "status": "ELIGIBLE",
  "authority": {
    "kind": "DELEGATED",
    "decision_id": "ADR-026"
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
      "path": "evidence/authorization/breadcrumb-request.txt",
      "sha256": "9f0b403c64cbc19268e6e5617ecdec5cd7a639044aa29c1d9073a7a7c053011c"
    },
    {
      "id": "SRC-IDENTITY",
      "path": "evidence/breadcrumb-pilot/source/identity.json",
      "sha256": "cfa579219fe04eda50001c4868af1a2944f82a909ed8084b7cf59ee0bf55a901"
    },
    {
      "id": "SRC-VARIABLES",
      "path": "evidence/breadcrumb-pilot/source/variables-and-notes.json",
      "sha256": "fdb6362cdfb5cccd252685fe95d519b1da0b6d3eef24f8c354369d595d50806c"
    },
    {
      "id": "SRC-ITEM_TEXT",
      "path": "evidence/breadcrumb-pilot/source/item-text.json",
      "sha256": "dd3ed66c3a5306145b156d851ea0fe62f70348d35bb6795dbabb3d698a4db167"
    },
    {
      "id": "SRC-ITEM_ICON",
      "path": "evidence/breadcrumb-pilot/source/item-icon.json",
      "sha256": "537be4d1445e798d192c82c71e01a323db1e958b67d91de108fb4baf79d7a11e"
    },
    {
      "id": "SRC-ITEM_OVERFLOW",
      "path": "evidence/breadcrumb-pilot/source/item-overflow.json",
      "sha256": "11e08ca989e132be5638d3e4eb69005428af9967038ba93ac46586b0fa637884"
    },
    {
      "id": "SRC-ICON-POLICY",
      "path": "protocols/06-PHOSPHOR-ICONS.md",
      "sha256": "aad27541d6cb8b9deadeac6ad966a0fe77d2203ce0989525b6c8c2028d5c0f68"
    }
  ],
  "dependencies": [
    {
      "kind": "token",
      "id": "breadcrumb-item.spacing-item-none",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "breadcrumb-item.spacing-item-gap",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "breadcrumb-item.color-text-link-default",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "breadcrumb-item.font-family",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "breadcrumb-item.font-link-style",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "breadcrumb-item.font-size",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "breadcrumb-item.font-line-height",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "breadcrumb-item.font-letter-spacing",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "breadcrumb-item.size-icon",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "breadcrumb-item.color-icon-separator-default",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "breadcrumb-item.color-text-link-hover",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "breadcrumb-item.color-stroke-focus",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "breadcrumb-item.border-focus-width",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "breadcrumb-item.radius-focus",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "breadcrumb-item.color-text-disabled",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "breadcrumb-item.color-icon-disabled",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "breadcrumb-item.color-text-current-default",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "breadcrumb-item.font-current-style",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "breadcrumb-item.color-icon-link-default",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "breadcrumb-item.color-icon-link-hover",
      "relation": "uses"
    }
  ],
  "requirements": [
    {
      "id": "REQ-API",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-VARIABLES",
        "SRC-ITEM_TEXT",
        "SRC-ITEM_ICON",
        "SRC-ITEM_OVERFLOW",
        "SRC-ICON-POLICY"
      ],
      "acceptance": [
        "Contrastar REQ-API con las fuentes y la evidencia proporcional del destino."
      ]
    },
    {
      "id": "REQ-ANATOMY",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-VARIABLES",
        "SRC-ITEM_TEXT",
        "SRC-ITEM_ICON",
        "SRC-ITEM_OVERFLOW",
        "SRC-ICON-POLICY"
      ],
      "acceptance": [
        "Contrastar REQ-ANATOMY con las fuentes y la evidencia proporcional del destino."
      ]
    },
    {
      "id": "REQ-GEOMETRY",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-VARIABLES",
        "SRC-ITEM_TEXT",
        "SRC-ITEM_ICON",
        "SRC-ITEM_OVERFLOW",
        "SRC-ICON-POLICY"
      ],
      "acceptance": [
        "Contrastar REQ-GEOMETRY con las fuentes y la evidencia proporcional del destino."
      ]
    },
    {
      "id": "REQ-TYPOGRAPHY",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-VARIABLES",
        "SRC-ITEM_TEXT",
        "SRC-ITEM_ICON",
        "SRC-ITEM_OVERFLOW",
        "SRC-ICON-POLICY"
      ],
      "acceptance": [
        "Contrastar REQ-TYPOGRAPHY con las fuentes y la evidencia proporcional del destino."
      ]
    },
    {
      "id": "REQ-STATES",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-VARIABLES",
        "SRC-ITEM_TEXT",
        "SRC-ITEM_ICON",
        "SRC-ITEM_OVERFLOW",
        "SRC-ICON-POLICY"
      ],
      "acceptance": [
        "Contrastar REQ-STATES con las fuentes y la evidencia proporcional del destino."
      ]
    },
    {
      "id": "REQ-COLOR",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-VARIABLES",
        "SRC-ITEM_TEXT",
        "SRC-ITEM_ICON",
        "SRC-ITEM_OVERFLOW",
        "SRC-ICON-POLICY"
      ],
      "acceptance": [
        "Contrastar REQ-COLOR con las fuentes y la evidencia proporcional del destino."
      ]
    },
    {
      "id": "REQ-TOKENS",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-VARIABLES",
        "SRC-ITEM_TEXT",
        "SRC-ITEM_ICON",
        "SRC-ITEM_OVERFLOW",
        "SRC-ICON-POLICY"
      ],
      "acceptance": [
        "Contrastar REQ-TOKENS con las fuentes y la evidencia proporcional del destino."
      ]
    },
    {
      "id": "REQ-FUNCTION",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-VARIABLES",
        "SRC-ITEM_TEXT",
        "SRC-ITEM_ICON",
        "SRC-ITEM_OVERFLOW",
        "SRC-ICON-POLICY"
      ],
      "acceptance": [
        "Contrastar REQ-FUNCTION con las fuentes y la evidencia proporcional del destino."
      ]
    },
    {
      "id": "REQ-QA",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-VARIABLES",
        "SRC-ITEM_TEXT",
        "SRC-ITEM_ICON",
        "SRC-ITEM_OVERFLOW",
        "SRC-ICON-POLICY"
      ],
      "acceptance": [
        "Contrastar REQ-QA con las fuentes y la evidencia proporcional del destino."
      ]
    }
  ],
  "profile_data": {
    "anatomy": [
      "container",
      "Label or Overflow or House",
      "Separator",
      "Focus ring"
    ],
    "composition": "fixed-sparse-variant-matrix",
    "accessibility": "defined-host-runtime-not-implemented"
  }
}
---
# BREADCRUMB-ITEM-001 · Breadcrumb item 1.0.0

### REQ-API

Breadcrumb item es un eslabón reutilizable con Label TEXT editable solo en type=text. type = text | icon | overflow, current y state son ejes VARIANT, con valores de cadena. Hay exactamente 13 combinaciones: text/current=false con default/hover/focus/disabled, text/current=true solo default, icon y overflow con current=false y cuatro estados. No completar el producto cartesiano ni crear estados actuales clicables. Default text/false/default. icon representa Inicio (House); overflow conserva el contenido fijo "..." de tres puntos, no una Label editable ni una elipsis Unicode.

### REQ-ANATOMY

Orden: texto Label u Overflow o icono House, seguido de Separator CaretRight; current=true tiene únicamente Label. Icon y Separator son instancias Phosphor Outline/Light vinculadas de 16 px, sin copias de vectores. No hay Slots ni controles swap propios en la raíz. Los contenedores Phosphor incluyen once paints blancos invisibles en la fuente, sin control público; el destino los omite igual que los cinco de Back, sin crear tokens para residuos que no renderizan. Los glyphs conservan sus bindings propios. Mantener estas dependencias fijas; no introducir iconos o botones distintos por cada estado.

### REQ-GEOMETRY

Auto Layout horizontal, HUG en ambos ejes, alineación MIN/CENTER; padding 0 y gap 4. Texto 14/20; iconos 16. Ejemplos fuente sin modificación: text no actual 99×20, current 82×20, icon 36×16, overflow 31×20. Sus anchos dependen del contenido salvo la huella fija de Overflow 11×20 con textAutoResize=NONE, horizontal FIXED y vertical FILL. Conservar clipping y constraints observados. Los ejemplos no son límites de caracteres ni anchos de producto.

### REQ-TYPOGRAPHY

Manrope Regular en enlaces/overflow; current usa SemiBold. Font 14 px, line-height 20 px y tracking 0 PIXELS. Aplicar tres estilos compartidos: breadcrumb/label/default, /hover con UNDERLINE y /current sin subrayado. Los seis campos tipográficos se vinculan a tokens; la cadena Semibold existente se corresponde con la fuente disponible SemiBold, sin cambiar Foundations. Label HUG/WIDTH_AND_HEIGHT; Overflow conserva su geometría de contenido fijo. Cambiar Label desde una instancia debe recalcular ancho y anillo.

### REQ-STATES

Default y focus conservan el texto del enlace; hover usa link-hover y subrayado para text/overflow. Disabled usa el rol disabled sin interacción. La variante actual es texto SemiBold, sin separador y no navegable. Focus añade un marco absoluto por fuera del eslabón completo, incluido el separador: stroke interior 2, radio 4, x=y=-4, ancho/alto del eslabón +8, constraints STRETCH/STRETCH. El outset 4 deriva del gap del item; separación interior = outset − stroke =2. No crear tokens para anchos dinámicos ni posiciones derivadas. La raíz carece de reacciones: seleccionar un estado no acredita activación de teclado ni cambio por hover en el presentador.

### REQ-COLOR

Solo el texto current cambia con Contable/Administrativo/Servicios/Personas, usando exactamente el vector fuente. El resto de roles son INVARIANT. Home sigue el texto del enlace equivalente: link-default en default/focus, link-hover en hover y disabled en disabled, mediante tokens SHAPE_FILL separados de TEXT_FILL conforme BH-P06. Es una adaptación explícita respecto del Home secondary de la raíz en default/focus. Separator es un delimitador decorativo sin texto asociado: usa separator-default, y disabled cuando corresponde; no toma el color de una etiqueta vecina. Su binding fuente real es icon/secondary aunque la descripción diga tertiary. El anillo usa el color de foco fijo de la raíz. Aliases y valores pertenecen al conjunto de tokens.

### REQ-TOKENS

BH-P07 gobierna mínimo, nombres, scopes y tres colecciones. El item usa veinte firmas, todas en component bajo breadcrumb/. Sus recetas distinguen uso y propiedad, con aliases completos en cuatro modos. No duplicar tokens por combinación ni fusionar sus responsabilidades con el contenedor. La tabla fija rutas nativas; CSS y los IDs estables pertenecen al token set.

| ID lógico | Ruta Figma |
|---|---|
| breadcrumb-item.spacing-item-none | breadcrumb/spacing/item-none |
| breadcrumb-item.spacing-item-gap | breadcrumb/spacing/item-gap |
| breadcrumb-item.color-text-link-default | breadcrumb/color/text/link-default |
| breadcrumb-item.font-family | breadcrumb/font/family |
| breadcrumb-item.font-link-style | breadcrumb/font/link-style |
| breadcrumb-item.font-size | breadcrumb/font/size |
| breadcrumb-item.font-line-height | breadcrumb/font/line-height |
| breadcrumb-item.font-letter-spacing | breadcrumb/font/letter-spacing |
| breadcrumb-item.size-icon | breadcrumb/size/icon |
| breadcrumb-item.color-icon-separator-default | breadcrumb/color/icon/separator-default |
| breadcrumb-item.color-text-link-hover | breadcrumb/color/text/link-hover |
| breadcrumb-item.color-stroke-focus | breadcrumb/color/stroke/focus |
| breadcrumb-item.border-focus-width | breadcrumb/border/focus-width |
| breadcrumb-item.radius-focus | breadcrumb/radius/focus |
| breadcrumb-item.color-text-disabled | breadcrumb/color/text/disabled |
| breadcrumb-item.color-icon-disabled | breadcrumb/color/icon/disabled |
| breadcrumb-item.color-text-current-default | breadcrumb/color/text/current-default |
| breadcrumb-item.font-current-style | breadcrumb/font/current-style |
| breadcrumb-item.color-icon-link-default | breadcrumb/color/icon/link-default |
| breadcrumb-item.color-icon-link-hover | breadcrumb/color/icon/link-hover |

### REQ-FUNCTION

Los eslabones no actuales remiten a un ancestro; Inicio identifica el nivel de entrada y overflow solicita el menú de ancestros ocultos. El host aporta nombre accesible Inicio, destinos y eventos; disabled no navega. Current representa la página actual y no es enlace. El contrato del contenedor define el orden y los datos de ruta; este componente no deduce URLs de Label. El separador es decorativo aria-hidden y el eslabón actual recibe aria-current=page en desarrollo futuro.

### REQ-QA

Verificar las 13 combinaciones desde instancias en cuatro modos: identidad remota, tipografía/estilo, aliases, paints, medidas y anillo tras Label corta/larga. Comparar Home con el token textual equivalente por estado; validar separadores como rol independiente y current como único rol temático. Tolerancias: 0.01 px, color 1e-6, identidades/scopes/aliases exactos. No acreditar web ni revisión independiente desde Figma.
