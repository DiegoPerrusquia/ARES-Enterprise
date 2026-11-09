"""Base model and small helpers shared by every ARES contract."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

from pydantic import BaseModel, ConfigDict, Field


def utcnow() -> datetime:
    """Return a timezone-aware UTC timestamp."""

    return datetime.now(tz=UTC)


def new_id(prefix: str) -> str:
    """Generate a short, prefixed, collision-resistant identifier.

    Example: ``new_id("task") -> "task_9f1c2a7b4e01"``.
    """

    return f"{prefix}_{uuid.uuid4().hex[:12]}"


class AresModel(BaseModel):
    """Strict base model for all contracts.

    ``extra="forbid"`` guarantees that unknown fields (for example, keys smuggled in from
    untrusted external content) are rejected rather than silently carried along.
    """

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
    )


class TimestampedModel(AresModel):
    """A contract that records when it was created."""

    created_at: datetime = Field(default_factory=utcnow)


__all__ = ["AresModel", "TimestampedModel", "new_id", "utcnow"]
