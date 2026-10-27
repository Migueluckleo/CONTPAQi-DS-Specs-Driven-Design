# Documentación de envíos

La única política es [BH-P08](../../protocols/08-GITHUB-RELEASE-DOCUMENTATION.md). Este directorio contiene registros generados y configuración; no un segundo protocolo.

Estado: repositorio Git y remoto aún no configurados. Actions y ruleset preparados, sin ejecución en GitHub. No existen notas ficticias, commits o releases creados en el workspace.

```sh
python3 -B -m blueheart context BH-P08
python3 -B -m blueheart.release_docs --help
```

## Comandos del flujo local

Aplicar las entradas y el cierre descritos en [REQ-P08-02](../../protocols/08-GITHUB-RELEASE-DOCUMENTATION.md#req-p08-02). Ejemplos para cuando el repositorio esté configurado y se autorice el envío:

```sh
# SHA completo del último estado remoto conocido; EMPTY para historia inicial.
python3 -B -m blueheart.release_docs prepare --base SHA_COMPLETO --decision ADR-011
# Opciones pertinentes:
# --evidence evidence/qa/COMPROBANTE.json
# --pending 'Figma: binding pendiente de verificar'
# --component-change 'BUTTON-001:major:Retiro de prop; usar la sustitución documentada'
# --kind release --release-version 1.0.0
```

`prepare` muestra la ruta del MD generado y ejecuta los controles locales. El commit documental lo incorpora según BH-P08; la herramienta no hace commits. Después:

```sh
python3 -B -m blueheart.release_docs verify --base SHA_COMPLETO --head HEAD
```

El formato, las categorías, la evidencia y la reconstrucción del receipt están en [REQ-P08-01/02](../../protocols/08-GITHUB-RELEASE-DOCUMENTATION.md#req-p08-01). La cobertura y límites del versionado de componentes están en [REQ-P08-03](../../protocols/08-GITHUB-RELEASE-DOCUMENTATION.md#req-p08-03); la distinción development/release en [REQ-P08-04](../../protocols/08-GITHUB-RELEASE-DOCUMENTATION.md#req-p08-04).

## Activación remota pendiente

[REQ-P08-05](../../protocols/08-GITHUB-RELEASE-DOCUMENTATION.md#req-p08-05) define las condiciones y la prueba de bloqueo obligatoria. El archivo [branch-ruleset.json](branch-ruleset.json) corresponde a la rama predeterminada y al check `release-documentation` del [workflow](../../.github/workflows/release-documentation.yml). El repositorio, plan, identidad del check y permisos se verifican al activarlo. Para crear la regla **si no hay una equivalente**, un administrador puede usar:

```sh
gh api --method POST repos/OWNER/REPO/rulesets --input docs/releases/branch-ruleset.json
```

Si ya existe, actualizar por su ID preservando las restricciones ajenas. La configuración local no acredita protección remota. Las salvaguardas contra recursión están en [REQ-P08-06](../../protocols/08-GITHUB-RELEASE-DOCUMENTATION.md#req-p08-06).

Referencias de configuración: [eventos Actions](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows), [API rulesets](https://docs.github.com/en/rest/repos/rules), [protección de ramas](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches). Las Actions están fijadas a SHAs de sus [releases oficiales de checkout](https://github.com/actions/checkout/releases/tag/v4.3.1) y [upload-artifact](https://github.com/actions/upload-artifact/releases/tag/v4.6.2).
