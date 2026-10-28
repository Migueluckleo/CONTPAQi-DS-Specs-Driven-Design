# ADR-020 · Tres colecciones

Resultado en Blue Heart DS: `primitive` (148), `semantic` (109) y `component` (129). Component contiene un solo grupo `button` (47), `avatar` (25 Avatar + 7 Avatar group) y `tab` (45 Tab + 5 Tabs). Las composiciones conservan contratos independientes; la agrupación no fusiona responsabilidades ni añade variables.

La regla operativa única es [BH-P07 REQ-P07-07](../../protocols/07-COMPONENT-TOKENS.md#req-p07-07). [La petición](../authorization/component-collection-request.txt) y ADR-020 sustentan el cambio; [el comprobante](../qa/component-collection-check.json) enlaza las verificaciones. El origen local y Figma siguen en solo lectura.

## Migración y compatibilidad

La API nativa no permite cambiar variableCollectionId. Se crearon 82 reemplazos dentro de la colección component existente, se migraron estilos, rangos de texto, paints, dimensiones e instancias y se retiraron cuatro colecciones al llegar a cero referencias. Las 257 variables de Foundations y 47 de Button conservan exactamente sus metadatos, IDs/keys y valores. Los componentes, variantes, slots, propiedades y sus identidades se mantienen.

[Mapa completo](migration-map.json): identidad lógica, nombre WEB, ruta, colección, ID/key anteriores y actuales. Los grupos Avatar group y Tabs usan calificadores group- dentro de avatar/tab. El contexto portable `button`, `tab` o `avatar` se sustituye por `component`; no se emparejan modos entre colecciones. Todos heredan los cuatro temas existentes y los roles fijos conservan su alias en los cuatro. Este cambio incompatible de consumo se versiona: BLUEHEART-TOKENS 3.0.0, Button 3.0.0 y Tab/Tabs/Avatar/Avatar group 2.0.0; no es una release oficial.

Las fuentes normativas anteriores quedan congeladas en [history](history/); las versiones anteriores de contratos permanecen en el catálogo como historia. El antiguo consumption/tab/current-build-plan.json sigue congelado por su referencia SHA en TAB-001@1.1.0; la receta actual es consumption/tab/build-plan.2.0.0.json y se selecciona desde el manifiesto. Los constructores actuales reutilizan component y rechazan rutas duplicadas. Los ledgers vigentes se enlazan en los manifiestos; no ejecutar un bootstrap histórico para regenerar activos existentes.

## Evidencia y límites

- [Antes](before/) y [después](after/): cinco páginas, 4,500 nodos. Las huellas de bindings normalizadas y los valores resueltos coinciden, con las leyendas documentales explícitamente identificadas.
- [Variables](after/variables.json): 906 controles, incluidos 129 registros y 516 aliases de modo, scopes de Foundations, colecciones y grupos. Cero fallos.
- [Estilos](styles.json), [gate global](reference-gate.json) y [retiro](retired.json). El inventario completo de páginas precede al retiro.
- [Comparación de PNG](visual/comparison.json): Overview de Tabs conserva exactamente todos sus píxeles respecto al corte anterior. [Tab](visual/tabs-spec.png) y [Avatar](visual/avatar-qa.png) fueron revisados después de actualizar las leyendas de contrato. Dos huellas de metadatos documentales difieren; no se afirma identidad binaria completa de esos frames. Se conserva apariencia y resolución, y no se convierten esas diferencias en nuevas reglas de diseño.
- [Contextos](context-check.json): los trece contratos vigentes pasan con la proyección compacta y el presupuesto existente. La combinación de modos baja de 64 a 4; no equivale a una promesa de ahorro de tokens o latencia.
- [Pruebas](tests.txt): 94 pruebas locales del núcleo, negativas, trazabilidad y Git/PDF pasan. El CI del envío ejecuta su propio corte y deja su recibo y PDF.

Los dos iconos con INSTANCE_SWAP requerían regenerar el intercambio desde su componente por defecto para actualizar los overrides de tamaño. Se verificó el binding final, el vínculo Phosphor y la conservación de apariencia. Los archivos created/migrated/icon-* describen pasos intermedios; el estado entregado es after y el comprobante de QA, no un intento aislado.

Continúan los límites de contraste aceptados (Tab 4.39:1/2.26:1 y Avatar warning 3.32:1), sin afirmación AA. No se ejecutó React, ARIA, teclado ni nueva reproducción de prototipos: se preservaron las reacciones registradas y los principales. No se publicaron biblioteca ni releases oficiales.
