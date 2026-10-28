# Loader · ADR-022

El [contrato MD](../../norms/components/loader.1.0.0.md) gobierna Loader; [consumo](../../consumption/loader/README.md), [migración](migration-map.json) y [QA](../qa/loader-pilot-check.json) enlazan las proyecciones y sus resultados. No se modificó el Figma origen ni el proyecto anterior.

Se construyeron 24 variantes públicas y seis ciclos compartidos de 24 fases. Las 15 firmas se agrupan en cinco colores de trazo, seis dimensiones y cuatro grosores, bajo component/loader. Únicamente brand sigue el tema. La dimensión 88 px requiere dos nuevas Foundations sin scope; las demás ya existían.

Button pasa a 4.0.0 al adoptar Loader y retirar dos tokens exclusivos; conserva sus otros 45 tokens. Se sustituyeron 15 dependencias de maestros y sus 16 usos heredados, sin resetear estos últimos. Los 90 principales mantienen geometría, contenido y reacciones fuera de Loader. El cambio corrige un desvío previo respecto del Button fuente: riel gris en secondary/link/text y remate redondo del arco. No preserva ese defecto como excepción.

El barrido incluyó páginas, hijos invisibles, rangos de texto y estilos; los tres sets privados, 72 fases y dos colores se retiraron con cero referencias y [aprobación explícita](../authorization/loader-retirement-approval.txt). [Historia](history/manifest.json) conserva bytes exactos de los tres contratos Button anteriores, registro previo y scripts retirados. Sus referencias se interpretan dentro de ese corte, no contra tokens actuales.

La [captura de destino](destination/variants.png) permite revisar todas las variantes. [La traza](playback/runtime-trace.json) y [comparación](playback/observations.json) conservan muestras del reproductor nativo, sin presentar conexiones almacenadas como reproducción ni certificar 30 fps. Reduced motion y semántica de navegador siguen como obligaciones de consumo. La revisión independiente no se ejecutó y no se atribuye aprobación humana del QA.

Los parámetros y tolerancias se fijaron en el contrato/pase previo; el QA nativo no fue una prueba de infraestructura. `python3 -B implementations/figma/loader-plan.py` reproduce las recetas locales. Los scripts Figma requieren las skills oficiales, sesión válida e IDs del ledger; no son adaptadores generales ni autorización para reconstruir activos existentes.
