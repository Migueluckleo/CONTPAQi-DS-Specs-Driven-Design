# Pase y cierre del encargo Avatar

Operación CREATE de la página fuente `1132:8891`: Avatar individual, Avatar group, presencia privada y documentación editable. Destinos autorizados: documentación y Figma Blue Heart DS. ADR-019 registra el encargo y la elección del responsable ante las contradicciones fuente. Los originales permanecen en solo lectura.

| Requisito / control | Operación | Evidencia de aceptación |
|---|---|---|
| BH-P01: identidad, autoridad y fuentes | Capturar la página completa y registrar los dos contratos MD | source/page-snapshot.json, source/discovery.json, catálogo y ADR-019 |
| BH-P07: función y estado | Seleccionar rutas propias y no inventar estados | token-names.json, consumption/avatar*/variable-map.csv |
| BH-P07: mínimo por firma | Agrupar usos reales por tipo/scope/vector completo | token-minimum.json y resultado component_token_minimum de check |
| BH-P07: tema y excepciones | Fondo principal temático; presencia, alternos y contador fijos | Contratos REQ-THEME, recetas y destination/consumer-qa.json |
| BH-P02: dependencia e identidad | Phosphor remoto; presencia privada; foto original; slot nativo | destination/avatar.json, group.json, foundation.json, binding-index.json |
| BH-P04: QA del destino | Auditoría de propiedades/bindings y pruebas desde instancias | destination/native-audit.json, consumer-qa.json y visual/ |
| BH-P04: límites de calidad | Medir contraste, conservar fidelidad adoptada y distinguir web | contrast.json y comprobante único ../qa/avatar-pilot-check.json |
| BH-P08: envío trazable | Preparar notas antes del push, validar por CI y entregar PDF | docs/releases/pushes/ y receipt de Actions |

La fuente se recorrió explícitamente: 498 nodos, 12 variantes Avatar y 4 Avatar group. Los dumps fallidos por límite de transporte no son evidencia de cambios ni pruebas de componentes: la herramienta confirmó rollback. El snapshot completo conservado declara cobertura completa. Las reacciones fuente de Avatar están vacías; no hay reproducción animada que acreditar. Las demostraciones de fallback y cálculo de +N son responsabilidades del consumidor, no automatismos creados por este encargo.

Las tolerancias se fijaron en los contratos antes del build: geometría 0.01 px y color 1e-6; identidades, scopes y aliases exactos. Las tablas y capturas son derivados observacionales; no sustituyen los propietarios MD ni añaden reglas.
