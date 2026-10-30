# Consumir Breadcrumb item

Ejecutar `python3 -B -m blueheart check` y consultar `python3 -B -m blueheart context BREADCRUMB-ITEM-001 --compact --modes '{"component":"Contable"}'`. El [MD 1.0.0](../../norms/components/breadcrumb-item.1.0.0.md) es la autoridad; el [manifiesto](manifest.json) fija identidad y hashes.

En [Breadcrumbs](https://www.figma.com/design/98xEw6sK8FRVNEhopM5SSz/Blue-Heart-DS?node-id=363-67) hay trece combinaciones reales de `type`, `current` y `state`. `Label` edita texto; Inicio y overflow mantienen contenido fijo. Usar la [composición Breadcrumb](../breadcrumb/README.md) para representar una ruta completa. Las propiedades de variante permiten estados observados; la raíz carece de transiciones conectadas.

La [receta](current-build-plan.json), el [mínimo de veinte firmas](token-minimum.json), el [ledger](current-native-ledger.json) y los mapas de [variables](variable-map.csv) y [bindings](binding-map.csv) derivan del MD y del token set seleccionado. `python3 -B consumption/breadcrumb/materialize-consumption.py` regenera ambos contratos de consumo. No ejecutar los scripts de construcción inicial sobre una familia ya creada.

La [observación fuente MD/YAML](../../evidence/breadcrumb-pilot/source/breadcrumb-item-component-contract.md) no es otra norma editable. [ADR-026 y el comprobante](../../evidence/qa/breadcrumb-pilot-check.json) registran las adaptaciones y sus pruebas. Home sigue el enlace textual equivalente conforme BH-P06; Separator conserva su rol decorativo. Solo current varía por tema. La normalización del binding Semibold a la fuente nativa SemiBold está comprobada sin cambiar Foundations.

El [contraste medido](../../evidence/breadcrumb-pilot/contrast.json) supera 4.5:1 en texto activo sobre blanco, incluidos los cuatro temas de current. Disabled conserva su rol inactivo y no se declara AA. No se extrapola a otras superficies ni se acredita implementación ARIA/teclado web o revisión independiente.
