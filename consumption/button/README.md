# Consumir Button desde una Skill

La fuente de verdad es [BUTTON-001@4.0.0](../../norms/components/button.4.0.0.md): diseño, función, requisitos y responsabilidades del consumidor. El [manifiesto derivado](manifest.json) enlaza ese contrato y su token set por hash con las identidades reales de Figma; no contiene otra definición editable de reglas. El [snapshot MD de inspección](../../evidence/button-pilot/source/component-contract.md) documenta lo observado, sin autoridad normativa.

## Entrada mínima

Desde la raíz de Blue Heart DS:

```sh
python3 -B -m blueheart check
python3 -B -m blueheart context BUTTON-001 --version 4.0.0 --compact --modes '{"component":"Contable"}'
python3 -B -m blueheart resolve-token button.color-button-primary-bg-hover --modes '{"component":"Contable"}'
```

Fijar los hashes de contrato, token set y snapshot al inicio del trabajo. La consulta compacta conserva los requisitos completos y los tokens propios y transitivos seleccionados; selecciona solamente los aliases necesarios para el tema. Declara el contexto de modos y conserva los overrides explícitos de alias. La procedencia por token se recupera del conjunto enlazado por hash. El límite se mide en bytes UTF-8 del JSON canónico, no en tokens de modelo ni en bytes de la presentación indentada del CLI. Un resultado BLOCKED nunca habilita consumir una salida parcial.

Los temas válidos de la colección `component` son `Contable` (predeterminado), `Administrativo`, `Servicios` y `Personas`. Si se necesita evidencia, usar `context BUTTON-001 --intent evidence` y abrir únicamente el selector afectado. No cargar todos los snapshots, protocolos históricos o el repositorio original para construir una pantalla.

## Prototipo Figma

La página [Buttons](https://www.figma.com/design/98xEw6sK8FRVNEhopM5SSz/Blue-Heart-DS?node-id=11-128) contiene cinco sets: `Button/primary`, `Button/secondary`, `Button/text`, `Button/link` y `Button/danger`. El tipo selecciona el set; `size` y `state` seleccionan una de sus 18 variantes. El manifiesto devuelve IDs/keys, las claves nativas de Label, visibilidad y swaps, y las correspondencias fuente/destino. Crear instancias vinculadas y modificar sus propiedades; no copiar formas ni recrear colores.

Aplicar el modo de la colección de componente sobre el contenedor consumidor. No cambiar los scopes ni los aliases fijos de las colecciones base. Los controles de icono están apagados por defecto; loading usa el loader y no admite iconos laterales en su anatomía. Loading consume instancias públicas de [Loader 1.0.0](../loader/README.md), sin ciclos privados Button. PlusCircle es una instancia vinculada de Phosphor, con correspondencia a `PlusCircleIcon weight="light"` del paquete oficial `@phosphor-icons/react`. Consultar [BH-P06](../../protocols/06-PHOSPHOR-ICONS.md); los demás iconos se resuelven desde esa misma biblioteca por variante y key, sin dibujar copias locales.

La prueba de consumo está en el frame [Contract and consumption](https://www.figma.com/design/98xEw6sK8FRVNEhopM5SSz/Blue-Heart-DS?node-id=16-32): matriz completa y cuatro instancias con etiqueta, iconos y estados modificados. Los componentes son locales a Blue Heart DS; no se publicó una biblioteca. Otro archivo requiere resolver disponibilidad/importación o una distribución autorizada, sin asumir que una key local ya está publicada.

## PoC funcional

La Skill debe interpretar los requisitos del MD y materializar las responsabilidades de la pantalla: confirmación destructiva, causa accesible de disabled, bloqueo de activaciones en loading, anuncio ocupado y composición de acciones. Figma no implementa HTML/ARIA ni servicios.

Hay dos límites explícitos: la variante loading HUG es más ancha que default y medium visual mide 40 px. El consumidor debe reservar ancho durante la operación y resolver el área táctil de 44 px cuando corresponda. No declarar esos requisitos cumplidos por una captura estática. Tampoco deducir contraste AA de la descripción fuente.

Los [protocolos Web](../../protocols/03-WEB-CONSTRUCTION.md) especifican el consumo para React, TypeScript, Tailwind y Next.js. El piloto no crea una biblioteca React; una implementación futura necesita un encargo y su QA de navegador. Esta guía es la interfaz documental para futuras Skills y no instala ni simula una Skill existente.

## Verificación e invalidación

Consultar el [comprobante del piloto](../../evidence/qa/button-pilot-check.json). Si cambia un hash del manifiesto, regenerarlo desde el catálogo y la relectura de Figma; si cambian reglas, revisar primero el MD y su versión seleccionada. `impact` informa consumidores declarados y señala rutas no mapeadas. No editar las proyecciones YAML/JSON para alterar una regla ni afirmar una revisión independiente que no se ejecutó.

La revisión 2.0.0 consolida 125 tokens en 47: un token por tipo, scope y vector de aliases en los cuatro temas. Varios estados pueden compartirlo. Para migrar nombres, consultar [variable-map.csv](../../evidence/button-reduction/variable-map.csv); las 90 variantes y sus propiedades no cambian. No usar la coincidencia en RGB o en un único tema como criterio de fusión.

Antes de construir o modificar cualquier componente, la Skill debe aplicar [BH-P07](../../protocols/07-COMPONENT-TOKENS.md). El campo `token_minimum` de cada documento de componente en `context` confirma el control de sus dependencias declaradas; no sustituye comparar las variables y bindings reales. Button usa el contrato vigente 4.0.0, conserva 45 tokens propios y depende de Loader 1.0.0 con 15 tokens independientes; el registro seleccionado es BLUEHEART-TOKENS@5.0.0.

La nomenclatura Figma observada usa `button/color/bg/primary-default`, `button/font/family` y la estructura completa de [BH-P07](../../protocols/07-COMPONENT-TOKENS.md#req-p07-02). El manifiesto conserva `name` lógico, `figmaName` nativo y `web`; resolver por ID/key y no buscar la variable nativa con el nombre CSS. Los adaptadores y QA reciben `figmaName` o el ID nativo. Las 47 rutas reales están en [observed-names.json](../../evidence/component-naming/observed-names.json).

La [corrección 2.0.1](../../evidence/button-focus-size/README.md) y su [comprobante de QA](../../evidence/qa/button-focus-size-check.json) verifican Secondary focus medium y small en el reproductor nativo. La [prueba anterior 2.0.0](../../evidence/button-playback/README.md) se conserva como evidencia histórica: sus dos advertencias quedan resueltas por esta corrección; no son pendientes vigentes. Ninguna prueba del reproductor acredita HTML/ARIA.

### Recetas reproducibles

Después de `check` y de resolver el contrato vigente, ejecutar:

```sh
python3 -B consumption/button/materialize-plan.py > /tmp/blueheart-button-plan.json
```

La salida combina el baseline histórico con la corrección mínima enlazada por hash en el manifiesto; conserva geometría, bindings, propiedades y tokens. No editar ni consumir directamente el baseline como receta vigente. Para `button-builder.js`, suministrar `DATA.contractVersion` desde el manifiesto y `DATA.variants` filtradas por familia desde esta salida; el adaptador rechaza Secondary focus con destino de otro tamaño antes de crear nodos. `button-check.js` recibe esas mismas variantes para calcular lo esperado. `button-review.js` recibe `DATA.contractPath` desde el mismo manifiesto. Estas proyecciones no autorizan reconstruir o duplicar componentes ya existentes.

La migración ADR-020 deja tres colecciones y se gobierna por [BH-P07 REQ-P07-07](../../protocols/07-COMPONENT-TOKENS.md#req-p07-07). El [mapa actual](../../evidence/collection-consolidation/migration-map.json) conserva identidades lógicas/WEB y enlaza IDs, rutas y modos nuevos; el [QA de la migración](../../evidence/qa/component-collection-check.json) complementa las pruebas históricas enlazadas arriba. Consultar `component` para el tema; las colecciones anteriores ya no existen en el destino.

### Dependencia Loader vigente

[El mapa ADR-022](../../evidence/loader-pilot/migration-map.json) y [su QA](../../evidence/qa/loader-pilot-check.json) sustituyen los tres ciclos anteriores, retiran los dos colores temporales y corrigen el riel/remate para igualar la fuente real. Los 90 IDs Button, sus dimensiones, contenido y transiciones quedan preservados. La proyección actual devuelve `plan.loader` y `recipe.loader.variantId/axes`; suministrar `DATA.loader` al constructor. No usar `spinnerFrames`, `spinnerFirst` ni los colores de loader del baseline histórico. Las 47 rutas citadas arriba describen el corte ADR-010; el manifiesto actual contiene 45. Los contratos anteriores exactos se consultan en [historia](../../evidence/loader-pilot/history/manifest.json).
