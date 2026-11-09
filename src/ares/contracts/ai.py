"""Minimal provider-neutral AI contracts (ARCHITECTURE §3.3).

These DTOs let the LLM / embedding provider *interfaces* be typed in Phase 1 without
committing to any provider. Concrete providers arrive in Phase 3. No provider SDK types
leak into the platform.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from .base import AresModel

Role = Literal["system", "user", "assistant"]


class LLMMessage(AresModel):
    """A single chat message."""

    role: Role
    content: str


class LLMResponse(AresModel):
    """A provider-neutral completion response."""

    content: str
    model: str
    input_tokens: int | None = Field(default=None, ge=0)
    output_tokens: int | None = Field(default=None, ge=0)
    stop_reason: str | None = None


class EmbeddingResponse(AresModel):
    """A provider-neutral embedding response."""

    vector: list[float]
    model: str
    dimensions: int = Field(gt=0)


__all__ = ["EmbeddingResponse", "LLMMessage", "LLMResponse", "Role"]
