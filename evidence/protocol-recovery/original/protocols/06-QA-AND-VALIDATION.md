# P06. QA documental y validación de implementación

**Versión:** 0.2.6 · **Sustituye al antiguo P05.**

## 1. Objetivo y separación

Lee [AGENTS.md](../AGENTS.md) y registra según [P05](05-SELF-DOCUMENTATION-AND-TRACEABILITY.md).

Este protocolo tiene dos revisiones diferentes:

- `CONTRACT_REVIEW`: antes de habilitar construcción, verifica el contrato candidato contra sus fuentes.
- `IMPLEMENTATION_REVIEW`: después de construir, verifica el resultado real contra el contrato aprobado y los datos vinculados.

Ninguna revisión documental crea aprobación humana. Ninguna creación de archivo o respuesta de escritura prueba que el componente funcione.

En el alcance delegado de [P03](03-CONTRACT-SYNTHESIS.md), `CONTRACT_REVIEW: PASS` puede habilitar `DELEGATED_FOR_BUILD` si no hay conflictos bloqueantes; sigue sin equivaler a `APPROVED`. `IMPLEMENTATION_REVIEW: PASS` acredita la implementación técnica y permite cierre técnico con revisión humana opcional según [DEC-AI-TECHNICAL-CLOSURE-001](../registry/DEC-AI-TECHNICAL-CLOSURE-001.md). En nuevos registros usa `user_audit: NOT_REQUIRED`; un `PENDING` histórico no impide el cierre por sí solo. El QA no puede ocultar decisiones materiales no demostradas bajo “mejor criterio”.

DEC-MIGRATION-SPECS-AUDIT-001 permite promover a `specs/` el contrato delegado solo después de ambos QA `PASS`, sin afirmar aprobación humana. Una instrucción posterior sobre fidelidad de color u otro requisito vuelve `STALE` el QA de la parte afectada hasta su readback y nueva evaluación; la promoción no puede usar un `PASS` que ya no cubre el requisito vigente. La auditoría humana se presenta por excepciones en un documento consolidado.

## 2. Resultados por comprobación

Usa `PASS`, `FAIL`, `BLOCKED` y `NOT_APPLICABLE`. Cada resultado incluye ID de requisito/control, alcance, fuente esperada, evidencia obtenida y explicación cuando no pasa.

`NOT_APPLICABLE` exige que el requisito esté realmente fuera del alcance revisado; no significa que una herramienta no pueda comprobarlo. Falta de lectura o evidencia para un requisito necesario se clasifica `BLOCKED`.

Una desviación aceptada conserva la diferencia y referencia de autorización. No cambies el resultado original a `PASS` para borrar el historial.

## 3. Revisión del contrato antes de habilitar construcción

### Entradas

Candidato de [P03](03-CONTRACT-SYNTHESIS.md), reporte de síntesis, fuentes identificadas, decisiones existentes, datos y plantilla aplicable. La fuente puede ser JSON, Figma o documentación; no hay obligación de acceder a Figma si el alcance se basa solo en datos locales.

### Controles documentales

| ID | Comprobación |
|---|---|
| DOC-01 | El tipo de contrato corresponde al contenido y no se fuerza la anatomía de Button a tokens. |
| DOC-02 | Frontmatter, tablas y bloques de código son legibles y válidos en sus formatos. |
| DOC-03 | Identidad, versión, alcance, fuentes y dependencias están declarados sin inventar metadatos. |
| DOC-04 | Toda afirmación normativa propuesta tiene procedencia y fuerza normativa identificables. |
| DOC-05 | Se distinguen observaciones, reglas aprobadas, inferencias y preguntas pendientes. |
| DOC-06 | No se copiaron valores, tokens, paquetes o variantes del ejemplo sin evidencia propia. |
| DOC-07 | Las referencias del JSON resuelven; datos no disponibles se marcan, no se reconstruyen intuitivamente. |
| DOC-08 | Existe una sola descripción canónica por token y no dos catálogos editables. |
| DOC-09 | Estados, propiedades, anatomía, variantes y restricciones no se contradicen entre secciones. |
| DOC-10 | Las reglas de tokens no contradicen tablas de tamaños o ejemplos con literales. |
| DOC-11 | `required`, `default`, `nullable`, icon-only y combinaciones permitidas no generan contradicciones. |
| DOC-12 | El mapeo Figma/web identifica límites y no garantiza capacidades no demostradas. |
| DOC-13 | Los criterios de aceptación son comprobables y enlazan requisitos reales. |
| DOC-14 | Las fuentes originales no fueron alteradas para ajustarlas al contrato. |
| DOC-15 | La autoridad está identificada: aprobación humana real o delegación técnica con solicitud, versión y alcance. No se inventa revisión humana ni se exige como gate rutinario. |
| DOC-16 | Los faltantes están separados por destino y no se ocultan bajo `NOT_APPLICABLE`. |
| DOC-17 | Para una familia destinada a Figma, el nombre exacto de su página está sustentado o `UNRESOLVED`, sin derivarlo de apariencia, variantes ni del archivo fuente. |
| DOC-18 | El mapeo de roles de color y tipografía referencia el JSON aprobado con digest y localizadores, distingue IDs de origen/destino, modo y evidencia; no crea equivalencias por igualdad visual. |

La revisión del ejemplo educativo no convierte sus decisiones en normas. Si su estructura muestra una tabla mal formada o una contradicción, registra el problema y usa una estructura válida para el candidato sin importar esa contradicción como requisito.

### Salida

Guarda el reporte en `qa/contracts/` y su registro. Si hay coherencia y cobertura suficiente para decisión, el candidato puede pasar a `IN_REVIEW`. Si faltan hechos necesarios, conserva `DRAFT` y las preguntas. Con QA documental `PASS`, P03 puede registrar `DELEGATED_FOR_BUILD` bajo la solicitud del usuario; la construcción requiere además preparación del destino. No espera aprobación humana rutinaria.

Se puede revisar un subconjunto, pero debe indicarse qué parte no quedó cubierta. No uses una aprobación parcial como aprobación de toda la familia.

## 4. Revisión de implementación

### Precondiciones

Contrato aprobado o delegado técnicamente según P03, versión/digest exactos, datos canónicos referenciados, decisiones de alcance, implementación registrada y capacidad de leer el resultado real. Si el contrato o los datos cambiaron, determina si se evalúa la versión anterior o se requiere reconstrucción.

### Secuencia

1. Deriva el checklist desde los requisitos del contrato vigente elegible antes de comparar el resultado.
2. Lee el destino real. No uses exclusivamente la respuesta con la que se creó.
3. Compara cada requisito obligatorio y documenta evidencia.
4. Clasifica defectos, faltantes, conflictos y limitaciones.
5. Corrige solo defectos deterministas de implementación dentro de una tarea autorizada.
6. Lee de nuevo después de la última corrección y repite controles afectados y dependientes.
7. Registra resultado por destino y alcance. No alteres el contrato para hacer pasar el test.

### Comprobaciones Figma

Aplica los controles SLOT-QA-01–09 de [P-SLOTS](SLOTS-REVIEW-AND-IMPLEMENTATION.md) cuando corresponda. La revisión documental siempre verifica aplicabilidad o justificación de no aplicación. La implementación debe demostrar edición de contenido variable desde una instancia consumidora, preservación de vínculos y tokens y layout correcto con distintas cantidades. No aceptar como evidencia suficiente el nombre Slot, una captura de cantidad fija o modificaciones al principal. Un requisito nuevo invalida únicamente el QA del alcance afectado hasta su revalidación.

Verifica archivo, **nombre exacto y unicidad de la página semántica por familia**, identidad, nombres, jerarquía, component sets, variantes, propiedades, estados, layout, tamaños, tipografía, contenido, bindings, modos, dependencias e interacciones documentadas.

Para colores y tipografía obligatorios, lee el binding real de cada propiedad aplicable y compara su ID local, colección, rol, alias y resolución por modo con el mapa derivado del JSON aprobado y de los IDs reales del destino. El mismo valor RGB o tipográfico sin binding no pasa. Comprueba excepciones explícitamente aprobadas por propiedad; no conviertas una limitación de la herramienta en `PASS`.

En esta migración, comprueba además que el scope técnico admite la propiedad y que la categoría semántica del nombre completo y `description` corresponde al uso real, aun cuando Figma permita el binding: roles de texto para texto, de fondo para superficies, de borde para strokes y de icono para iconografía. Los roles anidados como `color/feedback/danger/text` o `color/interactive/disabled/text` son texto; `color/focus/ring` es un trazo de foco. Revisa los paints de todas las variantes, incluidos estados e iconos opcionales, y distingue envolturas ocultas sin binding propio de paints consumidores efectivos. Si se creó un token nuevo bajo DEC-SEMANTIC-EXTENSIONS-001, compara su JSON de destino con la variable real campo por campo y verifica el alias a la primitiva existente en cada modo antes de validar los componentes consumidores.

Para tokens, compara colecciones/modos, nombres/tipos, valores, `description`, scopes, `codeSyntax` y el grafo de aliases. Traduce IDs con el mapa de origen/destino; no esperes que las cadenas de IDs coincidan entre archivos distintos.

La cobertura requerida de bindings y aliases no se sustituye por muestreo visual. Si una API solo permite inspección parcial, limita el resultado. No asegures cobertura completa porque algunos nodos coincidan.

### Comprobaciones web

La fase web está activada por DEC-WEB-COMPONENTS-001. Aplica [P07](07-WEB-COMPONENTS-AND-TECHNICAL-DOCUMENTATION.md): código, tipos, documentación, ejemplo sin backend y QA por familia. Evalúa el alcance web aplicable, interacciones, accesibilidad, consumo de tokens y pruebas en el entorno definido. La igualdad visual Figma/React es un control adicional, no reemplaza la conformidad de cada destino.

No declares teclado o accesibilidad web validados desde una captura de Figma.

## 5. Defectos y tolerancias

| Clase | Acción |
|---|---|
| `IMPLEMENTATION_DEFECT` | Corregir determinísticamente con autorización y volver a leer. |
| `CONTRACT_GAP` | Regresar a P03; no inventar el requisito que falta. |
| `SOURCE_CONFLICT` | Registrar fuentes y solicitar decisión. |
| `TOOL_LIMITATION` | Documentar operación no verificable; no marcar `PASS`. |
| `ACCEPTED_DEVIATION` | Conservar diferencia, aprobación, versión y alcance. |

No inventes tolerancias numéricas ni ajustes umbrales después de ver el resultado para hacerlo pasar. Los IDs lógicos, aliases, enums y textos canónicos exigen correspondencia exacta según su contrato. Si una conversión numérica o un render necesita tolerancia, debe estar definida y aprobada antes de certificar esa comparación.

## 6. Gate final

Por [DEC-AI-TECHNICAL-CLOSURE-001](../registry/DEC-AI-TECHNICAL-CLOSURE-001.md), el QA y cierre técnico no esperan revisión humana rutinaria. El agente mantiene documentación y evidencia; el cumplimiento de todos los controles obligatorios permite cerrar el alcance autorizado. Una revisión humana posterior es opcional y un defecto comunicado reabre solo la parte afectada para corrección y revalidación. Los errores, conflictos y evidencias ausentes siguen bloqueando el control correspondiente; esta política no transforma `NOT_RUN` en `PASS`.

En altas o modificaciones del DS, comprobar también [P08](08-SKILLS-AND-RELEASES.md): cobertura de la familia en ambas skills, hashes exactos de contratos/tokens/código/recursos, versión común, detección de derivados desactualizados y paquetes verificables. Cambios en instrucciones o scripts de una skill requieren las pruebas afectadas; no obligan a reconstruir una pantalla en Figma para afirmar únicamente integridad del paquete. Una prueba de traspaso Markdown acredita su contenido y correspondencia con el HTML; la fidelidad de una pantalla Figma exige construcción y lectura reales de ese destino.

`VALIDATED` requiere que todos los controles obligatorios aplicables pasen, que no haya conflicto ni lectura pendiente que afecte el resultado y que la trazabilidad esté completa.

`VALIDATED_WITH_EXCEPTIONS` se usa cuando el usuario acepta diferencias específicas. No equivale a cumplimiento íntegro. La excepción no autoriza cambios futuros ni otras implementaciones.

Si cambian después las fuentes o el destino, el estado anterior solo acredita la versión y lectura registradas. Marca `STALE` respecto de la nueva referencia hasta revalidar.

## 7. Registro mínimo

```yaml
qa_id: null
review_type: CONTRACT_REVIEW
contract_ref: null
contract_version: null
contract_digest: null
data_refs: []
implementation_ref: null
target: null
scope: null
checks: []
blocked_items: []
accepted_deviations: []
reviewer: null
executed_at: null
result: BLOCKED
```

El bloque es una plantilla, no un resultado real. Completa cada control con evidencia ejecutada; omite afirmaciones de instalación, lectura o aprobación que no puedas demostrar.
