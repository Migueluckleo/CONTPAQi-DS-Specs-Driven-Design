# CONTPAQi · componentes web

Biblioteca local y catálogo de **43 familias del DS** para diseñar pantallas en React, TypeScript, Tailwind y Next.js con datos de muestra. La pestaña «Variantes» permite inspeccionar las recetas documentadas y la vista interactiva probar sus controles. Cada ficha tiene código copiable, API, defaults, composición, fuentes y límites. La pantalla «Documentos» permite buscar, filtrar y agregar registros en memoria.

## Ejecutar

Desde la raíz del repositorio, con Node compatible y pnpm:

```sh
pnpm --dir implementations/web install --frozen-lockfile
pnpm --dir implementations/web dev
```

Abrir http://127.0.0.1:3000. El servidor es local. Los ejemplos no requieren Figma, autenticación ni un backend de producto. Recargar restaura los datos de muestra.

Para producir un catálogo estático:

```sh
pnpm --dir implementations/web build
python3 -m http.server 8807 --bind 127.0.0.1 --directory implementations/web/out
```

Abrir http://127.0.0.1:8807. Servir `out` por HTTP; abrir index.html con file:// no resuelve las rutas de Next. No hay despliegue ni paquete npm publicado.

Versiones exactas: Next **16.4.0**, React/React DOM **19.3.0**, Tailwind **4.3.3**, TypeScript **7.0.2**. Ver [package.json](package.json) y [lockfile](pnpm-lock.yaml). Verificado con Node **24.19.0**, pnpm **11.25.0** y Chrome. El runtime del entorno Codex se registró en [environment](../../registry/environment.md); no se instala Node globalmente. El desarrollo usa las dependencias locales ya instaladas.

## Crear una pantalla

Importar [styles.css](src/styles.css) una vez en el layout raíz. Para archivos dentro de este proyecto, `@/index` es el barrel del DS, no un paquete externo:

```tsx
// src/app/layout.tsx
import '../styles.css';
```

```tsx
'use client';
import { useState } from 'react';
import { Button, InputField, InlineNotification } from '@/index';

export default function NuevaPantalla() {
  const [nombre, setNombre] = useState('');
  const [mensaje, setMensaje] = useState('');
  return (
    <section data-ds-theme="contable" className="grid gap-6 p-8">
      <InputField label="Nombre" value={nombre}
        onChange={event => setNombre(event.target.value)} />
      <Button disabled={!nombre.trim()}
        onClick={() => setMensaje(`Vista previa: ${nombre}`)}>
        Probar acción
      </Button>
      {mensaje && <InlineNotification tone="info" title="Muestra local">
        {mensaje}
      </InlineNotification>}
    </section>
  );
}
```

Cada [ficha de componente](docs/components/README.md) incluye un ejemplo que se compila en el catálogo. Las props controladas y callbacks permiten conectar datos después. No hay reglas fiscales, permisos, guardado, subida remota ni respuestas de IA simuladas.

Para consumir en otro Next.js, copiar `src/components`, `src/lib`, `src/generated`, `src/index.ts` y `src/styles.css` conservando sus relaciones; copiar `public/assets` al public de destino. Usar las dependencias runtime y la integración Tailwind/PostCSS de este proyecto; adaptar el alias a la ubicación elegida. No copiar app, ejemplos o catálogo si solo se necesitan los componentes. Si el código queda fuera del árbol que Tailwind escanea, incluir esa ruta mediante `@source` en el CSS del consumidor. Las rutas de assets actuales parten de `/assets`; adaptar explícitamente al usar basePath o CDN.

Los Server Components pueden suministrar datos serializables. Estado, eventos y callbacks pertenecen a Client Components. Los módulos interactivos incluyen `'use client'`; la ficha recuerda la frontera. `data-ds-theme` admite contable, administrativo, servicios y personas. No modifica los colores propios de personajes/logos.

La tipografía compartida se deriva del [catálogo 0.1.2](../../specs/tokens/ai-design-system.typography.v0.1.2.json): 79 estilos, 18 base y 61 complementarios. [TYPOGRAPHY.md](docs/TYPOGRAPHY.md) conserva la receta y descripción canónicas. Los cuatro estilos terminados en `-underline` expresan el subrayado existente de Button Link, File Upload y los enlaces de Empty states; no cambian métricas ni bindings. `typographyClass(id)` aplica también `text-decoration-line`, y `--ds-type-style-id` identifica la receta inspeccionable. Las tres recetas materializadas conservan sus métricas CSS sin una segunda escala. La [enmienda de herencia nativa](../../specs/TYPOGRAPHY-NATIVE-INHERITANCE.amendment.v0.1.2.md) regula por separado el vínculo verificable de sus 103 consumidores Figma; la conformidad web no sustituye esa evidencia.

## Mantener y agregar componentes

El [P07](../../protocols/07-WEB-COMPONENTS-AND-TECHNICAL-DOCUMENTATION.md) exige código, tipos, documento, ejemplo y QA en toda alta o modificación. No agrega aprobación visual implícita.

1. Registrar el contrato vigente y sus enmiendas por el flujo documental existente.
2. Implementar el export y tipos en src/components y exponerlo en src/index.ts.
3. Agregar su ejemplo identificado en src/examples.tsx y sus variantes de referencia en src/variants.tsx y su entrada/fuentes/Slots/notas en [components.registry.json](components.registry.json).
4. Ejecutar `pnpm ds:generate` dentro de esta carpeta. Las 43 fichas, tokens y metadatos son derivados; no se editan a mano.
5. Ejecutar `pnpm verify` y `pnpm test:browser`; registrar alcance y diferencias.
6. Aplicar [P08](../../protocols/08-SKILLS-AND-RELEASES.md): sincronizar, comprobar y exportar las dos skills desde la raíz con `scripts/ds skills sync`, `scripts/ds skills check` y `scripts/ds skills export`. Actualizar las copias locales gestionadas autorizadas, registrar el release y cerrar el grafo con P05. El cierre completo falla si las skills quedaron desactualizadas.

El generador consulta la vista actual de contratos mediante scripts/ds, compara cobertura y hashes y falla si una familia activa carece de mapeo, export o ejemplo, o si una ficha cambió sin regenerarse. No considera completo un componente solo porque exista un archivo. Requiere los runtimes documentales existentes del repositorio para regenerar; el código generado puede consumirse sin ellos.

```sh
pnpm ds:generate
pnpm ds:check
pnpm verify
pnpm test:browser
```

Los tests de navegador usan Chrome instalado (`PLAYWRIGHT_CHANNEL` permite otro canal disponible) y sirven el build en 127.0.0.1:8807. Ejecutar build antes de probar. No descargan un navegador automáticamente. [QA y evidencia](../../qa/implementations/web.fidelity.v0.1.2.review.md).

## Alcance real

Las 43 familias tienen código y documentación inicial. [Adaptación web](docs/WEB-ADAPTATION.md) describe diferencias de HTML, unidades y comportamiento. Compilación e interacciones verificadas no certifican cada combinación de variantes ni igualdad pixel a pixel con Figma.

Logos dispone de **72/72 assets locales**, con IDs, formatos y hashes en [el manifiesto](../../sources/assets/web/logos.manifest.json). El componente acepta un archivo local mediante src; no sustituye silenciosamente un logo ausente. Las excepciones de color, geometría o auditoría pendientes en contratos continúan vigentes. No se declara conformidad WCAG integral.

## Cambios de API del barrido 0.1.2

Sidebar expone MenuItem y TopBar; sus tipos impiden combinaciones inexistentes. Table expone sus piezas para composición. Scrollbar representa los ocho presets visuales; el contenedor con desplazamiento nativo se consume como ScrollArea. ConversationGlyph conserva el dibujo específico de 32px. Button vuelve a los dos iconos visibles del maestro; las pantallas pueden ocultarlos explícitamente. Checkbox/Radio/Toggle y Avatar conservan los defaults visuales documentados: el consumidor debe controlar la selección y el significado real del estado. No se migran automáticamente pantallas externas.
