"""Audit event contract (ARCHITECTURE §7.4).

Every relevant operation records who, what, under which profile and scope, with what
outcome. Audit records are append-only in the governance subsystem; this contract defines
their shape. Sensitive values must be sanitized before they reach an audit sink.
"""

from __future__ import annotations

from typing import Any

from pydantic import Field

from .base import TimestampedModel, new_id
from .enums import OperationalProfile, Severity


class AuditEvent(TimestampedModel):
    """A single audit record."""

    event_id: str = Field(default_factory=lambda: new_id("audit"))
    actor: str = Field(min_length=1, description="User or component that initiated the action.")
    action: str = Field(min_length=1)
    component: str = Field(min_length=1)
    task_id: str | None = None
    profile: OperationalProfile | None = None
    scope_id: str | None = None
    agent_id: str | None = None
    tool_id: str | None = None
    approval_id: str | None = None
    status: str = Field(default="recorded")
    severity: Severity = Severity.INFO
    # Parameters must be sanitized (no secrets/tokens) before being stored.
    parameters: dict[str, Any] = Field(default_factory=dict)
    error_code: str | None = None


__all__ = ["AuditEvent"]
