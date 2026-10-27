# Button · Contrato observacional

Fuente: https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=2433-26890

Inspección COMPLETE · 2026-10-27T01:25:31.108898+00:00 · Evidencia Figma de solo lectura. Este documento no sustituye la autoridad del MD normativo de Blue Heart.

## Component Identity

Observed from Figma: GROUP Button component, 2433:26890, página ❖ Button. La composición contiene el set button y sus etiquetas; no es por sí misma un componente reusable.

## Anatomy

Derived structure: contenedor Button, Label, iconos opcionales, Focus ring y Loader. Se recorrieron 597 nodos, incluidos 150 invisibles; vectores completos en nodes.json.

## Dependencies

Observed from Figma: 180 instancias, 13 componentes únicos (12 locales y 1 remoto), 47 variables locales y cero estilos nombrados. Todas las referencias activas se resolvieron; no se generaron contratos de dependencias.

## Properties

Observed from Figma: Label=Button; Show left/right icon=false; Left/Right icon son INSTANCE_SWAP. Cada uno ofrece 1512 candidatos de biblioteca, no inspeccionados exhaustivamente ni importados.

## Variants

Observed from Figma: type=primary|secondary|text|link|danger, size=large|medium|small; 90 combinaciones existentes, sin inferir otras.

## States

Observed from Figma: default, hover, pressed, focus, loading, disabled.

## Layout

Observed from Figma: Auto Layout horizontal, ancho HUG, alturas 48/40/32 px. Padding/gap/bindings por variante en el YAML y nodes.json. strokesIncludedInLayout=false.

## Visual Styles

Observed from Figma: pinturas, opacidades, strokes y bindings conservados por nodo. Focus ring de 2px a 2px de distancia, radio 12; radio del control 8.

## Typography

Observed from Figma: Manrope Bold salvo text=Regular, 16px large y 14px medium/small, line-height 20px; link subrayado. No hay TextStyle asignado en este subárbol.

## Tokens

Observed from Figma: 47 referencias semánticas y sus valores resueltos en Contable, conservando aliases y todos los modos en las respuestas fuente. La normalización del destino no reescribe esta evidencia.

## Content

Observed from Figma: Button es contenido de ejemplo y Label es editable. La descripción define sentence case, máximo tres palabras y restricciones de datos sensibles; no convertir ejemplos fiscales en lógica ejecutable.

## Interactions

Observed from Figma: reacciones nativas parciales hover/pressed y ciclos AFTER_TIMEOUT. La descripción declara loading/disabled/confirmación; eso no acredita implementación web ni llamadas de servicio.

## Accessibility

Requires definition: integración HTML/ARIA, área táctil y auditoría de contraste. La frase Cumple AA en la fuente es una afirmación del autor, no un resultado medido aquí.

## External Dependencies

Observed from Figma: PlusCircle remoto activo con key e identidad legibles; biblioteca/proyecto/versión externa NOT_EXPOSED_BY_FIGMA_MCP.

## Unresolved Information

Requires definition: la guía pide ancho estable durante loading pero HUG crece; medium mide 40px frente al mínimo móvil de 44px descrito. Se conservan ambas evidencias.

## Implementation Notes

Evidencia de origen de solo lectura; no prescribe rediseño ni crea código de aplicación. El contrato MD normativo del piloto adopta y delimita su implementación por separado.

## Evidence / Confidence

HIGH para la observación estructural: 597/597 nodos, 0 pendientes, 13/13 componentes y 47/47 variables resueltos. YAML y MD salen del mismo modelo.
