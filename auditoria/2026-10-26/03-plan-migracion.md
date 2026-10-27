# Blue Heart DS · Plan de migración

Fecha: 26 de octubre de 2026 · Estado: plan propuesto. **No ejecutado.**

El original se conserva como referencia de solo lectura durante todas las fases. Este plan no autoriza cambios, publicación, instalaciones ni escrituras Figma. La presente entrega termina en análisis y documentación.

## 1. Estrategia

Migración por capacidades y familias, con comparación entre resultados del original y Blue Heart. Evitar tanto la copia íntegra como la reescritura simultánea. Se conserva la evidencia y se reemplazan mecanismos cuando exista equivalencia demostrada.

El nuevo sistema puede referenciar evidencia del original mientras se estabiliza el modelo; una release futura debe incluir o localizar de forma durable todo lo que requiera para reproducirse. Las rutas absolutas de esta auditoría son referencias locales de análisis, no el diseño final de distribución.

## 2. Fases, entregables y gates

| Fase | Trabajo propuesto | Entregable | Criterio de salida | Responsable lógico |
|---|---|---|---|---|
| 0. Acordar alcance | Resolver qué debe conservar Blue Heart: marca, consumidores, destinos, fidelidad y publicación. Delimitar cambios permitidos. | Decisiones de arquitectura y alcance inicial | No quedan ambigüedades que cambien el modelo o el piloto. | Coordinación + usuario en decisiones de producto |
| 1. Fijar referencia | Identificar un snapshot de contenido verificable del original y sus estados; conservar procedencia sin limpiar su Git. | Manifiesto de importación y mapa de activos | Cada activo seleccionado tiene origen/hash; ningún dato se presenta como proveniente solo de HEAD cuando no lo es. | Análisis de dominio |
| 2. Modelar contrato y resolver vigencia | Definir perfiles mínimos, relaciones tipadas, reglas de sustitución, estados y evidencia. Normalizar un piloto. | Esquema propuesto, contratos piloto y vista efectiva | Todos los requisitos vigentes del piloto están conservados; conflictos y desconocidos visibles; decisión revisada. | Análisis + verificación |
| 3. Probar núcleo y contexto | Implementar, una vez autorizado, validación determinista, índice, consulta e impacto sin Graphify obligatorio. | Núcleo mínimo y benchmark comparable | Cobertura y resultados al menos equivalentes en el piloto; contexto menor sin omisiones críticas. | Construcción de herramientas + verificación |
| 4. Separar destinos | Establecer paquete web y adaptador Figma; mantener equivalencias de IDs y tokens. | Una familia piloto por destino autorizado, con evidencia | Readback, comportamiento, preservación y recuperación probados; consumo web sin runtimes documentales. | Construcción por destino + verificación |
| 5. Distribuir y consumir | Separar motor de skill y corte DS; definir perfiles de paquetes y handoff. | Release candidata, skills y manifiesto de handoff | Instalación/consumo desde entorno limpio; identidad común, offline fijado y canal actual distinguidos; actualización/reversión probadas. | Construcción de distribución |
| 6. Migrar por lotes | Importar familias según dependencias, adaptar lo necesario y comparar. | Matriz de paridad por lote | No faltan requisitos, tokens, assets, API o evidencia requerida; excepciones documentadas. | Coordinación + responsables por familia |
| 7. Cambiar consumidores | Habilitar Blue Heart para usuarios seleccionados; conservar rollback. | Release aceptada y guía de transición | Pilotos reales completados; compatibilidad y rollback comprobados; pendientes no críticos aceptados explícitamente. | Coordinación + consumidores |
| 8. Optimizar con medición | Evaluar Graphify, empaquetado parcial, oficina visual y compilador offline alternativo. | Experimentos y decisiones de conservación/descarte | Beneficio medido incluyendo mantenimiento, coordinación y retrabajo. | Optimización + verificación |

No se asignan fechas ficticias. El esfuerzo real depende de accesos Figma, disponibilidad de consumidores, alcance visual y conflictos al consolidar contratos. El primer punto de estimación fiable es la salida de la fase 2.

## 3. Piloto recomendado

El piloto debe cubrir los problemas encontrados, no solo el componente más fácil de copiar.

| Caso | Qué pone a prueba | Qué debe preservarse |
|---|---|---|
| Foundations y subconjunto de tokens usado | Autoridad de datos, aliases, modos, unidades y equivalencias | Bytes de referencia, descripciones y significado; no inventar primitivas. |
| Button | Base heredada, seis enmiendas, propiedades, carga, danger y foco | Precedencia por requisito y diferencias Figma/web. |
| Select y sus dependencias necesarias | Composición, cantidades de muestra frente a Slots y consulta transitiva | Inserción/retirada/reordenación, semántica de teclado web y límites del contrato Figma. |
| Header como caso documental | Metadatos históricos en prosa | Identidad, autoridad, composición y trazabilidad tras normalización. |
| Excepción tipográfica de un consumidor | Herencia, escala y vínculo nativo frente a receta CSS | Separación entre evidencia del principal, instancia y web; no simplificar a igualdad de métricas. |
| Una pantalla pequeña con handoff | Consumo real y transferencia PO→Figma | Corte DS, instancias, props, estados, contenido, medidas y evidencia. |

Header puede probarse primero solo en el resolvedor. No es necesario construir simultáneamente todas sus dependencias Figma para validar la normalización de metadatos. La pantalla piloto y su destino deberán acordarse antes de esa fase.

## 4. Qué migrar y cómo

| Activo | Tratamiento | Condición |
|---|---|---|
| Inventario fuente de tokens | Conservar como evidencia y mapear al propietario futuro | Sin cambios silenciosos de nombres, unidades, aliases o valores. |
| Contratos y enmiendas | Consolidar norma vigente por familia, conservar historial | Matriz requisito anterior→nuevo requisito→prueba; ninguna equivalencia deducida solo por nombre. |
| Estados APPROVED/DELEGATED | Conservar significado y referencia histórica | No convertir delegación antigua en aprobación actual ni importar permisos de publicación. |
| Snapshots y QA | Referenciar o importar selectivamente por hash | El QA solo cubre su corte; discrepancias actuales abren una nueva verificación. |
| Código React | Reutilizar tras aislar API, estilos y assets | Tests y ejemplos confirman compatibilidad; cambios incompatibles se versionan. |
| Scripts Figma específicos | Conservar como evidencia/recetas de operación | Extraer capacidades reutilizables; no ejecutar los scripts con IDs del original en un destino nuevo. |
| Artwork y fuentes | Importar bytes con manifiesto de procedencia | Verificar derecho/alcance de distribución cuando se decida publicar, sin redibujar por conveniencia. |
| Skills | Reescribir entradas alrededor de la API de contexto común | Conservar tareas y entregas comprobadas; eliminar reglas duplicadas y cargadores mantenidos por separado. |
| Grafo histórico | Referencia de descubrimiento | Reindexar solo el corpus explícito del nuevo proyecto si la evaluación justifica Graphify. |
| `output/`, caches y paquetes históricos | No copiar masivamente | Clasificar evidencia única, entregables y derivados antes de seleccionar. |
| Oficina y eventos | Mantener como antecedente | No activar agentes por importar perfiles; no convertir IDs de ejecución antiguos en agentes vivos. |

La migración de marca y la reorganización del producto son decisiones distintas de la migración técnica. “Blue Heart DS” no basta para asumir que se deben renombrar tokens CONTPAQi, quitar personajes o cambiar temas.

## 5. Matriz de paridad y reglas de rechazo

Por familia se documentan: identidad anterior/nueva, versión normativa efectiva, requisitos conservados, tokens y assets, API web, binding Figma por destino, pruebas, excepciones y estado de migración. Puede referenciar evidencia común para no duplicarla.

Se rechaza el corte afectado cuando:

- Se pierde un MUST, prohibición, estado, variante o excepción vigente.
- Una enmienda parcial elimina requisitos no sustituidos.
- Una dependencia necesaria queda fuera del paquete sin indicarlo.
- Se deduce equivalencia de tokens solo por RGB o métrica.
- Una operación Figma duplica objetos al reintentar o afecta recursos fuera de alcance.
- Una prueba pasa usando expectativas generadas exclusivamente del mismo código que pretende validar.
- El release no puede relacionarse con sus fuentes exactas o no conserva la versión previa para rollback.

Un hallazgo crítico en una familia bloquea esa familia y los consumidores afectados; no convierte en fallidas las familias independientes. Un informe histórico con PASS no cubre automáticamente un nuevo destino Figma.

## 6. Medición de optimizaciones

Antes de comparar, fijar mismos contratos, tareas, dificultad y resultados esperados. Separar caché fría y caliente. Registrar tanto consultas como construcción de índices, generación, coordinación y reintentos.

| Indicador | Línea base disponible | Medición futura |
|---|---|---|
| Requisitos recuperados y omitidos | Casos del piloto con verificación contra fuentes | 100 % de requisitos obligatorios del alcance; cero omisiones críticas. |
| Contexto por consulta | Button: 810,499 bytes para componente en runtime retenido | Percentiles sobre tareas/familias representativas; objetivo piloto de reducción ≥50 % en consultas comunes, sujeto a cobertura. |
| Consulta de tokens | Reducción de bytes 75.20 % en el ensayo | Preservar acceso dirigido y probar aliases/dependencias fuera del caso Button. |
| Cierre sin cambios | Un recibo histórico de 96.683 s; no benchmark controlado | Medir repetidamente en mismo entorno; validar primero coste y alcance equivalentes. |
| Latencia de cambio local | Recibos heterogéneos de 69.01–260.375 s en cierres exitosos inspeccionados | Comparar por tipo de cambio y entradas invalidadas; no usar el rango como promedio. |
| Distribución | Bundle actual de 9,495,932 bytes | Bytes descargados, reutilizados, extraídos y copiados por tarea. |
| Contexto de arranque de oficina | 28,574 bytes de tres fuentes solicitadas | Coste real del encargo, incluido routing y recuperación de continuidad. |
| Consumo del modelo | No disponible por tarea en recibos examinados | Tokens/llamadas del runtime si existen; de lo contrario UNAVAILABLE. |
| Calidad del resultado | QA vigente por componente y caso | Defectos, correcciones y tiempo total; menor contexto no justifica peor resultado. |

Los objetivos son criterios propuestos para decidir, no resultados obtenidos ni compromisos aprobados. Si un índice directo pierde descubrimiento útil, conservar Graphify en ese tipo de tarea en lugar de forzar una sustitución total.

## 7. Riesgos de migración y recuperación

| Riesgo | Mitigación | Recuperación |
|---|---|---|
| Pérdida de semántica al consolidar | Matriz de requisitos, revisión por alcance y casos negativos | Rechazar la consolidación y continuar referenciando la versión original. |
| Confusión de IDs Figma | Namespace por archivo y mapa leído del destino | Detener escritura, leer estado y aplicar recuperación acotada verificada. |
| Reuso indebido de QA histórico | Comprobantes por hash/destino/entorno relevante | Invalidar únicamente alcance afectado y volver a probar. |
| Cambio de API web o rutas de assets | Pruebas de consumidores y compatibilidad explícita | Pin al paquete anterior y adaptador temporal si se justifica. |
| Versión publicada distinta de fuentes auditadas | Manifiesto del corte, CI y cambio de puntero al final | Volver al puntero anterior; no sobrescribir releases. |
| Dependencia desconocida fuera del corpus | Detección + revisión de relaciones no resueltas | Bloquear esa migración hasta resolver; no completar por inferencia. |
| Coste mayor por paquetes demasiado fragmentados | Benchmark de red/I/O y caché | Mantener bundle consolidado mientras no haya ventaja demostrada. |
| Rehacer una oficina antes de resolver el núcleo | Posponer UI y procesos permanentes | Seguir con herramientas mínimas y comprobantes legibles. |

La fuente original permanece intacta como referencia; la recuperación operativa debe usar releases anteriores de Blue Heart, sin depender de sobrescribir el original.

## 8. Decisiones necesarias antes de implementar

Estas decisiones no bloquean la auditoría entregada, pero sí cambian materialmente la implementación futura:

1. ¿Blue Heart conservará íntegramente identidad visual, temas y API CONTPAQi, o habrá cambios de producto/marca explícitos?
2. ¿El primer consumidor será mantenimiento del DS, prototipos PO, pantallas Figma o aplicaciones web? Recomendación: validar el núcleo con un recorrido pequeño PO→Figma, sin hacer depender todo el sistema de ese recorrido.
3. ¿Qué archivo/biblioteca Figma nuevo se usará y qué capacidades tiene el acceso? No asumir el archivo histórico como destino.
4. ¿Qué se publicará, para quién y en qué canal? Separar contenido, biblioteca, motores y evidencia interna.
5. ¿Qué compatibilidad deben conservar los consumidores actuales y durante cuánto tiempo?

La autorización actual cubre diagnóstico, propuesta y plan. **No se ha iniciado ninguna fase de programación o migración.**
