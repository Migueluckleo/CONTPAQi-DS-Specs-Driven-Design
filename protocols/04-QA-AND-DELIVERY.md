---
{
  "schema_version": 1,
  "id": "BH-P04",
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
    }
  ],
  "requirements": [
    {
      "id": "REQ-P04-01",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY",
        "SRC-USER-DOT"
      ],
      "acceptance": [
        "Cada control registra esperado, requisito, resultado, evidencia y alcance; NOT_APPLICABLE tiene razón."
      ]
    },
    {
      "id": "REQ-P04-02",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY"
      ],
      "acceptance": [
        "Matriz ejecutada cubre destinos afectados y separa resultados visuales, funcionales y estructurales."
      ]
    },
    {
      "id": "REQ-P04-03",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY"
      ],
      "acceptance": [
        "Comprobante único enlaza entradas y resultados; correcciones revalidan el alcance; revisión no ejecutada queda explícita."
      ]
    },
    {
      "id": "REQ-P04-04",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY",
        "SRC-CRITERIA"
      ],
      "acceptance": [
        "Resultado de minimización y contraste de inventario/bindings/nombres satisfacen BH-P07 sin atribuir QA remoto al check.",
        "La matriz comprueba REQ-P07-02/03/06: función/estado, mínimo y roles fijos/temáticos en todos los modos afectados; excepciones conservan límites."
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
      "Cambio y requisitos afectados",
      "Fuentes e implementación o documentación a verificar"
    ],
    "outputs": [
      "Comprobante único del alcance",
      "Diferencias y verificaciones pendientes"
    ],
    "responsibilities": [
      "verifier: resultados y cobertura",
      "coordinator: límites y cierre"
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
# BH-P04 · QA proporcional y entrega

### REQ-P04-01

**1. Dos momentos**

Propietario de aceptación operativa. La [política](../governance/policy.json) selecciona gates por tipo de cambio; el contrato de la familia aporta requisitos concretos. Este protocolo no añade una segunda aprobación ni sustituye revisión independiente cuando la política la exige.

Antes de construir, revisar el contrato contra fuentes exactas: autoridad, identidad/hash, coherencia, dependencias, combinaciones y aceptación. Después, comparar la implementación real contra ese contrato; no editar expectativas para hacerla pasar. Un borrador, un build o una escritura exitosa no acreditan una familia validada.

Registrar cada control como PASS, FAIL, BLOCKED o NOT_APPLICABLE con requisito, esperado, evidencia y alcance. NOT_APPLICABLE necesita una razón; la falta de capacidad o evidencia de un requisito necesario es BLOCKED. Una excepción conserva su diferencia y autorización, sin convertirla en cumplimiento exacto.

El impacto sobre consumidores se evalúa con [BH-P01 REQ-P01-07](01-COMPONENT-CONTRACT.md#req-p01-07); su mapa y prueba pertenecen al comprobante del encargo.

### REQ-P04-02

**2. Matriz de controles**

| Cambio | Comprobaciones pertinentes |
|---|---|
| Documentación | Referencias, coherencia, alcance y procedencia; sin construir componentes para validar un texto. |
| Contrato/API | Estructura, autoridad, requisitos, dependencias y consumidores afectados. |
| Token | Identidad, tipos, modos, aliases, ciclos, unicidad cromática, scopes y bindings de consumidores afectados. |
| Figma | Archivo/página/IDs, anatomía, propiedades, variantes, layout, tipografía, bindings y captura del resultado. |
| Web | Tipos, exports, defaults, composición, interacciones, navegador, geometría, tipografía y accesibilidad del alcance. |
| Herramienta | Casos positivos y negativos relevantes, preservación, determinismo y fallo parcial. |

Para tokens de componente comprobar alias a semántico y scopes específicos; para semánticos comprobar scopes vacíos y ausencia de duplicación por primitiva de color. Comprobar resolución en cada tema y los paints de instancias reales; un alias correcto por sí solo no demuestra el color consumidor. Probar el contexto que usará la Skill: debe retener todos los requisitos dentro del presupuesto, con identidad/hash y tema explícitos. Un contexto parcial nunca devuelve PASS.

En composición variable probar desde el consumidor: una cantidad menor y mayor que la muestra, cambios de orden/contenido exigidos, vínculo intacto y layout. Probar vacío si está permitido, contenido largo, ancho reducido y variantes afectadas. Las cantidades de prueba no se convierten en límites de producto. Una captura estática no acredita operaciones desde una instancia.

El QA de Figma no demuestra teclado/ARIA web; el QA web no demuestra un vínculo Figma. Conservar unidades y propiedades tipográficas resueltas, además de IDs o clases. Las tolerancias numéricas/visuales se fijan antes de comparar y se justifican por el destino; no se inventan después de ver un fallo. Las identidades y aliases requieren correspondencia exacta.

### REQ-P04-03

**3. Corrección, contexto y cierre**

Corregir defectos deterministas dentro del encargo y releer/reprobar el alcance afectado. Una brecha contractual o decisión material pendiente se registra con sus fuentes y limita ese alcance. No recolorear para hacer pasar contraste ni inventar comportamiento. Mantener el último comprobante válido identificado por sus entradas.

Reutilizar comprobaciones solo si coinciden fuentes, herramientas y salidas pertinentes. No repetir builds/checks tras PASS sin un cambio o incertidumbre nueva. `qa-plan` devuelve un plan; el comprobante acredita qué se ejecutó. Si falta revisión independiente, declararla NOT_RUN y no afirmar que el gate se completó.

Entregar un comprobante por encargo bajo `evidence/qa/`: solicitud/decisión, fuentes y hashes, contrato/revisión, destino/IDs o rutas, controles ejecutados, resultados, evidencia, diferencias y límites. No copiar la misma tabla a varios registros editables. Distinguir preparación, implementación y QA por destino; solo anunciar validación en lo efectivamente cubierto.

El cierre técnico sigue la autorización vigente y no espera una aprobación humana rutinaria adicional. Publicar, desplegar o cambiar de alcance se rige por la solicitud y la política, no por un PASS. Continuar con [BH-P05](05-MAINTENANCE-AND-RELEASES.md) únicamente si el cambio afecta derivados o distribución.

### REQ-P04-04

**Gate obligatorio de tokens por componente**

Aplicar [BH-P07](07-COMPONENT-TOKENS.md) a contratos, tokens y adaptadores de componentes. Registrar el resultado por familia de `component_token_minimum` en `check` y contrastarlo con recetas y variables construidas. Firmas redundantes o scopes múltiples bloquean el núcleo; variables no declaradas y bindings reales requieren inspección del destino. El conteo depende de cada familia, sin fijar 47 como límite. Una revisión documental sin cambio visual reutiliza el QA previo y no reconstruye Figma.

Para nomenclatura, inspeccionar las rutas nativas y su correspondencia por ID/key con el mapa de construcción: componente primero, grupos `/` y calificadores con guiones conforme a BH-P07. Registrar erratas o marcas temporales observadas sin generalizarlas. El check local no demuestra el nombre actual de una variable remota.

Añadir al comprobante los controles de [REQ-P07-02/03/06](07-COMPONENT-TOKENS.md#req-p07-06), enlazando su expectativa al contrato de familia y su resultado al destino. No basta un conteo bajo ni la coincidencia en el tema predeterminado. `check` valida firmas y aliases declarados; la clasificación funcional, las excepciones y el comportamiento remoto exigen revisión y evidencia del alcance. Para una modificación solo de protocolos, validar su consumo y referencias sin reconstruir Figma ni atribuir una nueva inspección remota.

### REQ-COLLECTION

Para la ubicación de variables, consumir [BH-P07 REQ-P07-07](07-COMPONENT-TOKENS.md#req-p07-07). El pase y QA del destino deben acreditar esa organización con su inventario nativo. El registro y la migración pertenecen a ADR-020 y al contrato vigente; no copiar aquí otra definición de la estructura.
