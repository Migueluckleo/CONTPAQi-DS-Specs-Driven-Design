---
{
  "schema_version": 1,
  "id": "BH-P07",
  "version": "2.0.0",
  "profile": "operational",
  "status": "ELIGIBLE",
  "authority": {
    "kind": "DELEGATED",
    "decision_id": "ADR-011"
  },
  "targets": [
    "documentation"
  ],
  "readiness": {
    "documentation": "READY"
  },
  "sources": [
    {
      "id": "SRC-AUTH",
      "path": "evidence/authorization/operational-protocols-request.txt",
      "sha256": "eefa6f1db2b1defd41541064238224cfcfb6690f19d0025700a30d17a7e903f0"
    },
    {
      "id": "SRC-RECOVERY",
      "path": "evidence/protocol-recovery/manifest.json",
      "sha256": "d7c7ae3dca2ee7d76102f591803b1426b9300030454523467f74c7801fc33d5c"
    }
  ],
  "dependencies": [],
  "requirements": [
    {
      "id": "REQ-P07-01",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY"
      ],
      "acceptance": [
        "Cada firma de la familia es única en todos los modos y conserva identidad semántica y scope."
      ]
    },
    {
      "id": "REQ-P07-02",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY"
      ],
      "acceptance": [
        "Rutas nuevas cumplen jerarquía componente/categoría/propiedad y mapean lógico/ID/Figma/WEB; excepciones observadas no se generalizan."
      ]
    },
    {
      "id": "REQ-P07-03",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY"
      ],
      "acceptance": [
        "Receta cubre usos y dependencias; check obtiene cero redundancias por contrato."
      ]
    },
    {
      "id": "REQ-P07-04",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY"
      ],
      "acceptance": [
        "Bindings migran antes de retirar IDs; no se pierden estados, aliases, unidades ni consumidores."
      ]
    },
    {
      "id": "REQ-P07-05",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY"
      ],
      "acceptance": [
        "Comprobante enlaza cantidades, firmas, nombres, scopes, instancias y contexto completo, con límites de inspección explícitos."
      ]
    }
  ],
  "profile_data": {
    "inputs": [
      "Usos reales por familia y modo",
      "Inventario y contrato seleccionado"
    ],
    "outputs": [
      "Firmas mínimas y receta uso a token",
      "Nombres, scopes y migración verificables"
    ],
    "responsibilities": [
      "analyst: agrupación y recetas",
      "builder: bindings y migración",
      "verifier: mínimo y correspondencia"
    ],
    "failure_states": [
      "BLOCKED: fuente, autoridad, dependencia o capacidad necesaria ausente",
      "FAIL: incumplimiento demostrado; reparar y verificar el alcance afectado"
    ],
    "applies_to": [
      "CREATE, UPDATE, MIGRATE o VALIDATE_ONLY dentro de la política y del encargo"
    ]
  }
}
---
# BH-P07 · Tokens de componente: mínimos y nombres

### REQ-P07-01

**Regla y propietario**

Obligatorio para CREATE, UPDATE y MIGRATE de cualquier componente, en Figma y desarrollo. ADR-009 convierte la consolidación en un control general; ADR-010 adopta la estructura de nombres aplicada por el responsable en Button. No autoriza construir familias fuera del encargo.

Antes de crear variables, reutilizar un token de la familia cuando coincidan **tipo, unidad, un único scope de propiedad y aliases semánticos en todos los modos de su colección**. Comparar identidades de alias y cualquier override explícito de modo; no solo valores resueltos, RGB o el tema activo. Colecciones con contextos de modo distintos no se consideran equivalentes automáticamente.

El contrato MD conserva diseño y función. Sus dependencias declaran todos los tokens que usa directamente la familia; sus recetas indican qué token consume cada parte, variante, tamaño y estado. Dos estados pueden seleccionar el mismo token. Los componentes hijos se verifican con sus propios contratos: no fusionar sus tokens con los del padre ni con otra familia por coincidencia de valor.

La cadena permanece propiedad → token de componente → semántico → primitiva. Primitivas y semánticos mantienen scopes vacíos. No crear semánticos duplicados ni variables para componentes inexistentes.

### REQ-P07-02

**Nombres de variables en Figma — obligatorio**

Todas las variables de componente se agrupan empezando por el **nombre del componente**, seguido de categorías y propiedades separadas por `/`. Usar minúsculas y `kebab-case` dentro de cada segmento. La barra organiza grupos; el guion compone un nombre o un calificador dentro del grupo.

```text
<componente>/<categoría>/<propiedad[-calificador]>
<componente>/color/<elemento>/<rol[-estado]>
```

La estructura admite tres segmentos para métricas/tipografía y cuatro para colores. No añadir niveles vacíos ni repetir el componente dentro de los segmentos. Usar el nombre estable de la familia en `kebab-case`, por ejemplo `button`, `input` o `date-picker`; estas últimas son ilustraciones de nomenclatura, no familias construidas.

| Categoría | Ejemplos observados en Button |
|---|---|
| `color` | `button/color/bg/primary-default`, `button/color/text/inverse`, `button/color/icon/brand`, `button/color/stroke/focus` |
| `font` | `button/font/family`, `button/font/label-style`, `button/font/size-compact` |
| `radius` | `button/radius/container`, `button/radius/focus` |
| `size` | `button/size/height-medium`, `button/size/content-large` |
| `spacing` | `button/spacing/xs`, `button/spacing/md` |
| `border` | `button/border/width-regular`, `button/border/width-emphasis` |

Para nuevas familias, conservar esta jerarquía y crear únicamente las categorías que necesiten sus propiedades reales. Un calificador como `primary-default` identifica el token compartido; no obliga a crear otro para focus/loading si la firma es idéntica. La receta sigue determinando todos sus consumidores.

No usar nombres planos como `color-button-primary-bg` para `variable.name` en Figma. Esta convención pertenece a la capa componente; no renombrar primitivas o semánticos por aplicarla. El nombre del segmento tampoco sustituye el scope nativo: `bg` corresponde a FRAME_FILL, `text` a TEXT_FILL, `icon` a SHAPE_FILL y `stroke` a STROKE_COLOR según su uso.

**Observaciones conservadas:** el responsable dejó `button/font/line-hight` y dos rutas `button/color/loader (temporal)/…`. Se registran exactamente en la evidencia; `line-hight` es una errata respecto de `line-height` y `(temporal)` es una anotación del piloto. No copiarlas como reglas de escritura para otras familias. La inspección documental no las corrigió en Figma. `button/font/weight` conserva actualmente tipo STRING y scope FONT_STYLE: el nombre no convierte el dato en un peso numérico.

**Identidad y desarrollo:** mantener separados ID lógico, ID/key de Figma, ruta Figma y `codeSyntax.WEB`. Consumir el nombre CSS explícitamente registrado; no inferirlo reemplazando `/` por `-`. En el piloto, las rutas cambiaron y el WEB existente se conservó. Cambiar la API CSS requiere su propia migración, conforme a BH-P05. Los adaptadores usan `figmaName` para crear la variable nativa y el nombre lógico para resolver recetas/tokens.

La [correspondencia observada de las 47 variables](../evidence/component-naming/observed-names.json) vincula cada ruta con sus IDs y su WEB. Es evidencia de nombres reales; los nombres de cada nueva familia se fijan en su contrato y mapa de construcción siguiendo esta regla.

### REQ-P07-03

**Antes de construir**

1. Extraer usos reales: parte, propiedad, variantes/estados, tipo/unidad, scope y alias por cada modo existente. Incluir tipografía, métricas, iconos y dependencias privadas, no solo colores.
2. Agrupar por la firma anterior. Una variable por grupo; nombrarla con la jerarquía componente/categoría/propiedad de este protocolo. Una diferencia necesaria debe señalar el campo de la firma que cambia. El nombre de un estado o una posible personalización futura no justifican duplicar una firma idéntica.
3. Registrar la correspondencia uso → token en la receta seleccionada por el contrato. Declarar cada token una sola vez en sus dependencias. No crear variables de antemano para el producto cartesiano de estados y tamaños.
4. Ejecutar `python3 -B -m blueheart check`. El núcleo bloquea firmas redundantes entre las dependencias directas de cada contrato de componente y scopes múltiples en tokens de componente. También valida aliases, tipos, unidades y cobertura de modos. Repetir la consulta de contexto que utilizará la Skill solo cuando cambien sus entradas.

No existe un cupo de 47 tokens para todos los componentes. El mínimo depende de los usos y mapas de cada familia. Button es un precedente medido: 125 → 47, sin modificar las 90 variantes ni los cuatro temas.

### REQ-P07-04

**Construcción y migración**

En Figma, crear únicamente los grupos seleccionados y enlazar las propiedades a sus tokens compartidos. Scope y binding son controles distintos: ambos deben corresponder a la propiedad real. Conservar identidad de componentes, instancias vinculadas y modos existentes. Aplicar BH-P02 y BH-P06 para construcción y Phosphor.

En React/Tailwind/TypeScript/Next.js, proyectar los mismos tokens seleccionados. Las recetas de variantes pueden reutilizar una variable CSS; no generar otro token por cada clase o estado. Aplicar BH-P03; no crear una segunda paleta editable en código.

Al consolidar una familia existente, guardar el corte previo y el mapa nombre/ID anterior → token conservado. Migrar bindings y consumidores antes de retirar variables, y bloquear el retiro si queda alguna referencia. Conservar aliases, valores, geometría, tipografía y comportamiento. Si cambia la API pública de tokens, registrar la versión y el mapa de migración conforme a BH-P05.

No reducir el contador mediante literals, ampliación de scopes, pérdida de estados, fusión por RGB o modos adicionales que codifiquen artificialmente variantes. El objetivo es reducir duplicación sin trasladar complejidad al consumidor.

### REQ-P07-05

**Gate de entrega**

BH-P04 exige evidencia del alcance afectado:

- Cantidad de usos, variables candidatas, firmas únicas, variables finales y referencias retiradas si hubo migración.
- `check` con cero redundancias por contrato; correspondencia entre dependencias, recetas y variables efectivamente construidas.
- Scopes, aliases en todos los modos, bindings reales y, cuando cambie el destino, prueba desde instancias consumidoras o navegador según corresponda.
- Rutas Figma únicas con componente primero, categorías y segmentos válidos; comprobar la correspondencia por ID/key con nombres lógicos y WEB. Registrar diferencias observadas sin sobreescribir cambios del responsable. `check` valida los tokens registrados; la ruta nativa se contrasta con Figma y el mapa de construcción.
- Preservación de los estados, apariencia y funcionamiento afectados; ningún ID retirado puede seguir referenciado.
- Contexto consumible con reglas completas, versiones y hashes. Una Skill no consume un resultado BLOCKED ni recrea tokens desde los nombres de las variantes.

`check` solo inspecciona datos registrados; no lee Figma, detecta variables remotas no declaradas ni acredita bindings o QA visual. El constructor debe contrastar el inventario real con el contrato para detectar omisiones. Una revisión puramente documental no requiere reconstruir el componente ni repetir QA de Figma sin cambios.

Evidencia de referencia: [consolidación Button](../evidence/button-reduction/README.md) y [comprobante](../evidence/qa/button-reduction-check.json). Los números de esa prueba no son límites para nuevas familias.
