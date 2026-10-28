# Avatar · consumo

Fuente normativa única: [AVATAR-001@2.0.0](../../norms/components/avatar.2.0.0.md). Resolver la selección y hash desde [manifest.json](manifest.json) y `python3 -B -m blueheart context AVATAR-001 --compact`. No reconstruir reglas desde las capturas ni desde nombres de variantes.

[Abrir Avatars en Blue Heart DS](https://www.figma.com/design/98xEw6sK8FRVNEhopM5SSz/Blue-Heart-DS?node-id=145-42). La página contiene Overview, Variants & states, una matriz de referencia y el panel de uso/QA. Los principales reutilizables quedan fuera de los marcos de revisión.

Derivados verificables:

- [Plan actual](current-build-plan.json): recetas y clasificación temática por token.
- [Mapa de variables](variable-map.csv): identidad lógica, ruta Figma, WEB, ID/key y scope.
- [Bindings reales](binding-map.csv): incluye consumidores heredados en Avatar group.
- [Mínimo medido](token-minimum.json): 25 firmas propias; no es el límite de otras familias.
- [Comprobante del encargo](../../evidence/qa/avatar-pilot-check.json) y [medición de contraste](../../evidence/avatar-pilot/contrast.json).

La iconografía conserva instancias de la biblioteca Phosphor del equipo. La fuente oficial de desarrollo expone [UserIcon](https://github.com/phosphor-icons/react/blob/master/src/csr/User.tsx) y [BuildingsIcon](https://github.com/phosphor-icons/react/blob/master/src/csr/Buildings.tsx), ambos con `weight="light"`; el [mapa leído en Figma](../../evidence/avatar-pilot/source/phosphor.json) identifica las keys. No se instaló ni implementó React; no se certifica igualdad de versiones entre Figma y una futura dependencia npm.

Para reproducir la proyección local: `python3 -B implementations/figma/avatar-plan.py`. Esto regenera datos derivados y no escribe Figma. Los scripts Avatar bajo implementations/figma son operaciones específicas del encargo, no un adaptador general. Antes de reejecutar una escritura, leer el ledger vigente enlazado en el manifiesto y el protocolo BH-P02; no duplicar entidades existentes.

El contrato distingue los cuatro temas reales, la presencia fija y las responsabilidades de carga/fallback, nombre accesible y foco del consumidor. Los siete modos de color anunciados en una descripción antigua no existen en la raíz; esa descripción permanece únicamente como evidencia histórica.

La migración ADR-020 deja tres colecciones y se gobierna por [BH-P07 REQ-P07-07](../../protocols/07-COMPONENT-TOKENS.md#req-p07-07). El [mapa actual](../../evidence/collection-consolidation/migration-map.json) conserva identidades lógicas/WEB y enlaza IDs, rutas y modos nuevos; el [QA de la migración](../../evidence/qa/component-collection-check.json) complementa las pruebas históricas enlazadas arriba. Consultar `component` para el tema; las colecciones anteriores ya no existen en el destino.
