# P08. Skills de consumo y releases

Por [DEC-AI-TECHNICAL-CLOSURE-001](../registry/DEC-AI-TECHNICAL-CLOSURE-001.md), la revisión humana es opcional y no bloquea el cierre de las skills. El agente conserva evidencia de integridad, vigencia y pruebas aplicables; los errores técnicos sí bloquean. El canal remoto de Evolution Lab se define en la sección 6 y sustituye la distribución con specs fijos para los nuevos motores.

**Versión:** 0.1.1 · **Decisión:** [DEC-DS-SKILLS-001](../registry/DEC-DS-SKILLS-001.md).

## 1. Alcance y disparador

Las dos skills son un entregable obligatorio del DS: [contpaqi-figma-screens](../skills/contpaqi-figma-screens/SKILL.md) y [contpaqi-po-prototypes](../skills/contpaqi-po-prototypes/SKILL.md). Leer AGENTS, P05, P06 y P07 según la parte modificada.

Aplicar este cierre después de un alta, cambio o retiro de componente, contrato, enmienda, token, asset o documentación/código de consumo. Primero completar los controles documentales y de implementación aplicables; después generar ambas skills desde el mismo corte. Publicar documentación y publicar una biblioteca Figma siguen siendo operaciones distintas: la actualización de estos paquetes no espera una publicación remota ni la simula.

La norma reside en los contratos y datos canónicos, no en la skill, el índice generado, un screenshot ni una copia Figma observada. Conservar estados documentales y límites; empaquetar un DRAFT como evidencia no lo hace elegible para gobernar un componente.

## 2. Fuente única y salidas

Las instrucciones, referencias y scripts editables viven en `skills/<nombre>/`. La selección de fuentes y el empaquetado se gobiernan por `config/ds-skills.json` y `scripts/ds_skills.py`. Los snapshots generados no se editan.

Cada versión común produce dos carpetas de skill, sus ZIP y manifiestos bajo `output/skills/`. Cada skill incluye:

- `SKILL.md` y metadatos de invocación, scripts y referencias necesarios.
- Snapshot con bytes originales de contratos, enmiendas, datos, assets y código requeridos, sin cachés, secretos, node_modules, builds ni grafo duplicado.
- `assets/snapshot-manifest.json`: rutas y SHA-256, digest común del DS y cobertura por familia.
- `assets/release.json`: versión, identidad y skill compañera. El índice de componentes es derivado, con fuentes y versiones; no inventa IDs Figma.

Las dos skills deben compartir versión y digest del DS. Los paquetes históricos se conservan; una modificación efectiva produce otra versión. Una ejecución sin cambios no genera una versión nueva ni fechas artificiales. El incremento de versión del paquete no cambia la versión o aprobación de sus contratos.

## 3. Cierre de un alta o modificación

1. Completar contrato/enmiendas, dependencias, código, ficha, ejemplo y QA aplicables de la familia conforme P03/P06/P07. Actualizar el registro web y los derivados documentales.
2. Ejecutar `scripts/ds skills sync`. El generador toma el corte actual de las fuentes y las dos plantillas. No actualizar solo una skill ni copiar archivos a mano dentro del paquete.
3. Ejecutar `scripts/ds skills check` y `scripts/ds skills export`. Verificar contenido, hashes, cobertura y reproducibilidad. Usar el incremento de versión explícito cuando corresponda; nunca reutilizar una versión histórica con bytes diferentes.
4. Actualizar las copias locales gestionadas con `scripts/ds skills install` cuando ese destino esté autorizado, como en esta decisión. Si hay cambios ajenos en una copia instalada, conservarlos y registrar el bloqueo de esa instalación; no sobrescribirlos silenciosamente. Los paquetes portables siguen disponibles para distribución manual. No afirmar que otras máquinas se actualizan solas.
5. Registrar versión, digest, paquetes, comandos, pruebas, instalación y límites en `registry/skills.md` y `qa/skills/`. Estos registros se excluyen del snapshot para evitar autorreferencia, pero permanecen en Graphify.
6. Actualizar la vista derivada y cerrar Graphify por P05. `scripts/ds check` incluye el gate de skills además de documentación, vista y grafo. `--docs-only` sirve durante preparación y no acredita el cierre completo.

Si falla el empaquetado, conservar la última versión verificable y registrar `STALE` o `BLOCKED`. No declarar terminada el alta con las skills pendientes. Este flujo no instala hooks, monitores ni servidores y no hace publicaciones externas.

## 4. Contrato entre las dos skills

La skill de Figma consume prompts, imágenes como referencias de composición y el traspaso de la skill de PO. Las referencias no autorizan a cambiar anatomía, tokens o variantes del DS. Buscar primero una solución existente; un componente local requiere fuentes, rol, composición y decisiones locales explícitas. No crear tokens ni aproximar logos/personajes para rellenar una ausencia.

La skill de PO reutiliza la biblioteca React documentada y compone faltantes localmente. Su HTML se abre sin servidor; compilarlo sí requiere herramientas de desarrollo. Mantener assets, fuentes y recursos de estados posteriores dentro del archivo final, y probarlo por `file://` aislado y sin red. No introducir APIs ni respuestas remotas simuladas.

El traspaso identifica versión/digest, contratos y hashes consumidos, tema, viewports, pantallas/estados, componentes por instancia, props/variantes, textos, Slots, tokens, decisiones locales y transiciones. Las medidas y capturas deben corresponder al HTML final, con su hash. El Markdown invoca `$contpaqi-figma-screens`; generarlo no ejecuta Figma.

La skill de Figma verifica esas fuentes y el destino real; conserva componentes e instancias editables, Auto Layout, textos, bindings y comportamiento de prototipo. Un componente existente inaccesible no equivale a uno inexistente. Un conflicto de versión o de diseño detiene solo la parte afectada. Comparar el resultado con las referencias del mismo viewport y estado; registrar diferencias sin inventar tolerancias ni prometer igualdad universal de rasterizado.

## 5. Verificación proporcional

Comprobar el generador con cambios, altas, bajas, datos alterados, rutas inválidas, ejecución sin cambios y protección de instalaciones editadas. Verificar los ZIP y que ambas skills resuelvan el mismo corpus. Validar sintaxis de las skills y probar decisiones relevantes con un evaluador independiente cuando cambie su flujo.

Si cambia el starter o empaquetador web, probar build, apertura del HTML movido y renombrado, red bloqueada, interacción y assets de estados posteriores; cotejar el Markdown con medidas y estado realmente capturados. Un build no sustituye esta prueba. La prueba del paquete Figma puede ser de instrucciones e integridad; reportar separadamente que no se construyó una pantalla si no se ejecutó Figma.

Los paquetes e informes son outputs del cierre; las reglas de diseño siguen en sus fuentes canónicas. Una pantalla producida con cualquiera de las skills conserva su propia procedencia y QA.

## 6. Canal GitHub y motor independiente

Por solicitud del usuario, las skills consultan GitHub en cada nuevo trabajo. `delivery: github-live-v1` separa los motores instalados de las fuentes del DS. Los paquetes nuevos contienen instrucciones, scripts y starter; no contienen `assets/design-system/`, el índice de componentes ni un snapshot normativo fijo. Las secciones anteriores sobre snapshots describen los paquetes históricos y la copia verificada de trabajo que ahora se descarga.

Después de cambios de fuentes y QA aplicable, ejecutar `python3 scripts/ds_remote.py` y `python3 scripts/ds_remote.py --check`. Esto genera `catalog/current.json`, un manifiesto inmutable y un archivo comprimido de datos por identidad bajo `catalog/releases/`. No son instaladores de skills. Conservar publicaciones anteriores para tareas ya iniciadas. El workflow `.github/workflows/publish-catalog.yml` ejecuta el generador y sus pruebas tras pushes autorizados a main; publica el canal solo si esas comprobaciones pasan. El control documental del catálogo no sustituye el QA de implementación de cada componente.

El puntero representa la última publicación validada. Mientras una automatización esté pendiente o fallida no se debe afirmar que el nuevo commit ya se consume. No se necesita reinstalar la skill por cambios compatibles de contenido. `scripts/ds skills sync/check/export/install` sigue gestionando motores, pero su fingerprint excluye el contenido DS; versiones y paquetes del motor cambian con sus instrucciones o herramientas. El gate de skills también comprueba la vigencia del catálogo. Generar el catálogo antes del cierre de skills.

En cada encargo, `resolve_ds.py` obtiene el puntero público sin autenticación, comprueba protocolo y hashes, reutiliza caché válida y prepara una carpeta de ejecución nueva. Fija esa identidad durante el encargo. El siguiente vuelve a consultar el canal. No usa silenciosamente datos antiguos si no hay red. Registra motor, identidad de datos y fuentes usadas. Los paquetes ZIP permanecen locales por solicitud del usuario; publicar el catálogo no los publica.

## Índice de consumo Graph-First · 2026-10-23

El índice reducido se prepara localmente después del cierre P05 CURRENT mediante `scripts/ds_consumption.py --prepare`, usando el intérprete configurado para Graphify. `scripts/ds_consumption.py` sin argumentos valida la preparación sin ejecutar extracción. Luego `scripts/ds_remote.py` ensambla catálogo e índice como una unidad y `--check` verifica su vigencia. GitHub Actions ejecuta únicamente pruebas, validación y publicación; no crea conocimiento semántico ni repara un índice STALE. Si falta preparación o difieren fuentes/herramientas, conserva el puntero anterior.

Una sola fuente `scripts/consumer_graph.py` se distribuye por el empaquetador en ambos motores. La versión del índice es independiente del protocolo compatible del catálogo. El grafo sigue siendo derivado; cada resultado remite al snapshot y documentos originales. Fallback registrado sobre fuentes verificadas; conflictos y límites nunca producen éxito parcial. Los comprobantes preparados viven en `catalog/prepared/`, excluidos del corpus Graphify como los demás derivados del catálogo.

El workflow usa `scripts/ds_consumption.py --publication-check`: una `publication_policy` explícita que comience por `HOLD` bloquea la publicación remota aunque el corte local sea íntegro. Esta comprobación no concede revisión humana ni cambia la política del documento. Preparar datos locales y autorizar publicación remota son estados separados.

## Cierre coordinado e incremental · 2026-10-23

Por [DEC-EFFICIENT-CLOSURE-001](../registry/DEC-EFFICIENT-CLOSURE-001.md), usar scripts/ds close --run ID según la [guía](../references/EFFICIENT-CLOSURE.md). El comando coordina escritores, comparte comprobaciones del mismo corte y genera catálogo y ZIP con integridad final. Sustituye la ejecución redundante de subcomandos equivalentes; conserva todos los criterios de QA. Los comandos individuales siguen disponibles. Los estados BUSY/WAITING_FOR_SEMANTICS requieren reutilizar al propietario, no otro rebuild; NEEDS_SEMANTICS conserva la extracción semántica del delta según la skill. Registrar métricas reales y límites de atribución. No concede publicación remota.
