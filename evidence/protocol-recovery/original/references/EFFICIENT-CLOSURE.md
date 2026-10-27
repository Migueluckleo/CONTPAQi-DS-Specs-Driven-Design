# Cierre local eficiente

Decisión: [DEC-EFFICIENT-CLOSURE-001](../registry/DEC-EFFICIENT-CLOSURE-001.md). Conserva los controles de [P05](../protocols/05-SELF-DOCUMENTATION-AND-TRACEABILITY.md) y [P08](../protocols/08-SKILLS-AND-RELEASES.md).

## Operación

Ejecutar scripts/ds close --run ID. Opcionalmente agregar --usage-start RUTA_JSON y --usage-end RUTA_JSON con observaciones reales del panel; --install actualiza las dos copias gestionadas cuando están autorizadas. El comando no hace commit, push, publicación de biblioteca ni llamadas remotas.

El comando produce hitos breves y un comprobante en output/closures/ID.json: documentación/vista, grafo, índice de consumo, catálogo, ZIP de ambas skills, instalación opcional e integridad final. sync ya genera ZIP inmutables: no se ejecuta export otra vez sobre el mismo corte.

NEEDS_SEMANTICS indica un lote preparado: extraer únicamente los chunks indicados según la skill Graphify y reanudar el mismo comando. No fabricar semántica mediante encabezados o sustitución AST. WAITING_FOR_SEMANTICS identifica un lote compartido cuyo propietario ya recibió esa responsabilidad; reutilizar sus chunks y resultado. Si cambian fuentes, usar otro ID. Con el grafo CURRENT no se repite extracción.

BUSY sale con código 75 e identifica al propietario del bloqueo. Esperar por hitos y volver a invocar tras su finalización, sin iniciar otro rebuild. Los comandos de grafo, catálogo y skills usan el mismo lock del sistema operativo, reentrante dentro del proceso y liberado al terminar incluso si el proceso falla. Nunca borrar el archivo de lock: permanece para conservar su inode; su contenido no significa que siga adquirido. Los intentos concurrentes se registran por separado y no pisan el comprobante del propietario.

## Reutilización e invalidación

La sesión comparte selección de fuentes y resultados deterministas por fingerprint del contenido. El parsing YAML se reutiliza por archivo, SHA-256 y parser. Cambios, altas y bajas invalidan la reutilización; antes del resultado final se vuelven a leer los bytes de las fuentes. Los artefactos derivados se verifican por sus comprobantes y hashes propios.

La extracción AST conserva el resultado bruto del cierre anterior únicamente si su hash y versión de herramientas coinciden con el cierre publicado. Reextrae archivos cambiados y consumidores transitivos identificados por evidencia entre archivos, aportando los nodos intactos como contexto de resolución. Las bajas eliminan contribuciones anteriores. El suplemento documental/JSON conserva contribuciones intactas cuando la membresía del corpus permanece igual.

Fallback conservador: primer cierre sin caché verificable, cambio del extractor/configuración, caché alterada o módulos de código nuevos ejecutan AST completo. Altas/bajas del corpus reconstruyen el suplemento de referencias porque pueden resolver referencias antes inexistentes. No se promete que todo lote sea parcial. Estos fallbacks son mecánicos y quedan medidos; no disparan extracción semántica global automática.

El ensamblado final sigue validando el corpus completo: cobertura, fuentes, duplicados, endpoints, manifiesto, JSON/reporte/HTML, procedencia y consultas. Las contribuciones semánticas intactas se reutilizan por hashes conforme P05. La detección de cambios de fuente o baseline concurrente impide declarar CURRENT.

## Contexto y medición

Leer AGENTS y las referencias pertinentes. Las reglas de diseño están en [su referencia](DESIGN-RULES.md), conservadas desde el documento anterior. Herramientas deben devolver resúmenes y rutas de evidencia, sin volcar inventarios o diffs completos. Usar búsquedas acotadas y scripts para operaciones repetibles. No iniciar agentes de mantenimiento permanentes ni repetir sondeos sin novedades.

El comprobante registra segundos por fase, hitos/llamadas internas, reutilizaciones, invocaciones, reintentos por fallo y contención. Las llamadas del agente y sus tokens quedan UNAVAILABLE si el entorno no ofrece una medición; no se equiparan a llamadas internas. El porcentaje de uso es compartido por cuenta y no permite atribuir costo exclusivo a este lote si hay actividad concurrente. Un reinicio de ventana impide comparar porcentajes.

Formato de observación: source, observed_at, limit_id, used_percent, window_minutes, resets_at y concurrent_activity. No guardar cuentas, credenciales ni identificadores personales. Registrar la observación final con scripts/ds metrics --run ID --usage-end RUTA_JSON. Un cambio de proceso requiere comparar medidas reales antes de afirmar un ahorro porcentual.

Este cierre acredita herramientas y fuentes locales. No sustituye QA visual/de interacción del componente ni autoriza publicar. Los HOLD documentales se conservan y se reportan aunque el cierre local sea correcto.
