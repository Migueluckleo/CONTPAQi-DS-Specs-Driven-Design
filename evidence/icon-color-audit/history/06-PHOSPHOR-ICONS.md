---
{
  "schema_version": 1,
  "id": "BH-P06",
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
      "id": "REQ-P06-01",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY"
      ],
      "acceptance": [
        "Figma referencia la biblioteca del equipo y desarrollo la distribución oficial, sin copia de vectores."
      ]
    },
    {
      "id": "REQ-P06-02",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY"
      ],
      "acceptance": [
        "Mapeo incluye peso, key/nodo e identidad de destino/export comprobados."
      ]
    },
    {
      "id": "REQ-P06-03",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY"
      ],
      "acceptance": [
        "El consumidor controla tokens y nombre accesible sin modificar maestros remotos."
      ]
    },
    {
      "id": "REQ-P06-04",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY"
      ],
      "acceptance": [
        "Prueba desde instancia verifica remote, swap, geometría y bindings; límites de loader/SSR/versiones quedan explícitos."
      ]
    }
  ],
  "profile_data": {
    "inputs": [
      "Icono, peso y destino",
      "Biblioteca de equipo o paquete oficial"
    ],
    "outputs": [
      "Mapeo de identidades por destino",
      "Instancia o import oficial verificado"
    ],
    "responsibilities": [
      "builder: selección e importación",
      "verifier: correspondencia y consumidor"
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
# BH-P06 · Iconos Phosphor

### REQ-P06-01

**Fuentes por destino**

Decisión vigente: ADR-007. Esta regla se aplica a los contratos nuevos, las Skills consumidoras y el piloto Button.

En Figma consumir componentes vinculados de la [biblioteca Phosphor del equipo](https://www.figma.com/design/xZSksKpcQTp5H3C4dZApBL/Phosphor-Icons?node-id=26-4). El enlace apunta a Cover; los componentes están en la página Components (`7484:1322`). La biblioteca es de solo lectura. Importar únicamente la variante necesaria por su key y conservar instancias, sin aplanar, desacoplar o mantener otra copia local del dibujo.

En desarrollo consumir directamente la distribución oficial [@phosphor-icons/react](https://github.com/phosphor-icons/react). No exportar el dibujo Figma a JSX, generar otra biblioteca de iconos ni introducir un paquete alternativo como intermediario. Al crear el entorno web, fijar versión y lockfile y verificar que el export solicitado existe. No se instaló una dependencia por esta decisión documental.

### REQ-P06-02

**Correspondencia trazable**

Cada icono consumido debe declarar nombre canónico, peso, variante Figma, file key, component key/node ID de origen, identidad importada de destino y export oficial de desarrollo. La igualdad de nombres no basta para acreditar equivalencia; verificar la variante y el peso. El identificador portable es la key del componente; un ID de importación puede cambiar entre archivos o si la importación no queda referenciada. Importar y vincular en la misma operación.

Button utiliza `PlusCircle`, `Format=Outline`, `Weight=Light`, key `46d251bb4099700c5852180f2370d265e5166432`, origen `8899:53827`. Desarrollo usa `PlusCircleIcon` con `weight="light"`. Outline es la representación vectorial de Figma; no es otro peso del paquete React. La [correspondencia comprobada](../evidence/phosphor/mapping.json) enlaza las fuentes y el destino.

### REQ-P06-03

**Tamaño, color y accesibilidad**

El componente consumidor controla tamaño y color mediante sus tokens. En Figma, conservar el binding WIDTH_HEIGHT del contenedor del icono y SHAPE_FILL de sus vectores, incluyendo instancias con iconos visibles y los cuatro temas. No cambiar el scope del semántico ni editar el maestro remoto para recolorear un uso.

En React, usar el tamaño del token consumidor y `currentColor` desde el token de icono del estado. Importar solamente los iconos utilizados. Para React Server Components/SSR, la distribución oficial ofrece `@phosphor-icons/react/ssr`; esas variantes no heredan IconContext. Resolver el límite cliente/servidor según BH-P03.

Un icono decorativo de un botón con etiqueta se oculta del árbol accesible. Una acción sin etiqueta visible necesita nombre accesible en el control; el nombre del asset no lo sustituye. El componente determina interacción y estado; Phosphor proporciona el dibujo.

### REQ-P06-04

**Validación**

Verificar key y remote=true desde la instancia efectiva, defaults y controles de swap, visibilidad, geometría y bindings después del reemplazo. Comprobar un consumidor con etiqueta e icono visibles. La falta de disponibilidad de una key se informa como dependencia bloqueada; no se resuelve dibujando una sustitución silenciosa. El loader animado de Button es un indicador de progreso específico, no un icono del catálogo Phosphor; conserva su contrato y sus ciclos nativos.

Fuentes oficiales verificadas para esta revisión: [README React](https://github.com/phosphor-icons/react/blob/master/README.md) y [export PlusCircleIcon](https://raw.githubusercontent.com/phosphor-icons/react/master/src/csr/PlusCircle.tsx). Este procedimiento no certifica igualdad de versiones entre la biblioteca del equipo y cada futura versión npm; conservar el mapeo por icono y comprobarlo al actualizar.
