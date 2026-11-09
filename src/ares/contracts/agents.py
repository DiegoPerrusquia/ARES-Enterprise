"""Agent contracts (ARCHITECTURE §3.4).

An agent declares what it can do and what it needs through an ``AgentContract``; requests
and responses flow through ``AgentRequest`` / ``AgentResponse``. Agents never receive
unrestricted access to tools — their allowed tools are declared explicitly.
"""

from __future__ import annotations

from typing import Any

from pydantic import Field

from .base import AresModel, TimestampedModel, new_id
from .enums import OperationalProfile, TaskStatus


class AgentContract(AresModel):
    """Static declaration of an agent's identity, capabilities and constraints."""

    agent_id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    domain: str = Field(min_length=1, description="Specialization domain, e.g. 'active_directory'.")
    capabilities: list[str] = Field(default_factory=list)
    allowed_tools: list[str] = Field(default_factory=list)
    required_permissions: list[str] = Field(default_factory=list)
    supported_profiles: list[OperationalProfile] = Field(default_factory=list)
    dependencies: list[str] = Field(default_factory=list)
    constraints: list[str] = Field(default_factory=list)


class AgentRequest(TimestampedModel):
    """A request routed to a specific agent."""

    request_id: str = Field(default_factory=lambda: new_id("areq"))
    task_id: str
    agent_id: str
    profile: OperationalProfile
    scope_id: str | None = None
    objective: str = Field(min_length=1)
    inputs: dict[str, Any] = Field(default_factory=dict)


class AgentResponse(TimestampedModel):
    """An agent's reply to an ``AgentRequest``."""

    request_id: str
    agent_id: str
    status: TaskStatus
    summary: str = ""
    outputs: dict[str, Any] = Field(default_factory=dict)
    evidence_ids: list[str] = Field(default_factory=list)
    finding_ids: list[str] = Field(default_factory=list)
    # Agent output is never trusted blindly; downstream consumers must still validate it.
    requires_validation: bool = True


__all__ = ["AgentContract", "AgentRequest", "AgentResponse"]
