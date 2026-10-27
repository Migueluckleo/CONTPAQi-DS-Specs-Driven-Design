# Consolidación de variables Button

La revisión inicial creó una variable por tipo, parte y estado aunque varios consumidores usaban el mismo alias. Esa independencia de edición no estaba requerida y multiplicó los tokens.

| Variables de componente | Antes | Ahora |
|---|---:|---:|
| Color | 88 | 26 |
| Métricas y tipografía | 37 | 21 |
| **Total** | **125** | **47** |

Se retiraron 78 variables: **62.4 % menos**. Las 251 primitivas y semánticos permanecen intactas. Hay 298 variables totales en el archivo.

El mínimo de 47 conserva un scope por propiedad y los cuatro mapas originales: es el número de firmas distintas de tipo, scope y aliases semánticos por tema. No se fusionó por RGB, se ampliaron scopes ni se añadieron modos para desplazar la complejidad.

Por ejemplo, diez variables de texto blanco de primary y danger se convierten en `color-button-text-inverse`. El ancho del loader y el del icono comparten los tres tokens de tamaño de contenido. Default, focus y loading pueden seleccionar el mismo fondo desde la receta. Texto e icono de marca siguen separados: en Servicios sus aliases difieren.

La API de tokens cambia en la revisión **2.0.0**; las 90 variantes y la API de propiedades Button se conservan. El [mapa CSV](variable-map.csv) registra los 125 nombres anteriores, su reemplazo y los IDs conservados. Las recetas del [contrato vigente](../../norms/components/button.2.0.0.md) son la correspondencia consumible, sin variables duplicadas por cada estado.

QA: 2,700 referencias de binding comparadas antes/después, 90 variantes contra origen, cuatro temas, 94 instancias consumidoras, cero referencias retiradas y 44 pruebas aprobadas. [Comprobante](../qa/button-reduction-check.json).
