# ARES Enterprise

**Autonomous Reconnaissance, Engineering & Security** — a modular, governed cybersecurity
engineering and intelligence platform specialized in Microsoft enterprise infrastructure
(Active Directory, Windows internals, EDR/XDR), security tooling development and
evidence-based research.

> **Status: Pre-Alpha / Foundation.** ARES is being built incrementally. Most of the
> platform described in the specification documents is **planned, not implemented**.
> See [`CAPABILITIES.md`](CAPABILITIES.md) for the authoritative, per-component status and
> [`ROADMAP.md`](ROADMAP.md) for the implementation order.

## What ARES is (and is not)

ARES is designed as an integrated security engineering platform where specialized engines
and agents collaborate through a controlled orchestration layer, with a **security
governance layer that holds authority over every operation**. It is not a chatbot and not a
thin wrapper around existing tools.

A core principle: the AI reasoning layer *proposes* actions; the governance layer *decides*
whether they are permitted; the execution layer performs only authorized operations. No
model-generated response can grant itself operational authority.

## Documentation

| Document | Purpose |
|---|---|
| [`CLAUDE.md`](CLAUDE.md) | Master project specification |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | Target system architecture |
| [`KNOWLEDGE_ENGINE.md`](KNOWLEDGE_ENGINE.md) | Knowledge & research engine specification |
| [`ROADMAP.md`](ROADMAP.md) | Phased implementation plan |
| [`CAPABILITIES.md`](CAPABILITIES.md) | Per-component implementation status |
| [`CHANGELOG.md`](CHANGELOG.md) | Notable changes |

## Requirements

- Python **3.12+** (CI runs 3.12 and 3.13)
- [`uv`](https://docs.astral.sh/uv/) for environment and dependency management
- Docker (for PostgreSQL + pgvector, from Phase 3 onward)

## Development setup

```bash
# Create the virtual environment and install core + dev dependencies
uv sync --extra dev

# Run the quality gate
uv run ruff check .
uv run mypy
uv run pytest
```

## Project layout

```text
src/ares/
├── contracts/   # Typed, validated data contracts shared across the platform
├── interfaces/  # Abstract ports (repositories, modules, agents, tools, LLM, governance)
└── core/        # Core Engine: config, logging, module registry, lifecycle
tests/
├── unit/        # Fast, offline, no external services
├── integration/ # Opt-in, may need services
├── security/    # Governance / trust-boundary assertions
└── e2e/         # End-to-end flows
```

Additional engines (Active Directory, Windows, EDR, Knowledge, …) are added phase by phase,
each behind the contracts and interfaces defined in `src/ares/`.

## Security

ARES is intended for **authorized** security assessment, research and engineering only.
External content (web pages, repositories, documents, tool output, LLM output) is treated
as untrusted and can never modify authorization policy or system behavior. See the project
specification for the full governance and trust-boundary model.

## License

[MIT](LICENSE)
