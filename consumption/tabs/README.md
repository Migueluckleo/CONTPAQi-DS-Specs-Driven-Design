# TABS-001 · consumo vigente

Fuente normativa única: [TABS-001@3.0.0](../../norms/components/tabs.3.0.0.md). Fijar identidad, versión, hash y snapshot desde [manifest.json](manifest.json); no reconstruir reglas desde capturas.

```sh
python3 -B -m blueheart check
python3 -B -m blueheart context TABS-001 --compact --modes '{"component":"Contable"}'
```

Tres variantes de grupo, cinco tokens propios y un slot nativo. Consume Tab 3.0.0; Dot es una dependencia transitiva. La selección y los paneles corresponden al consumidor.

[Abrir la página de Figma](https://www.figma.com/design/98xEw6sK8FRVNEhopM5SSz/Blue-Heart-DS?node-id=78-97). Las muestras usan instancias vinculadas. Los cuatro temas se seleccionan en component; los roles Dot conservan los mismos aliases. La organización de colecciones se define únicamente en [BH-P07](../../protocols/07-COMPONENT-TOKENS.md).

El [mapa de variables](variable-map.csv) distingue identidad lógica, ruta Figma, WEB y scope.

El [mapa de migración ADR-021](../../evidence/dot-pilot/migration-map.json) registra nueve bajas y sus sustituciones compartidas. [Dot](../dot/manifest.json) es el propietario del indicador; no recrear helpers o tokens privados. [La historia exacta](../../evidence/dot-pilot/history/manifest.json) conserva contratos y token set anteriores junto al commit fuente.

[QA actual](../../evidence/qa/dot-pilot-check.json): instancias, temas, geometría, estilos, aliases y preservación de consumidores. Las pruebas nativas anteriores siguen en evidence y Git; no equivalen a una reproducción nueva del prototipo. Las cuatro reacciones Tab se conservaron estructuralmente. Dot no contiene reacciones.

La biblioteca permanece local. Phosphor se consume desde la biblioteca del equipo, conforme a [BH-P06](../../protocols/06-PHOSPHOR-ICONS.md); no hay copias vectoriales. React/Next.js, teclado/ARIA web y publicación oficial continúan diferidos. [BH-P08](../../protocols/08-GITHUB-RELEASE-DOCUMENTATION.md) gobierna los envíos y sus PDFs.
