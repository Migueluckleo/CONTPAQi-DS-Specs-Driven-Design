# Tab: procedencia y QA del piloto

El propietario operativo es [TAB-001@1.0.0](../../norms/components/tab.1.0.0.md). La solicitud y sus dos decisiones están en [la evidencia de autorización](../authorization/tab-pilot-request.txt), adoptadas por ADR-015. El origen y el proyecto anterior permanecen en solo lectura.

El [comprobante único](../qa/tab-pilot-check.json) reúne resultados y límites; este índice no reproduce su matriz ni define reglas. [consumption/tab/](../../consumption/tab/README.md) es la entrada de consumo para Skills.

- `source/`: inventario completo de 151 nodos, 97 variables con cierre de aliases, dependencias, Phosphor, captura y contrato observacional MD/YAML. Las capturas por lotes conservan el transporte original; `nodes.json` y `variables.json` son sus consolidaciones verificables. Ninguna es norma del destino.
- `build-plan.json`: proyección de recetas y mínimo, generada desde esa evidencia con las siete diferencias autorizadas. El generador no consulta ni escribe Figma.
- `destination/`: baseline de 298 variables y Button, IDs de construcción, relecturas, mapas, comparación y captura final. Los deltas `after-text-current-*` e `icon-frame-metadata-correction.json` sustituyen únicamente los campos afectados en la comparación, conservando lo observado antes de la reparación.
- `native/`: capturas y trazas del reproductor real; hover/retorno, disabled y selección/paneles del ejemplo consumidor. Su comparación no demuestra HTML/ARIA o teclado web.
- `context-*.json`: proyecciones compactas verificadas para los cuatro temas, con los 19 requisitos íntegros.

Durante QA se corrigió el orden de enlace entre estilos y variables; BH-P02 conserva la regla y su fuente. También se normalizó después del binding de tamaño la metadata de borde no pintado del frame de icono; el vector remoto conserva exactamente su geometría. Después del playback se reconciliaron cuatro ejemplos pill con su estado hover declarado. Los principales, aliases y reacciones se comparan contra las expectativas originales, sin relajarlas para hacer pasar una diferencia.

Las pruebas de crecimiento crean y eliminan solamente sus propios nodos temporales; `focus-consumer-stress.json` conserva 24 casos e IDs removidos. Los frames de demostración y documentación permanecen; no se retienen nodos QA temporales. La revisión independiente se declara NOT_RUN.

Reproducción sobre las evidencias guardadas:

```sh
python3 -B implementations/figma/tab-verify.py
# Con el Python del runtime que incluya Pillow:
python3 -B implementations/figma/tab-native-verify.py
```

Estos comandos verifican capturas registradas. Para verificar una edición posterior de Figma hay que releer los IDs y regenerar la evidencia afectada; no basta volver a ejecutar un comparador sobre snapshots antiguos.
