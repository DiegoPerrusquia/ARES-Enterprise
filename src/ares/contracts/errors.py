"""Structured error model.

All ARES errors follow a single shape (ARCHITECTURE §12): a code, a human-readable
message, the originating component, a severity, optional structured context and optional
recovery guidance. This keeps error handling uniform and auditable across subsystems.
"""

from __future__ import annotations

from typing import Any

from .enums import Severity


class AresError(Exception):
    """Base class for all ARES errors."""

    # Subclasses may override these defaults.
    default_code: str = "ares_error"
    default_severity: Severity = Severity.MEDIUM

    def __init__(
        self,
        message: str,
        *,
        component: str,
        code: str | None = None,
        severity: Severity | None = None,
        context: dict[str, Any] | None = None,
        recovery: str | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.component = component
        self.code = code or self.default_code
        self.severity = severity or self.default_severity
        self.context: dict[str, Any] = context or {}
        self.recovery = recovery

    def to_dict(self) -> dict[str, Any]:
        """Serialize the error into a structured, log-safe mapping."""

        return {
            "code": self.code,
            "message": self.message,
            "component": self.component,
            "severity": self.severity.value,
            "context": self.context,
            "recovery": self.recovery,
        }

    def __str__(self) -> str:
        return f"[{self.code}] {self.message} (component={self.component})"


class ConfigurationError(AresError):
    """Raised when configuration is missing or invalid."""

    default_code = "configuration_error"
    default_severity = Severity.HIGH


class ContractValidationError(AresError):
    """Raised when data fails contract validation outside of Pydantic's own errors."""

    default_code = "contract_validation_error"


class AuthorizationError(AresError):
    """Raised when an operation is not permitted by the governance layer."""

    default_code = "authorization_error"
    default_severity = Severity.HIGH


class ScopeError(AresError):
    """Raised when an operation targets something outside the authorized scope."""

    default_code = "scope_error"
    default_severity = Severity.HIGH


class ModuleError(AresError):
    """Raised for module registration or lifecycle failures."""

    default_code = "module_error"


class ToolExecutionError(AresError):
    """Raised when a tool adapter fails to execute."""

    default_code = "tool_execution_error"


__all__ = [
    "AresError",
    "AuthorizationError",
    "ConfigurationError",
    "ContractValidationError",
    "ModuleError",
    "ScopeError",
    "ToolExecutionError",
]
