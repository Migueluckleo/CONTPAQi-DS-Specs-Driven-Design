# breadcrumb-item · observación Figma

Proyección de solo lectura del modelo [breadcrumb-item-component-contract.yaml](breadcrumb-item-component-contract.yaml). No gobierna Blue Heart; la autoridad reside en los contratos MD registrados y ADR-026.

## Cobertura

13 combinaciones; 58 nodos; 16 instancias; 19 variables efectivamente usadas; cero estilos nombrados. Recorrido completo, sin nodos pendientes. Fuente: 2425:35897 en la página 1098:28190.

## API observada

| Propiedad | Tipo | Default | Opciones |
|---|---|---|---|
| Label#2992:0 | TEXT | Breadcrumb |  |
| type | VARIANT | text | text, icon, overflow |
| current | VARIANT | false | false, true |
| state | VARIANT | default | default, disabled, hover, focus |

## Diseño y anatomía

Label o House o Overflow, seguido de CaretRight. Solo current carece de separador. Trece combinaciones reales, sin producto cartesiano. Manrope Regular 14/20; current SemiBold. Padding0, gap4, iconos16. Anillo absoluto -4 y tamaño +8, trazo2/radio4 con STRETCH. Hover subrayado en texto/overflow. Overflow mide11×20 y contiene tres puntos.

## Función, contenido y accesibilidad

Breadcrumb itemEslabón individual del Breadcrumb. Úsalo dentro del componente breadcrumb; su documentación completa (contenido LATAM, comportamiento, accesibilidad y tokens) está en breadcrumb.


Propiedades
type: text | icon (Inicio) | overflow ("…").
current: false | true (solo en text). La página actual va en text/brand SemiBold, sin separador.
state: default | hover (text/primary y subrayado) | focus (anillo de 2 px) | disabled.
Label: texto del eslabón (solo en type=text).

## Dependencias y límites

2 definiciones activas (0 locales, 2 remotas). Keys, used_by, aliases completos y detalle visual/tipográfico en YAML. La versión publicada remota no está expuesta. No hay destinos, menú, pantalla móvil ni reacciones; la función descrita requiere implementación del consumidor. No inferir URLs ni menú desde Label.

## Contradicciones registradas

La documentación usa elipsis, los nodos tres puntos; dice separador tertiary y el binding real es secondary. Home default/focus es secondary mientras el enlace es neutral strong: Blue Heart adopta paridad por BH-P06. Current tiene SemiBold literal sin binding de estilo. Back incluye un paint blanco invisible. Estas observaciones no cambian la fuente. Las decisiones de adaptación pertenecen a ADR-026 y a los contratos normativos, con evidencia de QA separada.
