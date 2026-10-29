# Contratos operativos de Blue Heart DS

Ocho propietarios Markdown, registrados por ID, versión y hash en [norms/catalog.json](../norms/catalog.json), perfil [operational](../schemas/operational.schema.json), autoridad ADR-011 y extensión de publicación/PDF ADR-012 y flujo sin aprobaciones obligatorias ADR-013. La elegibilidad documental no acredita implementación de los destinos ni amplía la fase. Cada archivo contiene entradas, salidas, responsables, fallos, requisitos y aceptación.

| ID | Propietario único | Versión |
|---|---|---|
| BH-P01 | [01-COMPONENT-CONTRACT](01-COMPONENT-CONTRACT.md) | 2.3.0 |
| BH-P02 | [02-FIGMA-CONSTRUCTION](02-FIGMA-CONSTRUCTION.md) | 2.3.1 |
| BH-P03 | [03-WEB-CONSTRUCTION](03-WEB-CONSTRUCTION.md) | 2.3.1 |
| BH-P04 | [04-QA-AND-DELIVERY](04-QA-AND-DELIVERY.md) | 2.3.0 |
| BH-P05 | [05-MAINTENANCE-AND-RELEASES](05-MAINTENANCE-AND-RELEASES.md) | 2.0.4 |
| BH-P06 | [06-PHOSPHOR-ICONS](06-PHOSPHOR-ICONS.md) | 2.1.0 |
| BH-P07 | [07-COMPONENT-TOKENS](07-COMPONENT-TOKENS.md) | 2.2.0 |
| BH-P08 | [08-GITHUB-RELEASE-DOCUMENTATION](08-GITHUB-RELEASE-DOCUMENTATION.md) | 1.2.4 |

Consultar solo el contrato del encargo y sus dependencias: `python3 -B -m blueheart context BH-P02`. `check` verifica estructura, autoridad, fuentes, hashes y cierre; no ejecuta Figma ni acredita QA de destinos. Los protocolos se consultan por tarea, sin añadir los ocho al contexto de cada componente. El contrato Button conserva diseño y función; los protocolos gobiernan el trabajo. Los valores permanecen en su conjunto de tokens.

## Procedencia y adaptación

Las [copias exactas](../evidence/protocol-recovery/original/protocols/) son evidencia histórica, sin autoridad operativa. Conservan los textos originales, incluidas referencias y permisos del proyecto anterior; no se ejecutan ni se leen automáticamente. Sus enlaces a contratos no copiados pertenecen al repositorio de origen. El [manifiesto](../evidence/protocol-recovery/manifest.json) identifica cada archivo, hash y copia.

| Original | Aplicación en Blue Heart |
|---|---|
| P01 Entorno | Preflight proporcional en BH-P01/BH-P03. No instala herramientas ni Graphify por leerlo. |
| P02 Ingesta | Fuentes, hashes y cobertura en BH-P01; sin recrear siete registros. |
| P03 Síntesis | Requisitos verificables y autoridad en BH-P01; perfil mínimo existente, sin 21 secciones obligatorias ni enmiendas paralelas activas. |
| P04 Figma | BH-P02 conserva lectura previa/posterior, identidad, composición y bindings. Usa el destino Blue Heart y la normalización vigente. |
| P05 Trazabilidad | Comprobante del encargo en BH-P04/BH-P05; no cierre Graphify obligatorio. |
| P06 QA | BH-P04 separa contrato, implementación y destinos; sin atribuir aprobación humana. |
| P07 Web | BH-P03 separa biblioteca React del catálogo Next.js; conserva tipos, ejemplos, composición y pruebas. |
| P08 Releases | BH-P05 conserva hashes, versiones e integridad; empaquetado y skills solo si son entregables afectados. |
| P-SLOTS | BH-P01/BH-P02/BH-P03/BH-P04 conservan cardinalidad y pruebas desde el consumidor. Sin imponer Slots a toda familia. |

También se copiaron reglas de diseño, cierre eficiente y README/package.json web como contexto. Se recupera la preservación de assets, tipografía y unidades; no se importan excepciones de personajes, contratos, permisos de migración/publicación, destinos antiguos ni versiones de dependencias.

Se elimina el acoplamiento entre un cambio local y reconstruir grafo, catálogo, dos skills y paquetes. La falta de binding o color no se resuelve mediante semánticos duplicados ni eligiendo una primitiva aproximada por conveniencia. La comprobación de esta recuperación acredita documentos y copias; no acredita un componente construido.

ADR-009 hace obligatorio BH-P07 para cada componente nuevo o modificado. La regla se aplica por familia; 47 es el resultado de Button, no un cupo global. `check` y `context` bloquean la ingesta de firmas redundantes declaradas.

ADR-010 fija la nomenclatura Figma con componente primero: `button/color/bg/primary-default`, `button/font/family` y `button/size/height-medium`. BH-P07 es el propietario de la regla; nombres CSS, rutas Figma e identidades se mantienen separados.

ADR-015 amplía el encargo a Tab individual. Las revisiones 2.0.1 de BH-P01/P02 y sus consumidores retiran la selección fija del piloto y actualizan dependencias exactas; BH-P08 1.2.1 conserva sus controles. Las reglas de minimización y nomenclatura de BH-P07 no cambian.

ADR-016/017 incorporan la página completa y TABS-001, con dependencia exacta del contrato Tab vigente. Las reglas de nombres y minimización siguen en BH-P07; cada familia conserva su propio contrato MD.

ADR-018 integra los criterios generales en BH-P07 (nombres por función/estado, mínimo por firma y comportamiento temático). BH-P01/P02/P03/P04 consumen sus requisitos; BH-P05/P08 mantienen el cierre con dependencias exactas. El gate `component-theme-behavior` se consulta con qa-plan; no certifica el destino por sí mismo.

ADR-020: la regla de colecciones pertenece a BH-P07 REQ-P07-07 y se consume por BH-P01/02/03/04/05/08. El catálogo fija las revisiones actuales; no recuperar reglas de colecciones por familia desde evidencia histórica.

ADR-021 incorpora la auditoría inversa obligatoria en [BH-P01 REQ-P01-07](01-COMPONENT-CONTRACT.md#req-p01-07). BH-P02/03/04/05/08 la consumen por referencia; qa-plan expone el gate `component-reverse-dependency-reuse`. El QA nativo y la migración siguen perteneciendo al comprobante de cada encargo.

ADR-024 incorpora la paridad icono/texto en BH-P06 REQ-P06-03/04; BH-P02 y BH-P03 consumen esa única definición. El QA del encargo conserva observaciones y resultados de Blue Heart, sin nueva lectura de la biblioteca origen.
