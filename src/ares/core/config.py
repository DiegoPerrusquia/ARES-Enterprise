"""Application configuration.

Settings are read from environment variables (prefix ``ARES_``) and an optional ``.env``
file. Secrets are never hardcoded; API keys are read from the environment by the provider
implementations, not stored here.
"""

from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict

from ares.contracts.enums import OperationalProfile


class Settings(BaseSettings):
    """Platform-wide configuration."""

    model_config = SettingsConfigDict(
        env_prefix="ARES_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    environment: str = "development"
    log_level: str = "INFO"
    log_json: bool = False

    # Persistence (Phase 3+). Optional until the storage layer exists.
    database_url: str | None = None

    # AI provider selection (Phase 4+). Keys live in the environment, not here.
    llm_provider: str = "anthropic"

    # Governance defaults (Phase 2 enforces them).
    default_profile: OperationalProfile = OperationalProfile.PASSIVE
    require_approval: bool = True


__all__ = ["Settings"]
