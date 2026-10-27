# P07. Componentes web y documentación técnica

Por [DEC-AI-TECHNICAL-CLOSURE-001](../registry/DEC-AI-TECHNICAL-CLOSURE-001.md), el agente documenta y verifica el trabajo web solicitado sin esperar revisión humana rutinaria. Los tests, build y QA pertinentes permiten cierre técnico cuando cumplen los criterios; los defectos informados posteriormente se registran, corrigen y revalidan en su alcance.

**Versión:** 0.3.3 · **Destino:** React + TypeScript + Tailwind CSS + Next.js.

## 1. Alcance autorizado

La solicitud [DEC-WEB-COMPONENTS-001](../registry/decisions.md) activa una biblioteca de código y documentación para diseñar pantallas sin depender de Figma ni de un backend. Sustituye la previsión React/TypeScript/Vite exclusivamente para esta capa. Lee AGENTS, P03, P05, P06 y P-SLOTS según el trabajo concreto.

Cada componente nuevo del DS debe contar con su implementación web y documentación técnica. Una ampliación de un componente existente debe actualizar el mismo entregable. No basta una imagen, un snippet sin dependencias ni una ficha vacía. Esta obligación no autoriza cambios de diseño, backend, publicación o instalaciones globales.

## 2. Fuentes y alcance por componente

Identificar contrato base, enmiendas aplicables, datos canónicos y dependencias por identidad y hash. Usar contratos vigentes para reglas visuales; el JSON referenciado gobierna los tokens. Conservar las excepciones de personajes y logos. Figma puede aportar evidencia adicional, pero no es requisito para ejecutar o consumir el código.

Para tipografía aplicar [FOUNDATIONS-TYPOGRAPHY-001](../specs/foundations/typography.contract.v0.1.0.md), su [enmienda de formato 0.1.1](../specs/foundations/typography.formatting.amendment.v0.1.1.md), la [enmienda nativa 0.1.2](../specs/TYPOGRAPHY-NATIVE-INHERITANCE.amendment.v0.1.2.md) y [DEC-TYPOGRAPHY-STYLES-001](../registry/DEC-TYPOGRAPHY-STYLES-001.md). El [catálogo JSON activo0.1.2](../specs/tokens/ai-design-system.typography.v0.1.2.json) es la fuente editable de estilos, propiedades, unidades, decoración y única `description` de uso. La [matriz normativa de 43 familias](../specs/TYPOGRAPHY-CONSUMPTION.amendment.v0.1.0.md) enlaza la enmienda de cada Spec con texto/rol/variante, ID lógico y TextStyle ID real; consumir esa asignación junto con la base y las otras enmiendas aplicables. No cambiar el inventario histórico para acomodar una receta ni duplicar un catálogo tipográfico en CSS, fichas o código.

Los contratos que anteriormente excluían web conservan ese alcance histórico: esta implementación es un destino nuevo autorizado, no una afirmación de validación web retrospectiva. Los estados de aprobación, auditoría humana, QA Figma y QA web se registran por separado. Las diferencias pendientes de las fuentes no se convierten en decisiones aprobadas al generar código.

Resolver como decisiones técnicas explícitas el nombre de export, props, traducción de unidades CSS, HTML y eventos necesarios para la demostración. Si existe una ambigüedad material de diseño o negocio, documentarla y limitar únicamente la parte afectada; no inventar intención, assets, estados visuales o servicios.

## 3. Entregable mínimo por familia

- Export React reutilizable y props TypeScript, con variantes y tamaños sustentados en el contrato.
- Tokens consumidos mediante variables CSS derivadas de las fuentes canónicas; Tailwind para composición y estilos. Conservar aliases y nombres lógicos; los CSS generados no se editan como otro inventario.
- Textos y rangos vinculados a los estilos compartidos de su enmienda por ID lógico, con propiedades CSS derivadas del catálogo y unidades explícitas. Para texto local nuevo seleccionar un estilo base por función; conservar los complementarios restringidos de los componentes existentes. No forzar toda receta compacta a la base ni sustituir porcentajes por px. Generar `text-decoration-line` desde `textDecoration`: un enlace con estilo de formato debe declarar ese ID, no el ID sin subrayado más un override. Documentar mapeo, dependencias y exclusiones justificadas, preservando el inventario histórico.
- Documento técnico con importación, props/tipos/defaults, variantes, contenido/Slots, comportamiento local, eventos, dependencias, tokens, restricciones y fuentes exactas.
- Ejemplo ejecutable y copiable con datos ficticios identificables, sin autenticación, API ni credenciales. Al retirar el ejemplo, el componente sigue siendo reutilizable.
- Evidencia de verificación por alcance. El build acredita compilación; no acredita por sí solo fidelidad visual, todas las variantes ni accesibilidad integral.

La implementación inicial y el catálogo viven en implementations/web. Su README explica ejecución, consumo y comandos reales. Cada familia debe tener una entrada de catálogo, documento y export trazables; el control de cobertura falla cuando falta alguno. Los componentes internos también se documentan cuando el contrato los hace consumibles.

## 4. Composición y funcionamiento sin backend

Revisar P-SLOTS por familia. En React, identificar explícitamente el equivalente web: children, props ReactNode o colecciones tipadas con identidad estable. Probar inserción, retirada y reordenación donde proceda; la cantidad del ejemplo no es un límite de producto. No presentar ese mecanismo React como un Slot nativo Figma.

Separar presentación, estado local de demostración y reglas del producto. Preferir props controladas y callbacks para que una pantalla conecte sus datos después. Acciones de archivos, selección, navegación, formularios o mensajes no deben fingir una operación remota exitosa. No incluir backend, persistencia o lógica de negocio no solicitada.

Los controles usan HTML y semántica de navegador apropiados. Documentar y comprobar nombres accesibles, foco, teclado, disabled y mensajes cuando sean aplicables. Las limitaciones cromáticas registradas se conservan: no recolorear el DS para hacer pasar una prueba.

## 5. Next.js y dependencias

Usar Next.js con React, TypeScript y Tailwind; fijar versiones compatibles en package.json y lockfile. Instalar dependencias dentro del proyecto autorizado. Usar Client Components donde hay estado/eventos del navegador y mantener claras sus fronteras. El catálogo puede exportarse estáticamente y servirse localmente; no requiere backend de producto.

Documentar fuentes, iconos y assets disponibles con su procedencia. Preservar geometría y colores autorizados. Un asset ausente es un límite real: no reemplazarlo silenciosamente por otro dibujo ni declararlo idéntico.

## 6. Verificación y alta de componentes

Antes de cerrar un alta o modificación:

1. Comprobar correspondencia del export, tipos, defaults, booleanas de visibilidad, swaps, documentación y ejemplo con el contrato y enmiendas citados. Mantener una matriz por familia; no sustituir un default del maestro por una preferencia de ejemplo.
2. Regenerar tokens, estilos tipográficos y metadatos; verificar hashes y cobertura sin alterar fuentes canónicas. Cada texto/rango modificado debe resolver al estilo documentado, incluidas variantes y estados pertinentes; clases o IDs sin propiedades resueltas concordantes no prueban conformidad. Comprobar métricas, decoración y overrides, preservando contenido, color y excepciones ajenas al cambio. Un `derivedFormattingFrom` conserva la receta y cambia solo el formato declarado; `derivedFrom` conserva las métricas materializadas sin multiplicar otra vez la escala. El QA web no acredita el vínculo Figma: para la excepción nativa0.1.2 conservar el ID lógico materializado y distinguir el estilo principal/cadena/escala de su implementación. Incluir enmienda y evidencia del overlay cuando la familia lo consuma; no aplicar otra transformación CSS ni aceptar un ID vacío por apariencia. Registrar el alcance y QA de cada destino por separado.
3. Ejecutar typecheck y build; probar la interacción modificada y sus composiciones dependientes.
4. Incluir las recetas documentadas en la galería de variantes y revisar en navegador geometría, tipografía, iconos, roles, estados y visibilidad afectados. Cuando hay medidas explícitas, contrastar cajas y posiciones con la fuente, además de inspeccionar el resultado visual. Probar contenido largo, Slots, tema y límites de ancho aplicables. Registrar cobertura concreta; una galería sin errores no demuestra por sí sola igualdad visual. No atribuir soporte responsive no probado.
5. Registrar resultado real, comandos, alcance visual/funcional, excepciones y límites en QA/implementaciones según P05. Un bloqueo de una familia no se oculta bajo el PASS general del catálogo.
6. Actualizar catálogo y documentación de la misma familia, incluido el mapeo de estilos tipográficos y cualquier complementario nuevo justificado. Registrar fuentes, cambios y QA según P05. Aplicar [P08](08-SKILLS-AND-RELEASES.md): regenerar ambas skills con el catálogo tipográfico y sus consumidores, verificar el mismo corte de fuentes y producir sus paquetes versionados. Si se usan copias locales gestionadas, actualizarlas y comprobarlas según P08. Un alta no queda cerrada con skills desactualizadas.
7. Cerrar Graphify por P05 sobre las fuentes relevantes, incluidos protocolos, generadores y QA de las skills; excluir node_modules, builds, cachés y copias empaquetadas redundantes.

El componente no se declara listo para consumo web si carece de código, documentación, ejemplo o comprobaciones aplicables. Eso no invalida automáticamente su implementación Figma histórica. Un requisito que no corresponde al componente se justifica como NOT_APPLICABLE; no se crea trabajo adicional sin evidencia.

El catálogo Next.js y el prototipo portable son entregables distintos. La skill para PO compila una aplicación Next.js a un HTML autónomo: el destinatario abre ese archivo sin servidor. La compilación requiere herramientas de desarrollo; el resultado no debe depender de ellas. Verificar `file://`, recursos de estados posteriores e interacción sin red antes de declarar esa portabilidad.
