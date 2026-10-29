# Badge · evidencia Figma de solo lectura

Inspección COMPLETE del set `1234:65377`, página `1234:53606`, archivo `9zs5RMR8LB5wHjW9Bd59BA`. Fecha: 2026-10-29T18:38:38.874516+00:00. Esta proyección y su YAML se derivan del mismo modelo; no son contratos normativos de Blue Heart.

18 combinaciones, 109 nodos inspeccionados, 36 instancias, un componente remoto activo, 35 variables usadas y cero estilos tipográficos nombrados en Label. Pendientes de recorrido: 0.

## API y anatomía observadas

- Show right icon#1234:0: BOOLEAN; default False.
- Show left icon#1234:7: BOOLEAN; default False.
- Label#1241:27: TEXT; default Label.
- Left icon#2817:26: INSTANCE_SWAP; default 2883:23475.
- Right icon#2817:33: INSTANCE_SWAP; default 2883:23475.
- type: VARIANT; default neutral ; opciones error, info, subtle, success, warning, neutral.
- size: VARIANT; default large ; opciones large, medium, small.

Left icon → Label → Right icon. Ambos iconos inicialmente ocultos. Sus controles son swaps, no ejes adicionales.

## Geometría, tipografía y visuales

| Size | Alto | Padding vertical/horizontal | Label | Icono |
|---|---|---|---|---|
| small |20|0/8|12/20|12|
| medium |24|4/8|12/16|16|
| large |32|4/12|14/24|16|

Manrope Regular; tracking 0 PIXELS. HUG horizontal/vertical, gap 4, radio 4. Solo subtle tiene borde interior 1, strokesIncludedInLayout=false; medium/large tienen maxHeight 24/32. Snapshot por tamaño conserva cada fill, stroke, binding y vector.

## Variables y dependencias

35 variables fuente locales resueltas, invariantes en los cuatro temas observados. El inventario YAML conserva IDs, keys, aliases y todos sus used_by. Presentation Outline/Fill remoto es el default activo de 36 instancias. Los 1512 candidatos por control de swap solo se cuentan; no se recorren. La biblioteca Phosphor se identifica mediante búsqueda, sin importar componentes al origen. La versión publicada y el archivo remoto no están expuestos.

## Función, contenido, interacción y accesibilidad

La descripción fuente define una etiqueta no interactiva para estado o metadatos. No se observaron reacciones ni eje de estado. La descripción conserva criterios de uso, tamaños, contenido LATAM e iconos decorativos; se transcribe íntegramente en YAML. Warning se declara por debajo de AA de texto. No se deducen eventos, teclado ni ARIA implementados desde Figma.

## Contradicciones y límites

Las descripciones ocultas de documentación dicen Button y no gobiernan Badge. El listado descriptivo de tallas de icono no coincide con la geometría real: se observan 12/16/16. Los ratios redondeados de la descripción no sustituyen una medición. Los ejemplos usan CheckCircle/WarningCircle/Info Light por swap y no cambian el default Presentation Fill.

## Evidencia y normalización

Modelo canónico: [component-contract.yaml](component-contract.yaml). Datos nativos: [identity](identity.json), [small](small.json), [medium](medium.json), [large](large.json), [variables](variables-and-notes.json), [variables restantes](variables-remaining.json) y [ejemplos](examples.json). La adaptación y la elección humana de conservar warning pertenecen a BADGE-001@1.1.0 y ADR-025.
