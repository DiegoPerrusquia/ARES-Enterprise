# ARES Enterprise — Capabilities Status

This is the authoritative, honest record of what exists. Per `CLAUDE.md` §26.4, every
capability is classified as one of:

- **Implemented** — real, working code with passing tests.
- **Partially Implemented** — usable but incomplete.
- **Experimental** — works in controlled conditions, not hardened.
- **Simulated** — mock/stub behavior for development only.
- **Planned** — specified but no functional code yet.
- **Blocked** — cannot proceed due to an external dependency or decision.

> A capability is never marked *Implemented* on the basis of empty files, interfaces or
> stubs alone.

## Foundation (Phase 0)

| Capability | Status | Notes |
|---|---|---|
| Project scaffolding (`pyproject.toml`, `src/` layout, `uv`) | Implemented | Builds; `uv sync` installs core + dev. |
| Quality gate (ruff + mypy strict + pytest) | Implemented | Runs green locally and in CI. |
| CI pipeline (GitHub Actions, Python 3.12 & 3.13) | Implemented | Lint, type-check, tests on both versions. |
| Integrity docs (README, ROADMAP, CAPABILITIES, CHANGELOG) | Implemented | Kept in sync with real state. |

## Core & Contracts (Phase 1)

| Capability | Status | Notes |
|---|---|---|
| Typed data contracts (tasks, agents, tools, findings, audit, governance) | Implemented | Pydantic v2, `extra="forbid"`, validated by tests. |
| Structured error model (`AresError` + subclasses) | Implemented | Code / component / severity / context / recovery. |
| Abstract interfaces (repository, module, agent, tool, LLM, governance, knowledge, audit) | Implemented | Ports only; concrete implementations land in later phases. |
| Configuration (`pydantic-settings`, `ARES_` env prefix) | Implemented | No secrets in code; `.env` driven. |
| Structured logging (structlog) | Implemented | Console or JSON; no secrets in logs. |
| Module registry + Core Engine lifecycle | Implemented | Register/start/stop, duplicate-id protection. |

## Everything else

| Area | Status |
|---|---|
| Security Governance (profiles, scope, authorization, approval, audit sink) | Planned |
| AI Reasoning & LLM provider abstraction | Planned |
| Orchestrator & multi-agent system | Planned |
| Knowledge & Research Engine | Planned |
| Tool integration adapters | Planned |
| Active Directory Security Engine | Planned |
| Windows Enterprise Engine | Planned |
| EDR/XDR Intelligence Engine | Planned |
| EDR Evasion Research Engine | Planned |
| Offensive Engineering & PoC Factory | Planned |
| Vulnerability / Network / Web / Cloud / Linux / DFIR engines | Planned |
| Dynamic Capability Engine | Planned |
| Reporting Engine | Planned |
| REST API & Web dashboard | Planned |
| CLI (interactive) | Planned — a minimal entrypoint exists; commands land in Phase 4 |
