---
{
  "schema_version": 1,
  "id": "BH-P03",
  "version": "2.3.1",
  "profile": "operational",
  "status": "ELIGIBLE",
  "authority": {
    "kind": "DELEGATED",
    "decision_id": "ADR-024"
  },
  "targets": [
    "documentation"
  ],
  "readiness": {
    "documentation": "READY"
  },
  "sources": [
    {
      "id": "SRC-AUTH",
      "path": "evidence/authorization/operational-protocols-request.txt",
      "sha256": "eefa6f1db2b1defd41541064238224cfcfb6690f19d0025700a30d17a7e903f0"
    },
    {
      "id": "SRC-RECOVERY",
      "path": "evidence/protocol-recovery/manifest.json",
      "sha256": "d7c7ae3dca2ee7d76102f591803b1426b9300030454523467f74c7801fc33d5c"
    },
    {
      "id": "SRC-CRITERIA",
      "path": "evidence/authorization/token-protocol-criteria-request.txt",
      "sha256": "fa308f8359ef963618e917e667d7334d25a025ae1b3d820787919190a4271f1e"
    },
    {
      "id": "SRC-COLLECTION",
      "path": "evidence/authorization/component-collection-request.txt",
      "sha256": "041814c7ca461cddd8d809a5ae3e9f179fdd096b92832c95f57efae3fb2eb11e"
    },
    {
      "id": "SRC-USER-DOT",
      "path": "evidence/authorization/dot-dependency-request.txt",
      "sha256": "13c94305c8dc4f6dcf44311f0197de27d164716ec08ad5c6e32c58c22705e533"
    },
    {
      "id": "SRC-ICON-ALIGNMENT",
      "path": "evidence/authorization/icon-color-alignment-request.txt",
      "sha256": "35568ec00f70dd642e02b342c165506315874951b932afd9c6c298fbae93a59f"
    }
  ],
  "dependencies": [
    {
      "kind": "contract",
      "id": "BH-P01",
      "version": "2.3.0",
      "relation": "uses"
    },
    {
      "kind": "contract",
      "id": "BH-P06",
      "version": "2.1.0",
      "relation": "uses"
    }
  ],
  "requirements": [
    {
      "id": "REQ-P03-01",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY",
        "SRC-USER-DOT"
      ],
      "acceptance": [
        "Responsabilidades y versiones del entorno están declaradas sin dependencias de aplicación dentro de la biblioteca."
      ]
    },
    {
      "id": "REQ-P03-02",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY"
      ],
      "acceptance": [
        "Tipos, exports, defaults y pruebas de interacción/composición corresponden al contrato público."
      ]
    },
    {
      "id": "REQ-P03-03",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY",
        "SRC-CRITERIA"
      ],
      "acceptance": [
        "CSS generado resuelve tokens y unidades; recetas conservan mínimo y nombres de BH-P07 sin inventario manual de valores.",
        "Proyección CSS y cambio de tema respetan REQ-P07-06; nombres se resuelven desde WEB registrado y no se genera otra paleta o token por clase."
      ]
    },
    {
      "id": "REQ-P03-04",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY"
      ],
      "acceptance": [
        "Prueba de la frontera cliente/servidor y ejemplos ejecutables en el modo de distribución declarado."
      ]
    },
    {
      "id": "REQ-P03-05",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY"
      ],
      "acceptance": [
        "Comandos reales, resultados y QA de navegador/accesibilidad cubren únicamente la implementación existente."
      ]
    },
    {
      "id": "REQ-P03-06",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-RECOVERY"
      ],
      "acceptance": [
        "Import oficial y peso/export coinciden con BH-P06."
      ]
    },
    {
      "id": "REQ-COLLECTION",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-COLLECTION"
      ],
      "acceptance": [
        "Consumir y verificar la organización de colecciones declarada únicamente en BH-P07 REQ-P07-07; no crear colecciones por familia."
      ]
    }
  ],
  "profile_data": {
    "inputs": [
      "Contrato seleccionado y destino web autorizado",
      "Versiones del stack y tokens seleccionados"
    ],
    "outputs": [
      "Biblioteca React tipada y adaptador consumidor",
      "Ejemplo ejecutable y pruebas pertinentes"
    ],
    "responsibilities": [
      "builder: API y construcción web",
      "verifier: comportamiento y accesibilidad"
    ],
    "failure_states": [
      "BLOCKED: fuente, autoridad, dependencia o capacidad necesaria ausente",
      "FAIL: incumplimiento demostrado; reparar y verificar el alcance afectado"
    ],
    "applies_to": [
      "CREATE, UPDATE, MIGRATE o VALIDATE_ONLY dentro de la política y del encargo"
    ]
  }
}
---
# BH-P03 · React, TypeScript, Tailwind y Next.js

### REQ-P03-01

**1. Responsabilidades del stack**

Prerequisito: [BH-P01](01-COMPONENT-CONTRACT.md). Define el stack solicitado sin instalarlo ni crear componentes en esta preparación.

| Parte | Responsabilidad |
|---|---|
| React | Componentes reutilizables y composición con API pública explícita. |
| TypeScript | Tipos de props, eventos, variantes y combinaciones permitidas. |
| Tailwind CSS | Composición visual y utilidades enlazadas a tokens. |
| Next.js | Aplicación consumidora, catálogo y ejemplos del DS. |

La biblioteca React no importa el catálogo, rutas de la aplicación, Graphify, contratos en runtime ni herramientas Figma. Los tipos y exports no se extraen con regex de un componente histórico. Mantener metadatos explícitos o información del compilador cuando haga falta generar documentación. Next.js no es dependencia conceptual de cada componente: una integración específica se mantiene en su adaptador.

Cuando se autorice el primer entorno web, inspeccionar herramientas disponibles y compatibilidad de versiones; fijar dependencias y lockfile en el proyecto. El package.json copiado es evidencia del sistema anterior, no la selección de versiones de Blue Heart. No instalar herramientas globales, backend, Storybook ni un segundo framework por este protocolo. Definir rutas reales al crear módulos; no crear paquetes o carpetas vacías para anticiparlos.

El impacto sobre consumidores se evalúa con [BH-P01 REQ-P01-07](01-COMPONENT-CONTRACT.md#req-p01-07); su mapa y prueba pertenecen al comprobante del encargo.

### REQ-P03-02

**2. API, composición y comportamiento**

Derivar exports, props, defaults, variantes y estados del contrato de la familia. Tipar eventos y combinaciones válidas; evitar `any` que oculte diferencias. Usar comprobación estricta de TypeScript como base del proyecto, con excepciones explícitas. [Referencia: strict](https://www.typescriptlang.org/tsconfig/strict.html).

Preferir HTML nativo y controles reales. Separar props controladas/callbacks de estado de demostración y reglas del producto. No fingir guardado, permisos, autenticación, subida remota o IA. Documentar efectos, foco, disabled, loading y mensajes solo cuando correspondan al contrato.

Representar composición mediante children, regiones ReactNode o colecciones tipadas con identidad estable, según la necesidad. Probar inserción, retirada y reordenación aplicables; usar claves estables, no un máximo derivado de la muestra. Esto demuestra composición React, no Slots nativos Figma.

### REQ-P03-03

**3. Tokens, Tailwind y tipografía**

Resolver la cadena con BH-P01 y aplicar obligatoriamente [BH-P07](07-COMPONENT-TOKENS.md): las recetas de estados reutilizan tokens compartidos y el adaptador no genera otra variable por cada clase o combinación. Ejecutar el gate de minimización antes de generar CSS o componentes. El CSS será una proyección generada de las fuentes seleccionadas; no otro inventario editable. No reemplazar un binding por el RGB equivalente ni usar escalas cromáticas de Tailwind como sustituto del DS. Las variables CSS de componente contendrán propiedad/estado y referenciarán los semánticos compartidos; su creación espera la familia real y la fase habilitada.

La proyección consume [REQ-P07-06](07-COMPONENT-TOKENS.md#req-p07-06) y verifica sus roles/excepciones al cambiar el tema en el navegador. No derivar la dependencia temática de una clase Tailwind o del nombre de un alias.

No convertir unidades implícitamente ni modificar pesos, interlineados, tracking, decoración o escalas para acomodar una clase. Conservar fuentes y assets con procedencia, rutas configurables y pruebas de carga; no depender sin declararlo de `/assets` en la raíz del consumidor. Las recetas compartidas futuras tendrán un propietario único y se verificarán por propiedades resueltas.

Con Tailwind 4, declarar las utilidades necesarias desde las variables del DS; al referenciar otras variables en `@theme`, considerar `inline` según dónde deban resolverse. Usar clases completas detectables, con mapas estáticos para variantes. Si el paquete queda fuera del escaneo, declarar sus fuentes explícitamente. No construir nombres de clases mediante interpolación parcial. [Tema](https://tailwindcss.com/docs/theme), [detección de clases](https://tailwindcss.com/docs/detecting-classes-in-source-files).

### REQ-P03-04

**4. Integración Next.js**

Mantener el límite cliente en módulos que necesiten estado, eventos o APIs del navegador; evitar marcar todo el catálogo como cliente por comodidad. Comprobar la frontera RSC y las props serializables que la cruzan; no pasar callbacks ordinarios desde un Server Component. El empaquetado de la biblioteca debe conservar las directivas cliente necesarias. [React: use client](https://react.dev/reference/rsc/use-client), [Next.js: Server y Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components).

Los ejemplos usan datos ficticios identificados y funcionan sin backend de producto. Una exportación estática se prueba en el modo de servicio y las rutas realmente elegidos. Un catálogo Next.js no equivale a un HTML autónomo: la portabilidad por `file://`, si se pide, tiene empaquetado y QA separados.

### REQ-P03-05

**5. Entregable y aceptación web**

Por familia entregar código reutilizable, tipos/exports, documentación técnica y un ejemplo ejecutable de las variantes/estados afectados. La documentación cubre importación, dependencias, API/defaults, composición, comportamiento, tokens, fuentes y límites. Los ejemplos no son la implementación de la biblioteca.

Definir en el primer entorno scripts reales de typecheck, pruebas, build y revisión en navegador. Ejecutarlos solo donde existan y correspondan al cambio. El build no acredita fidelidad o accesibilidad. Verificar teclado, nombres accesibles, foco y semántica además de pruebas automáticas; un widget ARIA requiere implementar su interacción, no solo añadir atributos. [WAI-ARIA: teclado](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/).

Aplicar [BH-P04](04-QA-AND-DELIVERY.md) y registrar alcance probado, comandos y evidencia. No publicar paquetes ni desplegar el catálogo por completar un build. Las referencias técnicas se consultaron el 26-10-2026; comprobarlas contra las versiones que se instalen al activar el entorno.

### REQ-P03-06

**Iconografía compartida**

Aplicar [BH-P06 · Phosphor](06-PHOSPHOR-ICONS.md): Figma consume la biblioteca del equipo mediante instancias vinculadas; desarrollo consume directamente el paquete oficial. Conservar mapeo de nombre, peso, variante y key/export, con color y tamaño desde tokens del consumidor.

Los nombres agrupados de Figma se leen como `figmaName` conforme a BH-P07. El CSS se consume desde el WEB registrado: no derivarlo automáticamente de esa ruta ni renombrar la API por una reorganización de grupos Figma.

### REQ-COLLECTION

Para la ubicación de variables, consumir [BH-P07 REQ-P07-07](07-COMPONENT-TOKENS.md#req-p07-07). El pase y QA del destino deben acreditar esa organización con su inventario nativo. El registro y la migración pertenecen a ADR-020 y al contrato vigente; no copiar aquí otra definición de la estructura.

La correspondencia cromática de icono y texto y su aceptación pertenecen a [BH-P06 REQ-P06-03/04](06-PHOSPHOR-ICONS.md#req-p06-03); consumir su versión seleccionada, sin copiar otra regla de color.
