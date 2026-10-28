# Consumir Tab desde una Skill

La fuente operativa es [TAB-001@2.0.0](../../norms/components/tab.2.0.0.md). El [manifiesto derivado](manifest.json) enlaza contrato, el token set vigente, recetas, identidades reales, propiedades, variables y QA. No contiene otra definición de reglas. La [inspección del origen](../../evidence/tab-pilot/source/component-contract.md) conserva lo observado, incluidas las diferencias autorizadas, sin gobernar el destino.

## Entrada mínima

```sh
python3 -B -m blueheart check
python3 -B -m blueheart context TAB-001 --version 2.0.0 --compact --modes '{"component":"Contable"}'
python3 -B -m blueheart resolve-token tab.color-tab-text-brand-hover --modes '{"component":"Contable"}'
```

Fijar hashes de contrato, el token set vigente y snapshot. El contexto vigente incluye los requisitos seleccionados y 45 tokens directos. Consultar el tamaño real y el presupuesto en la salida; no reutilizar métricas de 1.0.0. No cargar snapshots completos o el proyecto original para construir una pantalla. Ampliar por selector únicamente cuando se necesite evidencia. Un contexto BLOCKED no autoriza una proyección parcial.

El contenedor selecciona el modo de `component`: Contable, Administrativo, Servicios o Personas. Button, Tab, Tabs y Avatar heredan esa misma selección; no hay modos por colección de familia.

## Figma y prototipos

La página [Tabs](https://www.figma.com/design/98xEw6sK8FRVNEhopM5SSz/Blue-Heart-DS?node-id=78-97) contiene el set Tab: `type`, `selected` y `state` seleccionan 24 variantes. Resolverlas mediante los IDs/keys y propiedades del manifiesto, manteniendo instancias vinculadas. Los principales y `__Tab/Count` están fuera del frame de documentación.

La [matriz y ejemplos](https://www.figma.com/design/98xEw6sK8FRVNEhopM5SSz/Blue-Heart-DS?node-id=82-2) muestran estados, temas y overrides reales. Consultar [BH-P07](../../protocols/07-COMPONENT-TOKENS.md) antes de crear variables; las 45 firmas constituyen el mínimo de esta familia. La correspondencia completa está en [variable-map.csv](variable-map.csv): por ejemplo, `tab/color/text/primary-hover`, nombre lógico `--color-tab-text-brand-hover` y WEB `var(--color-tab-text-brand-hover)`. Usar ID o ruta Figma, nunca buscar el nombre CSS como nombre nativo.

El contrato define Label, icono opcional, swap Phosphor y Count opcional. Las claves exactas están en `propertyKeys`. Count se edita en la instancia anidada expuesta mediante `privateCount.propertyKey`; no es una propiedad raíz ni un servicio numérico. El helper pertenece a Tab y no habilita la familia Dot. Las etiquetas largas crecen mediante HUG; el consumidor resuelve espacio y overflow del conjunto.

ImageSquare Outline/Light permanece vinculado a Phosphor del equipo. El swap de prueba a PlusCircle conserva tamaño y token de color. Desarrollo consumirá el export oficial `ImageSquareIcon` con peso `light`; consultar [BH-P06](../../protocols/06-PHOSPHOR-ICONS.md). Los estilos tipográficos y de efecto se resuelven desde el manifiesto; su construcción sigue [BH-P02](../../protocols/02-FIGMA-CONSTRUCTION.md), incluida la preservación del vínculo al estilo después de aplicar variables.

El [tablero nativo](https://www.figma.com/proto/98xEw6sK8FRVNEhopM5SSz/Blue-Heart-DS?node-id=82-400&starting-point-node-id=82%3A400) prueba los cuatro hover y seis disabled. El [ejemplo de selección](https://www.figma.com/proto/98xEw6sK8FRVNEhopM5SSz/Blue-Heart-DS?node-id=82-487&starting-point-node-id=82%3A487) es una composición consumidora separada con tres paneles. Sus hotspots no agregan acciones de selección al principal ni constituyen una nueva familia pública Tabs.

Los componentes son locales a Blue Heart DS. No se publicó una biblioteca ni se presupone importación por key en otro archivo. React, Next.js, teclado y ARIA web requieren un encargo y validación propios; el prototipo Figma no los acredita.

## Verificación y actualización

El [comprobante de la reconciliación anterior](../../evidence/qa/tabs-page-reconciliation-check.json) enlaza controles, comparaciones, contraste y reproducción nativa. La revisión independiente no fue ejecutada y no se presenta como gate satisfecho. Las responsabilidades web del consumidor permanecen en el MD.

Las recetas se derivan de la evidencia inmutable con `python3 -B consumption/tab/materialize-plan.py`; no editar el JSON derivado para cambiar una regla. `tab-materialize.mjs` prepara entradas acotadas para el conector, no consulta ni escribe Figma. Requiere `BLUEHEART_FIGMA_HELPERS` apuntando al directorio `scripts/` de la skill oficial figma-generate-library que se haya cargado; no instala ni supone rutas de otro equipo. Los scripts de construcción y QA están bajo `implementations/figma/tab-*`; no volver a ejecutarlos sobre activos existentes sin reconciliar el manifiesto y ledger. Las operaciones están protegidas por fileKey y rechazan duplicados.

Al cambiar una fuente, revisar primero su propietario, versión y autoridad; regenerar las proyecciones afectadas y aplicar [BH-P04](../../protocols/04-QA-AND-DELIVERY.md). Los envíos y compatibilidad se rigen por [BH-P08](../../protocols/08-GITHUB-RELEASE-DOCUMENTATION.md), sin publicar releases oficiales por esta autorización.

La página completa reúne Overview, Variants & states y ambas familias. Segmented seleccionado usa morados fijos en default/hover en los cuatro temas; focus y disabled permanecen blancos. La limitación de contraste elegida está en REQ-CONTRAST del contrato vigente. Los nombres Figma usan rol/estado; los IDs lógicos y WEB anteriores se conservan por compatibilidad, como en Button. El [mapa de nombres](../../evidence/tabs-page-reconciliation/naming-map.json) es derivado.

La migración ADR-020 deja tres colecciones y se gobierna por [BH-P07 REQ-P07-07](../../protocols/07-COMPONENT-TOKENS.md#req-p07-07). El [mapa actual](../../evidence/collection-consolidation/migration-map.json) conserva identidades lógicas/WEB y enlaza IDs, rutas y modos nuevos; el [QA de la migración](../../evidence/qa/component-collection-check.json) complementa las pruebas históricas enlazadas arriba. Consultar `component` para el tema; las colecciones anteriores ya no existen en el destino.

El plan vigente está en [build-plan.2.0.0.json](build-plan.2.0.0.json). `current-build-plan.json` queda congelado únicamente porque TAB-001@1.1.0 lo fija por hash como evidencia histórica; no consumirlo como receta actual. El preparador requiere `BLUEHEART_FIGMA_SESSION` del encargo actual y consulta el ledger vigente.
