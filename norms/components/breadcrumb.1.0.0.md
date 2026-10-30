---
{
  "schema_version": 1,
  "id": "BREADCRUMB-001",
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
      "id": "SRC-COMPOSITION_1",
      "path": "evidence/breadcrumb-pilot/source/composition-1.json",
      "sha256": "3f7d818dff0350233c3ffcae652a4c3dfa17a3546a354d85520d5dda8e4decf9"
    },
    {
      "id": "SRC-COMPOSITION_2",
      "path": "evidence/breadcrumb-pilot/source/composition-2.json",
      "sha256": "119cedd22d45abf2d54d04f6ccdfb869c9f791ae925731a6dbd91182da426f85"
    },
    {
      "id": "SRC-COMPOSITION_DEEP",
      "path": "evidence/breadcrumb-pilot/source/composition-deep.json",
      "sha256": "c070e97f1f8a3f97ccbabd69925fa9da1186dd4be48a51d6ecec8bf4688554ab"
    }
  ],
  "dependencies": [
    {
      "kind": "token",
      "id": "breadcrumb.spacing-container-none",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "breadcrumb.spacing-back-gap",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "breadcrumb.size-back",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "breadcrumb.spacing-container-gap",
      "relation": "uses"
    },
    {
      "kind": "token",
      "id": "breadcrumb.color-icon-back-default",
      "relation": "uses"
    },
    {
      "kind": "contract",
      "id": "BREADCRUMB-ITEM-001",
      "version": "1.0.0",
      "relation": "composition"
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
        "SRC-COMPOSITION_1",
        "SRC-COMPOSITION_2",
        "SRC-COMPOSITION_DEEP"
      ],
      "acceptance": [
        "Contrastar REQ-API con las fuentes y la evidencia proporcional del destino."
      ]
    },
    {
      "id": "REQ-COMPOSITION",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-VARIABLES",
        "SRC-COMPOSITION_1",
        "SRC-COMPOSITION_2",
        "SRC-COMPOSITION_DEEP"
      ],
      "acceptance": [
        "Contrastar REQ-COMPOSITION con las fuentes y la evidencia proporcional del destino."
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
        "SRC-COMPOSITION_1",
        "SRC-COMPOSITION_2",
        "SRC-COMPOSITION_DEEP"
      ],
      "acceptance": [
        "Contrastar REQ-GEOMETRY con las fuentes y la evidencia proporcional del destino."
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
        "SRC-COMPOSITION_1",
        "SRC-COMPOSITION_2",
        "SRC-COMPOSITION_DEEP"
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
        "SRC-COMPOSITION_1",
        "SRC-COMPOSITION_2",
        "SRC-COMPOSITION_DEEP"
      ],
      "acceptance": [
        "Contrastar REQ-TOKENS con las fuentes y la evidencia proporcional del destino."
      ]
    },
    {
      "id": "REQ-NAVIGATION",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-VARIABLES",
        "SRC-COMPOSITION_1",
        "SRC-COMPOSITION_2",
        "SRC-COMPOSITION_DEEP"
      ],
      "acceptance": [
        "Contrastar REQ-NAVIGATION con las fuentes y la evidencia proporcional del destino."
      ]
    },
    {
      "id": "REQ-RESPONSIVE",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-VARIABLES",
        "SRC-COMPOSITION_1",
        "SRC-COMPOSITION_2",
        "SRC-COMPOSITION_DEEP"
      ],
      "acceptance": [
        "Contrastar REQ-RESPONSIVE con las fuentes y la evidencia proporcional del destino."
      ]
    },
    {
      "id": "REQ-CONTENT",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-VARIABLES",
        "SRC-COMPOSITION_1",
        "SRC-COMPOSITION_2",
        "SRC-COMPOSITION_DEEP"
      ],
      "acceptance": [
        "Contrastar REQ-CONTENT con las fuentes y la evidencia proporcional del destino."
      ]
    },
    {
      "id": "REQ-A11Y",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-VARIABLES",
        "SRC-COMPOSITION_1",
        "SRC-COMPOSITION_2",
        "SRC-COMPOSITION_DEEP"
      ],
      "acceptance": [
        "Contrastar REQ-A11Y con las fuentes y la evidencia proporcional del destino."
      ]
    },
    {
      "id": "REQ-DEPENDENCIES",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-USER",
        "SRC-IDENTITY",
        "SRC-VARIABLES",
        "SRC-COMPOSITION_1",
        "SRC-COMPOSITION_2",
        "SRC-COMPOSITION_DEEP"
      ],
      "acceptance": [
        "Contrastar REQ-DEPENDENCIES con las fuentes y la evidencia proporcional del destino."
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
        "SRC-COMPOSITION_1",
        "SRC-COMPOSITION_2",
        "SRC-COMPOSITION_DEEP"
      ],
      "acceptance": [
        "Contrastar REQ-QA con las fuentes y la evidencia proporcional del destino."
      ]
    }
  ],
  "profile_data": {
    "anatomy": [
      "container",
      "Back",
      "Items",
      "exposed Breadcrumb item instances"
    ],
    "composition": "fixed-with-exposed-component-instances",
    "accessibility": "defined-host-runtime-not-implemented"
  }
}
---
# BREADCRUMB-001 · Breadcrumb 1.0.0

### REQ-API

Breadcrumb compone instancias de BREADCRUMB-ITEM-001@1.0.0. levels = 2 | 3 | 4 | 5 | collapsed; default 2. Show back BOOLEAN true por defecto. Los items anidados están expuestos para editar Label y la combinación válida; no añadir un array ni Slots que Figma no define. Cada muestra fuente es una ruta independiente, no se deducen sus ancestros ocultos comparando sus textos con otra variante.

### REQ-COMPOSITION

Un contenedor horizontal HUG con Back y un frame Items. Back es Phosphor ArrowLeft Outline/Light de 16 px, no Button. Root tiene padding 0 y gap 8; Items tiene padding 0 y gap 4. Levels 2/3/4/5 contiene esa cantidad de items; collapsed contiene cuatro elementos visibles: primero, overflow y dos últimos. Exactamente un current=true, de tipo text, al final; todos los otros estados iniciales son default. Samples fuente: Contabilidad, Pólizas, Diario, Septiembre 2026 y Póliza P-0458 según cada receta. No convertir las etiquetas de ejemplo en datos fijos de producto.

### REQ-GEOMETRY

Altura natural 20 px; anchos de ejemplo con Back: 223,293,355,491,320 px para 2,3,4,5,collapsed. Show back=false retira 16+8=24 px sin dejar hueco. Conservar el vínculo del item, sus propiedades y sus anchos HUG al editar contenido. No fijar el ancho del contenedor a la muestra ni truncar etiquetas por conveniencia. El host elige collapsed cuando la ruta no cabe, sin un breakpoint numérico inventado.

### REQ-COLOR

Los cinco tokens propios del contenedor son invariantes en los cuatro modos. Back conserva primary como la raíz; es una acción iconográfica sin texto visible asociado. La tipografía, color temático de current y delimitadores se heredan del contrato item, sin overrides locales que bloqueen el tema. El paint blanco invisible del contenedor Back se omite y queda registrado como exclusión no renderizante: no cambia la apariencia ni existe un control para habilitarlo. No crear un token de fondo para ese residuo.

### REQ-TOKENS

Cinco firmas propias bajo el grupo breadcrumb/ de component: padding none, gap Back, gap Items, tamaño y color de Back. Los veinte tokens de item siguen siendo propiedad de su contrato hijo; no duplicar sus colores o métricas en el padre. BH-P07 gobierna el almacenamiento y mínimo. La tabla fija las rutas Figma; el conjunto de tokens conserva los aliases y WEB.

| ID lógico | Ruta Figma |
|---|---|
| breadcrumb.spacing-container-none | breadcrumb/spacing/container-none |
| breadcrumb.spacing-back-gap | breadcrumb/spacing/back-gap |
| breadcrumb.size-back | breadcrumb/size/back |
| breadcrumb.spacing-container-gap | breadcrumb/spacing/container-gap |
| breadcrumb.color-icon-back-default | breadcrumb/color/icon/back-default |

### REQ-NAVIGATION

El breadcrumb muestra ubicación jerárquica y permite navegar a ancestros. El último nivel es actual y no clicable. Show back solicita el nivel inmediato anterior, no history.back. Overflow solicita un menú con ancestros ocultos, en orden y con sus destinos. El host entrega esos datos y resuelve navegación/cierre/foco; no inferir URLs, targets Figma ni un menú inexistente a partir del texto. La referencia no aporta menú, destinos o reacciones; el entregable Figma representa componentes/estados editables y documenta estas responsabilidades sin simular una navegación implementada.

### REQ-RESPONSIVE

La guía fuente pide colapsar intermedios cuando hay más de cinco niveles o la ruta es larga. En móvil se presenta Back y el ancestro anterior como acceso de retorno; esa presentación no muestra current dentro de la barra y no se debe etiquetar al ancestro como página actual. Es una regla del host: la raíz no incluye variante móvil, menú ni breakpoint numérico. No presentar las cinco variantes de levels como una implementación de adaptación automática.

### REQ-CONTENT

Usar desde el segundo nivel de profundidad, para jerarquía y ubicación. Etiquetas en sentence case, con nombres reales de módulos; series/folios se conservan tal cual. Español/portugués pueden necesitar collapsed. No incluir datos personales sensibles como CURP/NSS en rutas; el responsable de producto decide los identificadores y autorización de datos de persona/empresa. No usar como navegación principal ni indicador de pasos. Conservar etiquetas legibles y el significado al colapsar.

### REQ-A11Y

En desarrollo futuro: nav con aria-label="Ruta de navegación" y lista ordenada; separadores decorativos aria-hidden; current con aria-current=page y sin enlace. Los destinos navegables y el control de overflow tienen nombres, teclado y foco; disabled no activa. El host gestiona foco del menú y navegación al ancestro. Contraste se mide sobre blanco en los cuatro temas; no copiar los ratios redondeados de la descripción como certificación. Figma y sus estados visuales no acreditan teclado/ARIA web.

### REQ-DEPENDENCIES

Resolver primero el item compartido y componer 18 instancias en los cinco principales; Back usa Phosphor remoto. La auditoría de las nueve páginas previas no encontró consumidores ni helpers de esta familia, por lo que no hay sustituciones pendientes. El menú no aparece como dependencia de diseño resuelta: pertenece al contrato funcional del host y deberá especificarse al construir una PoC que lo necesite. Origen y proyecto anterior permanecen en solo lectura.

### REQ-QA

Validar cinco composiciones y Show back true/false en cuatro modos, edición desde items expuestos, current único al final, ruta completa/collapsed y crecimiento por etiquetas largas. Probar sustitución de tipo por combinaciones soportadas y restauración sin desvincular. Verificar el mínimo 20+5, tres colecciones y ausencia de referencias fuente en bindings propios. Registrar evidencia nativa y revisión visual; navegación, menú, móvil y web se declaran sin implementación cuando falte evidencia.
