# Consumir Badge

Resolver `python3 -B -m blueheart context BADGE-001 --compact --modes '{"component":"Contable"}'`. El [MD](../../norms/components/badge.1.0.0.md) es la autoridad única; el [manifiesto](manifest.json) fija identidad y hashes.

La página [Badge](https://www.figma.com/design/98xEw6sK8FRVNEhopM5SSz/Blue-Heart-DS?node-id=281-63) contiene exclusivamente subtle/small con Label editable. El alcance fue elegido expresamente para la dependencia de Input; las otras 17 combinaciones de la biblioteca raíz y sus iconos están fuera de esta versión.

La [receta](current-build-plan.json), el [mínimo de 12 firmas](token-minimum.json), el [ledger](current-native-ledger.json) y los mapas de [variables](variable-map.csv) y [bindings](binding-map.csv) permiten reutilizar la misma instancia. Los cuatro modos conservan aliases invariantes. El [QA compartido con Input](../../evidence/qa/input-pilot-check.json) documenta MXN, USD y etiqueta larga, con tamaños derivados del texto, sin desacoplar la dependencia.
