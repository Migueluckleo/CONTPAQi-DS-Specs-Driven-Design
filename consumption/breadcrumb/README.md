# Consumir Breadcrumb

Ejecutar `python3 -B -m blueheart check` y consultar `python3 -B -m blueheart context BREADCRUMB-001 --compact --modes '{"component":"Contable"}'`. El [MD 1.0.0](../../norms/components/breadcrumb.1.0.0.md) es el propietario de diseño y comportamiento. Su dependencia exacta es [Breadcrumb item](../breadcrumb-item/README.md); no duplicar sus reglas o tokens.

La página [Breadcrumbs de Blue Heart DS](https://www.figma.com/design/98xEw6sK8FRVNEhopM5SSz/Blue-Heart-DS?node-id=363-67) contiene cinco composiciones: `levels=2/3/4/5/collapsed`, con `Show back` booleano. Los eslabones son instancias expuestas del componente hijo: editar sus etiquetas desde la instancia de consumo conserva HUG, tema y anillo. No hay Slots ni un array público nativo.

El [manifiesto](manifest.json), la [receta](current-build-plan.json), el [ledger](current-native-ledger.json), el [mínimo propio de cinco firmas](token-minimum.json) y los mapas de [variables](variable-map.csv) y [bindings](binding-map.csv) son proyecciones trazables. Se reproducen junto con el hijo mediante `python3 -B consumption/breadcrumb/materialize-consumption.py`, sin escribir en Figma. Los veinte tokens del hijo se consumen por composición; ambos contratos usan el grupo `breadcrumb/` dentro de `component`.

La [observación MD/YAML](../../evidence/breadcrumb-pilot/source/breadcrumb-component-contract.md), el [mapa de dependencias y adiciones](../../evidence/breadcrumb-pilot/migration-map.json) y el [QA ejecutado](../../evidence/qa/breadcrumb-pilot-check.json) enlazan las fuentes y el destino. La auditoría de las nueve páginas anteriores no encontró consumidores que sustituir. Los 493 tokens anteriores permanecen intactos; el corte 6.2.0 añade únicamente los 25 de esta familia.

El contrato define navegación jerárquica; el host aporta datos y destinos, menú de ancestros ocultos y adaptación móvil. La raíz no diseña esas pantallas ni contiene reacciones. No se acredita reproducción de navegación o implementación React. Las variantes se pueden editar y sus propiedades fueron ejercitadas nativamente; el QA distingue esto del funcionamiento de una aplicación.
