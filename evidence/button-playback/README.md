# Button: reproducción interactiva verificada

Prueba ejecutada el 27 de octubre de 2026 en el [reproductor nativo de Blue Heart DS](https://www.figma.com/proto/98xEw6sK8FRVNEhopM5SSz/Blue-Heart-DS?node-id=16-32&starting-point-node-id=16%3A32). Archivo `98xEw6sK8FRVNEhopM5SSz`, página Buttons `11:128`, frame consumidor `16:32`. Se usaron las instancias existentes, sin modificar maestros, variables ni el archivo de origen.

El [comprobante del encargo](../qa/button-playback-check.json) es el propietario del resultado, cobertura y límites. El contrato vigente sigue siendo [BUTTON-001@2.0.0](../../norms/components/button.2.0.0.md), especialmente REQ-PROTOTYPE. Esta evidencia no crea reglas nuevas.

Se ejercitaron las reacciones de los cinco sets públicos en large, medium y small: hover desde default y focus, retorno al salir, y Link mientras se mantiene pulsado y al soltarlo. También se probaron los controles disabled y Danger sin conexiones. Los loaders se observaron en cinco capturas temporales; las conexiones de sus tres ciclos de 24 frames se inspeccionaron por separado. La presencia de conexiones almacenadas no se usó como sustituto de la reproducción.

`runtime-trace.json` identifica entradas, coordenadas del viewport de 865 × 565, capturas y tiempos de las pulsaciones. La matriz completa se probó con la opción Fit width and height para mantener las posiciones estables; las capturas `readable-large-*` muestran después el detalle a mayor escala. Las primeras capturas de calibración del envío de entrada se excluyeron: una imagen tomada antes de mouse-down no acredita pressed. Las imágenes aceptadas de pressed se tomaron después de entregar la entrada y antes de soltar el botón.

`visual-observations.json` es una salida derivada, reproducible en lectura mediante:

```sh
python3 evidence/button-playback/compare-captures.py
```

El script requiere Pillow para leer las capturas, no para ejecutar el núcleo Blue Heart. Compara la misma región del mismo control: el estado activo cambia, el retorno recupera exactamente los píxeles iniciales y los controles sin acción permanecen iguales. Para la animación contrasta varias muestras del loader y un vecino estático. Esta comparación acompaña la revisión visual y el grafo por ID; no demuestra por sí sola corrección semántica, teclado ni ARIA. `artifact-manifest.json` permite comprobar la integridad de los insumos y salidas.

## Diferencias de origen conservadas

Secondary `focus` medium (`15:69`) y small (`15:76`) apuntan a hover large (`15:26`). La reproducción permite observar el cambio de tamaño y su retorno. Las conexiones coinciden con la fuente registrada; se documentan como advertencias, sin corregirlas silenciosamente ni inventar destinos. Una normalización de estos destinos requiere un cambio explícito del componente y de su contrato, con el QA correspondiente.

Los estados sin reacción no se convierten en navegación o servicios ficticios. El foco representado en Figma no demuestra foco por teclado HTML; disabled y loading no certifican bloqueo de servicios ni anuncios accesibles. No se midió una tasa de 30 fps: se verificó el parámetro de timeout almacenado y se observó animación real. Tampoco se certifican WCAG, todos los dispositivos/navegadores o una revisión independiente. El QA previo de los cuatro temas sigue siendo el de sus comprobantes originales; esta prueba interactiva usa el tema Contable del frame existente.
