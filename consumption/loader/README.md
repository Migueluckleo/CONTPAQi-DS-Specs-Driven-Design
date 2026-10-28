# Consumir Loader

Resolver `python3 -B -m blueheart check` y `python3 -B -m blueheart context LOADER-001 --compact --modes '{"component":"Contable"}'`. El [contrato MD](../../norms/components/loader.1.0.0.md) es la autoridad de diseño y función. Fijar su versión/hash y los del token set mediante el [manifiesto](manifest.json); las recetas y CSV son proyecciones, no paletas editables.

Crear una instancia vinculada de la variante `size`/`color` seleccionada en la página [Loader](https://www.figma.com/design/98xEw6sK8FRVNEhopM5SSz/Blue-Heart-DS?node-id=245-19). Consumir el set público; los seis ciclos internos no son una API de producto. El modo de `component` se hereda del contenedor. Solo el arco brand cambia con el tema; los nombres de token expresan su función y sus scopes corresponden a trazo, tamaño o grosor.

La [receta actual](current-build-plan.json), el [mínimo](token-minimum.json), el [mapa de variables](variable-map.csv) y el [mapa de bindings](binding-map.csv) permiten resolver las 15 firmas sin duplicarlas por variante o fase. La extensión de 88 px conserva una cadena completa y no cambia las Foundations anteriores. `python3 -B implementations/figma/loader-plan.py` reproduce la receta desde los propietarios seleccionados; no escribe en Figma.

Button 4.0.0 consume Loader 1.0.0. La [migración](../../evidence/loader-pilot/migration-map.json) conserva los 31 IDs consumidores existentes y el retiro de tres helpers/dos colores exclusivos. No importar ni reconstruir los helpers históricos archivados.

El [QA](../../evidence/qa/loader-pilot-check.json) distingue estructura, cuatro temas, preservación, visual y [reproducción nativa](https://www.figma.com/proto/98xEw6sK8FRVNEhopM5SSz/Blue-Heart-DS?node-id=247-50&starting-point-node-id=247%3A50). Se observaron ciclos con colores estables; el timeout nominal no certifica 30 fps. Los mensajes, temporizadores, reduced motion, ARIA y bloqueo de servicios corresponden al host funcional futuro; no están implementados en React por este encargo. Los componentes siguen locales, sin publicar biblioteca ni release oficial.
