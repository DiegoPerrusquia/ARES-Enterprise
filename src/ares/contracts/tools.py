"""Tool integration contracts (ARCHITECTURE §6).

Tools are invoked through adapters, never as arbitrary shell commands. A ``ToolManifest``
describes an adapter; ``ToolRequest`` / ``ToolResult`` carry an invocation and its outcome.
"""

from __future__ import annotations

from typing import Any

from pydantic import Field

from .base import AresModel, TimestampedModel, new_id


class ToolManifest(AresModel):
    """Static description of a tool adapter."""

    tool_id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    version: str = Field(default="unknown")
    description: str = Field(default="")
    install_requirements: list[str] = Field(default_factory=list)
    required_permissions: list[str] = Field(default_factory=list)
    default_timeout_seconds: float = Field(default=60.0, gt=0)
    # Whether this tool only observes (read-only) or can modify a target.
    read_only: bool = True


class ToolRequest(TimestampedModel):
    """A request to run a tool through its adapter."""

    request_id: str = Field(default_factory=lambda: new_id("treq"))
    tool_id: str
    task_id: str | None = None
    scope_id: str | None = None
    arguments: dict[str, Any] = Field(default_factory=dict)
    timeout_seconds: float | None = Field(default=None, gt=0)


class ToolResult(TimestampedModel):
    """The outcome of a tool invocation."""

    request_id: str
    tool_id: str
    success: bool
    exit_code: int | None = None
    stdout: str = ""
    stderr: str = ""
    parsed: dict[str, Any] = Field(default_factory=dict)
    duration_seconds: float | None = Field(default=None, ge=0)
    evidence_ids: list[str] = Field(default_factory=list)


__all__ = ["ToolManifest", "ToolRequest", "ToolResult"]
