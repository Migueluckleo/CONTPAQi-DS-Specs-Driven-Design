# Dot · ADR-021

El [contrato actual](../../norms/components/dot.1.0.0.md) es la fuente de reglas. [Consumo](../../consumption/dot/README.md), [mapa actual](migration-map.json) y [QA](../qa/dot-pilot-check.json) enlazan Figma, tokens y pruebas sin duplicar reglas.

Dependencias actuales:

| Consumidor | Dependencia | Sustitución |
|---|---|---|
| Avatar 3.0.0 | Dot 1.0.0 directa | Presencia activa/ocupada/inactiva, tres tamaños |
| Avatar group 3.0.0 | Avatar 3.0.0 → Dot | Hijos vinculados, presencia oculta conservada |
| Tab 3.0.0 | Dot 1.0.0 directa | count/medium; texto formateado conservado |
| Tabs 3.0.0 | Tab 3.0.0 → Dot | Hijos y overrides conservados |
| Button 3.0.0 | Ninguna | Sin incorporación de Dot |

Se reemplazaron 415 referencias existentes (238 de presencia y 177 de conteo), incluidos casos ocultos y heredados. El inventario final cuenta 503 referencias a Dot en todas las páginas, con 88 nuevas en su documentación y QA. Se retiraron dos helpers privados, nueve variables y un estilo sin consumidores. Las tres colecciones contienen 148 primitivas, 109 semánticos y 139 tokens de componente.

Las versiones mayores de los cuatro consumidores registran la sustitución de dependencias y el retiro de sus APIs privadas de tokens/propiedades. [El índice histórico](history/manifest.json) preserva las revisiones exactas, el token set anterior y el commit fuente; las revisiones que necesitan tokens retirados se excluyen del catálogo operativo, conforme a BH-P05. No se reescribieron sus bytes.

Reproducir derivados locales: `python3 -B consumption/dot/materialize-plan.py`, `python3 -B implementations/figma/avatar-plan.py`, `python3 -B consumption/tab/materialize-plan.py`, `python3 -B consumption/project-native-ledgers.py` y `python3 -B implementations/figma/dot-verify.py`. La última orden agrega observaciones ya guardadas; no accede a Figma ni repite sus pruebas nativas. Actualizar hashes de manifiestos solo después de producir el comprobante final. Los scripts no son un adaptador Figma general; sus escrituras requieren la skill oficial cargada, sesión vigente y reconciliación de activos existentes.

El contraste de Dot está medido en [contrast.json](contrast.json). Count y Max count son independientes. El consumidor decide formato, visibilidad, actualizaciones y semántica accesible. No hay reproducción interactiva aplicable a Dot: la raíz carece de reacciones. Las cuatro transiciones de Tab se verificaron estructuralmente; no se declara una nueva reproducción de ese prototipo. React y publicación de biblioteca permanecen diferidos. El origen y el proyecto anterior solo se leyeron.

Figma materializó el contenido de 24 slots de instancias al restaurar los overrides anidados; los 96 IDs derivados nuevos están vinculados con los anteriores en el mapa. Se comprobó conservación de posición, tamaño, estado, visibilidad y principal Dot por cada presencia; el contenido sigue vinculado a Avatar. El lector usa inventarios activos y rangos tipográficos: los getters por ID retienen objetos de tres variables tipográficas retiradas en caché, aunque están fuera de las colecciones y sin referencias actuales. El comprobante registra el barrido corregido, sin interpretar esa caché como variables activas.

El barrido final cubre 503 instancias Dot y 206 textos. Once contadores pertenecen a vistas de documentación que ya estaban ampliadas a 1,75×: Figma convierte sus métricas tipográficas en valores escalados. Se conservaron tamaño, contenido y aliases de fuente/peso; esas vistas se contrastan con el estilo canónico y la geometría anterior. Los maestros y los consumidores a escala canónica conservan el vínculo al estilo compartido. No se crearon tokens o estilos alternos por la ampliación.
