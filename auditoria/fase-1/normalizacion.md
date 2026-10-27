# Normalización de variables

> Corte histórico de Foundations, anterior al piloto Button. El estado vigente y su ampliación autorizada están en [la guía de consumo Button](../../consumption/button/README.md) y ADR-006. Las cantidades y restricciones de este corte no describen el piloto posterior.

Criterio vigente del responsable, registrado en ADR-003. Se aplica al catálogo local y a las variables ya guardadas en el archivo Figma destino, con autorización ADR-004 y relectura verificada.

## Regla de colores

**Una primitiva referenciada tiene un único semántico de color. Cada semántico apunta directamente a una sola primitiva, con alias fijo y `scopes: []`.**

No se crean dos semánticos para la misma primitiva por diferencias de uso, intención, componente, estado o tema. La comprobación utiliza el ID de la primitiva, no solo su hexadecimal: dos primitivas distintas no se fusionan por coincidir en RGB.

```text
Primitivo: blue-200 = #BFCEFE
Semántico: brand-accent → blue-200
Scopes del semántico: []

--color-button-primary-bg-hover → brand-accent
--color-input-primary-stroke-default → brand-accent
```

Los tokens consumidores separarán componente, variante, propiedad y estado. Sus nombres siguen `--color-{componente}-{variante}-{propiedad}-{estado}`. Los dos tokens mostrados son ejemplos del responsable, no variables de componente ya creadas.

El semántico no tiene scope de Frame, Shape, Fill, Stroke, Border, Text, ni otra propiedad. Tampoco se asigna `ALL_SCOPES`: la lista queda vacía. Los nombres semánticos no incorporan la propiedad consumidora ni su estado.

## Dos tablas, una función por tabla

- [Catálogo de semánticos de color](semanticos-color.csv): **42 entradas**, una por cada primitiva de color actualmente referenciada por aliases del inventario principal. Cada fila declara nombre, primitiva, ID de origen y `scopes: []`. No hay primitivas repetidas ni nombres duplicados.
- [Correspondencia completa](variables-normalizadas.csv): **291 filas**, una por variable original. Incluye las 145 primitivas, las 145 variables con aliases y el STRING literal de configuración `logo/categoria`, cuya clasificación sigue pendiente. En filas de color semántico, las columnas de tema seleccionan nombres del catálogo único; esas filas no son nuevas variables semánticas.

Los 81 colores primitivos se conservan. De ellos, 42 tienen referencias semánticas observadas y 39 permanecen como primitivas disponibles; no se añaden aliases sin una referencia que normalizar. La regla de unicidad aquí definida se refiere a colores, no a magnitudes de dominios distintos.

## Temas sin duplicar semánticos

El alias de cada semántico del catálogo es fijo. La selección por producto se documenta en la correspondencia y se aplicará en los tokens consumidores cuando se implementen. Así se conservan los colores de origen sin mantener varios semánticos que coincidan parcialmente por tema.

| Variable de origen | Contable | Administrativo | Servicios | Personas |
|---|---|---|---|---|
| `color/brand/accent` | `brand-accent` | `brand-administrativo-accent` | `brand-servicios-accent` | `brand-personas-accent` |

Esos cuatro nombres apuntan respectivamente a `blue-200`, `green-200`, `orange-200` y `purple-200`. El identificador de producto distingue paletas; no asigna un scope de aplicación.

Si varios nombres originales usan `blue-500`, todos seleccionan el mismo semántico `brand-strong`. Una diferencia observada entre `orange-600` y `orange-700` conserva dos primitivas distintas y, por tanto, dos semánticos distintos. No se cambian valores para forzar una fusión.

En el CSV de correspondencia, `nombre_normalizado` queda vacío cuando un registro de color selecciona semánticos distintos según tema; las cuatro columnas de tema contienen el resultado completo. Para primitivas y aliases no cromáticos, los nombres usan minúsculas y guiones. Los valores, tipos y aliases originales se conservan; se señalan las tres descripciones numéricas que no coinciden con su valor real.

## Evidencia y cobertura

El inventario original conserva sus nombres, scopes y valores tal como fueron leídos: documenta el origen y no prescribe el destino. Sus scopes no se copian a los semánticos normalizados.

Las [441 referencias adicionales](../../evidence/foundations/referenced-inventory.json), 333 locales no enumeradas y 108 remotas, permanecen separadas. No se presentan como variables propias activas confirmadas. Hay además 29 destinos de alias no leídos. Se requiere reconciliar esos registros antes de incorporarlos al catálogo; no se declara una normalización completa de bibliotecas externas.

La verificación comprueba unicidad de nombre y primitiva, scopes vacíos, cobertura de los 291 IDs y preservación exacta de cada destino primitivo en los cuatro temas. El resultado está en [normalization-check.json](../../evidence/qa/normalization-check.json).

## Aplicación en Figma

Las variables viven en [Blue Heart DS](https://www.figma.com/design/98xEw6sK8FRVNEhopM5SSz/Blue-Heart-DS?node-id=0-1):

| Colección | ID en destino | Variables | Modo |
|---|---|---:|---|
| `primitive` | `VariableCollectionId:6:2` | 145 | Value |
| `semantic` | `VariableCollectionId:6:148` | 106: 42 de color y 64 no cromáticas | Value |

Todas las variables tienen `scopes: []`. Las primitivas conservan los valores originales con su precisión; los 106 semánticos son aliases directos a primitivas del destino. No se creó `logo/categoria`, porque es configuración literal y no un alias semántico. No hay colecciones ni tokens de componente, nodos nuevos ni estilos nuevos.

La metadata WEB utiliza `var(--primitive-{nombre})` para primitivas y `var(--{nombre})` para semánticos. Distingue nombres que coinciden entre capas, como `font-weight-regular`; no genera CSS ni tokens de componente.

La [comprobación de aplicación](../../evidence/qa/figma-application-check.json) acredita una relectura de las 251 variables sin diferencias de valores, tipos, aliases, scopes o sintaxis. La [correspondencia de IDs](../../evidence/figma-application/application-map.json) conserva IDs/key nuevos y sus IDs originales.

El proyecto original y el archivo Figma origen permanecen en solo lectura. El catálogo normativo local sigue vacío; las variables aplicadas en Figma están documentadas por el plan y su relectura. No se crearon contratos ni implementaciones de componentes.
