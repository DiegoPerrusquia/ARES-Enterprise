"""Knowledge retrieval contracts (KNOWLEDGE_ENGINE §5).

Agents request context through a common contract and receive results that always carry
their provenance (source, URL, date, document, version) and a confidence classification.
Content without provenance must never be presented as verified knowledge.
"""

from __future__ import annotations

from datetime import datetime

from pydantic import Field

from .base import AresModel
from .enums import KnowledgeConfidence


class KnowledgeQuery(AresModel):
    """A request for knowledge from the retrieval engine."""

    query: str = Field(min_length=1)
    categories: list[str] = Field(default_factory=list)
    limit: int = Field(default=10, gt=0, le=100)
    min_confidence: KnowledgeConfidence | None = None


class KnowledgeResult(AresModel):
    """A single retrieved knowledge fragment with full provenance."""

    content: str
    source_id: str | None = None
    source_name: str | None = None
    url: str | None = None
    document_title: str | None = None
    document_version: str | None = None
    published_at: datetime | None = None
    retrieved_at: datetime | None = None
    snippet: str | None = None
    confidence: KnowledgeConfidence = KnowledgeConfidence.DOCUMENTED
    score: float | None = Field(default=None, ge=0.0)


__all__ = ["KnowledgeQuery", "KnowledgeResult"]
