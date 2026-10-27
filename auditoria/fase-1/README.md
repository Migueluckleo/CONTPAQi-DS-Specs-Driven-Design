# Blue Heart DS · Fase 1

> Corte histórico de Foundations, anterior al piloto Button. El estado vigente y su ampliación autorizada están en [la guía de consumo Button](../../consumption/button/README.md) y ADR-006. Las cantidades y restricciones de este corte no describen el piloto posterior.

Estado: arquitectura base implementada y verificada; auditoría Foundations realizada con limitaciones explícitas; normalización aplicada en el destino Figma y verificada mediante relectura. Fecha de contexto del proyecto: 26 de octubre de 2026.

## A. Arquitectura implementada

Se aplicó la arquitectura modular adoptada en la solicitud de Fase 1. El repositorio anterior no se utilizó como dependencia ni se copiaron sus contratos, scripts o componentes. Los documentos de la auditoría previa permanecen como antecedentes existentes.

```text
Blue Heart DS/
├── AGENTS.md                       entrada breve para agentes
├── README.md                       ejecución y límites del núcleo
├── blueheart.json                  localizadores de configuración
├── governance/
│   ├── policy.json                 reglas, roles, capas y gates
│   └── decisions.json              decisiones con actor, alcance y fuente
├── norms/catalog.json              selección normativa explícita: vacía
├── schemas/                        estructura común y perfiles diferenciados
├── blueheart/
│   ├── io.py                       lectura confinada, hashes y selectores
│   ├── schema.py                   vocabulario estructural cerrado
│   ├── contracts.py                Markdown, requisitos y cierre de dependencias
│   ├── tokens.py                   tipos, aliases, capas y modos
│   ├── workspace.py                catálogo, impacto, contexto y comprobaciones
│   ├── foundations_audit.py        análisis reproducible de evidencia Figma
│   └── __main__.py                 CLI de lectura
├── tests/                          casos sintéticos en memoria/directorios temporales
├── evidence/
│   ├── authorization/              solicitud actual conservada por hash
│   ├── foundations/                respuestas de Figma y matrices derivadas
│   └── qa/                         pruebas, manifiestos y comprobantes
└── auditoria/
    ├── 2026-10-26/                 diagnóstico arquitectónico previo
    └── fase-1/                     esta entrega y normalización de variables
```

No se crearon carpetas vacías para adaptadores, biblioteca React, componentes, releases ni Graphify. Sus responsabilidades están definidas en la política y su implementación sigue diferida.

### Mecanismos comprobados

| Mecanismo | Funcionamiento real | Límite |
|---|---|---|
| Catálogo normativo | Selección `current`, identidad, versión y SHA-256 explícitos; rechaza ambigüedad, hash alterado y archivo normativo no registrado. | Actualmente no hay contenido normativo. |
| Contratos SDD | Perfiles Foundation, componente y patrón; estructura y requisitos ligados a fuentes/aceptación. | La fase permite registrar solo Foundation; no se creó ningún contrato. |
| Autoridad | Decisión adoptada y acotada al ID; diferencia actor humano de decisión técnica. | No evalúa automáticamente la intención humana del texto fuente. |
| Dependencias | Referencias exactas y cierre transitivo; faltantes y ciclos bloquean. | Se apoya en relaciones declaradas; no descubre relaciones semánticas por inferencia. |
| Tokens | Identidad estable, procedencia por hash/selector/ID original, tipos, unidades, modos y arquitectura de tres capas. | Solo primitivas/semánticos habilitados; registro vacío y datos de prueba sintéticos. |
| Contexto | Reglas, dependencias o evidencia según intención; presupuesto de salida y rechazo sin éxito parcial. | La validación del catálogo es global; no se afirma I/O incremental a gran escala. |
| Impacto | Dependientes transitivos y rutas de evidencia; rutas no mapeadas quedan en revisión. | Las bajas requieren cotejo con el snapshot anterior; no se infieren consumidores externos. |
| QA proporcional | Plan de gates por clase de cambio, sin presentarlo como prueba ejecutada. | La revisión visual y de comportamiento pertenece al destino futuro. |
| Agentes | Roles y esquema de encargo con entradas, límites, aceptación y parada. | No se activaron procesos permanentes ni una oficina de agentes. |
| Auditoría | Recalcula inventario, aliases, grupos de igualdad y matrices desde respuestas MCP. | Reproducir los cálculos no actualiza la observación en vivo. |

### Decisiones y ajustes técnicos

- **ADR-001:** adopción de la arquitectura y autorización de Fase 1 por el responsable. La fuente es la solicitud actual, preservada en evidencia.
- **ADR-002:** ajuste técnico decidido por el agente dentro del alcance autorizado: Python 3.9+ y biblioteca estándar, frontmatter JSON y validación de un vocabulario JSON Schema cerrado. Se registra con actor `implementing_agent`; no se atribuye al usuario una aprobación detallada de esa elección.
- **ADR-003:** criterio del responsable para colores: un semántico por primitiva, alias fijo y scopes vacíos. Los temas se conservan en la correspondencia de consumo.
- **ADR-004:** autorización del responsable para aplicar únicamente primitivas y semánticos en el destino Figma. El origen sigue en solo lectura y no se permiten tokens de componente.
- JSON es un subconjunto de YAML 1.2, pero el parser acepta expresamente solo JSON entre `---`. Evita tanto instalar un parser como inventar un lector YAML general. Adoptar YAML más amplio o un validador estándar requiere una necesidad y pruebas concretas.
- El validador rechaza palabras de esquema no soportadas. No se declara conformidad completa con Draft 2020-12 ni se ocultan limitaciones bajo un PASS genérico.

No se instalaron dependencias. No se realizó publicación ni commit.

## B. Gobierno SDD optimizado

Las reglas operativas residen en `governance/policy.json`; las decisiones, en `governance/decisions.json`; los esquemas son propietarios de la estructura de datos. La documentación de capacidades se genera con `describe`. AGENTS dirige la lectura y no replica ocho protocolos.

Cada contrato tendrá un propietario Markdown. Los requisitos se redactan una vez bajo encabezados con ID; sus metadatos describen fuerza, procedencia, fuentes y aceptación. Los valores de diseño estarán en conjuntos de tokens referenciados, sin transcribir otro inventario editable en los contratos. Una observación de Figma se conserva en evidencia y no se vuelve normativa por estar guardada.

Los perfiles mínimos exigen:

| Perfil | Contenido específico adicional al núcleo común |
|---|---|
| Foundation | Dominios cubiertos, datos/referencias y criterios de aceptación. |
| Componente | Anatomía, composición y accesibilidad. Capacidad estructural preparada; contenido prohibido en esta fase. |
| Patrón | Contextos, comportamiento y accesibilidad. Capacidad estructural preparada; contenido diferido. |

Estado documental, autoridad y preparación por destino son dimensiones distintas. Los resultados QA se documentan por alcance; `qa-plan` nunca cambia una norma a validada. Los cambios de alto impacto o flujo requieren revisión independiente según el plan de QA; **esta entrega acredita pruebas automáticas y revisión del agente autor, no una ejecución independiente de otro verificador**.

Los roles se activan bajo demanda y reciben tareas acotadas. El esquema de encargo no concede permisos ni despacha agentes. React, Figma de escritura y Graphify no participan en `check`.

## C. Auditoría de Foundations

Origen: [Librería v1.1.0](https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=268-20245). El nodo `268:20245` corresponde a **Tabs**. La auditoría de variables se hizo a nivel de archivo, no únicamente sobre esa página.

Destino de la aplicación: [Blue Heart DS](https://www.figma.com/design/98xEw6sK8FRVNEhopM5SSz/Blue-Heart-DS?node-id=0-1). La auditoría inicial y el preflight de aplicación encontraron una página y cero variables/colecciones. Con autorización ADR-004 se crearon dos colecciones con 251 variables, verificadas mediante relectura.

La auditoría de origen utilizó `figma:figma-use`, con JavaScript de lectura y navegación de página. La aplicación posterior utilizó `figma-use` y `figma-generate-library` exclusivamente sobre las variables del destino; no modificó estilos ni creó nodos. Las respuestas completas y las recetas de censo están guardadas para comprobar el alcance de las afirmaciones.

### Inventario enumerado por la API local

| Colección | ID | Variables | Modos |
|---|---|---:|---|
| primitive | `VariableCollectionId:52:690` | 145 | Value, `52:0` |
| semantic | `VariableCollectionId:52:726` | 146 | Contable `52:2`; Administrativo `2849:0`; Servicios `2849:1`; Personas `2849:2` |

Contable es el modo predeterminado de semantic. Estos modos representan productos/temas; no se reinterpretaron como light/dark.

El conjunto enumerado contiene 162 COLOR, 118 FLOAT y 11 STRING. Hay 580 asignaciones de alias a 106 variables destino distintas. Se resolvieron los cuatro contextos reales de modos, sin ciclos, aliases locales rotos, incompatibilidad de tipos o modos faltantes en ese conjunto. `logo/categoria` contiene cuatro literales STRING en semantic, una diferencia respecto de la arquitectura objetivo estricta.

Hay 163 descripciones vacías: todas las 145 primitivas y 18 semánticos. Ninguna de estas 291 variables tiene `codeSyntax` definido. Las primitivas tienen scopes vacíos; seis semánticos utilizan `ALL_SCOPES`. La ausencia de una descripción o scope no demuestra por sí sola que un valor sea incorrecto.

También se leyeron estilos locales: 11 de efectos y ninguno de texto, pintura o grid. Los efectos no se convirtieron en tokens ni se inventó una equivalencia entre estilos y variables.

### Cobertura de consumidores

Se recorrieron **53 páginas, 46,235 nodos descendientes y 10,096 nodos de texto**, incluidos contenido oculto y Descarte. El censo recoge bindings de nodo, pinturas, efectos, grids y rangos de texto, más referencias de estilos. No registró errores de lectura de nodos/rangos en las respuestas exitosas.

De las 291 variables enumeradas, 159 tienen bindings directos observados y 132 no los tienen. Esto no significa que 132 sean eliminables: varias primitivas se utilizan a través de aliases y hay consumidores posibles en otros archivos que no cubre esta auditoría.

Por variable/página se conservaron conteos y hasta dos ejemplos identificables. Las matrices distinguen bindings directos, uso en Descarte y consumidores transitivos por alias. La suma de usos transitivos es un **límite superior**, porque un nodo puede consumir varias variables dependientes; no se presenta como número exacto de nodos únicos.

### Diferencia entre enumeración y lectura por ID

El censo encontró **441 IDs referenciados que no figuran en las 291 variables enumeradas**. Se pudo leer su metadata por ID:

- 108 devolvieron `remote: true`.
- 333 devolvieron `remote: false`, aunque no están en la enumeración local.
- Cuatro colecciones `colorWheelPrimitives_1…4` son legibles por ID, pero no aparecen en la enumeración local y devuelven listas de miembros vacías. Existen 320 registros referenciados vinculados a esas cuatro colecciones.
- Los otros 13 registros locales no enumerados señalan las colecciones primitive/semantic, pero faltan en sus listas de miembros.
- Dos de esos registros tienen consumidores fuera de Descarte, en Sidebar: `color/background/neutral/tertiary` (`VariableID:1089:8868`, un nodo) y `color/icon/neutral/primary` (`VariableID:1205:9990`, dos nodos).

Estos hechos son compatibles con referencias históricas o residuales, pero **no prueban su causa, vigencia, estado de eliminación o publicación**. Los registros permanecen separados con `RECONCILIATION_REQUIRED`. No se añadieron al catálogo vigente ni se consideraron automáticamente material migrable.

El inventario total observado por las dos vías contiene 732 IDs distintos, con alcances separados: 291 enumerados y 441 referenciados adicionales. No se declara inventario de todas las variables de las bibliotecas remotas ni de todos los archivos consumidores.

Los aliases de los registros adicionales remiten a otros 29 IDs que no se leyeron. Quedan listados en `further_alias_targets_not_read`; la resolución completa de esas cadenas está fuera del PASS del conjunto enumerado. No se sustituyen por valores inferidos ni se declaran rotos sin haberlos consultado.

## D. Normalización de variables

El criterio vigente es [normalizacion.md](normalizacion.md), registrado en ADR-003. Un único semántico de color por primitiva referenciada, alias fijo y `scopes: []`; componente, propiedad y estado se expresarán en los tokens consumidores.

[semanticos-color.csv](semanticos-color.csv) contiene las 42 entradas únicas del catálogo de color. [variables-normalizadas.csv](variables-normalizadas.csv) conserva la correspondencia de los 291 IDs originales: cada tema selecciona el semántico único que mantiene su primitiva de origen. La correspondencia no crea un semántico por fila. No se copiaron scopes del origen. Las variables normalizadas ya se guardaron en Figma: 145 primitivas y 106 semánticos; la [relectura](../../evidence/qa/figma-application-check.json) pasó sin diferencias.

## E. Matrices e inventarios

| Entregable | Contenido |
|---|---|
| [Inventario observado](</Users/miguel.leo/Desktop/Blue Heart DS/evidence/foundations/observed-inventory.json>) | 291 variables enumeradas, IDs/key, valores, tipos, scopes, modos, descripciones y aliases originales. |
| [Análisis reproducible](</Users/miguel.leo/Desktop/Blue Heart DS/evidence/foundations/analysis.json>) | 580 asignaciones de alias, 17 grupos candidatos por igualdad y matriz detallada por variable. |
| [Matriz de impacto, 291 filas](</Users/miguel.leo/Desktop/Blue Heart DS/evidence/foundations/impact-matrix.csv>) | Variable original, referencia a la correspondencia vigente, acciones, dependientes, páginas y ejemplos. |
| [Registros referenciados adicionales](</Users/miguel.leo/Desktop/Blue Heart DS/evidence/foundations/referenced-inventory.json>) | 441 registros y colecciones consultadas; distinción local no enumerado/remoto. |
| [Matriz complementaria, 441 filas](</Users/miguel.leo/Desktop/Blue Heart DS/evidence/foundations/referenced-impact-matrix.csv>) | Referencias adicionales, procedencia, consumidores fuera de Descarte y observaciones de bindings dentro de Descarte. |
| [Comprobación de Foundations](</Users/miguel.leo/Desktop/Blue Heart DS/evidence/qa/foundations-check.json>) | Resultados y límites de las verificaciones automatizadas. |

La matriz de impacto referencia el CSV de correspondencia vigente. Los nombres normalizados usan guiones y corresponden a variables creadas en Figma, según la [correspondencia de aplicación](../../evidence/figma-application/application-map.json). Los ejemplos con IDs de componentes son evidencia de consumidores leídos, no contratos ni implementaciones incorporadas a Blue Heart.

## F. QA y cierre

```sh
python3 -B -m unittest discover -s tests -v
python3 -B -m blueheart check
python3 -B -m blueheart manifest
python3 -B -m blueheart.foundations_audit --view summary
```

| Comprobación | Resultado y alcance |
|---|---|
| Pruebas de infraestructura, analizador y normalización | **37 PASS**; incluyendo fallos de integridad, rutas, autoridad, selección, dependencias, presupuesto, tipos, modos, unicidad de colores, scopes vacíos y correspondencia por tema. [Log](</Users/miguel.leo/Desktop/Blue Heart DS/evidence/qa/unit-tests.log>) |
| Catálogo inicial | **PASS:** cero contratos, conjuntos de tokens y tokens normativos. [Check](</Users/miguel.leo/Desktop/Blue Heart DS/evidence/qa/core-check.json>) |
| Dependencias adicionales | Ninguna instalada; núcleo independiente de Graphify, Figma y React. |
| Inventario enumerado | **PASS_OBSERVED_SCOPE:** 291 variables, cuatro contextos; estructura/aliases locales comprobados. |
| Registros fuera de enumeración | **RECONCILIATION_REQUIRED:** 333 locales y 108 remotos. No se oculta bajo el PASS anterior. |
| Normalización local de color | **42 semánticos / 42 primitivas referenciadas**, sin scopes ni duplicación; 291 IDs trazados y destinos de los cuatro temas preservados. [Comprobación](../../evidence/qa/normalization-check.json) |
| Estabilidad de variables enumeradas | Relectura de seis lotes: valores, IDs, scopes, descriptions, keys y aliases iguales. |
| Estabilidad de páginas y colecciones | Comparación final por IDs sin diferencias de contenido; el orden de arrays de enumeración no se usa como identidad. Una comparación inicial sensible al orden resultó falsa y se conserva con su aclaración. |
| Destino Figma | Relectura posterior a aplicación: una página sin contenido, dos colecciones, 145 primitivas y 106 semánticos. |
| Escrituras Figma | **PASS:** aplicación autorizada por ADR-004 y relectura de las 251 variables; aliases directos, scopes vacíos, 42 destinos de color únicos y cero tokens de componente. [Comprobante](../../evidence/qa/figma-application-check.json) |
| Revisión independiente | **NOT_RUN:** no se declara revisión de otro agente/persona. |
| QA visual, interacción y accesibilidad | **NOT_RUN:** fuera del alcance de auditoría de datos. |

Dos respuestas de Figma excedieron el límite de salida: el inventario completo y el censo detallado de Descarte. Se conservaron los errores y se recuperó la información con lotes/salidas acotadas, sin escrituras ni pérdida silenciosa de cobertura local. La metadata de estilos en Descarte quedó resumida a 20 IDs de 88; esto limita el análisis exhaustivo de estilos remotos, no el conteo de bindings locales.

La auditoría no inspecciona todas las aplicaciones consumidoras, no infiere unidades CSS desde FLOAT, no certifica contraste a partir de descripciones y no convierte registros legibles por ID en autoridad vigente. El manifiesto de evidencia identifica los bytes y recetas de esta entrega.

Comprobantes finales: [ejecución y límites de Fase 1](</Users/miguel.leo/Desktop/Blue Heart DS/evidence/qa/phase-1-check.json>) y [manifiesto de hashes de la entrega](</Users/miguel.leo/Desktop/Blue Heart DS/evidence/qa/evidence-manifest.json>).

La entrega termina con Foundations normalizadas guardadas en el destino Figma. Los registros no enumerados y las dependencias remotas permanecen fuera de la aplicación hasta reconciliarse. Los tokens y el contenido de componentes siguen excluidos.
