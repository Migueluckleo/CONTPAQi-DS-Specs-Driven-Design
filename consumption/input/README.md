# Consumir Input

Consultar `python3 -B -m blueheart check` y `python3 -B -m blueheart context INPUT-001 --compact --modes '{"component":"Contable"}'`. El [contrato MD](../../norms/components/input.2.0.0.md) gobierna diseño y comportamiento; el [manifiesto](manifest.json) fija sus hashes y dependencias.

La página [Input](https://www.figma.com/design/98xEw6sK8FRVNEhopM5SSz/Blue-Heart-DS?node-id=281-62) conserva 42 combinaciones. El [ledger](current-native-ledger.json) resuelve los sets Input/empty e Input/filled, sus propiedades nativas y la matriz size/status. La [receta](current-build-plan.json), el [mínimo](token-minimum.json), las [variables](variable-map.csv) y los [bindings](binding-map.csv) son proyecciones reproducibles del contrato y del registro.

Badge subtle/small es una [dependencia compartida](../badge/README.md) con Label editable en la instancia expuesta. Los iconos son instancias de Phosphor Light del equipo. Los colores de tema y las excepciones se resuelven únicamente como especifica REQ-THEME; el foco conserva las diferencias de la raíz por tamaño y valor.

El [QA baseline de geometría y API](../../evidence/qa/input-pilot-check.json) enlaza la comparación de 558 nodos propios, las 150 verificaciones de propiedades y temas y el swap de icono. La ayuda larga adopta altura adaptable y el tracking usa una conversión equivalente documentada en REQ-TYPOGRAPHY. El borde vacío conserva su limitación de contraste. La raíz no tiene reacciones: los estados visuales y la edición de propiedades no certifican captura de datos, validación, ARIA o teclado web. React y la revisión independiente siguen sin ejecutarse.

`python3 -B consumption/input/materialize-consumption.py` reproduce los índices desde sus propietarios y la evidencia nativa; no escribe en Figma. El builder específico exige el destino y una bitácora por operación; no es un adaptador general ni puede ejecutarse para reconstruir automáticamente páginas existentes.

La corrección [ADR-024](../../evidence/icon-color-audit/README.md) enlaza la paridad de iconos con su tipografía, el [QA vigente](../../evidence/qa/icon-color-audit-check.json) y la migración de tokens. El MD seleccionado conserva la regla; los snapshots anteriores son historia.
