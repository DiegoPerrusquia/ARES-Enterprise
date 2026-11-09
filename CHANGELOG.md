# Changelog

All notable changes to ARES Enterprise are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project follows
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Phase 0 — Foundation scaffolding:** `pyproject.toml` (hatchling build, `uv`-managed),
  `src/` package layout, ruff + mypy (strict) + pytest configuration, `.gitignore`,
  `.env.example`, GitHub Actions CI on Python 3.12 and 3.13, and the mandated integrity
  documents (`README`, `ROADMAP`, `CAPABILITIES`, `CHANGELOG`).
- **Phase 1 — Contracts & Core Engine:** typed Pydantic contracts (tasks, agents, tools,
  governance, findings, audit) with a structured error model; abstract interfaces for
  repositories, modules, agents, tools, LLM/embedding providers, governance, knowledge
  retrieval and audit; configuration via `pydantic-settings`; structured logging via
  structlog; and the Core Engine module registry and lifecycle.

[Unreleased]: https://github.com/diegoperrusquia/ares-enterprise/commits/main
