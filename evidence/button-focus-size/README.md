# Secondary focus: corrección Button 2.0.1

ADR-014 autoriza corregir dos destinos en Blue Heart DS. La regla operativa reside únicamente en [BUTTON-001@2.0.1, REQ-PROTOTYPE](../../norms/components/button.2.0.1.md#req-prototype); este directorio registra su ejecución y no crea otra norma.

| Transición nativa ON_HOVER / CHANGE_TO | Antes | Después | Altura lógica |
| --- | --- | --- | --- |
| Secondary focus medium `15:69` | hover large `15:26` | hover medium `15:32` | 40 px |
| Secondary focus small `15:76` | hover large `15:26` | hover small `15:38` | 32 px |

Resultado: **PASS del cambio solicitado**. [Comprobante](../qa/button-focus-size-check.json), [antes](before.json), [aplicación y preservación](patch.json), [relectura](after.json) y [traza nativa](runtime-trace.json).

En el reproductor nativo se activó cada instancia focus, se capturó hover y se salió para comprobar el retorno. Las alturas visibles coinciden con el hover estático del mismo tamaño: 31 px rasterizados para medium y 25 px para small a escala 865/1112. El [comparador](compare-captures.py) admite 1 px de rasterización subpíxel; la geometría lógica exacta se verifica por API. La diferencia del recorte focus antes/después es 0 en ambos casos. Los loaders fuera del recorte siguen animándose.

| Caso | Focus inicial | Hover activo | Focus restablecido |
| --- | --- | --- | --- |
| Medium | [captura](medium-focus-before.jpg) | [captura](medium-hover-active.jpg) | [captura](medium-focus-returned.jpg) |
| Small | [captura](small-focus-before.jpg) | [captura](small-hover-active.jpg) | [captura](small-focus-returned.jpg) |

La comparación dentro de la misma operación preserva la geometría, los bindings, la API de las 90 variantes, las reacciones de las otras 88 variantes, los helpers y las 298 variables: 251 foundations y 47 tokens Button. Solo cambian las dos aristas y las referencias documentales de versión (cinco descripciones y una anotación). No se crean nodos ni variables.

La [proyección vigente](../../consumption/button/README.md#recetas-reproducibles) aplica dos cambios por hash sobre el baseline histórico inmutable. [Verificación de reconstrucción](reconstruction-check.json): solo dos destinos cambian; tokens y todas las demás recetas quedan iguales. El [preflight del adaptador](builder-preflight-check.json) rechaza las recetas históricas incorrectas antes de importar o crear nodos. Ese control usa stubs de lectura; la prueba visual y de interacción procede del reproductor real.

Las dos advertencias del [QA 2.0.0](../qa/button-playback-check.json) quedan resueltas. Se conserva esa evidencia histórica sin reescribir sus resultados. El proyecto original conserva los 13 hashes de referencia comprobados; no se escribe allí ni en el Figma origen.

Alcance: QA dirigida por el agente implementador, sin afirmar revisión independiente, implementación web, HTML/ARIA o certificación WCAG. Los resultados frescos del núcleo y de su suite obligatoria se registran automáticamente en las notas de envío BH-P08; no sustituyen estas pruebas de Figma.
