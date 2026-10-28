# Tab — contrato de inspección del origen

**Evidencia Figma de solo lectura.** No gobierna la implementación de Blue Heart DS; el contrato operativo es `norms/components/tab.1.0.0.md`.

Fuente: https://www.figma.com/design/9zs5RMR8LB5wHjW9Bd59BA/Libreria-v1.1.0?node-id=1183-1146
Inspección: COMPLETE; 2026-10-28T01:15:07Z; 151/151 nodos, 48 invisibles, 0 pendientes.

## Component Identity

**Observed from Figma:** `tab` / `COMPONENT_SET` / `1183:1146`. Página `❖ Tabs`. Es una Tab individual reusable, no un Button ni el contenedor de Tabs.

## Anatomy

**Derived structure:** set → 24 variantes → Icon (oculto), Label, Badge Count (oculto), Focus ring (solo focus). Los 24 vectores se conservan como geometría referenciada de Phosphor, sin copias vectoriales.

## Dependencies

**Observed from Figma:** 48 instancias; 2 componentes únicos resueltos (ImageSquare remoto y Count medium local al origen); 97 variables usadas directa o transitivamente, todas resueltas; 1 estilo de efecto nombrado resuelto. El contador expuesto conserva Count y Max count del origen; solo Count está conectado al tipo activo.

## Properties

| Propiedad | Tipo | Predeterminado |
|---|---|---|
| Label#9058:0 | TEXT | `Tab` |
| Show icon#9058:25 | BOOLEAN | `False` |
| Icon#9058:50 | INSTANCE_SWAP | `4334:1074` |
| Show badge#9058:75 | BOOLEAN | `False` |
| type | VARIANT | `underline` |
| selected | VARIANT | `false` |
| state | VARIANT | `default` |

## Variants

**Observed from Figma:** 24 combinaciones; no eje size.

| ID | Combinación | Dimensiones observadas |
|---|---|---|
| 1183:1147 | type=underline, selected=false, state=default | 56 × 44 |
| 1183:1151 | type=underline, selected=false, state=hover | 56 × 44 |
| 1183:1159 | type=underline, selected=false, state=focus | 56 × 44 |
| 1183:1163 | type=underline, selected=false, state=disabled | 56 × 44 |
| 1183:1155 | type=underline, selected=true, state=default | 56 × 44 |
| 1334:8323 | type=underline, selected=true, state=hover | 56 × 44 |
| 1334:8329 | type=underline, selected=true, state=focus | 56 × 44 |
| 1334:8365 | type=underline, selected=true, state=disabled | 56 × 44 |
| 1308:5394 | type=pill, selected=false, state=default | 56 × 36 |
| 1308:5498 | type=pill, selected=false, state=hover | 56 × 36 |
| 1339:8387 | type=pill, selected=false, state=focus | 56 × 36 |
| 1308:5519 | type=pill, selected=false, state=disabled | 56 × 36 |
| 1339:8406 | type=pill, selected=true, state=default | 56 × 36 |
| 1334:8380 | type=pill, selected=true, state=hover | 56 × 36 |
| 1308:5512 | type=pill, selected=true, state=focus | 56 × 36 |
| 1339:8413 | type=pill, selected=true, state=disabled | 56 × 36 |
| 1308:5505 | type=segmented, selected=false, state=default | 48 × 28 |
| 9058:229 | type=segmented, selected=false, state=hover | 48 × 28 |
| 9058:234 | type=segmented, selected=false, state=focus | 48 × 28 |
| 9058:239 | type=segmented, selected=false, state=disabled | 48 × 28 |
| 9058:244 | type=segmented, selected=true, state=default | 48 × 28 |
| 9058:249 | type=segmented, selected=true, state=hover | 48 × 28 |
| 9058:254 | type=segmented, selected=true, state=focus | 48 × 28 |
| 9058:259 | type=segmented, selected=true, state=disabled | 48 × 28 |

## States

**Observed from Figma:** default, hover, focus y disabled; selected=true/false es un eje independiente.

## Layout

**Observed from Figma:** Auto Layout horizontal y ancho HUG. Alturas de ejemplo 44/36/28 px para underline/pill/segmented; padding vertical 12/8/4, horizontal 16/16/12 y gap 8. Icono 20 px; contador con mínimo 16 px. Focus ring con offset −4 y constraints STRETCH. La geometría completa está en `nodes.json` y en la proyección estructurada.

## Visual Styles

**Observed from Figma:** indicador inferior de 2 px en los estados definidos de underline; superficies de pill y segmented; anillo de foco de 2 px. Tres selected segmented activos usan elevation/shadow/sm. **Requires definition / source conflict:** el blanco descrito y los morados observados no coinciden; ADR-015 define la adaptación, sin alterar este snapshot.

## Typography

**Observed from Figma:** Manrope Regular 14/20 en no seleccionado; SemiBold 14/20 en seleccionado; Count Bold 10/16. Variables de estilo usan los strings originales; Figma expone los nombres de fuente resueltos. No hay estilos de texto nombrados en el origen inspeccionado.

## Tokens

**Observed from Figma:** 47 variables referenciadas directamente y 50 adicionales en el cierre de aliases; inventario total 97. El YAML conserva IDs, nombres, claves, colecciones, modos, valores y used_by. No son los tokens normalizados de Blue Heart DS.

## Content

**Observed from Figma:** textos de ejemplo “Tab” y “1”; Label editable. La descripción recomienda etiquetas cortas de 1–2 palabras. El texto de ejemplo no es una regla de negocio.

## Interactions

**Observed from Figma:** cuatro ON_HOVER/CHANGE_TO: underline y pill, con selected=false y true, default→hover. No se observan acciones de selección por click, gestión de grupo o paneles en este nodo. Los estados restantes existen como variantes seleccionables.

## Accessibility

**Observed from Figma:** descripción con role=tab, aria-selected, tablist y flechas; anillo visible. **Requires definition:** DOM/ARIA ejecutable, activación del grupo, paneles y nombres accesibles del contexto. No se acredita conformidad WCAG.

## External Dependencies

**Observed from Figma:** ImageSquare Outline Light remoto, key `f273018f11d7d4e938078bd0b21b0b3a9e7f2634`. La coincidencia con la biblioteca del equipo fue verificada separadamente en `phosphor.json`. Campos remotos no expuestos permanecen NOT_EXPOSED_BY_FIGMA_MCP.

## Unresolved Information

Se conserva la contradicción visual de segmented y el contraste original de pill hover como hechos del origen; ambos tienen resolución autorizada en el destino. Un hijo invisible requirió lectura por su padre y quedó recuperado. No hay nodos ni dependencias pendientes de inspección.

## Implementation Notes

Este par MD/YAML describe evidencia original, no crea componentes, código de aplicación o reglas productivas. El modelo estructurado usa el subconjunto JSON de YAML 1.2, como el snapshot anterior de Button. Las definiciones hijas son referencias, sin importar la familia Dot completa.

## Evidence / Confidence

**HIGH por cobertura**, no por certificación funcional: `inventory.json`, `nodes.json`, `variables.json`, `dependencies.json`, `phosphor.json` y `overview.png`. MD y YAML proceden del mismo modelo. Cada nodo y variable tiene selector y referencia de evidencia.
