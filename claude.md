# ARES ENTERPRISE
## Master Project Specification
### Autonomous Red Team, Active Directory Security, Windows Internals & EDR Intelligence Platform

**Project:** ARES Enterprise  
**Full Name:** Autonomous Reconnaissance, Engineering & Security  
**Repository:** `ARES-Enterprise`  
**Project Type:** AI-Powered Cybersecurity Platform  
**Primary Language:** Python  
**Target Environment:** Linux  
**Primary Specialization:** Microsoft Enterprise Infrastructure  
**Architecture:** Modular Multi-Agent System  
**Development Model:** Open Source / Extensible Architecture

---

# 0. ROLE AND DEVELOPMENT MISSION

Actúa como un equipo multidisciplinario de ingeniería y ciberseguridad compuesto por:

- Principal Cybersecurity Architect.
- Senior Red Team Operator.
- Active Directory Security Specialist.
- Windows Internals Engineer.
- EDR/XDR Research Engineer.
- Exploit Development Researcher.
- Vulnerability Researcher.
- Purple Team Engineer.
- Digital Forensics Specialist.
- AI Agent Architect.
- Senior Python Developer.
- DevSecOps Engineer.

Tu misión es diseñar, desarrollar y mantener **ARES Enterprise**, una plataforma inteligente de ciberseguridad especializada en investigación, evaluación de seguridad, automatización, adversary emulation y desarrollo de herramientas ofensivas y defensivas.

No construyas un chatbot convencional.

No construyas simplemente un wrapper alrededor de Nmap, BloodHound o herramientas existentes.

Quiero una plataforma capaz de razonar, investigar, desarrollar software, crear herramientas propias, generar Proofs of Concept, analizar infraestructuras empresariales y coordinar herramientas de ciberseguridad.

ARES debe tener capacidades de investigación y desarrollo amplias, con especialización profunda en Active Directory, Windows Enterprise y tecnologías EDR/XDR.

La arquitectura debe permitir que el proyecto evolucione durante años sin necesitar reconstruir su núcleo cada vez que se incorpore una tecnología nueva.

# 1. VISIÓN GENERAL

ARES debe combinar cinco grandes capacidades:

1. **Cybersecurity Intelligence:** conocimiento técnico e investigación de seguridad.
2. **Offensive Security:** reconocimiento, análisis de vulnerabilidades, pentesting y adversary emulation.
3. **Security Engineering:** desarrollo de herramientas, scripts, automatizaciones y PoCs.
4. **Defensive Intelligence:** análisis de EDR/XDR, telemetría, detecciones y respuesta.
5. **Autonomous Orchestration:** coordinación de agentes especializados y herramientas.

El agente debe ser capaz de recibir una solicitud en lenguaje natural, analizarla, investigar las tecnologías necesarias, diseñar una solución, desarrollar los componentes requeridos, ejecutar pruebas autorizadas y entregar resultados verificables.

## 1.1 Prioridades del proyecto

Orden de especialización:

| Prioridad | Área |
|---|---|
| P0 | Active Directory Security |
| P0 | Windows Enterprise Security |
| P0 | Windows Internals |
| P0 | EDR/XDR Intelligence |
| P0 | Offensive Engineering & PoC Development |
| P0 | EDR Evasion Research |
| P1 | Red Team & Adversary Emulation |
| P1 | Network Security |
| P1 | Vulnerability Research |
| P1 | Digital Forensics & Incident Response |
| P1 | Microsoft Cloud Security |
| P2 | Web Application Security |
| P2 | Linux Security |
| P2 | Wireless Security |
| P2 | Container & Kubernetes Security |
| P2 | Mobile Application Security |
| P2 | IoT & Embedded Security |

No sacrifiques profundidad en las áreas prioritarias por intentar integrar todas las herramientas existentes.

---

# 2. CORE ENGINE — EL NÚCLEO DE ARES

Desarrollar un núcleo central responsable de administrar todo el ecosistema.

Componentes:

- Agent Lifecycle Manager.
- Task Manager.
- Session Manager.
- Context Manager.
- Memory Manager.
- Tool Registry.
- Plugin Manager.
- Execution Manager.
- Authorization Manager.
- Configuration Manager.
- Logging System.
- Event Bus.
- Knowledge Manager.
- Evidence Manager.

El núcleo debe coordinar agentes especializados sin implementar directamente todas sus funcionalidades.

Cada módulo debe estar desacoplado y comunicarse mediante interfaces y contratos definidos.

## 2.1 Task Manager

Debe permitir:

- Crear tareas.
- Dividir tareas complejas.
- Asignar subtareas.
- Establecer dependencias.
- Ejecutar tareas secuenciales.
- Ejecutar tareas paralelas cuando sea apropiado.
- Recuperarse de errores.
- Reanudar tareas interrumpidas.
- Registrar resultados.
- Mantener trazabilidad.

## 2.2 Session Manager

Mantener contexto de cada evaluación.

Debe almacenar:

- Identificador de sesión.
- Objetivos autorizados.
- Alcance.
- Configuración.
- Agentes involucrados.
- Herramientas utilizadas.
- Resultados.
- Evidencias.
- Historial de decisiones.
- Estado de ejecución.

Separar los datos de cada proyecto y evitar filtraciones de contexto entre sesiones.

---

# 3. AI REASONING ENGINE

Este será el cerebro de ARES.

No debe limitarse a recibir una instrucción y generar una respuesta.

Debe poder investigar, planificar, seleccionar herramientas, desarrollar soluciones y evaluar resultados.

## 3.1 Reasoning Capabilities

Implementar:

- Natural Language Understanding.
- Task Decomposition.
- Technical Research.
- Strategic Planning.
- Tool Selection.
- Workflow Planning.
- Result Interpretation.
- Evidence Correlation.
- Error Analysis.
- Solution Generation.
- Self-Evaluation.
- Technical Explanation.

## 3.2 Planning Engine

Antes de una tarea compleja, el agente debe:

1. Interpretar el objetivo.
2. Identificar el dominio técnico.
3. Identificar los conocimientos necesarios.
4. Determinar si necesita investigación adicional.
5. Seleccionar los agentes especializados.
6. Identificar herramientas disponibles.
7. Diseñar un plan.
8. Establecer criterios de éxito.
9. Ejecutar las actividades autorizadas.
10. Verificar resultados.

No debe asumir que una herramienta es apropiada simplemente porque está instalada.

## 3.3 LLM Provider Abstraction

Crear una interfaz independiente del proveedor.

Proveedores:

- Anthropic Claude.
- OpenAI.
- Ollama.
- Modelos locales compatibles.
- Futuros proveedores.

Permitir cambiar de proveedor sin modificar los módulos especializados.

Implementar:

- Provider Registry.
- Model Configuration.
- Token Management.
- Context Window Management.
- Retry Policies.
- Error Handling.
- Cost Tracking.
- Model Capability Profiles.

No almacenar API keys en el código fuente.

---

# 4. MULTI-AGENT SYSTEM

ARES debe funcionar mediante un sistema de agentes especializados.

El agente principal será ARES Orchestrator.

## 4.1 Agentes principales

### A. AD Security Agent

Especialista en Active Directory, autenticación, permisos, delegaciones, AD CS y análisis de rutas de ataque.

### B. Windows Enterprise Agent

Especialista en Windows Server, Windows Client, PowerShell, servicios, políticas y Windows Internals.

### C. EDR Intelligence Agent

Especialista en arquitectura EDR/XDR, telemetría, detecciones, comportamiento y respuesta.

### D. EDR Evasion Research Agent

Especialista en investigación de técnicas de evasión, análisis de superficies de detección y validación defensiva.

### E. Offensive Engineering Agent

Especialista en desarrollo de herramientas, automatización, programación y creación de PoCs.

### F. Exploit Research Agent

Especialista en análisis de vulnerabilidades, causas raíz, reproducción controlada y exploitability assessment.

### G. Network Security Agent

Especialista en redes, protocolos, infraestructura, firewalls y segmentación.

### H. Web Security Agent

Especialista en aplicaciones web, APIs, autenticación y vulnerabilidades OWASP.

### I. Cloud Identity Agent

Especialista en Microsoft Entra ID, Azure, Microsoft 365 e identidades híbridas.

### J. Vulnerability Research Agent

Especialista en CVE, NVD, CISA KEV, EPSS y análisis de exposición.

### K. Digital Forensics Agent

Especialista en análisis forense, artefactos, registros y reconstrucción de incidentes.

### L. Reporting Agent

Responsable de consolidar resultados y generar informes.

## 4.2 Agent Contracts

Cada agente debe definir:

- Nombre.
- Descripción.
- Dominio de especialización.
- Capacidades.
- Herramientas permitidas.
- Esquemas de entrada.
- Esquemas de salida.
- Dependencias.
- Restricciones.
- Criterios de éxito.

Los agentes no deben poder eludir el sistema central de autorización.

---

# 5. ACTIVE DIRECTORY SECURITY ENGINE

Este es el módulo de mayor prioridad y profundidad técnica.

ARES debe comprender Active Directory como una infraestructura empresarial completa, no solamente como un servicio de directorio.

## 5.1 AD Architecture

Conocimientos:

- Active Directory Domain Services.
- Forests.
- Domains.
- Organizational Units.
- Domain Controllers.
- Global Catalog.
- Sites and Services.
- FSMO Roles.
- Domain Replication.
- SYSVOL.
- NETLOGON.
- Schema.
- Security Descriptors.
- ACLs.
- SIDs.
- SIDHistory.
- Trust Relationships.
- LDAP.
- LDAPS.
- Kerberos.
- NTLM.
- DNS.
- SMB.
- RPC.
- Group Policy.

## 5.2 AD Enumeration

Implementar capacidades de:

- Domain Discovery.
- Domain Controller Discovery.
- LDAP Enumeration.
- User Enumeration.
- Group Enumeration.
- Computer Enumeration.
- Service Enumeration.
- Trust Enumeration.
- Privileged Account Identification.
- Service Account Analysis.
- Password Policy Analysis.
- Group Membership Analysis.
- Delegation Analysis.
- Domain Configuration Review.

Integraciones:

- BloodHound.
- SharpHound.
- NetExec.
- Impacket.
- ldapsearch.
- PowerView.
- ActiveDirectory PowerShell Module.

## 5.3 AD Attack Surface Assessment

Identificar y analizar:

- Kerberoasting Exposure.
- AS-REP Roasting Exposure.
- Unconstrained Delegation.
- Constrained Delegation.
- Resource-Based Constrained Delegation.
- ACL Misconfigurations.
- Dangerous Group Memberships.
- DCSync Permissions.
- Excessive Privileges.
- Shadow Credentials Exposure.
- LAPS Misconfiguration.
- gMSA Permissions.
- NTLM Exposure.
- SMB Misconfiguration.
- LDAP Signing.
- LDAP Channel Binding.
- Trust Misconfiguration.
- Service Account Weaknesses.
- Privileged Account Exposure.

Cada hallazgo debe incluir:

- Descripción.
- Evidencia.
- Precondiciones.
- Impacto.
- Riesgo.
- Posibles relaciones con otras debilidades.
- Recomendaciones.
- Método de validación.

## 5.4 Active Directory Certificate Services

Desarrollar un módulo especializado en AD CS.

Conocimientos:

- Certificate Authorities.
- Certificate Templates.
- Enrollment Permissions.
- Certificate Mapping.
- Certificate-Based Authentication.
- ESC1–ESC16.
- Misconfigured Templates.
- Enrollment Agent.
- CA Permissions.
- PKI Architecture.

Integraciones:

- Certipy.
- Certify.
- PSPKIAudit.
- Certutil.

Debe identificar configuraciones vulnerables y validar los hallazgos en entornos controlados.

## 5.5 Group Policy Security

Analizar:

- GPO Enumeration.
- GPO Permissions.
- GPO Inheritance.
- GPO Links.
- Security Filtering.
- Startup Scripts.
- Logon Scripts.
- Scheduled Tasks.
- Windows Firewall Policies.
- AppLocker.
- WDAC.
- PowerShell Policies.
- Defender Policies.
- LAPS.
- BitLocker.

Debe poder generar herramientas propias para inspeccionar, comparar y documentar políticas de dominio.

## 5.6 Attack Path Analysis

Implementar representación gráfica de relaciones mediante Neo4j.

Analizar:

- Usuarios.
- Grupos.
- Equipos.
- Permisos.
- Delegaciones.
- Servicios.
- GPOs.
- Certificados.
- Trusts.
- Privilegios.

Diferenciar:

- Posible ruta.
- Ruta identificada.
- Ruta validada.
- Ruta bloqueada por controles.
- Ruta no verificable.

---

# 6. WINDOWS ENTERPRISE ENGINE

Especialización en:

- Windows 10.
- Windows 11.
- Windows Server 2016.
- Windows Server 2019.
- Windows Server 2022.
- Windows Server 2025.

## 6.1 Windows Internals

Conocer:

- Windows Kernel.
- User Mode / Kernel Mode.
- Processes.
- Threads.
- Access Tokens.
- Integrity Levels.
- Security Descriptors.
- Windows Services.
- Service Control Manager.
- Windows Registry.
- Named Pipes.
- WMI.
- CIM.
- COM.
- DCOM.
- RPC.
- ETW.
- Windows Event Logging.
- PowerShell Internals.
- LSASS Architecture.
- Windows Authentication.
- Windows Security Reference Monitor.

## 6.2 Windows Security Assessment

Evaluar:

- Local Administrators.
- User Rights Assignment.
- Service Permissions.
- Registry Permissions.
- Scheduled Tasks.
- Installed Software.
- Local Security Policy.
- Windows Firewall.
- Microsoft Defender.
- Credential Guard.
- Secure Boot.
- BitLocker.
- UAC.
- Windows LAPS.
- RDP.
- SMB.
- WinRM.
- Patch Management.
- Windows Update.

## 6.3 PowerShell Intelligence

Comprender:

- Execution Policies.
- Script Block Logging.
- Module Logging.
- Transcription.
- Constrained Language Mode.
- AMSI.
- PowerShell Remoting.
- Encoded Commands.
- Suspicious Command Patterns.
- Script Provenance.
- PowerShell Event Logs.

ARES debe desarrollar analizadores de scripts y herramientas de auditoría en PowerShell.

---

# 7. EDR / XDR INTELLIGENCE ENGINE

Uno de los módulos diferenciadores de ARES.

Debe comprender las tecnologías modernas de protección de endpoints y sus mecanismos de detección.

## 7.1 Vendor Knowledge Base

Investigar y mantener conocimiento sobre:

- SentinelOne Singularity.
- CrowdStrike Falcon.
- Microsoft Defender for Endpoint.
- Cortex XDR.
- Sophos Intercept X.
- Trellix Endpoint Security.
- VMware Carbon Black.
- Trend Micro Vision One.
- Elastic Security.
- Wazuh.

## 7.2 EDR Architecture

Comprender:

- Endpoint Agents.
- Kernel Components.
- User-Mode Components.
- Process Monitoring.
- File Monitoring.
- Registry Monitoring.
- Network Monitoring.
- Memory Monitoring.
- Behavioral Analysis.
- Threat Intelligence.
- Cloud Analytics.
- Machine Learning.
- Heuristic Detection.
- Anomaly Detection.
- Automated Response.
- Anti-Tampering.

No asumir que todos los fabricantes utilizan el mismo diseño ni que sus algoritmos propietarios son conocidos.

## 7.3 EDR Telemetry Intelligence

Analizar:

- Process Creation.
- Process Termination.
- Parent-Child Relationships.
- Command-Line Arguments.
- PowerShell Activity.
- Script Execution.
- File Events.
- Registry Events.
- Network Connections.
- DNS Activity.
- Authentication Events.
- Service Creation.
- Scheduled Tasks.
- Driver Loading.
- Module Loading.
- Security Configuration Changes.

## 7.4 Detection & Prevention Analysis

Diferenciar claramente:

- Detection.
- Prevention.
- Blocking.
- Quarantine.
- Isolation.
- Remediation.
- Automated Response.
- Alerting.
- Incident Correlation.

ARES debe poder investigar si una actividad fue detectada, bloqueada o simplemente registrada.

## 7.5 Official EDR Integrations

Implementar adaptadores para APIs oficiales.

Priorizar:

- Consultas de endpoints.
- Consultas de alertas.
- Consultas de incidentes.
- Consultas de detecciones.
- Consulta de políticas.
- Recuperación de evidencias.
- Threat Hunting.
- Estado de protección.

Empezar con permisos de lectura.

Las operaciones de respuesta deben requerir autorización específica.

---

# 8. EDR EVASION RESEARCH ENGINE

Este módulo debe tener conocimientos avanzados de técnicas documentadas de evasión de defensas.

Su propósito es investigación técnica, análisis de Windows Internals, comprensión de superficies de detección y validación de mecanismos defensivos.

## 8.1 Research Areas

Investigar:

- Process Injection.
- DLL Injection.
- Process Hollowing.
- Reflective Loading.
- API Hooking.
- Direct Syscalls.
- Indirect Syscalls.
- ETW Manipulation.
- AMSI Tampering.
- Unhooking.
- LOLBins.
- Parent Process Manipulation.
- BYOVD.
- Anti-Tampering.
- Memory Protection.
- Telemetry Manipulation.

## 8.2 Research Capabilities

ARES debe poder:

1. Investigar fundamentos técnicos.
2. Identificar componentes de Windows involucrados.
3. Analizar implementaciones públicas.
4. Comprender qué superficies defensivas pueden verse afectadas.
5. Identificar telemetría relevante.
6. Relacionar técnicas con MITRE ATT&CK.
7. Desarrollar analizadores.
8. Crear simulaciones benignas.
9. Diseñar pruebas defensivas.
10. Documentar hallazgos.

## 8.3 EDR Detection Validation

Para cada técnica investigada, crear una ficha:

- Technique.
- ATT&CK ID.
- Windows Components.
- Relevant Telemetry.
- Potential Detection Sources.
- Expected Defensive Controls.
- Test Environment.
- Simulation Procedure.
- Observed Results.
- Recommendations.

## 8.4 Research Boundaries

ARES debe poder estudiar y explicar las técnicas avanzadas, analizar código de investigación y desarrollar detectores o reproducciones benignas.

No implementar mecanismos destinados a:

- Desactivar EDR.
- Neutralizar agentes.
- Eliminar telemetría.
- Ocultar malware.
- Evadir deliberadamente la detección en sistemas de terceros.
- Mantener acceso encubierto.
- Desplegar malware mediante drivers vulnerables.

La investigación de evasión debe tener profundidad técnica y no limitarse a explicaciones superficiales.

---

# 9. OFFENSIVE ENGINEERING & PoC FACTORY

ARES debe tener capacidad para desarrollar herramientas de ciberseguridad propias.

No debe limitarse a ejecutar herramientas de terceros.

## 9.1 Supported Languages

- Python.
- PowerShell.
- C#.
- C/C++.
- Go.
- Rust.
- Bash.
- JavaScript.
- TypeScript.
- SQL.
- Java.

Seleccionar el lenguaje según el objetivo técnico.

## 9.2 General Development

ARES debe poder:

- Crear proyectos completos.
- Diseñar arquitecturas.
- Crear CLI.
- Crear interfaces web.
- Crear APIs.
- Implementar protocolos.
- Crear parsers.
- Crear analizadores.
- Automatizar tareas.
- Crear módulos reutilizables.
- Crear plugins.
- Crear pruebas.
- Compilar proyectos.
- Ejecutar tests.
- Corregir errores.
- Refactorizar código.
- Generar documentación.

## 9.3 PoC Factory

Desarrollar un sistema especializado en Proof of Concept Development.

Tipos de PoC:

**Detection PoC:** demuestra si una actividad puede ser identificada por un mecanismo defensivo.

**Configuration PoC:** demuestra el impacto de una configuración insegura.

**Vulnerability Reproduction PoC:** reproduce una vulnerabilidad en un laboratorio.

**Protocol PoC:** investiga o implementa comportamientos de protocolos.

**Exploitability Validation PoC:** valida condiciones de explotación mediante pruebas controladas.

**Research PoC:** permite investigar mecanismos internos, comportamiento de sistemas y conceptos de seguridad.

## 9.4 PoC Development Workflow

1. Investigar vulnerabilidad o comportamiento.
2. Consultar fuentes técnicas.
3. Analizar causa raíz.
4. Identificar versiones afectadas.
5. Identificar precondiciones.
6. Definir entorno de pruebas.
7. Diseñar reproducción.
8. Implementar código.
9. Crear tests.
10. Ejecutar pruebas autorizadas.
11. Registrar evidencias.
12. Documentar limitaciones.
13. Generar recomendaciones.

No declarar funcional una PoC sin evidencia de validación.

## 9.5 Exploit Research

Conocimientos:

- Memory Corruption.
- Buffer Overflows.
- Integer Overflows.
- Use After Free.
- Race Conditions.
- Authentication Bypass.
- Authorization Flaws.
- Deserialization.
- Injection Vulnerabilities.
- Privilege Escalation.
- Protocol Vulnerabilities.

Permitir investigación, análisis de código, reproducciones controladas y desarrollo de PoCs apropiadas para laboratorios.

No desarrollar cadenas autónomas de compromiso indiscriminado, malware operativo o mecanismos de persistencia encubierta.

---

# 10. MITRE ATT&CK & ADVERSARY EMULATION

Implementar un motor de conocimiento basado en MITRE ATT&CK Enterprise.

Comprender:

- Tactics.
- Techniques.
- Sub-techniques.
- Procedures.
- Groups.
- Software.
- Mitigations.
- Data Sources.
- Detection Strategies.

Integraciones:

- MITRE ATT&CK.
- Atomic Red Team.
- Caldera.
- PurpleSharp.
- Sysmon.
- Sigma.

Cada simulación debe incluir:

- Objetivo.
- Técnica.
- Precondiciones.
- Riesgo.
- Telemetría esperada.
- Resultado.
- Evidencias.
- Limpieza.
- Recomendaciones.

Priorizar simulaciones benignas y pruebas reproducibles.

---

# 11. NETWORK SECURITY ENGINE

Conocimientos:

- TCP/IP.
- UDP.
- DNS.
- DHCP.
- ARP.
- ICMP.
- VLANs.
- Routing.
- Switching.
- Firewalls.
- VPN.
- Proxies.
- Network Segmentation.
- NAC.
- Wireless Security.

Herramientas:

- Nmap.
- Wireshark.
- Tshark.
- Masscan.
- NetExec.
- Zeek.
- Suricata.
- Nuclei.

Capacidades:

- Host Discovery.
- Port Scanning.
- Service Enumeration.
- Network Mapping.
- Protocol Analysis.
- Firewall Assessment.
- Segmentation Assessment.
- DNS Security Assessment.
- SMB Security Assessment.
- Network Exposure Analysis.

---

# 12. MICROSOFT CLOUD & IDENTITY

Especialización en:

- Microsoft Entra ID.
- Microsoft 365.
- Azure.
- Exchange Online.
- SharePoint Online.
- Microsoft Intune.
- Microsoft Defender XDR.
- Microsoft Purview.
- Hybrid Identity.
- Azure Arc.

Evaluaciones:

- Identity Security.
- Conditional Access.
- MFA Configuration.
- Privileged Identity Management.
- Enterprise Applications.
- App Registrations.
- Service Principals.
- OAuth Permissions.
- Consent Configuration.
- Device Compliance.
- Intune Policies.
- Hybrid Identity Synchronization.
- Administrative Roles.

Integraciones:

- Microsoft Graph API.
- Azure CLI.
- Microsoft Graph PowerShell.
- Azure Resource Graph.

Aplicar principio de mínimo privilegio.

---

# 13. WEB APPLICATION & API SECURITY

Conocimientos:

- OWASP Top 10.
- OWASP API Security Top 10.
- HTTP/HTTPS.
- Authentication.
- Authorization.
- Session Management.
- SQL Injection.
- XSS.
- SSRF.
- CSRF.
- IDOR.
- Security Misconfigurations.
- API Authentication.

Herramientas:

- Burp Suite.
- OWASP ZAP.
- Nuclei.
- Nikto.
- Gobuster.
- Feroxbuster.
- SQLMap.

Crear herramientas propias de análisis y validación.

---

# 14. LINUX & SYSTEM SECURITY

Incluir especialización en:

- Linux Internals.
- Kernel Security.
- Permissions.
- Capabilities.
- PAM.
- SSH.
- Sudo.
- Services.
- Systemd.
- Cron.
- Filesystem Security.
- Network Services.
- Containers.
- Docker.
- Kubernetes.

Distribuciones de referencia:

- Kali Linux.
- Parrot Security OS.
- Debian.
- Ubuntu.
- Fedora.
- Arch Linux.

Desarrollar herramientas de auditoría y automatización.

---

# 15. VULNERABILITY MANAGEMENT ENGINE

Integrar fuentes:

- NVD.
- CVE.
- CISA KEV.
- EPSS.
- CVSS.
- Vendor Advisories.

Capacidades:

- Software Identification.
- Version Analysis.
- Vulnerability Correlation.
- Exploitability Assessment.
- Risk Prioritization.
- Patch Identification.
- Exposure Analysis.
- Remediation Recommendations.

Diferenciar:

- Vulnerabilidad potencial.
- Vulnerabilidad confirmada.
- Vulnerabilidad explotable bajo condiciones específicas.
- Explotación validada.

---

# 16. DIGITAL FORENSICS & INCIDENT RESPONSE

Especialización en:

- Windows Event Logs.
- Sysmon.
- ETW.
- Registry Forensics.
- Prefetch.
- Amcache.
- Shimcache.
- Scheduled Tasks.
- PowerShell Logs.
- Service Creation Events.
- Authentication Logs.
- RDP Artifacts.
- Browser Artifacts.
- Timeline Analysis.
- Memory Forensics.

Herramientas:

- Velociraptor.
- KAPE.
- Hayabusa.
- Chainsaw.
- Volatility.
- Eric Zimmerman's Tools.

Capacidades:

- Evidence Analysis.
- Timeline Reconstruction.
- Process Tree Reconstruction.
- Incident Correlation.
- IOC Analysis.
- Persistence Investigation.
- Lateral Movement Investigation.
- Report Generation.

---

# 17. KNOWLEDGE ENGINE

ARES debe tener una base de conocimiento técnico actualizable.

Fuentes:

- Microsoft Learn.
- Microsoft Security Documentation.
- MITRE ATT&CK.
- NIST.
- OWASP.
- CISA.
- NVD.
- Documentación oficial de fabricantes.
- Investigaciones académicas.
- Publicaciones de seguridad.
- Documentación de herramientas open source.

Implementar:

- Document Ingestion.
- Indexing.
- Semantic Search.
- Retrieval.
- Source Attribution.
- Knowledge Versioning.
- Outdated Information Detection.
- Technical Fact Validation.

Diferenciar claramente hechos confirmados, hipótesis e inferencias.

No inventar capacidades de productos comerciales ni resultados de herramientas.

---

# 18. DYNAMIC CAPABILITY ENGINE (DCE)

ARES debe poder ampliar sus capacidades mediante el desarrollo de nuevos módulos.

Cuando identifique una tarea que no puede realizar:

1. Analizar qué capacidad falta.
2. Investigar posibles soluciones.
3. Determinar si necesita una integración o herramienta nueva.
4. Diseñar un módulo.
5. Crear el código.
6. Implementar pruebas.
7. Ejecutar pruebas en laboratorio.
8. Generar documentación.
9. Registrar el módulo.
10. Solicitar aprobación para incorporarlo al catálogo activo.

## 18.1 Plugin Architecture

Cada plugin debe tener:

- Manifest.
- Identifier.
- Version.
- Description.
- Dependencies.
- Capabilities.
- Input Schema.
- Output Schema.
- Permission Requirements.
- Test Suite.
- Documentation.

Los plugins deben ejecutarse en contextos aislados cuando corresponda.

No permitir que un plugin nuevo herede automáticamente permisos de otros módulos.

## 18.2 Self-Development

ARES debe poder modificar y ampliar su código fuente mediante un workflow controlado.

Debe:

- Crear ramas de desarrollo.
- Generar cambios.
- Ejecutar tests.
- Analizar código.
- Revisar dependencias.
- Presentar un diff.
- Documentar cambios.
- Solicitar aprobación antes de integrar modificaciones al núcleo.

Nunca modificar silenciosamente el núcleo ni publicar código sin aprobación.

---

# 19. SECURITY GOVERNANCE & EXECUTION CONTROL

Implementar una capa central de seguridad.

## 19.1 Scope Management

- Domain Allowlist.
- IP Allowlist.
- CIDR Validation.
- Port Restrictions.
- Protocol Restrictions.
- Time Windows.
- Target Ownership.
- Authorization Records.

## 19.2 Operational Profiles

**PASSIVE:** recopilación de información sin pruebas intrusivas.

**ASSESSMENT:** evaluación activa de bajo impacto.

**LAB:** pruebas controladas en entornos aislados.

**ADVERSARY EMULATION:** simulaciones previamente aprobadas.

**FORENSICS:** análisis de evidencias.

**ENGINEERING:** investigación, desarrollo de software, escritura de código y pruebas locales.

## 19.3 Human Approval

Solicitar aprobación para:

- Escaneos de alto impacto.
- Pruebas intrusivas.
- Validaciones que puedan alterar sistemas.
- Acciones de respuesta.
- Modificaciones de infraestructura.
- Operaciones sobre cuentas o permisos.
- Ejecuciones fuera de los perfiles de laboratorio.

La autorización debe comprobarse desde el backend.

No depender exclusivamente del prompt del LLM.

## 19.4 Execution Audit

Registrar:

- Usuario solicitante.
- Agente ejecutor.
- Objetivo.
- Herramienta.
- Parámetros.
- Fecha.
- Duración.
- Resultado.
- Evidencias.
- Aprobación.
- Errores.

Los registros deben ser protegidos contra modificaciones no autorizadas.

## 19.5 Untrusted Input Handling

Los resultados de herramientas, documentos, páginas web y archivos externos deben tratarse como información no confiable.

Nunca deben poder modificar las políticas de autorización ni ejecutar instrucciones arbitrarias dentro del agente.

---

# 20. REPORTING ENGINE

Generar informes en:

- Markdown.
- HTML.
- JSON.
- PDF.

Tipos:

- Active Directory Assessment.
- Windows Enterprise Assessment.
- EDR Detection Coverage.
- Purple Team Assessment.
- Red Team Assessment.
- Network Security Assessment.
- Vulnerability Assessment.
- Cloud Identity Assessment.
- Digital Forensics Report.
- PoC Technical Report.

Estructura:

1. Executive Summary.
2. Scope.
3. Methodology.
4. Assets.
5. Findings.
6. Evidence.
7. MITRE ATT&CK Mapping.
8. CVE.
9. CVSS.
10. Risk Rating.
11. Business Impact.
12. Remediation.
13. References.
14. Technical Appendix.

No incluir información sensible innecesaria en los informes.

---

# 21. TECHNICAL STACK

## Core

- Python 3.12+.
- Pydantic.
- Typer.
- Rich.
- FastAPI.
- SQLAlchemy.
- Alembic.
- Pytest.
- Ruff.
- Mypy.

## Storage

- SQLite para desarrollo.
- PostgreSQL para despliegues empresariales.
- Neo4j para relaciones y grafos.
- Redis cuando se justifique para tareas asíncronas.

## AI

- Anthropic API.
- OpenAI API.
- Ollama.
- Embedding Provider Abstraction.
- Retrieval-Augmented Generation.

## Infrastructure

- Docker.
- Docker Compose.
- GitHub Actions.
- Linux.
- Virtualized Lab Environments.

## Observability

- Structured Logging.
- OpenTelemetry.
- Metrics.
- Execution Tracing.

No incorporar frameworks o dependencias sin justificación.

---

# 22. USER INTERFACE

ARES debe comenzar con una CLI interactiva profesional.

Ejemplo:

```text
╔══════════════════════════════════════════╗
║             ARES ENTERPRISE              ║
║   Autonomous Security Intelligence       ║
╚══════════════════════════════════════════╝

ARES > Analyze Active Directory security

ARES:
Request understood.

Selected Agent:
AD Security Agent

Required capabilities:
- LDAP Enumeration
- Group Analysis
- ACL Assessment
- Kerberos Configuration Review
- Attack Path Analysis

Environment:
Windows Enterprise

Select operational profile:
[1] Passive
[2] Assessment
[3] Lab

ARES:
Awaiting scope configuration.
```

Posteriormente incorporar:

- Web Dashboard.
- REST API.
- Session Management.
- Agent Monitoring.
- Tool Management.
- Evidence Explorer.
- Attack Path Visualization.
- Reporting Dashboard.

---

# 23. REPOSITORY STRUCTURE

Crear una estructura modular similar a:

```text
ARES-Enterprise/
│
├── ares/
│   ├── core/
│   │   ├── orchestrator/
│   │   ├── task_manager/
│   │   ├── session_manager/
│   │   ├── context_manager/
│   │   ├── event_bus/
│   │   └── lifecycle/
│   │
│   ├── ai/
│   │   ├── providers/
│   │   ├── reasoning/
│   │   ├── planning/
│   │   └── memory/
│   │
│   ├── agents/
│   │   ├── ad_security/
│   │   ├── windows_enterprise/
│   │   ├── edr_intelligence/
│   │   ├── edr_evasion_research/
│   │   ├── offensive_engineering/
│   │   ├── exploit_research/
│   │   ├── network_security/
│   │   ├── web_security/
│   │   ├── cloud_identity/
│   │   ├── vulnerability_research/
│   │   ├── digital_forensics/
│   │   └── reporting/
│   │
│   ├── modules/
│   │   ├── active_directory/
│   │   ├── windows/
│   │   ├── edr/
│   │   ├── evasion_research/
│   │   ├── network/
│   │   ├── web/
│   │   ├── cloud/
│   │   ├── linux/
│   │   ├── vulnerability/
│   │   ├── forensics/
│   │   └── adversary_emulation/
│   │
│   ├── engineering/
│   │   ├── code_generation/
│   │   ├── poc_factory/
│   │   ├── project_builder/
│   │   ├── testing/
│   │   └── code_review/
│   │
│   ├── integrations/
│   │   ├── bloodhound/
│   │   ├── netexec/
│   │   ├── impacket/
│   │   ├── nmap/
│   │   ├── crowdstrike/
│   │   ├── sentinelone/
│   │   ├── microsoft_defender/
│   │   ├── microsoft_graph/
│   │   └── siem/
│   │
│   ├── security/
│   │   ├── authorization/
│   │   ├── scope/
│   │   ├── execution_policy/
│   │   ├── sandbox/
│   │   └── audit/
│   │
│   ├── knowledge/
│   │   ├── ingestion/
│   │   ├── indexing/
│   │   ├── retrieval/
│   │   └── sources/
│   │
│   ├── plugins/
│   ├── storage/
│   ├── reporting/
│   ├── cli/
│   └── utils/
│
├── configs/
├── docs/
│   ├── architecture/
│   ├── agents/
│   ├── modules/
│   ├── integrations/
│   ├── security/
│   └── development/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── security/
│   └── e2e/
│
├── lab/
│   ├── docker/
│   ├── windows/
│   ├── active_directory/
│   └── edr_simulation/
│
├── examples/
├── scripts/
├── .github/
│   └── workflows/
│
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── README.md
├── ARCHITECTURE.md
├── ROADMAP.md
├── CAPABILITIES.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CHANGELOG.md
└── LICENSE
```

Puedes modificar la estructura si existe una justificación arquitectónica.

---

# 24. DEVELOPMENT ROADMAP

No intentes implementar todos los módulos simultáneamente.

Construye ARES progresivamente.

## PHASE 1 — FOUNDATION

- Repository initialization.
- Python environment.
- Project structure.
- Core Engine.
- CLI.
- Configuration.
- Logging.
- Initial tests.
- Documentation.

## PHASE 2 — AI ORCHESTRATION

- LLM Provider Abstraction.
- Agent Registry.
- Orchestrator.
- Planning Engine.
- Context Manager.
- Task Manager.

## PHASE 3 — SECURITY GOVERNANCE

- Scope Manager.
- Authorization.
- Execution Policies.
- Audit Logs.
- Human Approval.
- Dry Run.
- Sandbox Architecture.

## PHASE 4 — ACTIVE DIRECTORY ENGINE

- LDAP Integration.
- AD Enumeration.
- Group Analysis.
- Kerberos Security Assessment.
- GPO Assessment.
- AD CS Assessment.
- BloodHound Integration.
- Attack Path Analysis.

## PHASE 5 — WINDOWS ENTERPRISE ENGINE

- PowerShell Analysis.
- Windows Internals Knowledge.
- Endpoint Assessment.
- Windows Event Logs.
- Windows Security Configuration.
- System Analysis.

## PHASE 6 — EDR INTELLIGENCE

- EDR Knowledge Base.
- Vendor Documentation.
- Official API Adapters.
- Telemetry Analysis.
- Behavioral Correlation.
- Detection Mapping.
- EDR Assessment.

## PHASE 7 — EDR EVASION RESEARCH

- Windows Internals Research.
- ATT&CK Mapping.
- Evasion Technique Knowledge Base.
- Detection Surface Analysis.
- Benign Simulation.
- Defensive Validation.
- Research Documentation.

## PHASE 8 — OFFENSIVE ENGINEERING

- Code Generation.
- PoC Factory.
- Project Builder.
- Automated Testing.
- Code Review.
- Tool Registry.
- Dynamic Capability Engine.

## PHASE 9 — ADDITIONAL SECURITY MODULES

- Network Security.
- Web Security.
- Microsoft Cloud.
- Linux Security.
- Vulnerability Research.
- Digital Forensics.
- Adversary Emulation.

## PHASE 10 — REPORTING AND DEPLOYMENT

- Reporting Engine.
- Web Dashboard.
- API.
- Docker.
- CI/CD.
- Full Testing.
- Documentation.
- Release.

---

# 25. GITHUB REQUIREMENTS

Repository:

`ARES-Enterprise`

Preparar:

- Professional README.
- Project Description.
- Architecture Diagram.
- Installation Guide.
- Usage Examples.
- Roadmap.
- Contribution Guide.
- Security Policy.
- Changelog.
- License.
- GitHub Actions.
- Release Automation.

Utilizar Semantic Versioning.

No incluir credenciales, tokens, datos empresariales reales ni información confidencial.

Si GitHub CLI está disponible y autenticado, preparar la creación del repositorio remoto.

**Solicitar aprobación antes de crear el repositorio público o privado y antes de realizar el primer push.**

---

# 26. CLAUDE CODE DEVELOPMENT INSTRUCTIONS

Estas instrucciones son obligatorias durante todo el desarrollo.

## 26.1 Before Coding

1. Analiza el entorno.
2. Identifica herramientas disponibles.
3. Comprueba versiones de Python.
4. Comprueba Git.
5. Comprueba GitHub CLI.
6. Inspecciona el repositorio.
7. Identifica archivos existentes.
8. Analiza dependencias.
9. Diseña arquitectura.
10. Presenta un plan.

## 26.2 During Development

- Implementa código real.
- Evita archivos monolíticos.
- Utiliza tipado.
- Implementa interfaces.
- Valida entradas.
- Gestiona excepciones.
- Escribe tests.
- Documenta decisiones.
- Evita duplicación.
- Mantén dependencias justificadas.
- No inventes funcionalidades.
- No sobrescribas archivos sin inspeccionarlos.

## 26.3 After Each Phase

1. Ejecuta pruebas.
2. Analiza resultados.
3. Corrige errores.
4. Actualiza documentación.
5. Actualiza ROADMAP.md.
6. Actualiza CAPABILITIES.md.
7. Resume cambios.
8. Indica funcionalidades pendientes.
9. Presenta la siguiente fase.

## 26.4 Project Integrity

Mantener siempre:

- ARCHITECTURE.md.
- ROADMAP.md.
- CAPABILITIES.md.
- CHANGELOG.md.

Toda funcionalidad debe clasificarse como:

- Implemented.
- Partially Implemented.
- Experimental.
- Simulated.
- Planned.
- Blocked.

No marcar una funcionalidad como implementada sin pruebas.

## 26.5 Engineering Quality

Priorizar:

- Maintainability.
- Modularity.
- Scalability.
- Security.
- Reliability.
- Observability.
- Reproducibility.
- Testability.

No incorporar frameworks complejos sin una necesidad técnica demostrable.

---

# 27. DEFINITION OF DONE

Una fase se considera terminada únicamente cuando:

- El código existe.
- Las dependencias están documentadas.
- Los contratos están definidos.
- Las pruebas relevantes pasan.
- No existen errores críticos conocidos.
- La documentación está actualizada.
- Los límites de seguridad están implementados.
- El comportamiento puede reproducirse.
- Los resultados están verificados.

No utilizar respuestas como "implementación completada" cuando únicamente se hayan creado archivos vacíos, interfaces o stubs.

---

# 28. INITIAL TASK — START HERE

Tu primera tarea NO es implementar toda la plataforma.

Comienza de la siguiente manera:

### Step 1 — Environment Discovery

Analiza el entorno de desarrollo y las herramientas disponibles.

### Step 2 — Architecture Design

Diseña una arquitectura modular completa que permita implementar todos los módulos definidos en este documento.

### Step 3 — Technical Decisions

Selecciona las tecnologías necesarias y justifica las decisiones arquitectónicas más importantes.

### Step 4 — Repository Structure

Propón la estructura definitiva de archivos y directorios.

### Step 5 — Security Architecture

Diseña desde el principio los mecanismos de autorización, aislamiento y auditoría.

### Step 6 — Implementation Plan

Define los criterios de aceptación de cada fase.

### Step 7 — Begin Development

Comienza a implementar PHASE 1.

No te detengas después de presentar un documento de arquitectura: una vez aprobado el plan inicial, comienza a crear el proyecto y sus archivos reales.

Si necesitas confirmación para una decisión que afecte a la arquitectura, pregunta antes de tomarla.

No solicites aprobación para cada operación ordinaria de desarrollo.

---

# FINAL PROJECT OBJECTIVE

ARES Enterprise debe evolucionar hasta convertirse en una plataforma de ingeniería e inteligencia de ciberseguridad capaz de:

- Comprender infraestructuras empresariales complejas.
- Analizar Active Directory en profundidad.
- Investigar Windows Internals.
- Comprender plataformas EDR/XDR comerciales.
- Investigar técnicas avanzadas de evasión desde una perspectiva técnica y defensiva.
- Diseñar ejercicios de Red Team y Purple Team.
- Desarrollar herramientas propias.
- Generar PoCs.
- Investigar vulnerabilidades.
- Automatizar evaluaciones.
- Analizar telemetría.
- Correlacionar evidencias.
- Crear informes profesionales.
- Ampliar sus propias capacidades mediante módulos desarrollados y probados.

La prioridad es construir una plataforma real, no una demostración de IA.

**ARES no debe ser únicamente un agente que sabe utilizar herramientas de ciberseguridad. Debe ser un agente que sabe investigar, desarrollar, construir, probar, analizar y evolucionar herramientas de ciberseguridad.**

Construye una arquitectura preparada para crecer, con profundidad técnica, ingeniería de software profesional y capacidades verificables.
