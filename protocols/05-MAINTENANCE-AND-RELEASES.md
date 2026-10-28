---
{
  "schema_version": 1,
  "id": "BH-P05",
  "version": "2.0.2",
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
    },
    {
      "id": "SRC-CRITERIA",
      "path": "evidence/authorization/token-protocol-criteria-request.txt",
      "sha256": "fa308f8359ef963618e917e667d7334d25a025ae1b3d820787919190a4271f1e"
    }
  ],
  "dependencies": [
    {
      "kind": "contract",
      "id": "BH-P01",
      "version": "2.1.0",
      "relation": "uses"
    },
    {
      "kind": "contract",
      "id": "BH-P04",
      "version": "2.1.0",
      "relation": "uses"
    }
  ],
  "requirements": [
    {
      "id": "REQ-P05-01",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY"
      ],
      "acceptance": [
        "Una revisión vigente por identidad/hash y antecedentes trazables; sin segundo propietario de reglas o valores."
      ]
    },
    {
      "id": "REQ-P05-02",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY"
      ],
      "acceptance": [
        "Contexto completo dentro del presupuesto; impacto compara altas/cambios/bajas y declara rutas sin mapear."
      ]
    },
    {
      "id": "REQ-P05-03",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY"
      ],
      "acceptance": [
        "Derivados tienen integridad y consumidor identificado; registro Git/release remite a BH-P08."
      ]
    },
    {
      "id": "REQ-P05-04",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY"
      ],
      "acceptance": [
        "Se regeneró únicamente lo afectado y las capacidades diferidas no se presentan como implementadas."
      ]
    }
  ],
  "profile_data": {
    "inputs": [
      "Cambios y consumidores afectados",
      "Corte anterior y nuevo corte"
    ],
    "outputs": [
      "Versión seleccionada y mapa de migración",
      "Derivados afectados con integridad"
    ],
    "responsibilities": [
      "coordinator: compatibilidad y distribución",
      "optimizer: medición solo ante necesidad"
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
# BH-P05 · Mantenimiento, contexto y distribución

### REQ-P05-01

**1. Un propietario y una versión seleccionada**

Aplicar cuando cambien fuentes vigentes, artefactos derivados o un entregable de consumo. No reconstruir una plataforma de distribución para cerrar una edición local.

La política y decisiones conservan permisos; `norms/catalog.json` selecciona contratos y tokens por identidad, versión y hash. `evidence/` conserva observaciones, copias históricas y comprobantes. `protocols/` contiene los contratos operativos seleccionados en ese mismo catálogo, sin duplicarlos en `norms/`. No duplicar valores de tokens en instrucciones, CSS editable y contratos.

Registrar una revisión y su alcance cuando cambie una norma. Conservar versiones anteriores como evidencia y seleccionar una sola vigente; no sobrescribir el contenido aprobado de una revisión. Las aprobaciones y QA pertenecen al corte que identifican, no a toda revisión futura.

### REQ-P05-02

**2. Consulta e invalidación**

Leer primero el índice de protocolos y el propietario pertinente. Para entidades registradas usar contexto por identidad e intención; ampliar hacia requisitos originales y dependencias cuando la tarea lo requiera. Para Button usar `context BUTTON-001 --compact --modes '{"button":"Contable"}'`; el presupuesto se mide sobre JSON canónico UTF-8, sin el espaciado de presentación CLI. El modo predeterminado es Contable y la salida lo declara; los overrides explícitos del alias prevalecen en su traza. No cargar inventarios completos, snapshots ni todos los protocolos como arranque obligatorio. El mapa de consumo solo enlaza identidades, propiedades y nodos; no duplica requisitos editables del MD.

Identificar altas, cambios y bajas y sus consumidores. `impact` cubre dependencias declaradas actuales; una ruta sin correspondencia o una baja requiere comparar el corte anterior. La ausencia de relación declarada no demuestra ausencia de consumidores. Revalidar únicamente la parte afectada con cobertura suficiente; no propagar un fallo local a familias independientes.

### REQ-P05-03

**3. Derivados y distribución**

Regenerar únicamente salidas cuyos datos, herramientas o configuración hayan cambiado. Verificar sus hashes finales y referencias antes de declararlas vigentes. Evitar autorreferencias: un manifiesto no incluye su propio hash; los comprobantes no se empaquetan como otra definición normativa que obligue a regenerar continuamente.

Separar versiones de esquema, contenido DS, biblioteca/adaptadores y motor de skill. Un cambio compatible de contenido no exige reinstalar una skill. Preparar artefactos inmutables e integridad antes de cambiar un puntero de consumo autorizado; conservar el último corte válido si falla. El registro de envíos, las releases oficiales y la compatibilidad de componentes pertenecen a [BH-P08](08-GITHUB-RELEASE-DOCUMENTATION.md).

Un paquete debe declarar exports, CSS y assets necesarios sin depender del repositorio original. El catálogo Next.js es un consumidor. Un modo offline fija su corte; un canal actual consulta y fija el resultado al inicio del encargo. No cambiar el corte a mitad de tarea ni usar una caché antigua silenciosamente.

### REQ-P05-04

**4. Automatización bajo demanda**

Graphify continúa opcional y sin implementar. No forma parte del check, la consulta obligatoria ni el cierre de cada componente. Si posteriormente se incorpora, será una proyección con procedencia de fuentes, sin autoridad para aprobar reglas. No se recupera la obligación histórica de sincronizar un grafo global.

Las skills, paquetes y oficina de agentes se mantienen solo cuando existan y el encargo los afecte. No generar dos skills en cada cambio de token, instalar copias locales, iniciar agentes persistentes, hooks o monitores al copiar protocolos. Los roles de la política describen responsabilidades y no despachan trabajo por sí solos.

Registrar bytes, tiempos, invocaciones y reintentos cuando puedan medirse; no equiparar reducción de texto con ahorro garantizado de tokens o latencia. En coordinación futura, reutilizar el resultado del propietario de un trabajo activo y su evidencia; no reconstruir en paralelo lo mismo ni borrar locks. No se implementa aquí un servicio o scheduler.

El mantenimiento termina al poder localizar la regla vigente, sus fuentes y el QA del alcance sin depender de la conversación. Los procedimientos preparados no acreditan software, componentes, adaptadores o pipelines aún inexistentes.
