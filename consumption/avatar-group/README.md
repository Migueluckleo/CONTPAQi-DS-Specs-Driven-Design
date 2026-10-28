# Avatar group · consumo

Fuente normativa única: [AVATAR-GROUP-001@2.0.0](../../norms/components/avatar-group.2.0.0.md), dependiente de [Avatar](../avatar/README.md). Consultar `python3 -B -m blueheart context AVATAR-GROUP-001 --compact`; la [selección derivada](manifest.json) fija versiones, hashes y destino.

- [Variables propias](variable-map.csv): siete firmas únicas, todas invariantes.
- [Bindings propios reales](binding-map.csv); los bindings heredados pertenecen al mapa de Avatar.
- [Receta seleccionada](../avatar/current-build-plan.json), [mínimo](../avatar/token-minimum.json) y [QA del encargo](../../evidence/qa/avatar-pilot-check.json).

El contrato gobierna el slot, el traslape, el contador y la coordinación de tamaños. La edición del slot no calcula automáticamente el contador ni normaliza el tamaño de un hijo insertado. La fila de QA muestra una reordenación técnica deliberada; los ejemplos de uso mantienen el contador al final.

La decisión del responsable conserva el anillo observado de 1 px. El alterno warning conserva el binding fuente y presenta **3.32:1** de contraste con iniciales blancas, inferior a 4.5:1 para texto normal. La [medición](../../evidence/avatar-pilot/contrast.json) conserva el método y los demás resultados; este caso no se declara AA.

Los tres espaciados negativos requeridos se incorporaron en BLUEHEART-TOKENS 2.1.0. El [mapa de Foundations](../../evidence/figma-application/application-map.json) mantiene las 251 correspondencias previas y registra seis identidades nuevas mediante ADR-019; no duplica colores semánticos.

La migración ADR-020 deja tres colecciones y se gobierna por [BH-P07 REQ-P07-07](../../protocols/07-COMPONENT-TOKENS.md#req-p07-07). El [mapa actual](../../evidence/collection-consolidation/migration-map.json) conserva identidades lógicas/WEB y enlaza IDs, rutas y modos nuevos; el [QA de la migración](../../evidence/qa/component-collection-check.json) complementa las pruebas históricas enlazadas arriba. Consultar `component` para el tema; las colecciones anteriores ya no existen en el destino.
