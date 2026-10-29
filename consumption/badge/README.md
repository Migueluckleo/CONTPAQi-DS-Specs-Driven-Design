# Consumir Badge

Ejecutar `python3 -B -m blueheart check` y consultar `python3 -B -m blueheart context BADGE-001 --compact --modes '{"component":"Contable"}'`. El [MD 1.1.0](../../norms/components/badge.1.1.0.md) es la autoridad única; el [manifiesto](manifest.json) fija identidad y hashes.

La página [Badge](https://www.figma.com/design/98xEw6sK8FRVNEhopM5SSz/Blue-Heart-DS?node-id=332-234) contiene la familia completa: 18 combinaciones, Label editable y Phosphor opcional por swap. El set compartido anterior fue ampliado conservando IDs; no existe otro Badge temporal. Input sigue consumiendo subtle/small.

La [receta](current-build-plan.json), el [mínimo de 35 firmas](token-minimum.json), el [ledger](current-native-ledger.json) y los mapas de [variables](variable-map.csv) y [bindings](binding-map.csv) son derivados del propietario seleccionado. `python3 -B consumption/badge/materialize-consumption.py` los reproduce sin modificar Figma. No ejecutar el bootstrap histórico de Badge desde Input.

El [mapa de migración](../../evidence/badge-pilot/migration-map.json) conserva doce variables y añade veintitrés, sin primitivos ni semánticos nuevos. El [comprobante](../../evidence/qa/badge-pilot-check.json) separa inspección fuente, QA nativo, integración y límites. La [inspección MD/YAML de solo lectura](../../evidence/badge-pilot/source/component-contract.md) documenta la raíz y no es otra norma editable.

Warning conserva la raíz por elección humana: contraste 2.962:1, insuficiente para AA de texto. Los demás resultados, diferencias de default y límites de implementación se consultan en el contrato y el comprobante. No hay reacciones interactivas porque Badge es informativo. React y revisión independiente siguen sin ejecutarse.
