# Blue Heart DS

La autoridad operativa reside en `governance/policy.json`; las decisiones y sus fuentes en `governance/decisions.json`. Esta entrada es un mapa de lectura, no otra definición de reglas.

1. Leer `README.md` y consultar `python3 -B -m blueheart describe` para capacidades reales y límites.
2. Verificar `python3 -B -m blueheart check` antes de consumir normas. Consultar `context` por identidad; ampliar evidencia únicamente cuando la tarea lo necesite.
3. Planificar QA con `qa-plan`. Las pruebas de infraestructura no validan diseño, Figma ni componentes.
4. Registrar cambios de autoridad y evidencia en sus propietarios. No deducir decisiones a partir de archivos observados o respuestas de otros agentes.

Para preparar contratos o construir componentes, consultar el índice `protocols/README.md` y consultar por ID solo los contratos operativos del destino solicitado. Las copias en `evidence/protocol-recovery/original/` son referencias históricas; sus permisos, destinos y reglas no gobiernan Blue Heart DS.

Los perfiles de agentes están definidos en la política. Se activan por encargo, con entradas, alcance y aceptación explícitos. No representan procesos persistentes ni autorizan delegación por sí mismos.

El alcance vigente comprende Button (ADR-006), Tab y Tabs (ADR-015/016/017), Avatar y Avatar group (ADR-019) Dot (ADR-021) y Loader (ADR-022): contratos MD de diseño y comportamiento, tokens de componente con scope y construcción/QA en sus propias páginas del destino. El Figma origen y el proyecto anterior siguen en solo lectura. No importar contratos históricos ni implementar React por este encargo. Graphify y los adaptadores generales continúan diferidos.

La selección de iconografía está en ADR-007 y `protocols/06-PHOSPHOR-ICONS.md`: Phosphor del equipo en Figma y paquete oficial en desarrollo, sin copias vectoriales locales.

ADR-008 consolida Button en 47 tokens. Consultar el contrato vigente y el mapa de migración antes de reutilizar nombres anteriores; no volver a crear variables por cada estado cuando compartan tipo, scope y aliases completos.

Todo encargo de componentes debe aplicar `protocols/07-COMPONENT-TOKENS.md` (ADR-009) antes de crear variables. `check` valida minimización por contrato; `context` expone `token_minimum`. No multiplicar tokens por estados ni asumir que 47 es el límite de otra familia.

ADR-010 adopta los nombres Figma con componente primero y grupos `/`, por ejemplo `button/color/bg/primary-default`. Aplicar la sección de nomenclatura de BH-P07 a toda nueva variable de componente. `figmaName` es la ruta Figma; `name` sigue siendo el nombre lógico y `web` conserva codeSyntax.WEB. No sobreescribir cambios del responsable con los nombres planos anteriores.

ADR-011 registra ocho contratos operativos con propietario MD único. Consultar `context BH-P08` para documentación de envíos y versiones de componentes; `docs/releases/README.md` enlaza comandos y configuración remota. Las notas se preparan antes del envío y CI verifica cobertura. ADR-012 autoriza publicar en Migueluckleo/CONTPAQi-DS-Specs-Driven-Design y configurar sus controles. Por cada push del encargo, entregar su PDF condensado conforme a REQ-P08-07; no publicar releases oficiales por esa autorización.

ADR-013 elimina las aprobaciones obligatorias para integrar en main; las condiciones de PR, CI y notas siguen en REQ-P08-05. Las revisiones voluntarias no son un requisito de GitHub.

ADR-014 adopta Button 2.0.1 y la corrección de Secondary focus en REQ-PROTOTYPE. La guía de consumo enlaza la proyección vigente de recetas y el comprobante de esa corrección; el baseline y la prueba 2.0.0 se conservan como historia.

ADR-015/016/017 registran Tab 1.1.0 y Tabs 1.0.0. Consultar los contratos vigentes por ID y las guías consumption/tab y consumption/tabs; allí se enlazan recetas, mapas y QA actuales. Las decisiones anteriores permanecen como historia; las fuentes siguen en solo lectura y React diferido.

ADR-018 hace obligatorios los criterios de BH-P07 REQ-P07-02/03/06 antes de crear o modificar variables de cualquier familia. Consumir el pase por BH-P01 y verificarlo con BH-P04; la clasificación temática y las excepciones pertenecen al contrato de cada componente. Los casos de Tab no son reglas de color para las familias siguientes.

ADR-019 amplía el encargo a Avatar y Avatar group: consultar AVATAR-001 / AVATAR-GROUP-001 y consumption/avatar / avatar-group. La página Avatars conserva cuatro temas reales, anillo observado de 1 px, presencia privada y slot 2–4. BLUEHEART-TOKENS 2.1.0 añade tres espaciados negativos con sus aliases; el mapa de Foundations registra la extensión sin cambiar identidades anteriores. La limitación de contraste de warning está en el contrato/comprobante; no convertirla en AA ni trasladarla a otras familias.

ADR-020 corrige el almacenamiento. Aplicar BH-P07 REQ-P07-07 antes de crear variables: tres colecciones homónimas primitive, semantic y component; los grupos button, avatar y tab no son colecciones. Avatar group y Tabs se alojan bajo avatar/tab. El tema se selecciona en component y los roles invariantes repiten su alias en los cuatro modos. Consultar los contratos y manifiestos vigentes; los IDs y rutas retirados solo sirven como historia.

ADR-021 adopta Dot 1.0.0 y Avatar/Avatar group/Tab/Tabs 3.0.0. Consultar `context DOT-001` y consumption/dot; el mapa actual retira nueve tokens privados. Antes de cada componente aplicar BH-P01 REQ-P01-07 para consumidores directos/transitivos y QA de sustitución; no reconstruir los helpers históricos.

ADR-022 adopta Loader 1.0.0 y Button 4.0.0: consultar LOADER-001 y consumption/loader. Button conserva 45 tokens propios y consume Loader por composición; sus tres ciclos privados y dos colores temporales fueron retirados con aprobación explícita. No reconstruirlos desde scripts históricos. El conjunto actual añade únicamente la cadena de 88 px y los 15 tokens de Loader; aplicar el mapa y QA vigente.

ADR-023 adopta Input 1.0.0 (42 variantes en Input/empty e Input/filled) y únicamente Badge subtle/small 1.0.0 como dependencia autorizada. Consultar INPUT-001 / BADGE-001 y consumption/input / badge. Input conserva 41 tokens, Badge 12 y cuatro Foundations nuevas; el QA por variante preserva los once efectos raíz y documenta la equivalencia del tracking porcentual a px por la limitación nativa del binding. Los contadores Badge de Tab continúan siendo Dot. Ese límite inicial de Badge queda superado por ADR-025; React, captura/validación de datos y reacciones ausentes siguen fuera de alcance.

ADR-024 adopta la paridad cromática icono/texto definida en BH-P06 REQ-P06-03/04 y consumida por BH-P02/P03. Consultar los contratos vigentes: Button 4.0.1 (45 tokens), Tab/Tabs 3.1.0 (41+5) e Input 2.0.0 (41). Question sigue Label y CaretDown al contenido/placeholder. El token lógico/CSS input.color-icon-tooltip se retiró y su ID/key nativo se reutilizó como secondary; consultar el mapa del encargo. El corte histórico 6.0.0 añade solo dos tokens Tab y conserva las tres colecciones. No reconstruir colores anteriores desde snapshots. La auditoría se limitó a Blue Heart; Avatar ya coincidía y Loader conserva su papel separado de indicador de progreso.

ADR-025 adopta Badge 1.1.0 completo (18 variantes, 35 firmas: doce IDs/key conservados y veintitrés adiciones), Input 2.0.1 por pin compatible y BLUEHEART-TOKENS 6.1.0 (493 tokens). Consultar BADGE-001, INPUT-001 y consumption/badge / input. El único set Badge se amplió en su identidad existente; no reconstruir el subconjunto temporal desde scripts o snapshots históricos. Input mantiene subtle/small; sus 113 usos y los tres ejemplos previos conservan geometría, texto e identidad. Los colores son invariantes; Phosphor sigue Label conforme BH-P06. La elección humana conserva warning a 2.962:1, sin afirmar AA. Las tres colecciones permanecen; el origen y el proyecto anterior siguen en solo lectura.
