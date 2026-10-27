# P05. Autodocumentación y trazabilidad

Por [DEC-AI-TECHNICAL-CLOSURE-001](../registry/DEC-AI-TECHNICAL-CLOSURE-001.md), cada agente documenta fuentes, solicitud, cambios, verificaciones reales y límites de su trabajo. La ausencia de revisión humana no crea una tarea pendiente ni frena el cierre técnico. Una observación posterior abre un registro de defecto, alcance y revalidación, conservando la evidencia anterior.

**Versión:** 0.2.6 · **Sustituye al antiguo P04.**

## 1. Propósito

Mantener memoria verificable de qué fuentes entraron, qué contrato se elaboró, quién aprobó qué versión, qué se construyó, dónde y con qué resultado. Acompaña ingesta, síntesis, aprobación, construcción y QA. No inventa intención ni aprueba requisitos.

Lee [AGENTS.md](../AGENTS.md). Registra hechos, evidencias y razones resumidas; no se requieren monólogos internos ni una cadena privada de razonamiento.

## 2. Registros y responsabilidades

| Registro | Contenido propio |
|---|---|
| `registry/sources.md` | ID de fuente, ruta/URL, versión/snapshot, hash, rol, autoridad comprobada y cobertura. |
| `registry/contracts.md` | Identidad, ruta, versión, estado documental, datos referenciados y preparación por destino. |
| `registry/decisions.md` | Aprobaciones, rechazos, cambios autorizados y resolución de conflictos. |
| `registry/implementations.md` | Contrato/versión/datos → archivo, página, nodos y mapa de IDs reales. |
| `registry/qa.md` | Tipo de revisión, versión, requisitos, evidencias y resultado. |
| `registry/environment.md` | Herramientas/capacidades verificadas, configuración sin secretos y estado del grafo. |
| `registry/skills.md` | Releases de las dos skills: versión común, digest del DS, paquetes, QA e instalación local comprobada. |

Crea solo los registros que la tarea necesita. No reemplaces registros existentes por plantillas vacías. Usa rutas relativas y vínculos reales cuando exista el recurso. Una ruta prevista debe marcarse como prevista, no como entregable generado.

## 3. Estado en dimensiones separadas

No uses un único `status` para describir todo el proyecto.

- Fuentes: `RECEIVED`, `INDEXED`, `BLOCKED`, `CONFLICT`, `SUPERSEDED`.
- Contratos: `DRAFT`, `IN_REVIEW`, `DELEGATED_FOR_BUILD` (delegación de P03 respaldada por solicitud y QA documental), `APPROVED`, `REJECTED`, `SUPERSEDED`, según [P03](03-CONTRACT-SYNTHESIS.md).
- Preparación de cada destino: `READY`, `BLOCKED`, `CONFLICT`.
- Implementación por destino: `NOT_STARTED`, `IMPLEMENTING`, `IMPLEMENTED`, `VALIDATING`, `VALIDATED`, `VALIDATED_WITH_EXCEPTIONS`, `FAILED`, `STALE`.

La preparación ausente significa desconocida, no `READY`. Un contrato puede estar aprobado para Figma y tener web fuera de alcance. Una implementación puede estar validada contra una versión anterior y quedar `STALE` frente a la nueva.

Para el trabajo delegado según [DEC-AI-TECHNICAL-CLOSURE-001](../registry/DEC-AI-TECHNICAL-CLOSURE-001.md), registra `user_audit: NOT_REQUIRED` y `human_review_policy: OPTIONAL_NON_BLOCKING`. Conserva los `PENDING` históricos como evidencia, sin tratarlos por sí solos como gate de cierre. `VALIDATED` describe el QA técnico de la implementación contra el contrato delegado, no aceptación humana de su contenido.

En la migración bajo DEC-MIGRATION-SPECS-AUDIT-001, registra por separado ubicación publicada en `specs/`, QA técnico y auditoría humana. La promoción por QA no cambia `DELEGATED_FOR_BUILD` a `APPROVED`. Consolida en un documento de auditoría por excepciones solo ambigüedades, conflictos y decisiones materiales no resueltas; no conviertas cada contrato conforme en una aprobación individual solicitada al usuario.

Tras la promoción documental, DEC-MIGRATION-SPECS-CANONICAL-001 sitúa cualquier revisión normativa o enmienda en `specs/`. Registra allí la versión sustituida y su alcance, y enlaza QA, decisión e IDs de implementación desde los registros; conserva borradores y evidencia histórica sin convertirlos en una norma paralela. Una edición que cambie requisitos nunca se disfraza de simple movimiento de archivo.

Los estados extendidos de 0.2.0 deben migrarse desde los registros anteriores conservando su historial, no reasignarse masivamente sin evidencia.

## 4. Trazabilidad de síntesis

Para cada contrato candidato registra fuentes exactas, localizadores, transformaciones, cobertura, requisitos candidatos y reporte de síntesis. Usa la [plantilla de reporte](../templates/contract-synthesis-report.template.md).

Ejemplo de campos del registro, no de un contrato real:

```yaml
contract_id: null
path: null
version: null
document_status: DRAFT
source_refs: []
source_digests: []
synthesis_report: null
document_qa_record: null
approval_decision: null
readiness_by_target: {}
```

Completa los campos con evidencia. No asignes `owner: Design System`, un paquete de React o `stable` porque aparecían en el ejemplo educativo.

## 5. Aprobaciones y decisiones

Registra quién decidió, fecha real, solicitud o respuesta que autoriza, entidad, versión, alcance, requisitos adoptados y vínculos a fuentes. Para aprobación, conserva digest del candidato revisado, digest del contrato publicado y de sus datos vinculados, según el procedimiento de P03.

No edites requisitos durante una promoción administrativa. Si cambian requisitos, vuelve a revisión. Un rechazo conserva su razón y la revisión rechazada. Una aprobación no retroactiva no convierte ejecuciones previas no autorizadas en correctas.

## 6. Trazabilidad de implementación

Para [P-SLOTS](SLOTS-REVIEW-AND-IMPLEMENTATION.md), registra además aplicabilidad, versión del protocolo, mecanismo nativo o alternativa autorizada, IDs anfitrión/Slot/dependencias, operaciones probadas desde una instancia, cantidades de prueba y QA. Mantén separados el QA histórico y la conformidad con una nueva exigencia de Slots; no declares migrados componentes aún pendientes.

Para cada lote significativo registra:

```yaml
implementation_id: null
artifact_name: null
artifact_type: null
target: figma
implementation_status: NOT_STARTED
contract_ref: null
contract_version: null
contract_digest: null
data_refs: []
source_refs: []
dependency_refs: []
target_locator:
  file_key: null
  page_name: null
  page_id: null
  node_ids: []
id_mapping_ref: null
operation: null
tool_and_version: null
before_evidence: []
actions_completed: []
after_evidence: []
qa_record: null
known_deviations: []
timestamp: null
```

No declares una operación realizada cuando solo fue planeada. Para componentes, conserva nombre exacto e ID real de la página de la familia y el mapa de IDs de variables desde el JSON aprobado hacia el destino. Separa el binding esperado del binding efectivamente leído. No guardes claves API ni credenciales dentro de registros o snapshots.

## 7. Historia y sustituciones

El ID lógico de un contrato sobrevive a movimientos y revisiones. Registra `supersedes` y `superseded_by`; conserva el historial sin mantener dos versiones activas para el mismo alcance.

Los hashes se calculan, no se transcriben como prueba de ejecución. Diferencia SHA-256 de bytes de cualquier serialización canónica o hash que excluya campos. Registra el método si se usan distintos digests.

Si cambia un contrato o JSON que sostiene una implementación, identifica consumidores afectados y marca necesidad de revalidación. No sustituyas la referencia de una implementación antigua por la versión nueva sin reconstrucción o QA.

## 8. Graphify y persistencia

Herramienta local para ejecutar estos controles: [guía scripts/ds](../references/PROJECT-TOOLING.md). La entrada común implementa verificación, vista derivada y cierre; no sustituye la autoridad ni los criterios GRAPH-SYNC siguientes.

Graphify no sustituye los registros ni decide aprobación. Consulta el grafo vigente para localizar fuentes, pero abre la fuente exacta para validar la afirmación. Un borrador indexado sigue siendo borrador.

Por [DEC-GRAPH-CONTINUOUS-SYNC-001](../registry/DEC-GRAPH-CONTINUOUS-SYNC-001.md), queda autorizada de forma permanente la sincronización local del grafo completo del corpus DS después de cambios relevantes. Es parte del cierre de cada lote coherente, no una pregunta de aprobación repetida ni un disparador por cada herramienta. Contratos, JSON, decisiones, protocolos, QA y registros requieren extracción semántica además del análisis estructural; AST-only no demuestra documentación actualizada.

GRAPH-SYNC-01: detectar archivos nuevos, cambiados y eliminados contra hashes, conservando fuentes y respaldos; excluir secretos, derivados, temporales y datos externos al proyecto. Comprobar rutas JSON de diseño excluidas por filtros sin desactivar globalmente la protección de secretos.

GRAPH-SYNC-02: completar extracción del delta y reutilizar contribuciones sin cambios solo por hash/procedencia; reconciliar sustituciones normativas e historia sin convertir borradores en aprobaciones. Actualizar graph.json, GRAPH_REPORT.md y graph.html del mismo corte.

GRAPH-SYNC-03: verificar cobertura de archivos soportados, manifiesto contra bytes finales, ausencia de IDs duplicados/endpoints rotos, diagnóstico de integridad, correspondencia de outputs y consultas de la decisión/contrato/token recién modificados. Registrar alcance real y exclusiones. Los cambios de cierre en registros también deben quedar indexados antes del gate final.

GRAPH-SYNC-04: declarar CURRENT solo tras las comprobaciones. Si no hay delta, basta verificar hashes y outputs. Si hay bloqueo, preservar el último grafo válido, registrar STALE/BLOCKED con causa y comunicarlo; no marcar el proyecto plenamente sincronizado. Esta autorización no instala herramientas, no modifica hooks/globales, no sube datos a servicios externos y no inicia monitores. Una exclusión posterior del usuario prevalece.

Las reglas locales de estados, triggers de actualización, readback, diagnóstico y procedencia del grafo se conservan en la [referencia operativa de Graphify](../references/GRAPH-OPERATIONS.md). Esta referencia complementa P01/P05; no es un séptimo protocolo ni convierte el grafo en autoridad.

## 9. Salida al usuario

Para las skills aplica [P08](08-SKILLS-AND-RELEASES.md). Registra por separado integridad del paquete, vigencia respecto del DS, pruebas del generador/HTML, instalación local y validación de una pantalla concreta. El versionado de la skill no aprueba contratos ni acredita una ejecución Figma que no ocurrió. Los registros de release y su QA quedan fuera del snapshot de consumo para evitar que sus propios hashes obliguen a generar otra versión; siguen siendo fuentes del grafo del proyecto.

Explica qué se recibió, redactó o construyó; desde qué fuentes; qué comprobaciones se ejecutaron; qué está aprobado y qué no; qué bloquea la siguiente fase. Usa vínculos a archivos/IDs verificables y no afirmes validaciones inexistentes.

El criterio de cierre es que otro agente pueda continuar con los archivos del proyecto sin depender de esta conversación ni confundir una plantilla con un contrato vigente.

## Índice de consumo Graph-First · 2026-10-23

El índice reducido se prepara localmente después del cierre P05 CURRENT mediante `scripts/ds_consumption.py --prepare`, usando el intérprete configurado para Graphify. `scripts/ds_consumption.py` sin argumentos valida la preparación sin ejecutar extracción. Luego `scripts/ds_remote.py` ensambla catálogo e índice como una unidad y `--check` verifica su vigencia. GitHub Actions ejecuta únicamente pruebas, validación y publicación; no crea conocimiento semántico ni repara un índice STALE. Si falta preparación o difieren fuentes/herramientas, conserva el puntero anterior.

Una sola fuente `scripts/consumer_graph.py` se distribuye por el empaquetador en ambos motores. La versión del índice es independiente del protocolo compatible del catálogo. El grafo sigue siendo derivado; cada resultado remite al snapshot y documentos originales. Fallback registrado sobre fuentes verificadas; conflictos y límites nunca producen éxito parcial. Los comprobantes preparados viven en `catalog/prepared/`, excluidos del corpus Graphify como los demás derivados del catálogo.

## Cierre coordinado e incremental · 2026-10-23

Por [DEC-EFFICIENT-CLOSURE-001](../registry/DEC-EFFICIENT-CLOSURE-001.md), usar scripts/ds close --run ID según la [guía](../references/EFFICIENT-CLOSURE.md). El comando coordina escritores, comparte comprobaciones del mismo corte y genera catálogo y ZIP con integridad final. Sustituye la ejecución redundante de subcomandos equivalentes; conserva todos los criterios de QA. Los comandos individuales siguen disponibles. Los estados BUSY/WAITING_FOR_SEMANTICS requieren reutilizar al propietario, no otro rebuild; NEEDS_SEMANTICS conserva la extracción semántica del delta según la skill. Registrar métricas reales y límites de atribución. No concede publicación remota.
