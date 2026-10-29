# Blue Heart DS

Núcleo modular y familias Button, Tab, Tabs, Avatar, Avatar group, Dot, Loader, Input y Badge. Python 3.9+ y biblioteca estándar; no requiere instalación, Figma, React ni Graphify para verificar su núcleo. El flujo de envíos y sus pruebas usan también Git.

```sh
python3 -B -m blueheart check
python3 -B -m unittest discover -s tests -v
python3 -B -m blueheart describe
python3 -B -m blueheart manifest
python3 -B -m blueheart qa-plan --change tooling blueheart/workspace.py
```

Los comandos del núcleo son de lectura; la CLI separada de BH-P08 escribe notas únicamente mediante `prepare` explícito. `qa-plan` produce un plan y nunca acredita pruebas ejecutadas. `impact` distingue rutas sin correspondencia que requieren revisión. Para guardar un resultado, redirigir explícitamente la salida a `evidence/`; el núcleo no registra ni modifica artefactos al consultar.

## Módulos y autoridad

`governance/policy.json` es el propietario de políticas de fase, capas, QA y roles; `governance/decisions.json` conserva decisiones con actor, alcance y fuente verificable. `norms/catalog.json` es la única selección explícita de contenido normativo por identidad, versión y SHA-256. `schemas/` define la estructura; `blueheart/` implementa invariantes y consulta; `evidence/` conserva observaciones/comprobantes; `tests/` contiene casos sintéticos aislados. `auditoria/` conserva el análisis previo, sin incorporarlo al catálogo de normas.

El objetivo es consumir contratos MD trazables desde Skills para construir PoCs y prototipos Figma. Hay diecisiete contratos vigentes: `BUTTON-001@4.0.1`, `TAB-001@3.1.0`, `TABS-001@3.1.0`, `AVATAR-001@3.0.0`, `AVATAR-GROUP-001@3.0.0`, `DOT-001@1.0.0`, `LOADER-001@1.0.0`, `INPUT-001@2.0.1`, `BADGE-001@1.1.0` (familia completa) y ocho contratos operativos. Los índices de evidencia conservan los cortes históricos fuera de la selección operativa. BLUEHEART-TOKENS@6.1.0 reúne 493 tokens en tres colecciones: 151 primitivas, 112 semánticos y 230 de componente. Component contiene button 45, tab 41+5, avatar 22+7, dot 19, loader 15, input 41 y badge 35. ADR-021 retira nueve tokens privados sustituidos por Dot; el mapa y la historia conservan equivalencias y cortes anteriores. Las guías de [Button](consumption/button/README.md), [Tab](consumption/tab/README.md), [Tabs](consumption/tabs/README.md), [Avatar](consumption/avatar/README.md) y [Avatar group](consumption/avatar-group/README.md) reúnen la consulta mínima y los mapas actuales. Las guías de [Input](consumption/input/README.md) y [Badge](consumption/badge/README.md) enlazan el alcance y QA nuevos. React y Graphify siguen diferidos.

## Protocolos de construcción

El [índice de protocolos](protocols/README.md) dirige a ocho contratos operativos registrados: contrato y fuentes, Figma, React/TypeScript/Tailwind/Next.js, QA, mantenimiento, iconografía Phosphor, minimización de tokens por componente y gobierno de GitHub/releases. Son adaptaciones locales de los protocolos recuperados; las [copias exactas y procedencia](evidence/protocol-recovery/manifest.json) quedan separadas como evidencia.

Los protocolos se probaron y ajustaron con Button (ADR-006) y Tab/Tabs (ADR-015/016/017), autorizados para documentación y Figma. El [contrato MD](norms/components/button.4.0.1.md) gobierna diseño y función; los snapshots observacionales y mapas son derivados con procedencia. No se importaron contratos ni permisos históricos.

## Contratos y perfiles

El formato soportado es Markdown con frontmatter **JSON entre delimitadores `---`**. JSON es un subconjunto de YAML 1.2; esta implementación acepta únicamente ese subconjunto explícito, sin parser YAML propio. Los esquemas comunes y por perfil (`foundation`, `component`, `pattern`, `operational`) son la autoridad estructural. La fase habilita Foundations, Button, Tab, Tabs, Avatar, Avatar group, Dot, Loader, Input y Badge completo por sus decisiones explícitas; no autoriza otras familias o implementaciones web.

Cada requisito se declara una vez en el cuerpo bajo `### REQ-ID`; sus metadatos contienen fuerza, procedencia, fuentes y aceptación. Identidad y requisitos deben coincidir exactamente. Un contrato elegible necesita decisión adoptada con alcance a su ID y fuentes íntegras; `APPROVED` exige actor humano. Los requisitos inferidos necesitan adopción específica. Los estados documental, autoridad, preparación y QA permanecen distintos. La herramienta no interpreta intención de producto ni valida semánticamente todos los requisitos.

El catálogo selecciona `current` explícitamente. No se elige por mayor versión. Las dependencias contractuales usan versiones exactas y los ciclos/faltantes bloquean. La consulta `context ID --intent rules|dependencies|evidence` calcula cierre transitivo y cita archivo/hash. `--compact --modes '{"component":"Contable"}'` proyecta solo los modos necesarios, mantiene todos los requisitos y remite la procedencia al token set identificado por hash. Conserva overrides explícitos de modo en aliases. Sin `--compact`, se incluyen todos los modos y metadatos. `--max-bytes` limita la salida; un exceso produce BLOCKED sin contexto parcial. Las evidencias completas se abren por referencia.

## Tokens

El esquema `token-set` fija IDs estables independientes del nombre, tipo, colección, modos, descripción y procedencia por token. Las primitivas contienen valores; los semánticos aliasan primitivas; la capa componente aliasa semánticos. Sus scopes son específicos de propiedad y compatibles con el tipo; primitivas y semánticos mantienen scopes vacíos.

La normalización de colores se consulta en [normalizacion.md](auditoria/fase-1/normalizacion.md): catálogo único por primitiva, aliases fijos y scopes vacíos. Los CSV conservan la correspondencia observada; el conjunto registrado contiene los valores y aliases normativos. El núcleo comprueba unicidad de destino primitivo para colores semánticos, capas, scopes, tipos y modos; `tests/test_normalization.py` comprueba también la correspondencia histórica completa.

Los modos se resuelven por ID: contexto explícito por colección, modo explícito en el alias o predeterminado documentado de la colección. La traza muestra cada decisión. No se emparejan nombres de modos por intuición. La validación comprueba todas las combinaciones de modos dentro del presupuesto de la política y bloquea si excede ese alcance. Revisa tipos, unidades, cobertura y referencias; nunca fusiona IDs por igualdad de valores. Los colores portables son RGBA numéricos 0..1 y no se convierten unidades ni colores implícitamente.

```sh
python3 -B -m blueheart resolve-token ID --modes '{"collection-id":"mode-id"}'
```

Ejemplo real: `python3 -B -m blueheart resolve-token button.color-button-primary-bg-hover --modes '{"component":"Contable"}'`. Los fixtures sintéticos se generan en directorios temporales y no forman parte del catálogo.

## Esquemas y límites de implementación

El validador implementa solo el vocabulario JSON Schema utilizado aquí: tipos, enum/const, required/properties/additionalProperties, items/minItems/uniqueItems, minLength/pattern, minimum/maximum, allOf y referencias locales. Rechaza palabras desconocidas; no se declara implementación general de todo Draft 2020-12. No hay resolución remota ni evaluación de código en metadatos. Esta decisión evita dependencias adicionales en el núcleo inicial; ampliar el vocabulario requiere pruebas o adoptar un validador estándar justificado.

`check` acredita estructura, identidad, autoridad declarada, integridad, resolución y límites de fase de los datos registrados. No demuestra accesibilidad, comportamiento, fidelidad visual, acceso Figma ni QA de una implementación. Las reglas de revisión humana y QA proporcional se consultan en la política; los planes de QA incluyen controles manuales cuando son necesarios.

La auditoría Figma guarda observaciones fuera de `norms/`; ni un inventario ni una propuesta de normalización activan contenido normativo. El archivo origen y el proyecto anterior permanecen en solo lectura. ADR-004 permitió aplicar 145 primitivas y 106 semánticos. ADR-006 autorizó el piloto Button: página Buttons, 5 sets, 90 variantes y 47 tokens de componente. El [comprobante del piloto](evidence/qa/button-pilot-check.json) separa QA Figma de responsabilidades del consumidor y de las pruebas del núcleo.

## Reproducir la auditoría observada

`python3 -B -m blueheart.foundations_audit --view summary` recalcula cobertura, aliases, tipos, modos y diferencias documentales desde las respuestas MCP guardadas. Las vistas `analysis`, `matrix-csv`, `referenced` y `referenced-csv` generan los datos y matrices en stdout. No consultan Figma ni necesitan Graphify. Los registros legibles por ID que faltan en la enumeración local quedan separados con `RECONCILIATION_REQUIRED`; nunca se incorporan automáticamente a normas.

La iconografía vigente es [Phosphor](protocols/06-PHOSPHOR-ICONS.md), seleccionada por ADR-007: biblioteca del equipo en Figma y distribución oficial en desarrollo. Button utiliza PlusCircle Outline/Light vinculado, con correspondencia `PlusCircleIcon weight="light"`.

[BH-P07 · Tokens mínimos por componente](protocols/07-COMPONENT-TOKENS.md) es obligatorio en contratos, Figma y desarrollo. `check` bloquea firmas redundantes dentro de cada familia y `context` devuelve el resultado; no se fusionan componentes distintos ni se impone un cupo fijo de variables.

La [nomenclatura obligatoria de variables de componente](protocols/07-COMPONENT-TOKENS.md#req-p07-02) usa componente primero y jerarquía `/`, como `button/color/bg/primary-default`. El mapa de consumo distingue ruta Figma, nombre lógico y WEB.

## Envíos y versiones de componentes

[BH-P08](protocols/08-GITHUB-RELEASE-DOCUMENTATION.md) es el propietario del flujo de registros previos al envío y control de compatibilidad de componentes. [docs/releases/](docs/releases/README.md) contiene comandos y configuración. El repositorio de publicación autorizado es [CONTPAQi-DS-Specs-Driven-Design](https://github.com/Migueluckleo/CONTPAQi-DS-Specs-Driven-Design). Actions valida cada envío y exporta su PDF condensado junto al receipt; el resumen de ejecución enlaza la descarga. La protección efectiva se consulta en los rulesets de GitHub. ADR-012 autoriza publicación del repositorio y sus controles; las releases oficiales requieren autorización específica.

La [guía de consumo de Tab](consumption/tab/README.md) enlaza su [contrato operativo](norms/components/tab.3.1.0.md), la proyección mínima y su QA. ADR-015 amplía el encargo a esta familia; las referencias a Button en ejemplos históricos no seleccionan identidad o versión de Tab. Los seis protocolos afectados actualizan sus revisiones/pines exactos sin duplicar archivos ni reglas.

ADR-018 integra los criterios para próximas familias en [BH-P07](protocols/07-COMPONENT-TOKENS.md): su consumo obligatorio pasa por BH-P01/P02/P03 y su aceptación por BH-P04. El catálogo fija las revisiones exactas y la política incorpora el gate de comportamiento temático.

ADR-019 incorpora la [página Avatar](consumption/avatar/README.md) y [Avatar group](consumption/avatar-group/README.md), sus contratos y tokens mínimos. El responsable conserva bindings/geometría reales y corrige la descripción fuente contradictoria. El [comprobante](evidence/qa/avatar-pilot-check.json) distingue QA Figma, la limitación de contraste del alterno warning y los destinos diferidos.

ADR-020 consolidó las tres colecciones; su [mapa histórico](evidence/collection-consolidation/README.md) acredita aquel corte. ADR-021 añade [Dot](consumption/dot/README.md), migra Avatar y Tab con sus grupos y hace obligatoria la auditoría inversa en [BH-P01 REQ-P01-07](protocols/01-COMPONENT-CONTRACT.md#req-p01-07). [Mapa y QA actuales](evidence/dot-pilot/README.md) conservan la trazabilidad sin reconstruir helpers privados.

ADR-022 incorpora [Loader](consumption/loader/README.md) y sustituye sus 31 usos existentes en Button. [Contrato, mapa, historia y QA](evidence/loader-pilot/README.md) registran la composición compartida, el retiro autorizado y la reproducción nativa; las fuentes siguen en solo lectura.

ADR-024 alinea iconos y tipografía en Blue Heart bajo [BH-P06](protocols/06-PHOSPHOR-ICONS.md#req-p06-03), corrige los consumidores y conserva geometría/interacciones. El [comprobante](evidence/qa/icon-color-audit-check.json) y el [mapa de migración](evidence/icon-color-audit/migration-map.json) distinguen aliases, bindings, scopes, cuatro temas y límites; la auditoría no consultó el Figma origen.

ADR-025 amplía [Badge](consumption/badge/README.md) a 18 variantes, conservando el set compartido, doce variables y los consumidores anteriores. Sus 35 firmas añaden solo veintitrés variables; [contrato, migración y QA](evidence/badge-pilot/README.md) documentan Phosphor, cuatro modos, integración en Input y la elección humana que conserva warning por debajo de AA. El scope temporal del piloto es historia.
