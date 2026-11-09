"""Governance contracts (ARCHITECTURE §7).

These describe scope, authorization decisions and human approval. They are *contracts* only;
the enforcing logic is the Security Governance subsystem (Phase 2). Defining them now lets
Phase 1 interfaces carry authorization parameters from the start.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import Field

from .base import AresModel, TimestampedModel, new_id
from .enums import ApprovalStatus, OperationalProfile


class ScopeDefinition(TimestampedModel):
    """The authorized boundary for an assessment (ARCHITECTURE §7.2)."""

    scope_id: str = Field(default_factory=lambda: new_id("scope"))
    name: str = Field(min_length=1)
    owner: str = Field(min_length=1, description="Authorization owner / approver identity.")
    profile: OperationalProfile
    authorized_targets: list[str] = Field(default_factory=list)
    excluded_targets: list[str] = Field(default_factory=list)
    allowed_operations: list[str] = Field(default_factory=list)
    restricted_operations: list[str] = Field(default_factory=list)
    starts_at: datetime | None = None
    expires_at: datetime | None = None
    enabled: bool = True


class AuthorizationDecision(AresModel):
    """The governance layer's verdict on a proposed operation."""

    allowed: bool
    reason: str = Field(min_length=1)
    requires_approval: bool = False
    matched_scope_id: str | None = None
    # Identifier of the policy / rule that produced this decision, for auditability.
    policy_id: str | None = None


class ApprovalRequest(TimestampedModel):
    """A request for explicit human approval of a sensitive operation (§7.3)."""

    approval_id: str = Field(default_factory=lambda: new_id("appr"))
    task_id: str
    scope_id: str | None = None
    operation: str = Field(min_length=1)
    justification: str = Field(min_length=1)
    details: dict[str, Any] = Field(default_factory=dict)
    status: ApprovalStatus = ApprovalStatus.PENDING


class ApprovalRecord(TimestampedModel):
    """The recorded outcome of an approval request, bound to the task it approved."""

    approval_id: str
    task_id: str
    status: ApprovalStatus
    decided_by: str | None = None
    decided_at: datetime | None = None
    comment: str | None = None


__all__ = [
    "ApprovalRecord",
    "ApprovalRequest",
    "AuthorizationDecision",
    "ScopeDefinition",
]
