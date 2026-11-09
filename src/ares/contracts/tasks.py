"""Task contracts exchanged with the orchestrator / task manager."""

from __future__ import annotations

from typing import Any

from pydantic import Field

from .base import TimestampedModel, new_id
from .enums import OperationalProfile, Severity, TaskStatus


class TaskRequest(TimestampedModel):
    """A unit of work submitted to ARES."""

    task_id: str = Field(default_factory=lambda: new_id("task"))
    intent: str = Field(min_length=1, description="Short machine/human intent label.")
    description: str = Field(min_length=1, description="Natural-language description.")
    profile: OperationalProfile = OperationalProfile.PASSIVE
    scope_id: str | None = Field(
        default=None, description="Reference to the authorized scope this task runs under."
    )
    parent_task_id: str | None = None
    parameters: dict[str, Any] = Field(default_factory=dict)
    requested_by: str | None = None


class TaskError(TimestampedModel):
    """A single error attached to a task result."""

    code: str
    message: str
    severity: Severity = Severity.MEDIUM


class TaskResult(TimestampedModel):
    """The outcome of a task."""

    task_id: str
    status: TaskStatus
    summary: str = ""
    output: dict[str, Any] = Field(default_factory=dict)
    evidence_ids: list[str] = Field(default_factory=list)
    finding_ids: list[str] = Field(default_factory=list)
    errors: list[TaskError] = Field(default_factory=list)


__all__ = ["TaskError", "TaskRequest", "TaskResult"]
