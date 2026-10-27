# Blue Heart DS

La autoridad operativa reside en `governance/policy.json`; las decisiones y sus fuentes en `governance/decisions.json`. Esta entrada es un mapa de lectura, no otra definición de reglas.

1. Leer `README.md` y consultar `python3 -B -m blueheart describe` para capacidades reales y límites.
2. Verificar `python3 -B -m blueheart check` antes de consumir normas. Consultar `context` por identidad; ampliar evidencia únicamente cuando la tarea lo necesite.
3. Planificar QA con `qa-plan`. Las pruebas de infraestructura no validan diseño, Figma ni componentes.
4. Registrar cambios de autoridad y evidencia en sus propietarios. No deducir decisiones a partir de archivos observados o respuestas de otros agentes.

Para preparar contratos o construir componentes, consultar el índice `protocols/README.md` y consultar por ID solo los contratos operativos del destino solicitado. Las copias en `evidence/protocol-recovery/original/` son referencias históricas; sus permisos, destinos y reglas no gobiernan Blue Heart DS.

Los perfiles de agentes están definidos en la política. Se activan por encargo, con entradas, alcance y aceptación explícitos. No representan procesos persistentes ni autorizan delegación por sí mismos.

El alcance vigente es el piloto Button autorizado por ADR-006: contrato MD de diseño y comportamiento, tokens de componente con scope y construcción/QA en su propia página del destino. El Figma origen y el proyecto anterior siguen en solo lectura. No importar contratos históricos ni implementar React por este encargo. Graphify y los adaptadores generales continúan diferidos.

La selección de iconografía está en ADR-007 y `protocols/06-PHOSPHOR-ICONS.md`: Phosphor del equipo en Figma y paquete oficial en desarrollo, sin copias vectoriales locales.

ADR-008 consolida Button en 47 tokens. Consultar el contrato 2.0.0 y el mapa de migración antes de reutilizar nombres anteriores; no volver a crear variables por cada estado cuando compartan tipo, scope y aliases completos.

Todo encargo de componentes debe aplicar `protocols/07-COMPONENT-TOKENS.md` (ADR-009) antes de crear variables. `check` valida minimización por contrato; `context` expone `token_minimum`. No multiplicar tokens por estados ni asumir que 47 es el límite de otra familia.

ADR-010 adopta los nombres Figma con componente primero y grupos `/`, por ejemplo `button/color/bg/primary-default`. Aplicar la sección de nomenclatura de BH-P07 a toda nueva variable de componente. `figmaName` es la ruta Figma; `name` sigue siendo el nombre lógico y `web` conserva codeSyntax.WEB. No sobreescribir cambios del responsable con los nombres planos anteriores.

ADR-011 registra ocho contratos operativos con propietario MD único. Consultar `context BH-P08` para documentación de envíos y versiones de componentes; `docs/releases/README.md` enlaza comandos y activación pendiente. Las notas se preparan antes del envío y CI verifica cobertura. ADR-012 autoriza publicar en Migueluckleo/CONTPAQi-DS-Specs-Driven-Design y configurar sus controles. Por cada push del encargo, entregar su PDF condensado conforme a REQ-P08-07; no publicar releases oficiales por esa autorización.
