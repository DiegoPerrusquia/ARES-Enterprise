"""LLM and embedding provider ports (ARCHITECTURE §3.3).

The Core never depends on a specific provider. Anthropic, OpenAI, Ollama and local models
are reached through these ports; swapping a provider must not touch consuming modules.
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from ares.contracts.ai import EmbeddingResponse, LLMMessage, LLMResponse


@runtime_checkable
class LLMProvider(Protocol):
    """A chat-completion provider."""

    @property
    def name(self) -> str: ...

    def complete(
        self,
        messages: list[LLMMessage],
        *,
        model: str | None = None,
        max_tokens: int | None = None,
        temperature: float | None = None,
    ) -> LLMResponse: ...


@runtime_checkable
class EmbeddingProvider(Protocol):
    """A text embedding provider."""

    @property
    def name(self) -> str: ...

    def embed(self, text: str, *, model: str | None = None) -> EmbeddingResponse: ...


__all__ = ["EmbeddingProvider", "LLMProvider"]
