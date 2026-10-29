# Auditoría de color de iconos · ADR-024

La auditoría se realizó exclusivamente en Blue Heart DS, con su [autorización](../../evidence/authorization/icon-color-alignment-request.txt). No se consultó el Figma origen ni se modificó el proyecto anterior.

El [comprobante](../qa/icon-color-audit-check.json) es el propietario de resultados y límites. La regla operativa pertenece a [BH-P06](../../protocols/06-PHOSPHOR-ICONS.md#req-p06-03); los contratos de Button, Tab, Tabs e Input definen qué texto corresponde a cada icono. Los snapshots before/after son evidencia, no reglas.

Se observaron 262 pares en principales y 131 divergencias de vector cromático por tema. Se corrigieron aliases y bindings de Button, Tab e Input y 15 overrides en instancias existentes. Avatar ya coincidía con Initials; Dot, Loader y el subconjunto Badge no contienen iconos Phosphor. Loader mantiene su contrato específico de indicador de progreso.

Se probaron 624 combinaciones de variante/tema, 1032 comparaciones de icono/texto y 148 swaps con verificación de key remota, tamaño y bindings. Los 60 casos vacíos de Button son loading sin Phosphor, no omisiones de QA. Se conservaron los 159 principales afectados, su geometría, tipografía, propiedades e interacciones.

El [mapa](migration-map.json) y el [plan derivado](pairing-plan.json) registran dos firmas nuevas de Tab y la reutilización del ID/key Figma anterior de tooltip bajo input/color/icon/secondary. La retirada de la API lógica/CSS anterior exige Input 2.0.0 y BLUEHEART-TOKENS 6.0.0; no se borraron variables nativas. Tab/Tabs 3.1.0 incorporan cobertura compatible y Button 4.0.1 corrige la implementación sin cambiar su API. Las Foundations no cambiaron.

Los textos y fondos se conservaron: segmented sigue teniendo las limitaciones de contraste ya autorizadas (4.39:1 default, 2.26:1 hover); igualar sus iconos no certifica AA. No se implementó React ni se atribuye revisión independiente.

Las recetas actuales aplican esta proyección sobre la evidencia histórica sin reescribirla. Los contratos y catálogos anteriores se conservan bajo history/ y por Git. La bitácora nativa diferencia creación de variables de su inventario final.

La proyección tab/current-build-plan conservaba un espejo anterior a la sustitución de su Badge privado. Se sincronizó con la receta vigente y Dot, retirando de ese espejo los seis tokens y 48 nodos privados ya sustituidos; esto no reconstruye ni retira objetos Figma. `python3 -B consumption/tab/materialize-plan.py` reproduce también los CSV actuales desde los propietarios y la correspondencia nativa conservada.
