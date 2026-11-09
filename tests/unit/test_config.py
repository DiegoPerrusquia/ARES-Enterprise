"""Unit tests for configuration loading."""

from __future__ import annotations

import pytest

from ares.contracts.enums import OperationalProfile
from ares.core.config import Settings


def test_defaults() -> None:
    settings = Settings(_env_file=None)  # type: ignore[call-arg]
    assert settings.environment == "development"
    assert settings.log_level == "INFO"
    assert settings.log_json is False
    assert settings.default_profile is OperationalProfile.PASSIVE
    assert settings.require_approval is True
    assert settings.database_url is None


def test_env_override(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ARES_LOG_LEVEL", "DEBUG")
    monkeypatch.setenv("ARES_LOG_JSON", "true")
    monkeypatch.setenv("ARES_DEFAULT_PROFILE", "LAB")
    monkeypatch.setenv("ARES_REQUIRE_APPROVAL", "false")

    settings = Settings(_env_file=None)  # type: ignore[call-arg]
    assert settings.log_level == "DEBUG"
    assert settings.log_json is True
    assert settings.default_profile is OperationalProfile.LAB
    assert settings.require_approval is False
