# Badge completo · ADR-025

El [contrato Badge 1.1.0](../../norms/components/badge.1.1.0.md) es la fuente normativa; [Input 2.0.1](../../norms/components/input.2.0.1.md) fija el pin de consumo. [BLUEHEART-TOKENS 6.1.0](../../norms/tokens/blueheart.6.1.0.json) conserva los 470 tokens anteriores y añade 23 para completar las 35 firmas de Badge. No hay otra norma editable en esta carpeta.

[Solicitud y elección humana](../authorization/badge-full-request.txt), [inspección fuente MD/YAML](source/component-contract.md), [receta de usos](build-plan.json), [mínimo](token-minimum.json), [migración](migration-map.json) y [QA único](../qa/badge-pilot-check.json) hacen trazable el cambio. Los archivos fuente se leyeron sin modificar el proyecto ni el Figma originales.

El único set `282:3` de la página Badge se amplió de 1 a 18 combinaciones. Se conservaron `282:2`, Label `282:4`, su propiedad, doce variables y sus keys. Se añadieron 17 variantes y controles Phosphor opcionales; no se creó otra implementación temporal. Los 113 usos de Input y tres muestras previas conservaron identidad, contenido y geometría. La página actual tiene 39 instancias de demostración vinculadas. Tab continúa consumiendo Dot.

El default local permanece subtle/small por compatibilidad; la raíz parte de neutral/large. Las posiciones de maestros se organizan para que Figma mantenga ese default, sin modificar sus métricas. La raíz real usa iconos 12/16/16 y tipografía 12/20, 12/16 y 14/24; no se copiaron textos ocultos que hablaban de Button ni se dedujeron tallas desde la descripción.

El QA nativo cubre 360 bindings, 288 casos de variantes/temas/iconos con dos etiquetas, 216 swaps remotos y 1,008 pares de color. Desde Input: 168 casos y 504 ediciones de moneda. Las pruebas temporales fueron retiradas; la [captura final](after/badge.png) muestra la página a escala normal sin recortes. Warning conserva 2.962:1 por elección humana y falla el umbral de 4.5:1; no se acredita AA. Revisión independiente y React no ejecutados; Badge no tiene reacciones porque no es interactivo.

La captura [previa](history/qa-reader-visibility.json) del QA conserva un fallo del lector: ocultaba descendientes de instancias y comparaba el icono derecho con el índice izquierdo. Se corrigió la visibilidad del lector y se repitieron todos los casos; no se modificaron expectativas de diseño para aprobarlos. La [historia](history/manifest.json) conserva bytes y hashes del corte anterior fuera de la selección normativa.

Consumo actual: [guía Badge](../../consumption/badge/README.md), [guía Input](../../consumption/input/README.md). Los materializadores leen los MD seleccionados; no restauran el subconjunto desde scripts históricos. La documentación observacional YAML es JSON compatible con YAML 1.2 y no añade un parser al núcleo.
