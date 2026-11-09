"""Knowledge retrieval port (KNOWLEDGE_ENGINE §5, §12).

Agents obtain technical context through this single contract. Direct, unrestricted access
to storage tables is not allowed.
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from ares.contracts.knowledge import KnowledgeQuery, KnowledgeResult


@runtime_checkable
class KnowledgeRetriever(Protocol):
    """Provides evidence-backed knowledge fragments to agents."""

    def search(self, query: KnowledgeQuery) -> list[KnowledgeResult]: ...


__all__ = ["KnowledgeRetriever"]
