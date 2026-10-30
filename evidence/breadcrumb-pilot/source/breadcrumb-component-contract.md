# breadcrumb · observación Figma

Proyección de solo lectura del modelo [breadcrumb-component-contract.yaml](breadcrumb-component-contract.yaml). No gobierna Blue Heart; la autoridad reside en los contratos MD registrados y ADR-026.

## Cobertura

5 combinaciones; 83 nodos; 36 instancias; 14 variables efectivamente usadas; cero estilos nombrados. Recorrido completo, sin nodos pendientes. Fuente: 2425:35937 en la página 1098:28190.

## API observada

| Propiedad | Tipo | Default | Opciones |
|---|---|---|---|
| Show back#8903:1 | BOOLEAN | True |  |
| levels | VARIANT | 2 | 2, 3, 4, 5, collapsed |

## Diseño y anatomía

Back ArrowLeft16 y frame Items con instancias expuestas de breadcrumb-item. Contenedor HUG, padding0, gap8; Items gap4. Anchos de muestras 223/293/355/491/320 y alto20. Show back retira24px. Colapsado: primero, overflow y dos últimos. Una sola página actual final; cada muestra es independiente.

## Función, contenido y accesibilidad

BreadcrumbRuta de navegación que muestra dónde está el usuario dentro de la jerarquía del producto y le permite regresar a niveles anteriores (p. ej. Contabilidad › Pólizas › Diario › Póliza P-0458).


Propiedades
levels: 2 | 3 | 4 | 5 | collapsed. Número de niveles visibles; collapsed muestra el primero, "…" y los dos últimos.
Show back: flecha para regresar al nivel anterior (encendida por defecto).
Cada eslabón es una instancia de breadcrumb-item: cambia su Label y su type según el caso.


Estructura (breadcrumb-item)
type: text | icon | overflow. icon es el acceso a Inicio (casa); overflow ("…") agrupa niveles ocultos y abre un menú con ellos.
current: false | true. true es la página actual: text/brand en SemiBold, sin separador, sin cambio en hover y no clicable (aria-current="page").
state: default | hover | focus | disabled.
Label: texto del eslabón.


Tamaños
Un solo tamaño: texto de 14 px (font/size/sm, interlineado 20) e íconos de 16 px, alineado con Button medium y small.


Contenido para LATAM
Usa los nombres reales de módulos y documentos: Nómina › Periodos › Quincena 18; Facturación › CFDI emitidos › A-1024.
Sentence case, sin abreviar módulos; los folios y series se muestran tal cual (P-0458, A-1024).
Español y portugués ocupan ~30% más: con más de 5 niveles o rutas largas usa levels=collapsed.
No muestres datos personales en la ruta (CURP, NSS); para personas usa nombre o número de empleado.
En multiempresa, el primer nivel puede ser la empresa o RFC activo.


Comportamiento
El último eslabón es siempre la página actual y no es enlace.
Con más de 5 niveles colapsa los intermedios en "…"; al activarlo muestra un menú con los niveles ocultos.
La flecha de regresar lleva al nivel inmediato anterior, no al historial del navegador.
En móvil muestra solo la flecha y el nivel anterior.


Accesibilidad
Envuélvelo en un nav con aria-label="Ruta de navegación" y una lista ordenada.
Los separadores (›) son decorativos (aria-hidden).
Contraste: enlaces text/secondary 7.6:1 (hover text/primary 17.9:1), página actual text/brand 4.7–6.3:1 en los 4 modos. Los separadores (icon/tertiary) son decorativos.
Hover: cambia a text/primary y se subraya; el color no es el único indicador. La página actual no reacciona al hover.
Foco visible: anillo de 2 px color/focus/ring con 2 px de separación.


Do / Don't
✅ Úsalo a partir del segundo nivel de profundidad.
✅ El último nivel siempre es la página actual.
✅ Usa collapsed cuando la ruta no quepa en una línea.
❌ No lo uses como navegación principal ni como pasos de un asistente (usa Multi Step Indicator).
❌ No pongas la página actual como enlace.
❌ No cambies colores ni tamaños a mano.


Tokens
Texto color/text/{secondary|primary|brand|disabled} · Ícono color/icon/{secondary|primary|tertiary|disabled} · Foco color/focus/ring + stroke/md + radius/sm · Espaciado spacing/xs | sm | none · Íconos size/lg · Tipografía font/family/base Regular/SemiBold, font/size/sm, font/line-height/sm, font/letter-spacing/normal.

## Dependencias y límites

5 definiciones activas (3 locales, 2 remotas). Keys, used_by, aliases completos y detalle visual/tipográfico en YAML. La versión publicada remota no está expuesta. No hay destinos, menú, pantalla móvil ni reacciones; la función descrita requiere implementación del consumidor. No inferir URLs ni menú desde Label.

## Contradicciones registradas

La documentación usa elipsis, los nodos tres puntos; dice separador tertiary y el binding real es secondary. Home default/focus es secondary mientras el enlace es neutral strong: Blue Heart adopta paridad por BH-P06. Current tiene SemiBold literal sin binding de estilo. Back incluye un paint blanco invisible. Estas observaciones no cambian la fuente. Las decisiones de adaptación pertenecen a ADR-026 y a los contratos normativos, con evidencia de QA separada.
