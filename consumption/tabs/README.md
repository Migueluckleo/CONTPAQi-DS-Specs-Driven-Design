# Consumo de Tabs

Consultar `python3 -B -m blueheart context TABS-001 --compact --modes '{"tab":"Contable","tabs":"Value"}'` y fijar el contrato [TABS-001](../../norms/components/tabs.1.0.0.md), su dependencia exacta Tab y hashes del [manifiesto](manifest.json). Las reglas pertenecen al MD.

El manifiesto identifica tres variantes y un único slot público compartido. Crear una instancia vinculada, editar los hijos del slot y aplicar el tema de `tab` al contenedor consumidor. La colección `tabs` tiene un solo modo Value porque sus cinco valores son invariantes; los hijos heredan el tema de `tab`. No crear cuatro copias idénticas ni duplicar tokens de Tab.

La [página completa](https://www.figma.com/design/98xEw6sK8FRVNEhopM5SSz/Blue-Heart-DS?node-id=78-97) incluye Overview y Variants & states. La [prueba real de slot](../../evidence/tabs-page-reconciliation/slot-qa.json) acredita dos y seis hijos, reordenamiento, contenido y foco desde instancias para los tres tipos. La [verificación vigente](../../evidence/qa/tabs-page-reconciliation-check.json) separa controles ejecutados, fidelidad, contraste aceptado y límites. No hay publicación de biblioteca ni implementación React/ARIA por este encargo.
