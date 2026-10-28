# Consumo de Tabs

Consultar `python3 -B -m blueheart context TABS-001 --compact --modes '{"component":"Contable","tabs":"Value"}'` y fijar el contrato [TABS-001](../../norms/components/tabs.2.0.0.md), su dependencia exacta Tab y hashes del [manifiesto](manifest.json). Las reglas pertenecen al MD.

El manifiesto identifica tres variantes y un único slot público compartido. Crear una instancia vinculada, editar los hijos del slot y aplicar el tema de `component` al contenedor consumidor. Los cinco tokens propios son invariantes y viven bajo `tab/`; sus aliases se repiten en los cuatro modos compartidos conforme a BH-P07 REQ-P07-07. No crear otra colección ni duplicar variables por tema.

La [página completa](https://www.figma.com/design/98xEw6sK8FRVNEhopM5SSz/Blue-Heart-DS?node-id=78-97) incluye Overview y Variants & states. La [prueba real de slot](../../evidence/tabs-page-reconciliation/slot-qa.json) acredita dos y seis hijos, reordenamiento, contenido y foco desde instancias para los tres tipos. La [verificación vigente](../../evidence/qa/tabs-page-reconciliation-check.json) separa controles ejecutados, fidelidad, contraste aceptado y límites. No hay publicación de biblioteca ni implementación React/ARIA por este encargo.

La migración ADR-020 deja tres colecciones y se gobierna por [BH-P07 REQ-P07-07](../../protocols/07-COMPONENT-TOKENS.md#req-p07-07). El [mapa actual](../../evidence/collection-consolidation/migration-map.json) conserva identidades lógicas/WEB y enlaza IDs, rutas y modos nuevos; el [QA de la migración](../../evidence/qa/component-collection-check.json) complementa las pruebas históricas enlazadas arriba. Consultar `component` para el tema; las colecciones anteriores ya no existen en el destino.
