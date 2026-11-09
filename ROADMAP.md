# ARES Enterprise — Roadmap

This roadmap reconciles the phase plans in `CLAUDE.md` (§24) and `ARCHITECTURE.md` (§17).
Where the two documents disagreed on ordering, the safer ordering was chosen: **security
governance is established before AI reasoning, tool execution and any specialized engine.**

The platform is built as a **walking skeleton first** — a thin vertical slice that exercises
every architectural contract end to end — and only then widened across domains.

Legend: ✅ done & verified · 🔨 in progress · ⏳ planned

| Phase | Component | Objective | Status |
|---|---|---|---|
| 0 | Foundation scaffolding | Project layout, `uv` env, tooling (ruff/mypy/pytest), CI, integrity docs | ✅ |
| 1 | Contracts + Core Engine | Typed contracts, abstract interfaces, config, structured logging, module registry, lifecycle | ✅ |
| 2 | Security Governance | Operational profiles, scope management, backend authorization, human approval, append-only audit | ⏳ |
| 3 | AI Reasoning abstraction | Provider-independent LLM + embedding abstraction, fully mockable offline | ⏳ |
| 4 | Orchestrator (skeleton close) | One vertical flow: request → plan → agent stub → knowledge query → evidence → audit | ⏳ |
| 5 | Knowledge Engine | Source registry, ingestion, PostgreSQL+pgvector storage, hybrid retrieval, on-demand research | ⏳ |
| 6 | Tool Integration | Standardized tool adapter pattern + first read-only adapter, routed through governance | ⏳ |
| 7 | Active Directory Engine | Initial read-only AD enumeration and analysis capabilities | ⏳ |
| 8 | Dynamic Capability Engine | Controlled capability lifecycle; never auto-merges to core | ⏳ |
| 9 | Reporting & Deployment | Reporting engine, Docker, CI/CD, release automation | ⏳ |

## Acceptance criteria per phase

A phase is **done** only when its code exists, dependencies are documented, contracts are
defined, relevant tests pass, no known critical bugs remain, documentation is updated, and
behavior is reproducible (`CLAUDE.md` §27).

- **Phase 0** — `ruff`, `mypy` and `pytest` run green against the package; CI workflow passes.
- **Phase 1** — Contracts validate inputs/outputs under tests; the Core Engine starts, registers a module, and shuts down cleanly.
- **Phase 2** — An out-of-scope or unapproved action is **blocked in the backend**, not in a prompt, proven by tests.
- **Phase 3** — Provider swap requires no changes to consuming modules; all tests run offline against a mock provider.
- **Phase 4** — A single CLI command runs end to end through governance and leaves an audit trail.
- **Phase 5** — Register source → process document → generate embeddings → hybrid search → cited result, all offline-testable (`KNOWLEDGE_ENGINE.md` §18).
- **Phase 6** — A tool execution is authorizable, auditable and reproducible in tests.
- **Phase 7** — A passive AD assessment produces findings with evidence in a lab.
- **Phase 8** — A capability passes design → test → review → human approval → registration.
- **Phase 9** — A report is generated and the platform deploys reproducibly.
