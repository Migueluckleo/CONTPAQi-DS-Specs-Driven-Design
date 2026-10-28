---
{
  "schema_version": 1,
  "id": "BH-P08",
  "version": "1.2.1",
  "profile": "operational",
  "status": "ELIGIBLE",
  "authority": {
    "kind": "DELEGATED",
    "decision_id": "ADR-013"
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
      "id": "SRC-ENGINE",
      "path": "blueheart/release_docs.py",
      "sha256": "11606dbb79fe91f8c70e3ff5b42a64f4e6db9947b2095abbeb60de46af23c5e0"
    },
    {
      "id": "SRC-CI",
      "path": ".github/workflows/release-documentation.yml",
      "sha256": "d5aab3c4047b09b44baf8a15c7faff88e563b915d356d02444f2c66434f6f82c"
    },
    {
      "id": "SRC-PROTECTION",
      "path": "docs/releases/branch-ruleset.json",
      "sha256": "27920ceb674fb6ae2f71e05397f96a7aa2546cc490ffc836de8bf2bf408dee93"
    },
    {
      "id": "SRC-PUBLICATION-AUTH",
      "path": "evidence/authorization/github-publication-pdf-request.txt",
      "sha256": "be6e33ab56476bab9c859ab541d121516aa94a1c25aa6390c3012810529730ed"
    },
    {
      "id": "SRC-PDF",
      "path": "blueheart/release_pdf.py",
      "sha256": "765ae146452cb817af160ff7068a8688a6767a662d164c21a606983a27b565d7"
    },
    {
      "id": "SRC-PDF-DEPENDENCY",
      "path": "docs/releases/requirements-pdf.txt",
      "sha256": "207ab33432bbe639e5cc8fce0bc03f982d0842af6c180aca114b1586844a3d18"
    },
    {
      "id": "SRC-NO-REVIEWER-AUTH",
      "path": "evidence/authorization/main-without-reviewer-request.txt",
      "sha256": "ffa1572afeb363d4cb2887b72212e6b24e546a95554ab7a045b96244733b5cdd"
    }
  ],
  "dependencies": [
    {
      "kind": "contract",
      "id": "BH-P05",
      "version": "2.0.1",
      "relation": "uses"
    }
  ],
  "requirements": [
    {
      "id": "REQ-P08-01",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH"
      ],
      "acceptance": [
        "Verificar registro único por envío con los casos de tests/test_release_docs.py y la evidencia del alcance; la protección remota requiere prueba en GitHub."
      ]
    },
    {
      "id": "REQ-P08-02",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-ENGINE"
      ],
      "acceptance": [
        "Verificar preparación previa y cierre documental con los casos de tests/test_release_docs.py y la evidencia del alcance; la protección remota requiere prueba en GitHub."
      ]
    },
    {
      "id": "REQ-P08-03",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-ENGINE"
      ],
      "acceptance": [
        "Verificar compatibilidad y versiones de componentes con los casos de tests/test_release_docs.py y la evidencia del alcance; la protección remota requiere prueba en GitHub."
      ]
    },
    {
      "id": "REQ-P08-04",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-ENGINE"
      ],
      "acceptance": [
        "Verificar desarrollo y releases oficiales con los casos de tests/test_release_docs.py y la evidencia del alcance; la protección remota requiere prueba en GitHub."
      ]
    },
    {
      "id": "REQ-P08-05",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-ENGINE",
        "SRC-CI",
        "SRC-PROTECTION",
        "SRC-NO-REVIEWER-AUTH"
      ],
      "acceptance": [
        "La regla activa exige PR y el check release-documentation de GitHub Actions (15368), con estado actualizado, cero aprobaciones y sin revisión de último push, Code Owners ni revisores específicos.",
        "Comprobar que CI, notas obligatorias, conservación de SHAs, resolución de conversaciones y prohibiciones de bypass, force push y borrado se mantienen; integrar una PR con CI aprobado sin otro revisor."
      ]
    },
    {
      "id": "REQ-P08-06",
      "force": "MUST",
      "provenance": "DERIVED",
      "sources": [
        "SRC-AUTH",
        "SRC-ENGINE",
        "SRC-CI",
        "SRC-PROTECTION"
      ],
      "acceptance": [
        "Verificar no recursión, autoridad y aceptación con los casos de tests/test_release_docs.py y la evidencia del alcance; la protección remota requiere prueba en GitHub."
      ]
    },
    {
      "id": "REQ-P08-07",
      "force": "MUST",
      "provenance": "EXPLICIT",
      "sources": [
        "SRC-PUBLICATION-AUTH",
        "SRC-PDF",
        "SRC-PDF-DEPENDENCY",
        "SRC-CI"
      ],
      "acceptance": [
        "Cada push produce un PDF condensado identificado por SHA y asociado a su receipt y MD; la prueba de incumplimiento produce PDF de fallo y CI no cero.",
        "Verificar render, acentos, enlaces, alcance de pruebas y ausencia de edición manual o commits recursivos.",
        "El agente entrega el PDF de cada push realizado durante su encargo; para pushes externos GitHub Actions conserva el artefacto descargable y su enlace en el resumen."
      ]
    }
  ],
  "profile_data": {
    "inputs": [
      "Rango Git completo y catálogo en sus extremos",
      "Pruebas ejecutadas, referencias QA, decisiones e impacto de componentes"
    ],
    "outputs": [
      "Registro MD único por tanda y receipt verificable por push",
      "Check CI y configuración de protección preparada",
      "PDF condensado por push y enlace de descarga en el resumen de Actions"
    ],
    "responsibilities": [
      "coordinator: rango, compatibilidad, pendientes y autorización de publicación",
      "builder: preparación local de notas sin publicar",
      "verifier: cobertura CI y pruebas de incumplimiento",
      "administrador del repositorio: activación y prueba de protección remota",
      "coordinator: entregar el PDF de cada push realizado en el encargo; Actions conserva el PDF de pushes externos"
    ],
    "failure_states": [
      "NONCOMPLIANT: cobertura, integridad, versión o prueba inválida; salida 2 y CI fallido",
      "PENDING_REMOTE_CONFIGURATION: repositorio/protección aún no configurados"
    ],
    "applies_to": [
      "Todos los pushes de ramas y tags del repositorio Blue Heart DS una vez configurado",
      "Versiones de contratos y tokens de componentes registrados"
    ]
  }
}
---
# BH-P08 · Gobierno de GitHub y Release Documentation

### REQ-P08-01

**Registro único por envío**

Cada actualización de rama debe quedar cubierta por registros bajo `docs/releases/pushes/`. Cada registro tiene base, payload, commits SHA completos, archivos/altas/cambios/bajas, categorías added/changed/fixed/removed, pruebas ejecutadas con comando/resultado/salida/hash, verificaciones pendientes, decisiones arquitectónicas pertinentes y referencias a evidencias existentes. Un rename se representa determinísticamente como baja y alta. Los mensajes de commits describen cambios funcionales; la clasificación automática no inventa funcionalidades a partir de nombres de archivo.

La nota es un único MD con frontmatter JSON y cuerpo generado del mismo registro. El cuerpo no se edita como otra fuente. No mantener un changelog global ni duplicar las tablas de QA de BH-P04: referenciarlas por ruta/hash con `--evidence`. Las fuentes históricas y registros anteriores son inmutables; sus correcciones se documentan mediante otro envío. El índice y ejemplos de operación están en [docs/releases/](../docs/releases/README.md).

### REQ-P08-02

**Preparación previa y cierre documental**

Primero preparar los commits de contenido con árbol limpio. `python3 -B -m blueheart.release_docs prepare --base SHA_COMPLETO` ejecuta los controles locales y genera la nota del payload HEAD, sin hacer commit ni push. Usar la última punta remota conocida de esa rama como base, o EMPTY al documentar historia inicial. Declarar decisiones, QA existente y pendientes mediante opciones; no aprobar automáticamente pruebas de destino que no se ejecutaron.

El último commit del envío añade solo esa nota; su padre es exactamente el payload declarado. No puede incluir cambios de código, configuración o QA adicionales. Ejecutar `verify --base SHA_COMPLETO --head HEAD` antes de publicar. Si el contenido cambia antes del cierre, regenerar contra el nuevo payload; si ya se envió, usar otro registro. Pueden enviarse varias tandas disjuntas que ya tengan sus cierres, sin volver a documentar los mismos commits. Las notas de ascendencia integrada se referencian, no se copian.

El SHA del commit que contiene la nota no puede formar parte de esa misma nota. CI lo resuelve y emite un receipt con before/after, todos los commits/archivos del envío, cierres y referencias. El artifact no crea commits; Git permite reconstruir esa asociación a partir del commit que añadió cada nota. La herramienta genera notas MD solo en prepare explícito; verify y ci no escriben el repositorio. El adaptador PDF genera salidas derivadas en output/ o en el temporal del runner.

### REQ-P08-03

**Compatibilidad y versiones de componentes**

La versión del componente es independiente de la versión de los protocolos, del esquema, del motor y de la release del sistema. Una edición exclusiva de gobierno no aumenta Button. Para componentes registrados, comparar el catálogo y el contenido del contrato y sus dependencias transitivas de contratos/tokens entre la base y el payload. Registrar automáticamente identidad, versión/hash anterior y nuevo, firma de dependencias e impacto. También se conserva la lista completa de archivos de Git.

Todo cambio detectado sobre un componente existente exige una nueva versión SemVer estable x.y.z, declaración patch/minor/major y justificación/migración (`--component-change ID:impacto:justificación`). Patch corrige sin cambiar el contrato público, minor añade comportamiento compatible y major rompe consumidores; incluso en 0.x se exige major para roturas para evitar ambigüedad. CI comprueba el incremento mínimo declarado y bloquea reutilizar una versión modificada. La clasificación semántica se revisa con BH-P04: CI no puede deducir compatibilidad de un diff. Un retiro requiere major y estrategia de sustitución/migración; un alta inicial conserva la versión registrada.

Un cambio en tokens compartidos puede afectar familias sin editar su MD: la detección sigue aliases en todos los modos y dependencias transitivas. Una familia afectada exige evidencia de QA existente o pendientes explícitos. No reconstruir otras familias para justificar el registro. La cobertura actual es contratos y tokens registrados; cuando exista una biblioteca React, extender la detección a sus archivos/API públicos antes de afirmar que sus versiones están gobernadas automáticamente. No hay biblioteca web implementada por este contrato.

### REQ-P08-04

**Desarrollo y releases oficiales**

development es el valor predeterminado y no publica nada. release exige versión estable explícita, cero verificaciones pendientes y referencias a QA de destino si hay componentes afectados, incluidas altas iniciales. Un tag de release debe ser vX.Y.Z, corresponder al registro release y apuntar a su cierre documental; se verifica la cobertura. Preparar notas o un tag no autoriza publicar. No crear ni enviar tags, paquetes o GitHub Releases sin autorización del responsable. Las notas de release conservan referencias a registros existentes en su ascendencia; no replican manualmente un historial acumulado.

La entrega de artefactos y sus consumidores sigue BH-P05. El control de infraestructura no sustituye el QA de destinos exigido por BH-P04. ADR-011 preparó el mecanismo; ADR-012 autoriza publicar este repositorio y configurar sus controles; ADR-013 ajusta main para operar sin aprobaciones obligatorias. La autorización no incluye publicar una release oficial.

### REQ-P08-05

**CI y protección de integraciones**

El workflow [.github/workflows/release-documentation.yml](../.github/workflows/release-documentation.yml) corre para todos los pushes de ramas/tags y PRs, sin filtros que omitan documentación. Lee historia completa, repite check/tests y ejecuta el verificador con los SHAs del evento. Una rama nueva verifica toda su ascendencia; un force push cuya base ya no sea ancestro incumple. Commits sin cobertura, registros alterados, versión insuficiente, tests fallidos o metadatos incoherentes producen salida NONCOMPLIANT y código no cero.

La rama protegida exige el check `release-documentation` de GitHub Actions (integration_id 15368) y PR actualizada, con merge commits que conserven los SHAs. ADR-013 fija cero aprobaciones obligatorias: no exigir aprobación del último push, Code Owners, revisores específicos ni aprobación adicional por cambios sin atribución. Las revisiones son voluntarias y no constituyen un gate de integración. Se conserva la resolución de conversaciones abiertas; el autor puede resolverlas. El autor puede integrar su propia PR cuando CI y la documentación cumplen la política, sin bypass ni otra persona. La aceptación técnica y su evidencia permanecen exigibles; no atribuir una revisión humana que no ocurrió. Una integración solo se acepta si no introduce contenido distinto del segundo padre y el primer padre ya está incorporado allí; las resoluciones se hacen y documentan antes del cierre en la rama de trabajo. Squash, rebase y merge queue no están habilitados por este diseño. Una actualización local requiere preparar y verificar sus notas antes de enviar; el check del push puede detectar incumplimiento después de recibirlo. Las reglas de protección impiden integrarlo.

Al configurarse el repositorio remoto correcto, un administrador aplica y verifica la configuración [branch-ruleset.json](../docs/releases/branch-ruleset.json), respetando restricciones existentes. Debe comprobar el bloqueo con una PR incumplida y el desbloqueo tras corregirla. Sin repositorio, permisos o plan compatible, registrar la activación como pendiente; no declarar protección remota por validar un JSON. No inicializar ni publicar por leer el protocolo.

### REQ-P08-06

**No recursión, autoridad y aceptación**

El token de Actions tiene únicamente contents:read. El workflow no escribe commits, hace push ni publica releases. La nota se genera localmente antes del envío, y el receipt se guarda fuera del worktree como artifact. No hay bots que se documenten a sí mismos, workflows de escritura encadenados, exclusiones de paths, hooks obligatorios ni omisión de checks para commits documentales. La protección no depende de saltarse a un actor bot.

Aceptación local: ocho protocolos registrados con estructura, requisitos, autoridad, fuentes íntegras, versiones exactas, dependencias acíclicas y contexto completo; pruebas de envíos válidos, sin nota, nota incompleta/alterada, payload posterior, merges, tags, fallos de pruebas, cambios transitivos y compatibilidad de componentes. Registrar las verificaciones remotas pendientes y conservar el original intacto. El procedimiento ejecutable y los ejemplos solo enlazan este contrato como propietario de la política; no crean una segunda norma.


### REQ-P08-07

**PDF condensado en cada push**

Cada push de Blue Heart DS produce un PDF condensado de sus release notes. El MD registrado sigue siendo el dato propietario; el PDF se genera desde ese registro y el receipt real del envío, sin mantener otro resumen editable. Identificar repositorio, tipo development/release, fecha, SHA final, cantidad de commits/archivos, cambios agregados/modificados/corregidos/eliminados, pruebas y resultados, pendientes, decisiones pertinentes y versiones de componentes. Condensar listados extensos y enlazar el detalle verificable, sin ocultar que se omitieron entradas de la vista resumida. Un PDF de desarrollo no anuncia una release oficial.

GitHub Actions genera el PDF con el adaptador `python3 -B -m blueheart.release_pdf`, lo conserva junto al receipt como artefacto descargable y coloca su enlace en el resumen de ejecución. Si la documentación o un check fallan, el PDF informa el incumplimiento; generar ese PDF no cambia el resultado fallido ni habilita integración. Si la generación/exportación falla, el check también falla. Los fallos que impidan obtener el repositorio o ejecutar Actions requieren reintentar el flujo; no se puede afirmar que un PDF inexistente fue entregado.

El agente que hace un push en un encargo entrega al responsable su PDF correspondiente, también para los envíos de prueba, e identifica cuáles incumplieron. Para pushes externos a un encargo, el artefacto de Actions es el canal automático de entrega; no se introduce un monitor ni se promete iniciar una conversación. Conservar la asociación permanente en Git; el artifact usa la retención de GitHub y puede regenerarse con sus referencias.

El PDF se escribe en `output/pdf/` local (ignorado por Git) o fuera del worktree en CI, después de resolver el SHA final. No se añade al commit documental, no genera otro push y no modifica notas históricas. ReportLab es una dependencia opcional fijada del adaptador; el núcleo de arquitectura conserva la biblioteca estándar. Verificar representación visual, legibilidad, acentos y enlaces antes de entregar una nueva plantilla o un PDF local.
