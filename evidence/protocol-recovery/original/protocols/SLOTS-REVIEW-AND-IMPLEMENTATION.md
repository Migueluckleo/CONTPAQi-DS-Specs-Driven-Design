# P-SLOTS · Revisión e implementación de Slots

**Versión:** 0.1.0 · **Fecha:** 2026-09-29 · **Tipo:** protocolo transversal de P03/P04/P06.

## 1. Propósito, autoridad y alcance

La decisión [DEC-SLOTS-REVIEW-001](../registry/decisions.md) exige revisar y agregar Slots donde la cantidad o composición del contenido deba variar. Se aplica antes de construir o modificar una familia y al revisar componentes existentes afectados. No exige convertir todas las capas en Slots ni ejecutar una auditoría global antes de continuar.

Lee [AGENTS.md](../AGENTS.md), [P03](03-CONTRACT-SYNTHESIS.md), [P04](04-FIGMA-CONSTRUCTION.md), [P05](05-SELF-DOCUMENTATION-AND-TRACEABILITY.md) y [P06](06-QA-AND-VALIDATION.md). Usa [P01](01-ENVIRONMENT-AND-TOOLS.md) para comprobar capacidades necesarias, sin instalar herramientas ni ampliar permisos por este protocolo.

La revisión de aplicabilidad es obligatoria; la implementación solo cuando corresponde. La autorización del protocolo no aprueba contratos futuros, nuevos comportamientos de producto, cambios de paleta ni modificaciones destructivas. Se mantienen las autorizaciones delegadas vigentes de la migración y sus límites.

## 2. Revisión de aplicabilidad · antes del contrato y de P04

SLOT-REV-01: inspeccionar anatomía, contratos, evidencia fuente y necesidades explícitas del usuario. Identificar regiones donde se deba insertar, eliminar, reordenar o sustituir contenido sin cambiar el principal. Listas de opciones, regiones de acciones o contenido compuesto son candidatos, no autorización automática.

Registrar por familia `slot_applicability: REQUIRED | NOT_APPLICABLE | UNRESOLVED`, con evidencia y justificación. Estos valores clasifican aplicabilidad, no sustituyen los estados de contrato, preparación o QA de P05/P06. `NOT_APPLICABLE` exige una razón concreta; no basta que la fuente antigua no tuviera Slots.

| Necesidad demostrada | Criterio de composición |
|---|---|
| Cambiar una cadena | Propiedad de texto; por sí sola no requiere Slot. |
| Mostrar/ocultar una parte fija | Propiedad booleana si cubre la necesidad; no simula cardinalidad abierta. |
| Sustituir un único icono/componente | Instance swap cuando corresponda; no equivale a lista extensible. |
| Cambiar cantidad, orden o composición de hijos | Revisar e implementar Slot conforme a este protocolo. |

SLOT-REV-02: separar cantidad de muestra y cardinalidad del producto. Cinco opciones en un ejemplo NO significan un máximo de cinco. No crear una variante por cantidad ni un conjunto prefijado de booleanas como sustituto silencioso de un Slot requerido. Tampoco prometer cardinalidad ilimitada o rendimiento no probado.

## 3. Definición en el contrato · P03

SLOT-DOC-01: documentar cada Slot dentro de Anatomy, Properties y Composition rules; vincular sus criterios en Acceptance criteria. Mantener las 21 secciones existentes, sin crear una segunda especificación editable.

Para cada región registrar:

- Identificador semántico estable, propósito, evidencia y propietario de la región.
- Componente anfitrión y ubicación conceptual; IDs reales solo después de leerlos.
- Contenido permitido y dependencias locales reutilizables. Distinguir restricciones comprobadas técnicamente de recomendaciones documentales.
- Operaciones admitidas: insertar, quitar, reordenar y/o sustituir, según necesidad demostrada.
- Contenido inicial de demostración, separado de mínimo/máximo de producto. Límites desconocidos se marcan `UNRESOLVED`, no se inventan.
- Responsabilidad del contenedor y de sus hijos sobre ancho, altura, padding, gap, alineación, crecimiento, overflow, clipping y anclaje de overlays.
- Propiedades editables del contenido; herencia de temas, roles semánticos y bindings que se deben conservar.
- Tratamiento vacío, contenido largo y listas extensas: reglas conocidas o decisiones pendientes, sin inventar mensajes ni interacción.
- Mecanismo de implementación propuesto, capacidad pendiente/verificada y matriz de pruebas.

SLOT-DOC-02: para contratos ya publicados, realizar revisión versionada o enmienda directamente en `specs/`, identificando requisitos sustituidos y consumidores afectados. No alterar observaciones históricas ni reescribir el contrato anterior para aparentar que ya contemplaba Slots.

## 4. Comprobación de capacidad · preflight P04

SLOT-CAP-01: comprobar en la documentación y herramientas realmente disponibles si pueden crearse, configurarse, editarse y leerse Slots nativos en el archivo destino. Citar la evidencia y limitaciones; no asumir una API ni que la herramienta disponible soporte todas las funciones de la interfaz.

Preferir Slots nativos cuando estén disponibles y cubran el contrato. Un frame llamado `Slot`, auto layout, instancia expuesta o instance swap NO acredita por sí mismo un Slot nativo ni la capacidad de variar hijos desde una instancia consumidora.

Si falta capacidad de escritura/lectura o una operación requerida no es verificable, registrar `TOOL_LIMITATION` y `BLOCKED` para ese alcance. No marcarlo implementado ni usar un sustituto de cantidad fija. Una alternativa de composición debe identificarse como tal, demostrar las mismas operaciones necesarias y contar con una decisión explícita aplicable antes de reemplazar el requisito de Slot nativo; no ocultarla bajo el mismo nombre.

## 5. Implementación acotada · P04

SLOT-IMP-01: construir desde la revisión del contrato habilitada por aprobación o delegación aplicable. Reutilizar página, componentes y dependencias locales. Conservar los IDs existentes siempre que la capacidad lo permita; documentar cualquier necesidad de migración antes de modificar consumidores.

SLOT-IMP-02: el anfitrión define estructura y reglas del contenedor; el contenido reutiliza componentes del sistema. No desacoplar instancias, aplanar, duplicar principales ni editar globalmente una dependencia para simular flexibilidad.

SLOT-IMP-03: conservar auto layout, comportamiento de ancho/altura y anclajes definidos. En listas variables, comprobar que agregar/quitar contenido actualiza su disposición; no conservar una altura de cinco filas como límite accidental. No añadir scroll, límites de altura ni comportamiento vacío sin respaldo del contrato.

SLOT-IMP-04: conservar tokens y variables semánticas locales por scope, aliases y herencia de los modos. Insertar contenido no autoriza literals nuevos, bindings a primitivas directas ni roles de texto en fondos. Si falta un token, aplicar el procedimiento vigente de extensiones y sincronización JSON/contrato/Figma.

## 6. QA documental y de implementación · P06

Cada control se registra como `PASS`, `FAIL`, `BLOCKED` o `NOT_APPLICABLE` con evidencia. No se aprueba por el nombre de una capa, por una captura estática o por haber agregado hijos al principal mediante script.

| Control | Comprobación requerida |
|---|---|
| SLOT-QA-01 | Aplicabilidad, contenido permitido, operaciones, límites conocidos y origen de decisiones documentados. |
| SLOT-QA-02 | Mecanismo real leído de vuelta; identidad y configuración del Slot, anfitrión y dependencias identificadas. Si no es nativo, la alternativa está declarada y autorizada. |
| SLOT-QA-03 | En una instancia consumidora, agregar y quitar elementos; reordenar/sustituir si el contrato lo exige. No editar el principal para hacer pasar esta prueba; la instancia sigue vinculada. |
| SLOT-QA-04 | Probar una cantidad menor y otra mayor que la muestra, además de la muestra inicial y un elemento. Los números elegidos son datos de prueba, no límites de producto. |
| SLOT-QA-05 | Probar vacío cuando esté permitido. Si su significado no está definido, registrar pendiente de producto y el efecto estructural observado, sin inventar una política de estado vacío. |
| SLOT-QA-06 | Probar contenido largo, ancho reducido y una lista mayor: reflow, tamaños, espaciado, clipping/overflow y anclaje según contrato. Captura después de composición y de cualquier corrección visual. |
| SLOT-QA-07 | Verificar bindings, scopes, aliases y temas aplicables en contenido insertado/reordenado, además del contenedor. Igualdad RGB no sustituye el binding. |
| SLOT-QA-08 | Comprobar preservación de propiedades/overrides pertinentes al cambiar variantes del anfitrión, sin reset inesperado del contenido. Documentar capacidades no soportadas. |
| SLOT-QA-09 | Confirmar que el contenido original, principales ajenos e instancias fuera del alcance no cambiaron; registrar IDs, readback y revisión contractual exacta. |

Si el Slot es obligatorio y una operación esencial no pasa o carece de evidencia, no cerrar ese alcance como `VALIDATED` ni promoverlo por un QA anterior. No certificar comportamiento web, ARIA, teclado o rendimiento desde este QA Figma.

## 7. Trazabilidad, retroactividad y cierre · P05

Registrar en el contrato/QA/estado de implementación: versión de P-SLOTS aplicada, aplicabilidad, regiones revisadas, mecanismo, IDs, capacidades verificadas, casos/cantidades probadas, efectos sobre dependencias, resultados y pendientes. Cada registro referencia al contrato propietario; no duplica valores canónicos.

El QA histórico conserva la validez para la versión y alcance que comprobó. Una nueva exigencia de Slots marca `STALE` el alcance afectado respecto del requisito nuevo, sin borrar resultados anteriores ni afirmar que todas las familias fallaron. Mantener una cola de revisión por excepciones y atenderla al intervenir cada familia.

Primer caso explícito: **Select/Dropdown**. El usuario requiere más o menos opciones, por lo que la aplicabilidad es `REQUIRED`. Las cinco filas del ejemplo son contenido inicial, no capacidad máxima. El set actual con siete instancias expuestas no acredita implementación de Slot. Preparar su enmienda en specs, comprobar capacidad nativa y ejecutar las pruebas antes de darlo por migrado.

Este protocolo no impone cantidades concretas, una API frontend, cambios de colores ni una migración masiva automática. El cierre documental del protocolo no significa que Select o las demás familias ya tengan Slots.
