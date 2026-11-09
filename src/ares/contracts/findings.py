"""Security finding contract (CLAUDE.md §5.3).

Every finding carries its evidence, preconditions, impact and recommendations, so that no
result is presented without the context needed to judge it.
"""

from __future__ import annotations

from pydantic import Field

from .base import TimestampedModel, new_id
from .enums import Severity


class SecurityFinding(TimestampedModel):
    """A single security finding produced by an agent or engine."""

    finding_id: str = Field(default_factory=lambda: new_id("find"))
    task_id: str | None = None
    title: str = Field(min_length=1)
    description: str = Field(min_length=1)
    severity: Severity = Severity.MEDIUM
    preconditions: list[str] = Field(default_factory=list)
    impact: str = ""
    evidence_ids: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
    references: list[str] = Field(default_factory=list)
    # MITRE ATT&CK technique IDs, e.g. "T1558.003".
    attack_ids: list[str] = Field(default_factory=list)
    # Related CVE identifiers, e.g. "CVE-2021-42287".
    cve_ids: list[str] = Field(default_factory=list)
    validation_method: str | None = None


__all__ = ["SecurityFinding"]
