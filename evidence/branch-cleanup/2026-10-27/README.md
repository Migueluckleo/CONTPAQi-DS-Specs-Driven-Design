# Archivo de ramas auxiliares · 2026-10-27

Evidencia histórica; no registra nuevas normas ni sustituye BH-P08. La autorización para archivar y eliminar las ramas está en `authorization.txt`.

- `fix/main-without-reviewer` (`55b9fe7bd067eb63adb9eb9f514a304123d4b8d2`) quedó integrada en main por PR #2, merge `0d13f89ea4a945d156e0867d0a0227a6bff4a05f`.
- `verification/protocol-08` (`b108e09b54764f5c57b68f49c92448d15545d284`) contiene tres commits de pruebas no integrados. Su bundle conserva los objetos y SHAs originales; requiere la base `e7cc8ddd216ca61c497a5e8e58d33a726b09c0b3`, que permanece en la ascendencia de main. No se activan los contenidos de esa rama en el producto.
- `historical-branch-protection-check.json` es una observación anterior a ADR-013: su requisito de una aprobación dejó de estar vigente. `historical-test-push.md` es una copia del registro histórico; no es una nueva nota de publicación ni añade cobertura al flujo activo.
- Los JSON de runs/PR, receipts y extractos de logs preservan la prueba negativa (CI rechazó falta de notas), la corrección posterior y la integración sin revisión. No se atribuye aprobación humana. Los PDF históricos siguen en output/pdf y se pueden regenerar desde estos datos y el historial recuperado; no se duplican como fuente en Git.
- `manifest.json` vincula SHA-256, procedencia y comprobación de recuperación. La eliminación se hará después de integrar este archivo con CI aprobado; el manifiesto previo no afirma que ya se hayan eliminado las referencias.

## Comprobar o recuperar sin crear ramas auxiliares

Desde un clon de main:

```sh
git bundle verify evidence/branch-cleanup/2026-10-27/protocol08-test-history.bundle
git bundle unbundle evidence/branch-cleanup/2026-10-27/protocol08-test-history.bundle
git show b108e09b54764f5c57b68f49c92448d15545d284:docs/releases/verification/branch-protection-check.json
git log e7cc8ddd216ca61c497a5e8e58d33a726b09c0b3..b108e09b54764f5c57b68f49c92448d15545d284
```

`unbundle` restaura objetos, no ramas. Solo si se desea trabajar en la prueba histórica se puede crear una rama explícitamente; no es necesario para consultar la evidencia. Un respaldo local completo adicional se conserva bajo output/archives/branch-cleanup-2026-10-27/.
