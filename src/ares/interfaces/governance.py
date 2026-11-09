"""Governance port (ARCHITECTURE §7, §15.4).

The reasoning layer may *propose* actions; this service *decides* whether they are allowed.
It is enforced in the backend and is intentionally separate from the AI layer so that no
model output can grant itself authority. Concrete enforcement arrives in Phase 2.
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from ares.contracts.enums import OperationalProfile
from ares.contracts.governance import AuthorizationDecision
from ares.contracts.tasks import TaskRequest
from ares.contracts.tools import ToolRequest


@runtime_checkable
class AuthorizationService(Protocol):
    """Backend authority over task and tool execution."""

    def authorize_task(self, task: TaskRequest) -> AuthorizationDecision: ...

    def authorize_tool(
        self, request: ToolRequest, *, profile: OperationalProfile
    ) -> AuthorizationDecision: ...


__all__ = ["AuthorizationService"]
