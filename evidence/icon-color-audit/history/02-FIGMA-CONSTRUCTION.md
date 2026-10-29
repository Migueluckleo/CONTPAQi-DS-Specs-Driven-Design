---
{
  "schema_version": 1,
  "id": "BH-P02",
  "version": "2.3.0",
  "profile": "operational",
  "status": "ELIGIBLE",
  "authority": {
    "kind": "DELEGATED",
    "decision_id": "ADR-021"
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
    },
    {
      "id": "SRC-TAB-AUTH",
      "path": "evidence/authorization/tab-pilot-request.txt",
      "sha256": "a01ef90b7236d87a5cf1c1fa1dcc872b5924b206515a3e306aae0ae6b2d6a586"
    },
    {
      "id": "SRC-TAB-TYPOGRAPHY",
      "path": "evidence/tab-pilot/destination/style-link-correction.json",
      "sha256": "21552b04d690c457731babd11d5596000e347765e114d78891286234ac183541"
    },
    {
      "id": "SRC-CRITERIA",
      "path": "evidence/authorization/token-protocol-criteria-request.txt",
      "sha256": "fa308f8359ef963618e917e667d7334d25a025ae1b3d820787919190a4271f1e"
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
      "id": "BH-P01",
      "version": "2.3.0",
      "relation": "uses"
    },
    {
      "kind": "contract",
      "id": "BH-P06",
      "version": "2.0.0",
      "relation": "uses"
    }
  ],
  "requirements": [
    {
      "id": "REQ-P02-01",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY",
        "SRC-TAB-AUTH",
        "SRC-USER-DOT"
      ],
      "acceptance": [
        "Preflight demuestra destino, página, capacidades e inventario; no hay escrituras al origen."
      ]
    },
    {
      "id": "REQ-P02-02",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY"
      ],
      "acceptance": [
        "Mapa parte/propiedad/modo/binding y recuperación por IDs están completos antes de escribir."
      ]
    },
    {
      "id": "REQ-P02-03",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY",
        "SRC-TAB-TYPOGRAPHY"
      ],
      "acceptance": [
        "Instancias permanecen vinculadas; layout, tipografía, composición e interacciones observadas satisfacen el contrato."
      ]
    },
    {
      "id": "REQ-P02-04",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY",
        "SRC-TAB-AUTH"
      ],
      "acceptance": [
        "Lectura posterior y captura corresponden a los IDs entregados; referencias y foco no quedan recortados."
      ]
    },
    {
      "id": "REQ-P02-05",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY"
      ],
      "acceptance": [
        "Mapeo de iconos y consumidor cumplen BH-P06 mediante keys e instancias reales."
      ]
    },
    {
      "id": "REQ-P02-06",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY",
        "SRC-CRITERIA"
      ],
      "acceptance": [
        "Variables observadas, recetas y dependencias corresponden al mínimo y nombres de BH-P07; retiros no conservan referencias.",
        "Lectura posterior contrasta función/estado y comportamiento temático de REQ-P07-02/06 contra variables e instancias reales."
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
        "Consumir y verificar la organización de colecciones declarada únicamente en BH-P07 REQ-P07-07; no crear colecciones por familia."
      ]
    }
  ],
  "profile_data": {
    "inputs": [
      "Contrato seleccionado",
      "Destino autorizado e inventario real"
    ],
    "outputs": [
      "Componentes vinculados y mapa de bindings",
      "Lectura posterior y evidencia visual"
    ],
    "responsibilities": [
      "builder: escritura delimitada e idempotencia",
      "verifier: lectura posterior y aceptación"
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
# BH-P02 · Construcción de componentes en Figma

### REQ-P02-01

**1. Preflight del destino**

Prerequisito: [BH-P01](01-COMPONENT-CONTRACT.md). La decisión adoptada del encargo autoriza la familia concreta en su página dedicada; no elegirla por un ejemplo histórico de Button. ADR-004 conserva la procedencia de las variables base.

Obtener el destino de [policy.json](../governance/policy.json): Blue Heart DS, `98xEw6sK8FRVNEhopM5SSz`. El origen `9zs5RMR8LB5wHjW9Bd59BA` y el proyecto anterior son de solo lectura. Un ID histórico nunca se utiliza como ID local de escritura.

Leer páginas, objetos existentes, componentes, variables y estilos relevantes. Confirmar permisos y operaciones de escritura y lectura necesarias; verificar capacidades concretas, no solo conexión. Cargar las skills Figma exigidas por la herramienta utilizada antes de sus llamadas; no reemplazar sus reglas técnicas con recetas antiguas.

Determinar la página de familia por identidad y contenido. Reutilizarla; al crear una familia nueva, usar una página dedicada con nombre funcional del encargo/contrato, una sola para sus variantes y ejemplos. Resolver decisiones editoriales rutinarias dentro del encargo. Si hay dos candidatas o contenido ajeno, registrar el conflicto; no duplicar ni mover recursos ajenos para imponer organización. El page ID se registra después de crearlo o leerlo. No crear páginas de muestras por el mero hecho de crear variables.

El impacto sobre consumidores se evalúa con [BH-P01 REQ-P01-07](01-COMPONENT-CONTRACT.md#req-p01-07); su mapa y prueba pertenecen al comprobante del encargo.

### REQ-P02-02

**2. Mapa de construcción**

Para cada parte/variante/estado anotar propiedad Figma, token lógico, variable de destino, colección, modo y binding esperado. Resolver primero dependencias y tokens. Aplicar las reglas comunes de [BH-P01](01-COMPONENT-CONTRACT.md); no replicar ni reinterpretar el inventario histórico.

Los nuevos tokens deben aliasar semánticos existentes. El scope se configura sobre ese token consumidor y se comprueba para la propiedad concreta; no se añade al semántico. Verificar esta extensión antes de vincular la familia. Si todavía falta la definición autorizada de la capa de componente, preparar el mapa y registrar el requisito pendiente; no usar una copia semántica con nombre de fondo, texto o borde.

Planificar operaciones y recuperación por IDs exactos. Antes de UPDATE guardar los atributos afectados y sus referencias. CREATE debe comprobar si la identidad ya existe. No repetir un script completo ante un error sin leer qué se creó. Registrar el avance fuera del archivo Figma; no usar datos ocultos del lienzo como diario de ejecución.

### REQ-P02-03

**3. Construcción y composición**

Crear solo la anatomía, propiedades, combinaciones y estados sustentados; dependencias antes que consumidores. Mantener principales reutilizables e instancias vinculadas; no duplicar maestros, aplanar ni desacoplar para simular composición.

Usar Auto Layout para relaciones entre elementos y tamaños acordes al contexto. Comprobar crecimiento, ancho/altura, espaciado, alineación, overflow y contenido largo. No fijar alturas o cardinalidad a partir de la cantidad del ejemplo. Cargar las fuentes reales antes de modificar texto; comprobar familias/pesos disponibles sin aproximarlos silenciosamente. Conservar asignación tipográfica, unidades y excepciones explícitas.

Cuando se combinan estilos tipográficos y variables, vincular las variables al estilo compartido y aplicar ese estilo al finalizar las ediciones tipográficas. Verificar que el ID del estilo y los bindings sigan presentes en los nodos y sus instancias; crear el estilo sin conservar su vínculo no acredita su uso. Evidencia de la corrección: `SRC-TAB-TYPOGRAPHY`.

Leer y conservar `strokesIncludedInLayout`: puede cambiar el ancho HUG incluso con las mismas métricas. En QA normalizar el binding de strokeWeight cuando Figma lo representa mediante cuatro bindings de lado; comprobar que todos coincidan. Registrar por separado opacity del nodo y del paint: su producto determina el alpha efectivo. Conservar comandos vectoriales y comparar sus coordenadas con la tolerancia numérica declarada para geometría, porque Figma puede normalizar floats.

Los bindings son referencias reales, no colores o métricas pegados. Una limitación de API no se disimula con un literal. Las dependencias privadas deben limitarse al uso real: Button recupera tres tamaños y 24 frames del spinner por tamaño, no todas las variantes de la librería. Un ciclo AFTER_TIMEOUT almacenado se comprueba estructuralmente y no acredita reproducción en el presentador. Separar representación visual de interacciones de prototipo y comportamiento de navegador; Figma no acredita por sí solo teclado ni ARIA.

Si hay contenido variable, verificar soporte real para Slots nativos y las operaciones necesarias. Un frame llamado Slot, Auto Layout, instancias expuestas o instance swap no acreditan un Slot nativo. Una alternativa declarada puede satisfacer composición si el encargo y contrato la admiten y se demuestra; no presentarla como capacidad nativa. Probar inserción/retirada y reordenación/sustitución exigidas desde una instancia consumidora, sin editar el principal ni romper su vínculo.

### REQ-P02-04

**4. Escritura, recuperación y entrega**

Agrupar operaciones relacionadas en lotes seguros de reintentar. Mantener escrituras secuenciales, devolver todos los IDs afectados y registrar campos/cantidades relevantes. Ante un fallo, detener consumidores dependientes, releer el resultado parcial y reparar solo lo identificado. No prometer rollback universal.

Leer bindings, aliases, tipos, scopes, modos, propiedades, variantes y layout realmente escritos. Conservar una captura visual del alcance construido y otra después de una corrección visual, si la hubo. No repetir inspecciones idénticas cuando las entradas y el resultado no cambiaron; cubrir lo que falte según [BH-P04](04-QA-AND-DELIVERY.md).

Comprobar el foco desde una instancia con etiqueta e iconos modificados, incluidos los contenedores de muestra: una geometría correcta puede quedar recortada por clipsContent del padre. Corregir el contenedor del ejemplo sin cambiar la anatomía contractual del componente.

La entrega identifica contrato/hash, archivo/página/nodos, mapa de variables, cambios realizados, pruebas, diferencias y límites. Crear nodos no equivale a validar la familia. Publicar la biblioteca sigue siendo una acción distinta.

### REQ-P02-05

**Iconografía compartida**

Aplicar [BH-P06 · Phosphor](06-PHOSPHOR-ICONS.md): Figma consume la biblioteca del equipo mediante instancias vinculadas; desarrollo consume directamente el paquete oficial. Conservar mapeo de nombre, peso, variante y key/export, con color y tamaño desde tokens del consumidor.

### REQ-P02-06

**Consolidación de tokens de componente**

Aplicar obligatoriamente [BH-P07](07-COMPONENT-TOKENS.md) antes de crear variables. Nombrarlas con componente primero y grupos separados por `/`, como `button/color/bg/primary-default`; usar el campo `figmaName` seleccionado por el contrato/mapa. Contrastar los tokens seleccionados con el inventario real del destino para detectar variables no declaradas. Migrar bindings antes de retirar IDs y comprobar referencias en maestros, helpers e instancias consumidoras.

El mapa de REQ-P02-02 consume también [REQ-P07-06](07-COMPONENT-TOKENS.md#req-p07-06). Antes de escribir, verificar ese pase; después, leer nombres, aliases y paints de los consumidores en los modos afectados según BH-P04. Crear variables o configurar sus scopes sin esa lectura no cierra la aceptación.

### REQ-COLLECTION

Para la ubicación de variables, consumir [BH-P07 REQ-P07-07](07-COMPONENT-TOKENS.md#req-p07-07). El pase y QA del destino deben acreditar esa organización con su inventario nativo. El registro y la migración pertenecen a ADR-020 y al contrato vigente; no copiar aquí otra definición de la estructura.
