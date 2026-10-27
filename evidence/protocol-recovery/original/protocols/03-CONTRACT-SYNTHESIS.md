# P03. Construcción de contratos Markdown a partir de fuentes

**Versión:** 0.2.5 · **ID estable:** P03 · **Nombre operativo:** Contract Synthesis

## 1. Propósito

Convertir fuentes ingestas en un contrato `.md` trazable, revisable y suficientemente preciso para reconstruir un artefacto sin improvisar. Las entradas pueden ser un inventario JSON, un nodo Figma, documentación o una combinación de ellas.

Este protocolo añade el paso que separa ingeniería inversa de implementación. No modifica el Figma fuente ni el destino. No crea componentes, no cambia valores de tokens y no aprueba su propio resultado.

Lee [AGENTS.md](../AGENTS.md), [P02](02-DOCUMENT-INGESTION-AND-STORAGE.md) y [P05](05-SELF-DOCUMENTATION-AND-TRACEABILITY.md). Antes de habilitar construcción o entregar la síntesis, aplica la revisión documental de [P06](06-QA-AND-VALIDATION.md).

## 2. Límites de responsabilidad

| Protocolo | Responsabilidad |
|---|---|
| P02 | Conservar, clasificar y ubicar lo recibido. |
| P03 | Analizar evidencia, formular el contrato candidato y exponer faltantes. |
| P06, revisión documental | Comprobar trazabilidad, coherencia y verificabilidad del candidato. |
| Usuario | Definir el encargo; aportar decisiones materiales necesarias y observaciones posteriores opcionales. |
| P04 | Construir únicamente desde la especificación aprobada o delegada técnicamente y lista. |
| P05 | Mantener procedencia, decisiones, estado y relaciones en todas las fases. |

La aprobación del método, de una plantilla, de este protocolo o de una auditoría no aprueba automáticamente el contenido de un contrato nuevo.

## 3. Modos de entrada

### A. JSON → contrato MD

Selecciona la plantilla [Foundations/Tokens](../templates/foundations.contract.template.md) si la entrada define variables, colecciones, modos o foundations. Un JSON que describe componentes puede usar la plantilla de componente si realmente aporta ese contenido.

Documenta lo que el JSON contiene y lo que no permite demostrar. No infieras una biblioteca de componentes porque existan tokens con nombres relacionados con botones.

### B. Nodo Figma → contrato MD

Selecciona la plantilla [Componente](../templates/component.contract.template.md) cuando el nodo represente una familia o componente identificable. Un frame de pantalla o una instancia aislada puede permitir un contrato parcial, no necesariamente uno completo de toda la familia.

La inspección es de solo lectura y se limita al nodo, descendientes y referencias necesarias dentro del alcance autorizado. No reutilices automáticamente el archivo destino como fuente.

### C. Fuentes combinadas → contrato MD

Combina JSON, nodos, contratos relacionados, decisiones y auditorías. Declara qué fuente respalda cada dimensión. Si el JSON gobierna un token y Figma muestra otro valor, conserva ambas evidencias y registra la discrepancia, no una tercera definición inventada.

### D. Contrato MD existente → revisión

Si ya existe un contrato aprobado para esa entidad, verifica su versión y propone un cambio trazable solo si la tarea lo solicita. No generes un contrato canónico paralelo ni cambies su ID por reorganizar carpetas.

## 4. Precondiciones y alcance

Debe existir una solicitud para sintetizar o revisar contratos y al menos una fuente real accesible. Si no hay fuentes, detente después de preparar el procedimiento: no fabriques un Button o un inventario de prueba.

Antes de analizar, registra entidad objetivo, tipo, alcance de extracción, destino(s) de implementación previstos y fuentes disponibles. Los nombres de archivo de ejemplo no prueban que esos archivos estén en el repositorio.

Si faltan datos, puedes producir un borrador parcial con limitaciones. La falta de evidencia impide aprobar o construir los requisitos afectados, no obliga a perder el trabajo documental ya sustentado.

## 5. Registro de fuentes y evidencia

Cada fuente recibe un ID estable `SRC-...` y un localizador verificable:

- Archivo: ruta relativa al repositorio, versión si existe y SHA-256 de sus bytes.
- JSON: además, collection/variable ID cuando aplique y un selector preciso. Se puede registrar un JSON Pointer junto al ID estable para sobrevivir a cambios de orden.
- Figma: file key, node ID, tipo de nodo, fecha y snapshot de la respuesta obtenida. Diferencia instancia, componente principal y component set.
- Markdown: ruta, versión y encabezado o rango que respalda la afirmación.
- Decisión del usuario: referencia al registro con fecha, decisión, alcance y versión afectada.

Nunca inventes un hash, un node ID, una lectura de Figma ni una fecha de aprobación. Si solo posees un informe que afirma haber inspeccionado consumidores, la fuente de tu afirmación es ese informe; no presentes la inspección como propia.

### Clasificación de afirmaciones

| Etiqueta | Significado | Uso en el contrato candidato |
|---|---|---|
| `EXPLICIT` | Declarado literalmente por una fuente identificada. | Puede respaldar una regla; verificar autoridad y alcance de esa fuente. |
| `DERIVED` | Resultado determinista de datos explícitos. | Registrar datos de entrada y transformación reproducible. |
| `OBSERVED` | Propiedad leída en una implementación. | Puede proponerse como baseline de reconstrucción, con adopción humana pendiente. |
| `INFERRED` | Interpretación plausible no demostrada. | Solo propuesta abierta en el reporte; no obligación vigente. |
| `UNRESOLVED` | No se dispone de evidencia suficiente. | Registrar pregunta e impacto. |
| `CONFLICT` | Fuentes relevantes discrepan. | Bloquear la decisión afectada y conservar ambas referencias. |

Estas etiquetas clasifican procedencia, no prioridad ni aprobación. Un ejemplo puede contener una frase explícita que no sea válida para nuestro sistema. Una aprobación futura adopta una decisión para reconstrucción; no demuestra que fuera la intención histórica del sistema original.

## 6. Análisis del JSON

Comprueba sintaxis y, cuando exista un esquema aprobado, su conformidad. No inventes un esquema y luego anuncies que la fuente cumple un estándar externo. Un esquema elaborado por el agente es un candidato separado hasta aprobación.

Para un inventario de tokens revisa, según campos presentes:

1. Colecciones, IDs, nombres, tipos, modos y modo predeterminado.
2. Cobertura de valores por modo, aliases y referencias externas.
3. Integridad de referencias, ciclos y compatibilidad de tipos.
4. Descripciones, scopes y `codeSyntax` reales.
5. Valores literales y relaciones primitive/semantic efectivamente declaradas.
6. Ambigüedades de unidades, tipografía y conversiones entre plataformas.
7. Cambios documentados por auditorías frente a los bytes recibidos.

No redondees valores, renombres tokens, alteres aliases, reemplaces scopes ni llenes `codeSyntax` durante esta fase. Cero, cadena vacía, lista vacía, `null` y campo ausente no significan lo mismo.

Un `FLOAT` no define por sí solo una unidad CSS. No conviertas automáticamente `regular` a un peso numérico, una fracción a porcentaje, o un valor de tracking a `em`. Registra la unidad demostrada o el mapeo pendiente.

Si dos tokens comparten valor, no los fusiones. Si una variable semántica tiene un literal, consérvalo salvo instrucción aprobada. Si no aparecen sombras u otros foundations, limita la afirmación a la cobertura del inventario; no declares que no existen en todo el sistema.

### Datos canónicos y una sola descripción

El contrato MD debe referenciar la versión exacta del JSON aprobado para valores, aliases, modos y `description`, sin transcribir un catálogo editable completo.

Declara explícitamente qué campos delega al JSON. Las descripciones detalladas de tokens viven únicamente en `description`. No agregues `usage`, `figmaDescription` ni `aiDescription`. Los reportes de evidencia guardan localizadores, hallazgos y razones, no una segunda documentación de uso que compita con la canónica.

Cuando haga falta mejorar semántica, registra la necesidad como cambio propuesto. La síntesis del contrato no autoriza modificar el inventario. Un JSON previamente aprobado no necesita reaprobación si permanece idéntico; la nueva interpretación normativa del MD sí necesita revisión.

## 7. Análisis del nodo Figma

Antes de leer, verifica las capacidades necesarias con [P01](01-ENVIRONMENT-AND-TOOLS.md). Si falta acceso, registra el bloqueo sin inventar resultados.

Captura identidad, jerarquía, componentes anidados, propiedades, variantes, tamaños, estados representados, layout, dimensiones, contenido, overrides y bindings disponibles. Diferencia el valor resuelto de la referencia a variable y el modo explícito del heredado.

No deduzcas comportamiento web, teclado, accesibilidad, reglas de producto o intención de uso solamente de la apariencia. No conviertas un estado llamado `disabled` en evidencia de que el navegador bloqueará eventos. No conviertas una dimensión observada en regla universal de tamaño fijo si no se conoce el comportamiento de layout.

Un componente de una sola variante no demuestra todo el conjunto. Cuando exista component set o main component relacionado, inspecciónalo solo dentro del alcance autorizado. Registra variantes leídas y faltantes. No inventes el producto cartesiano de todas las propiedades como combinaciones válidas.

No conviertas automáticamente propiedades de Figma en la API conceptual del contrato. Conserva el nombre nativo como evidencia y propone un mapeo cuando se necesite. Una propiedad booleana por sí sola no demuestra todas las consecuencias de interacción que pueda representar.

Usa capturas como evidencia visual complementaria. Una imagen no acredita un binding, alias, estado interactivo o propiedad que no se haya leído.

## 8. Síntesis del modelo conceptual

Separa identidad, variantes, tamaños, estados, contenido y comportamiento. No elimines diferencias observadas para que encajen en un modelo ideal.

Construye una matriz con afirmación, evidencia, cobertura, posible requisito y pregunta pendiente. Para cada requisito candidato asigna un ID estable `REQ-...`, fuerza normativa propuesta (`MUST`, `MUST NOT`, `SHOULD` o `MAY`), fuente y forma de comprobación.

En `DRAFT` e `IN_REVIEW`, todos los requisitos son candidatos, aunque usen vocabulario normativo. Una afirmación `OBSERVED` puede originar un requisito propuesto de reconstrucción si se identifica como adopción pendiente. Una inferencia de intención no debe camuflarse como un `MUST` demostrado: permanece en propuestas hasta que una decisión explícita la respalde.

Cada `MUST` debe poder verificarse. Evita mandatos vacíos como “debe verse correcto”. No generes criterios de QA que solo comparen el agente contra su propio resumen, sin regresar a las fuentes y al contrato aprobado.

## 9. Estructura del contrato

### Revisión transversal de Slots

Aplica [P-SLOTS](SLOTS-REVIEW-AND-IMPLEMENTATION.md) antes de declarar preparación para construcción. Registra aplicabilidad por familia y, cuando corresponda, región semántica, contenido permitido, cardinalidad frente a cantidad de muestra, operaciones, layout, herencia de tokens y pruebas. Integra sus reglas en las secciones existentes de Anatomy/Properties/Composition/Acceptance criteria. No equipares instancias expuestas o swaps a un Slot nativo ni apruebes una lista fija como contenido variable. Cambios posteriores a publicación se versionan en specs; los detalles de capacidad y cierre se rigen por P-SLOTS.

Para componentes conserva las 21 secciones de la plantilla derivada del ejemplo entregado: Purpose, Contract, Anatomy, Properties, Variants, Sizes, States, Behavior, Accessibility, Design tokens, Content rules, Composition rules, Responsive behavior, Edge cases, Forbidden combinations, Design ↔ Code mapping, Acceptance criteria, Examples, Source of truth, Change management y Changelog.

Para foundations usa una estructura específica de inventario, escalas, aliases, modos, documentación semántica, unidades, destino y aceptación. No fuerces `loading`, `disabled` o anatomía de Button en un contrato de tokens.

En cada sección usa contenido demostrado o la marca `UNRESOLVED` con pregunta e impacto. `NOT_APPLICABLE` requiere justificación; no sirve para esconder información que sí es necesaria pero desconocida. No mantengas `TODO` en una versión aprobada para una fase que dependa de ese campo.

Los metadatos `owner`, versión de producto, paquete de código, madurez y URLs no se copian del ejemplo. El frontmatter debe ser YAML válido con delimitadores e indentación consistentes. Mantén las tablas con columnas bien formadas y los bloques de código cerrados.

### Mapeo Figma/frontend

Para nuevas incorporaciones al DS, [P07](07-WEB-COMPONENTS-AND-TECHNICAL-DOCUMENTATION.md) exige además implementación React/TypeScript/Tailwind/Next.js, documentación técnica y ejemplo sin backend. La solicitud DEC-WEB-COMPONENTS-001 activa este destino para las familias existentes. La API técnica y el comportamiento local se documentan por alcance; no modifican silenciosamente la norma visual ni aprueban reglas de negocio.

Un contrato puede tener alcance inicial `figma` y dejar `web` fuera de la implementación actual. Registra esa frontera, no declares validación web inexistente.

Para cualquier mapeo, anota propiedad conceptual, propiedad observada, evidencia y limitaciones. No prometas equivalencia 1:1 si una herramienta no la soporta. Los valores de diseño no se obtienen de una salida React si existe una especificación aprobada aplicable.

Para cada familia destinada a `AI-Design-System`, propone un **nombre exacto de página** basado en la función semántica de la familia, con fuente o decisión que lo respalde. No lo derives del color, tamaño, estado, variante, nombre del archivo antiguo ni de una regla automática de singular/plural. Si el nombre no está decidido, marca `UNRESOLVED` y no declares la construcción `READY`. Una página existente solo se asigna tras verificar su identidad y contenido; el nombre propuesto no demuestra que ya exista.

El contrato identifica por parte y estado los roles de color y tipografía del componente, y referencia el token lógico de `AI-Design-System` que se propone consumir. Para ello consulta el [JSON de variables aprobado](../sources/inventories/tokens.inventory.json) bajo `FOUNDATIONS-TOKENS-001`: registra su digest vigente y localizadores de colección/variable/modo, y toma de él nombres, tipos, modos, valores, aliases y la única `description` canónica. No duplica esos valores como catálogo editable en cada contrato. Distingue token observado en la fuente, token semántico local del destino, evidencia de equivalencia de **uso** y binding requerido; igualdad de valor visual no basta. Para tipografía cubre las propiedades aplicables —familia, peso, tamaño, interlineado y espaciado de letras— sin inventar tokens ausentes. Un mapa derivado por ID real de destino se verifica en el preflight P04 antes de marcar `READY`. Si no existe correspondencia semántica, registra `CONTRACT_GAP`/`UNRESOLVED` para decisión; no copies el literal de origen ni crees una variable nueva por intuición.

## 10. Auditoría y reporte de síntesis

Antes de habilitar construcción, aplica P06 a nivel documental. Produce un reporte con la [plantilla de síntesis](../templates/contract-synthesis-report.template.md): fuentes, cobertura, evidencia, requisitos, conflictos, inferencias, dudas, transformaciones y resultado de revisión.

Clasifica cada pregunta pendiente por el destino que bloquea. La falta de nombres CSS puede bloquear web sin impedir reconstruir variables en Figma. La falta de un binding obligatorio sí bloquea el elemento Figma afectado. No generalices el bloqueo a toda la familia si puede acotarse explícitamente.

No sugieras que este reporte demuestra una inspección nueva del Figma destino. No conviertas una auditoría del contrato en validación de implementación.

## 11. Estados, revisión y aprobación

El estado documental del contrato es independiente del estado de implementación:

```text
DRAFT → IN_REVIEW → APPROVED
                  ↘ DELEGATED_FOR_BUILD (QA documental y solicitud autorizada)
                  ↘ REJECTED → DRAFT revisado
APPROVED → nueva versión candidata
APPROVED anterior → SUPERSEDED cuando la sustitución se aprueba
```

`DRAFT`: contrato candidato, incluso parcial. `IN_REVIEW`: candidato coherente, con paquete de fuentes identificado, listo para la revisión documental. Ninguno permite construir por sí solo.

`APPROVED` exige una aprobación explícita del usuario para entidad, versión y alcance. Silencio, una instrucción genérica de continuar o un `status: stable` importado no bastan si no identifican inequívocamente el candidato.

Por DEC-MIGRATION-SPECS-AUDIT-001, la ubicación en `specs/` ya no prueba por sí sola `APPROVED`: los contratos delegados de esta migración se promueven allí solo tras QA documental e implementación técnica `PASS`, con estado `DELEGATED_FOR_BUILD` y `user_audit: PENDING` visibles. Una promoción administrativa de ruta no modifica requisitos; si hay una nueva instrucción que afecta valores o criterios, reabre y revalida ese alcance antes de la promoción.

Por DEC-MIGRATION-SPECS-CANONICAL-001, después de esa promoción cualquier ajuste normativo se prepara y conserva en `specs/` como nueva versión o enmienda del contrato vigente. Se registra qué sustituye, se revalida el alcance afectado y se sincroniza la implementación cuando corresponde. `drafts/` sigue disponible para evidencia de origen y trabajo previo a la primera promoción, no para una segunda especificación vigente.

### Delegación general para el trabajo de IA solicitado

[DEC-AI-TECHNICAL-CLOSURE-001](../registry/DEC-AI-TECHNICAL-CLOSURE-001.md) elimina la espera de aprobación humana rutinaria. Tras QA documental `PASS`, el agente registra solicitud, fuentes y hashes, alcance, dependencias, requisitos, destino y decisión de delegación; usa `DELEGATED_FOR_BUILD`, `user_audit: NOT_REQUIRED` y `human_review_policy: OPTIONAL_NON_BLOCKING`. Con preparación `READY`, continúa la implementación que el usuario pidió. Una tarea de solo documentación no habilita escrituras en Figma.

La publicación en `specs/` de contratos delegados exige QA documental y de implementación técnica `PASS`; conserva el estado delegado. Las revisiones de contratos ya publicados se redactan en su ubicación canónica, con alcance de sustitución y QA afectado. `APPROVED` sigue reservado a decisión humana explícita. Los pendientes históricos de auditoría humana son no bloqueantes; las incertidumbres materiales y controles técnicos pendientes siguen limitando su alcance.

### Antecedente: delegación para la Librería anterior

Las siguientes condiciones históricas conservan su procedencia. Su exclusividad de alcance y espera de auditoría humana quedan sustituidas por la delegación general anterior; las restricciones de diseño y evidencia se mantienen.

[DEC-LEGACY-MIGRATION-DELEGATION-001](../registry/decisions.md) autoriza **solo** la migración desde el archivo fuente `9zs5RMR8LB5wHjW9Bd59BA` al destino `AI-Design-System` con auditoría humana posterior, sin aprobación previa de cada contrato. Tras lectura profunda de la familia y `CONTRACT_REVIEW` en `PASS`, un contrato versionado puede pasar a `DELEGATED_FOR_BUILD` si identifica su fuente, digest, nombre de página semántico, mapa al JSON de variables aprobado, dependencias y requisitos verificables. Esta etiqueta habilita el preflight P04 para esta decisión; **no es aprobación humana del contenido** ni se extiende a otras fuentes, destinos o cambios futuros.

Si el Figma anterior y su descripción discrepan sin prioridad demostrada, falta un token local obligatorio, el nombre de página es ambiguo o se requiere una decisión de producto no demostrada para construir, conserva el punto `CONFLICT`/`UNRESOLVED` y no lo eleves a `DELEGATED_FOR_BUILD`. Dentro de la delegación, el agente puede elegir **entre tokens ya aprobados** por su `description` y rol semántico, registrando la diferencia respecto del token/valor fuente y su impacto visual. Si una propiedad observada no tiene categoría tokenizada en el JSON —por ejemplo, una sombra— puede conservarse como literal de origen, con excepción explícita por propiedad y auditoría posterior; esto no autoriza crear variables. Las inferencias de comportamiento o producto no se vuelven norma por el mero ejercicio de criterio. Después de la construcción y QA, el contrato permanece pendiente de auditoría del usuario hasta una decisión explícita; no cambies su estado a `APPROVED` por haberlo implementado.

La autorización posterior [DEC-SEMANTIC-EXTENSIONS-001](../registry/decisions.md) permite, para esta migración, proponer roles semánticos adicionales cuando los existentes no cubren el uso con scope y significado correctos. Cada extensión debe aliasar una primitiva ya documentada, vivir en un JSON de destino versionado y separado del inventario histórico, tener contrato y QA documental, y anunciarse al usuario antes de escribirla en Figma. Esta autorización no permite inventar nuevos valores primitivos, reutilizar un rol `text` como fondo por coincidencia RGB ni alterar silenciosamente variables compartidas. Los datos de cada token nuevo siguen pendientes de auditoría humana.

La preparación para cada destino se registra aparte como `READY`, `BLOCKED` o `CONFLICT`. La aprobación no garantiza que las dependencias estén implementadas ni que el MCP pueda escribir.

### Cómo registrar una aprobación

1. Presenta candidato, versión, digest de bytes, fuentes y preguntas pendientes.
2. Obtén decisión humana identificable. Si aprueba una propuesta pendiente, intégrala en una revisión explícita y muestra qué se adoptó; no ocultes modificaciones.
3. Publica el contrato en `specs/`, actualiza únicamente los metadatos de aprobación/ubicación que correspondan y conserva el candidato revisado como evidencia.
4. Calcula el digest final y registra aprobación con versión, digest revisado, digest publicado y digests de datos vinculados. Documenta cualquier diferencia administrativa. No insertes el hash del propio archivo dentro de su contenido.
5. Cualquier cambio normativo posterior o cambio de datos dependientes invalida esa aprobación para la nueva revisión y exige revalidar los artefactos afectados.

No marques como aprobado un requisito contradictorio o desconocido. La aprobación de un subconjunto requiere alcance explícito y excluye dependencias no resueltas; no significa que el sistema completo esté aprobado.

## 12. Entregables y pase a construcción

La síntesis produce:

- `drafts/contracts/<entity>.contract.md` o una revisión identificada.
- `drafts/reports/<entity>.synthesis.md` con evidencia y cobertura.
- Registros de fuentes, contrato, revisión y preguntas actualizados según P05.

No exige construir Figma ni generar frontend. Si no se pidió implementar, termina después de la revisión y espera instrucciones.

P04 solo puede comenzar cuando exista contrato aprobado para el alcance o `DELEGATED_FOR_BUILD` bajo la delegación general o una decisión específica de esta sección, datos vinculados verificables, dependencias necesarias resueltas, destino y capacidades de escritura comprobados, y autorización de la tarea. Un inventario organizado no sustituye este gate.

## 13. Casos de control del protocolo

| Caso | Comportamiento esperado |
|---|---|
| Solo JSON de tokens | Contrato de foundations; no inventar Button. |
| Nodo de una instancia | Evidencia parcial; no anunciar toda la familia cubierta. |
| Altura observada sin comportamiento de layout | Proponer reproducción acotada; no regla universal. |
| Estado visual sin lógica de teclado | Documentar visual y pendiente de comportamiento. |
| Token citado en el ejemplo pero ausente en datos | No crearlo ni usarlo como token aprobado. |
| Markdown contradice campo delegado al JSON | Registrar conflicto; no arreglar silenciosamente. |
| `codeSyntax` vacío | Conservar; mapeo web pendiente cuando haga falta. |
| MCP de solo lectura | Permite extracción compatible; no autoriza escritura. |
| No hay fuentes nuevas | No crear contrato real; reportar que está preparado el flujo. |
| Se repite la tarea con mismas fuentes | Reutilizar identidad y comparar; evitar duplicados. |

## 14. Definición de terminado de esta fase

La fase está terminada cuando el candidato y su reporte son accesibles, sus afirmaciones tienen respaldo o limitación explícita, las fuentes no se alteraron, las dudas están registradas, la revisión documental tiene evidencia y se comunica el estado de aprobación sin confundirlo con implementación.

“Contrato redactado” no significa “contrato aprobado”. “Contrato aprobado” no significa “componente construido”.
