# ARES ENTERPRISE — KNOWLEDGE & RESEARCH ENGINE
## Implementation Specification

**Module:** Knowledge & Research Engine  
**Architecture:** Hybrid Knowledge Acquisition  
**Parent System:** ARES Enterprise  
**Priority:** Critical  
**Development Status:** To Be Implemented

---

# 1. MISSION

Diseña e implementa el sistema de adquisición, investigación, procesamiento, almacenamiento, recuperación y actualización de conocimiento de ARES Enterprise.

Este módulo debe permitir que ARES:

1. Mantenga una base de conocimiento técnico actualizada.
2. Investigue temas específicos cuando una tarea lo requiera.
3. Consulte documentación oficial y fuentes externas.
4. Analice repositorios y proyectos open source.
5. Procese investigaciones, artículos, documentación y código.
6. Identifique información obsoleta.
7. Correlacione información de distintas fuentes.
8. Almacene conocimiento reutilizable.
9. Proporcione contexto técnico a los agentes especializados.
10. Identifique vacíos de conocimiento y proponga nuevas investigaciones.

El sistema debe funcionar bajo un modelo híbrido:

- Continuous Research: investigación y actualización periódica.
- On-Demand Research: investigación específica activada por tareas.

No implementar un sistema que simplemente descargue documentos y los almacene.

Se necesita un pipeline completo de conocimiento con trazabilidad, validación, versionado, búsqueda y evaluación de calidad.

# 2. ARCHITECTURE

Implementar los siguientes componentes.

## 2.1 Source Registry

Catálogo centralizado de fuentes de información.

Cada fuente debe almacenar:

- source_id.
- name.
- description.
- source_type.
- domain.
- url.
- category.
- publisher.
- trust_level.
- access_method.
- update_frequency.
- last_checked.
- last_successful_sync.
- license_information.
- enabled.
- configuration.

Tipos de fuentes:

- Official Documentation.
- Security Advisories.
- Vulnerability Databases.
- Git Repositories.
- Research Papers.
- Technical Blogs.
- Security Publications.
- Threat Intelligence.
- Standards and Frameworks.
- Vendor Documentation.

Implementar un sistema de registro de nuevas fuentes.

Las fuentes deben poder habilitarse, deshabilitarse, actualizarse y eliminarse mediante operaciones administrativas controladas.

No confiar automáticamente en una fuente por estar registrada.

## 2.2 Continuous Research Engine

Desarrollar un motor de investigación periódica.

Responsabilidades:

- Administrar fuentes registradas.
- Programar actualizaciones.
- Consultar documentos nuevos.
- Detectar cambios.
- Detectar documentos eliminados.
- Identificar versiones nuevas.
- Evitar descargas duplicadas.
- Registrar errores.
- Reintentar operaciones fallidas.
- Controlar límites de solicitudes.
- Mantener historial de sincronización.

La frecuencia debe configurarse individualmente por fuente.

Implementar inicialmente un scheduler sencillo y desacoplado.

No introducir Celery, Redis u otros sistemas distribuidos hasta que exista una necesidad demostrable.

Las tareas deben poder reanudarse después de una interrupción.

## 2.3 On-Demand Research Engine

Permitir que cualquier agente solicite una investigación técnica.

Ejemplo:

```text
ARES:
Research the security implications of Resource-Based
Constrained Delegation in Active Directory.
```

Workflow:

1. Interpretar la pregunta.
2. Identificar el dominio técnico.
3. Determinar qué información necesita.
4. Consultar Knowledge Base.
5. Identificar vacíos de información.
6. Seleccionar fuentes relevantes.
7. Investigar documentación adicional.
8. Procesar los resultados.
9. Comparar fuentes.
10. Evaluar confiabilidad.
11. Generar una respuesta fundamentada.
12. Almacenar conocimiento reutilizable cuando corresponda.

La investigación debe tener límites configurables de:

- Tiempo.
- Número de fuentes.
- Tamaño de documentos.
- Cantidad de resultados.
- Tokens.
- Coste del proveedor.
- Profundidad de investigación.

No investigar indefinidamente.

## 2.4 Knowledge Ingestion Pipeline

Implementar una arquitectura basada en adaptadores.

Formatos iniciales:

- HTML.
- Markdown.
- PDF.
- TXT.
- JSON.
- XML.
- CSV.
- Git Repositories.
- GitHub API.
- RSS / Atom.

Pipeline:

```text
SOURCE
  |
  v
FETCHER
  |
  v
CONTENT EXTRACTION
  |
  v
NORMALIZATION
  |
  v
METADATA EXTRACTION
  |
  v
DEDUPLICATION
  |
  v
CHUNKING
  |
  v
QUALITY VALIDATION
  |
  v
EMBEDDING GENERATION
  |
  v
KNOWLEDGE STORAGE
  |
  v
INDEXING
```

Cada etapa debe tener interfaces independientes.

Si una etapa falla, registrar el error y evitar almacenar información incompleta como conocimiento validado.

## 2.5 Document Processing

Crear procesadores independientes por formato.

Responsabilidades:

- Extraer texto.
- Preservar encabezados.
- Identificar tablas cuando sea posible.
- Extraer metadatos.
- Detectar idioma.
- Identificar fechas.
- Identificar autores y publicadores.
- Extraer referencias.
- Preservar ubicación y procedencia.

Los documentos PDF deben permitir recuperar información por página.

Los repositorios de código deben conservar rutas y referencias a archivos.

## 2.6 Code Intelligence Engine

Crear un módulo especializado en investigación de código fuente.

Debe poder:

- Clonar repositorios autorizados.
- Consultar GitHub API.
- Identificar lenguajes.
- Analizar estructura.
- Identificar dependencias.
- Detectar versiones.
- Examinar README.
- Examinar documentación.
- Identificar módulos.
- Identificar funciones relevantes.
- Analizar relaciones entre archivos.
- Extraer referencias técnicas.
- Registrar commits y releases.

Permitir análisis de repositorios de herramientas como:

- BloodHound.
- Impacket.
- NetExec.
- Certipy.
- Certify.
- Atomic Red Team.
- Caldera.
- Sigma.
- Sysmon.
- Velociraptor.
- Nuclei.

No asumir que un repositorio es seguro por ser popular.

Tratar el código descargado como contenido no confiable.

No ejecutar automáticamente scripts, binarios, instaladores ni código de repositorios externos.

Las pruebas dinámicas deben requerir un entorno de laboratorio aislado y una política de ejecución explícita.

# 3. KNOWLEDGE STORAGE

Implementar una capa de persistencia independiente del motor de recuperación.

## 3.1 Initial Database Architecture

Utilizar:

- PostgreSQL.
- pgvector.
- SQLAlchemy.
- Alembic.

SQLite puede utilizarse para pruebas unitarias o entornos de desarrollo simplificados.

No introducir Neo4j en la primera implementación. Mantener una interfaz para integrarlo posteriormente.

## 3.2 Data Models

Diseñar modelos para:

### Source

Representa una fuente registrada.

### Document

Representa un documento original.

### DocumentVersion

Representa cada versión detectada de un documento.

### DocumentChunk

Representa los fragmentos procesados.

### Embedding

Representa las representaciones vectoriales asociadas al contenido.

### ResearchTask

Representa una investigación solicitada.

### ResearchResult

Representa los resultados de una investigación.

### ResearchReference

Representa una referencia utilizada.

### KnowledgeEntity

Representa conceptos técnicos, tecnologías, productos, herramientas o vulnerabilidades.

### KnowledgeRelationship

Representa relaciones entre entidades.

### SyncJob

Representa una operación de sincronización.

### KnowledgeFeedback

Representa correcciones y evaluaciones de calidad.

Implementar relaciones, restricciones e índices apropiados.

Evitar duplicación de datos.

## 3.3 Provenance and Versioning

Todo conocimiento almacenado debe poder rastrearse hasta su fuente original.

Registrar:

- Source ID.
- Original URL.
- Document title.
- Publisher.
- Author cuando esté disponible.
- Publication date.
- Retrieval date.
- Document version.
- Content hash.
- License information.
- Processing version.
- Confidence metadata.

Nunca presentar contenido sin procedencia como información verificada.

Mantener historial de modificaciones.

## 3.4 Vector Search

Implementar búsqueda semántica con pgvector.

Crear una abstracción para proveedores de embeddings.

No acoplar el sistema a un único proveedor.

Permitir:

- Embeddings remotos.
- Embeddings locales.
- Configuración de dimensiones.
- Versionado de modelos.
- Reindexación.
- Búsqueda por similitud.
- Filtros por fuente.
- Filtros por categoría.
- Filtros por fecha.
- Filtros por confianza.

No mezclar embeddings generados con modelos incompatibles.

Implementar búsqueda híbrida:

- Semantic Search.
- Full-Text Search.
- Metadata Filtering.

Cuando sea útil, combinar resultados mediante un mecanismo de ranking.

# 4. KNOWLEDGE VALIDATION ENGINE

La calidad del conocimiento es prioritaria.

Implementar validaciones para:

- Fuente.
- Fecha.
- Autoridad.
- Consistencia.
- Duplicación.
- Actualidad.
- Evidencia.
- Contradicciones.
- Completitud.

Clasificar los conocimientos en:

**VERIFIED:** respaldado por documentación primaria o evidencia reproducible.

**DOCUMENTED:** respaldado por una fuente técnica confiable.

**EXPERIMENTAL:** observado en pruebas controladas.

**HYPOTHESIS:** inferencia pendiente de validación.

**DEPRECATED:** información obsoleta o sustituida.

No convertir automáticamente una hipótesis en un hecho.

No asignar confianza arbitraria mediante un número generado por el LLM.

Mantener los criterios de clasificación transparentes.

## 4.1 Source Reliability

Crear un sistema configurable de evaluación de fuentes.

Considerar:

- Autoridad del publicador.
- Documentación primaria.
- Fecha.
- Reputación técnica.
- Evidencia.
- Independencia de las fuentes.
- Posibles contradicciones.

Una fuente oficial también puede estar incompleta o desactualizada.

## 4.2 Contradiction Detection

Cuando dos fuentes proporcionen información diferente:

1. Detectar la discrepancia.
2. Identificar las afirmaciones involucradas.
3. Registrar sus referencias.
4. Comparar fechas y versiones.
5. Evaluar cuál es más relevante.
6. Mantener la contradicción documentada.
7. Evitar elegir arbitrariamente una versión.

# 5. KNOWLEDGE RETRIEVAL ENGINE

Este componente proporcionará información a los agentes de ARES.

Implementar:

- Semantic Retrieval.
- Keyword Retrieval.
- Full-Text Search.
- Hybrid Search.
- Metadata Filtering.
- Relevance Ranking.
- Context Assembly.
- Citation Generation.

Cada resultado debe incluir:

- Contenido.
- Fuente.
- URL.
- Fecha.
- Documento.
- Versión.
- Fragmento relevante.
- Clasificación de confianza.

Los agentes deben poder solicitar contexto mediante una interfaz común.

Ejemplo conceptual:

```python
results = knowledge_engine.search(
    query="Active Directory Kerberos delegation",
    categories=["active_directory"],
    limit=10
)
```

Diseñar contratos reales y validar sus entradas y salidas.

# 6. SECURITY RESEARCH TAXONOMY

Crear una taxonomía inicial que permita organizar el conocimiento.

Categorías:

```text
cybersecurity/
├── active_directory/
│   ├── architecture/
│   ├── kerberos/
│   ├── ldap/
│   ├── acl/
│   ├── delegation/
│   ├── adcs/
│   ├── gpo/
│   └── attack_paths/
│
├── windows/
│   ├── internals/
│   ├── authentication/
│   ├── powershell/
│   ├── services/
│   ├── registry/
│   ├── event_logging/
│   └── security_controls/
│
├── edr_xdr/
│   ├── vendors/
│   ├── architecture/
│   ├── telemetry/
│   ├── detection/
│   ├── response/
│   └── limitations/
│
├── evasion_research/
│   ├── process_injection/
│   ├── memory/
│   ├── etw/
│   ├── amsi/
│   ├── api_hooking/
│   └── defensive_validation/
│
├── network_security/
├── web_security/
├── cloud_security/
├── linux_security/
├── vulnerability_research/
├── exploit_development/
├── digital_forensics/
├── threat_intelligence/
└── adversary_emulation/
```

La taxonomía debe ser extensible.

No codificar todas las categorías de forma rígida.

# 7. CONTINUOUS KNOWLEDGE UPDATE

Implementar actualizaciones periódicas.

Fuentes iniciales recomendadas:

## Official Documentation

- Microsoft Learn.
- Microsoft Security.
- MITRE ATT&CK.
- NIST.
- OWASP.
- CISA.
- GitHub Security Advisories.

## Vulnerability Intelligence

- NVD.
- CVE Program.
- CISA KEV.
- FIRST EPSS.

## Research and Open Source

- GitHub Releases.
- GitHub Security Advisories.
- arXiv.
- Documentación oficial de herramientas.
- Publicaciones técnicas especializadas.

## Vendor Intelligence

- CrowdStrike.
- SentinelOne.
- Microsoft Defender.
- Palo Alto Networks.
- Sophos.
- Elastic.

Implementar conectores por fuente.

Priorizar APIs oficiales, feeds y documentación estructurada.

Respetar términos de servicio, licencias, límites de uso y políticas de acceso.

No realizar scraping indiscriminado.

## 7.1 Change Detection

Detectar:

- Nuevos documentos.
- Documentos modificados.
- Nuevas versiones.
- Nuevas publicaciones.
- Releases.
- Avisos de seguridad.
- Cambios en documentación.

Utilizar hashes de contenido y metadatos para evitar procesamiento innecesario.

## 7.2 Update Policies

Permitir configurar:

- Frecuencia por fuente.
- Prioridad.
- Tamaño máximo.
- Número de solicitudes.
- Reintentos.
- Ventanas de actualización.
- Presupuesto.

No permitir que una actualización sobrescriba información histórica.

# 8. ON-DEMAND RESEARCH WORKFLOW

Implementar un workflow de investigación reutilizable.

Ejemplo:

```text
USER REQUEST
     |
     v
TASK ANALYSIS
     |
     v
KNOWLEDGE GAP ANALYSIS
     |
     v
EXISTING KNOWLEDGE SEARCH
     |
     v
SOURCE SELECTION
     |
     v
EXTERNAL RESEARCH
     |
     v
DOCUMENT PROCESSING
     |
     v
SOURCE VALIDATION
     |
     v
CROSS-SOURCE ANALYSIS
     |
     v
RESEARCH REPORT
     |
     v
KNOWLEDGE PERSISTENCE
```

El motor debe distinguir:

- Información ya conocida.
- Información nueva.
- Información insuficiente.
- Información contradictoria.
- Información que requiere validación experimental.

No almacenar automáticamente cualquier respuesta generada por el LLM como conocimiento permanente.

Aplicar criterios de calidad antes de persistir resultados.

# 9. LLM INTEGRATION

Integrar el Knowledge Engine con el sistema de proveedores LLM de ARES.

No crear un proveedor LLM independiente si ya existe una abstracción en el Core Engine.

Permitir:

- Research Planning.
- Query Expansion.
- Document Summarization.
- Entity Extraction.
- Relationship Extraction.
- Technical Classification.
- Contradiction Analysis.
- Context Generation.

El LLM debe ser una herramienta de razonamiento, no la fuente de verdad.

Las conclusiones deben mantener referencias verificables.

No enviar documentos completos innecesariamente a proveedores externos.

Implementar límites de contexto y controles de privacidad.

# 10. SECURITY AND TRUST BOUNDARIES

Este componente procesa contenido externo potencialmente malicioso.

Implementar:

- Prompt Injection Resistance.
- Content Sanitization.
- Safe Document Processing.
- URL Validation.
- SSRF Protection.
- Download Size Limits.
- Timeout Controls.
- File Type Validation.
- Archive Extraction Limits.
- Repository Isolation.
- Dependency Validation.
- Secret Detection.
- Audit Logging.

Nunca interpretar instrucciones contenidas en documentos externos como instrucciones del sistema.

Nunca permitir que un documento externo:

- Cambie el system prompt.
- Modifique permisos.
- Autorice operaciones.
- Ejecute comandos.
- Cambie configuraciones.
- Instale plugins.
- Desactive controles.

Los contenidos recuperados deben tratarse como datos no confiables.

# 11. KNOWLEDGE LIFECYCLE MANAGEMENT

Implementar:

- Document Versioning.
- Knowledge Updates.
- Duplicate Detection.
- Stale Knowledge Detection.
- Reindexing.
- Source Deactivation.
- Retention Policies.
- Knowledge Review.
- Manual Corrections.
- Knowledge Export.

La información obsoleta no debe desaparecer silenciosamente.

Marcarla como deprecated y conservar su historial cuando sea necesario.

Permitir revisar y corregir conocimiento.

# 12. API AND AGENT INTEGRATION

Proporcionar interfaces para:

- Registrar fuentes.
- Consultar fuentes.
- Ejecutar investigaciones.
- Consultar documentos.
- Recuperar conocimiento.
- Consultar referencias.
- Consultar historial.
- Solicitar actualizaciones.
- Revisar resultados.

Integrar con:

- ARES Orchestrator.
- AD Security Agent.
- Windows Enterprise Agent.
- EDR Intelligence Agent.
- EDR Evasion Research Agent.
- Offensive Engineering Agent.
- Exploit Research Agent.
- Vulnerability Research Agent.
- Digital Forensics Agent.

Cada agente debe poder consultar conocimiento mediante un contrato común.

No permitir acceso directo e irrestricto a las tablas de almacenamiento.

# 13. OBSERVABILITY

Registrar:

- Fuente consultada.
- Tiempo de respuesta.
- Documentos procesados.
- Errores.
- Duplicados.
- Documentos rechazados.
- Embeddings generados.
- Costes de API.
- Tokens utilizados.
- Resultados recuperados.
- Calidad de recuperación.

Crear métricas para evaluar:

- Freshness.
- Retrieval Precision.
- Retrieval Recall.
- Source Coverage.
- Duplicate Rate.
- Processing Failure Rate.
- Citation Coverage.

No inventar métricas cuando no existan datos suficientes para calcularlas.

# 14. INITIAL IMPLEMENTATION STACK

Priorizar:

- Python 3.12+.
- Pydantic.
- SQLAlchemy.
- Alembic.
- PostgreSQL.
- pgvector.
- HTTPX.
- FastAPI cuando se necesite API.
- Pytest.
- Ruff.
- Mypy.

Evaluar librerías para:

- PDF extraction.
- HTML processing.
- Markdown processing.
- RSS parsing.
- Git integration.
- Embeddings.

No añadir dependencias innecesarias.

Mantener interfaces independientes del proveedor.

No implementar Neo4j inicialmente.

No introducir Redis o Celery inicialmente salvo que exista una justificación técnica.

# 15. REPOSITORY INTEGRATION

Integrar el módulo en la arquitectura existente de ARES.

Antes de desarrollar:

1. Leer CLAUDE.md.
2. Inspeccionar la estructura actual.
3. Revisar ARCHITECTURE.md.
4. Revisar ROADMAP.md.
5. Identificar interfaces existentes.
6. Identificar componentes reutilizables.
7. Evitar duplicar funcionalidades.
8. Proponer los cambios necesarios.

La implementación debe respetar las convenciones existentes.

Estructura conceptual:

```text
ares/
├── knowledge/
│   ├── core/
│   ├── sources/
│   ├── ingestion/
│   ├── processing/
│   ├── validation/
│   ├── storage/
│   ├── embeddings/
│   ├── retrieval/
│   ├── research/
│   ├── scheduler/
│   ├── code_intelligence/
│   ├── lifecycle/
│   └── api/
```

Modificar esta estructura si existe una solución mejor.

# 16. IMPLEMENTATION PHASES

## Phase 1 — Knowledge Foundation

- Interfaces.
- Data models.
- Database architecture.
- Source Registry.
- Configuration.
- Logging.
- Initial tests.

## Phase 2 — Ingestion

- HTTP Fetchers.
- HTML Processor.
- Markdown Processor.
- PDF Processor.
- GitHub Integration.
- Document Normalization.
- Deduplication.

## Phase 3 — Knowledge Storage

- PostgreSQL.
- pgvector.
- Document Versioning.
- Chunk Storage.
- Embedding Abstraction.
- Search Indexes.

## Phase 4 — Retrieval

- Semantic Search.
- Full-Text Search.
- Hybrid Search.
- Metadata Filters.
- Citation Generation.
- Retrieval Evaluation.

## Phase 5 — On-Demand Research

- Research Agent.
- Knowledge Gap Analysis.
- Source Selection.
- Cross-Source Validation.
- Research Reports.
- Knowledge Persistence.

## Phase 6 — Continuous Research

- Scheduler.
- Source Synchronization.
- Change Detection.
- Retry Management.
- Update Policies.
- Monitoring.

## Phase 7 — Code Intelligence

- Repository Inspection.
- Release Tracking.
- Dependency Analysis.
- Code Structure Extraction.
- Documentation Indexing.

## Phase 8 — ARES Integration

- Agent Interfaces.
- Orchestrator Integration.
- Research Task Routing.
- Context Assembly.
- API.
- CLI Commands.

# 17. TESTING REQUIREMENTS

Crear pruebas unitarias, de integración y seguridad.

Casos mínimos:

- Registrar una fuente.
- Consultar una fuente.
- Descargar un documento.
- Procesar HTML.
- Procesar Markdown.
- Procesar PDF.
- Detectar duplicados.
- Versionar documentos.
- Generar chunks.
- Generar embeddings.
- Buscar por similitud.
- Ejecutar búsqueda híbrida.
- Recuperar referencias.
- Detectar información obsoleta.
- Ejecutar una investigación.
- Actualizar una fuente.
- Reanudar una sincronización.
- Rechazar contenido inválido.
- Detectar intentos de prompt injection.
- Bloquear URLs internas no autorizadas.
- Respetar límites de tamaño y tiempo.

Las pruebas no deben depender de Internet.

Utilizar fixtures y mocks.

Crear pruebas de integración opcionales para fuentes reales, separadas de la suite principal.

# 18. ACCEPTANCE CRITERIA

La implementación se considera funcional cuando:

1. ARES puede registrar fuentes.
2. Puede recuperar documentos.
3. Puede procesarlos.
4. Puede almacenar documentos y versiones.
5. Puede generar embeddings.
6. Puede realizar búsquedas.
7. Puede recuperar fragmentos con referencias.
8. Puede ejecutar investigaciones bajo demanda.
9. Puede programar actualizaciones.
10. Puede detectar cambios.
11. Puede registrar errores.
12. Puede integrarse con agentes.
13. Puede identificar conocimiento obsoleto.
14. Tiene pruebas automatizadas.
15. Tiene documentación.

No marcar funcionalidades como implementadas si solo existen interfaces o stubs.

# 19. DEVELOPMENT INSTRUCTIONS

No implementes todas las fases en una única operación.

Primero inspecciona el repositorio.

Después presenta:

- Arquitectura propuesta.
- Componentes existentes reutilizables.
- Nuevos componentes.
- Dependencias necesarias.
- Modelo de datos.
- Plan de implementación.
- Riesgos técnicos.

Una vez definido el plan, comienza Phase 1.

Al terminar cada fase:

1. Ejecuta pruebas.
2. Corrige errores.
3. Actualiza documentación.
4. Actualiza CAPABILITIES.md.
5. Actualiza ROADMAP.md.
6. Documenta decisiones.
7. Presenta resultados.

No inventes resultados.

No instales dependencias sin justificarlas.

No reemplaces componentes existentes sin analizarlos.

No modifiques el núcleo de ARES innecesariamente.

# 20. FINAL OBJECTIVE

El resultado debe ser un sistema de conocimiento autónomo, verificable y extensible que convierta a ARES Enterprise en una plataforma capaz de investigar y mantener conocimiento técnico sobre:

- Active Directory.
- Windows Internals.
- Windows Enterprise.
- EDR/XDR.
- EDR Evasion Research.
- Red Team.
- Purple Team.
- Vulnerability Research.
- Exploit Development.
- Network Security.
- Web Security.
- Cloud Security.
- Digital Forensics.
- Security Engineering.

El conocimiento debe ser reutilizable entre agentes, estar respaldado por fuentes y mantener su procedencia.

ARES debe saber qué conoce, de dónde lo obtuvo, cuándo fue actualizado, qué tan confiable es y qué necesita investigar todavía.

**Begin with repository inspection and Phase 1 implementation.**
