"""Shared enumerations used across ARES contracts.

These enums encode vocabulary that the whole platform agrees on: operational profiles,
severities, knowledge confidence levels and lifecycle states. They are defined once here
so that no module invents its own strings.
"""

from __future__ import annotations

from enum import StrEnum


class OperationalProfile(StrEnum):
    """Governance profiles that bound what operations are permitted (ARCHITECTURE §7.1)."""

    PASSIVE = "PASSIVE"
    ASSESSMENT = "ASSESSMENT"
    LAB = "LAB"
    ADVERSARY_EMULATION = "ADVERSARY_EMULATION"
    FORENSICS = "FORENSICS"
    ENGINEERING = "ENGINEERING"


class Severity(StrEnum):
    """Severity scale for findings, errors and audit events."""

    INFO = "INFO"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class KnowledgeConfidence(StrEnum):
    """Confidence classification for stored knowledge (KNOWLEDGE_ENGINE §4)."""

    VERIFIED = "VERIFIED"
    DOCUMENTED = "DOCUMENTED"
    EXPERIMENTAL = "EXPERIMENTAL"
    HYPOTHESIS = "HYPOTHESIS"
    DEPRECATED = "DEPRECATED"


class TaskStatus(StrEnum):
    """Lifecycle of a task handled by the orchestrator / task manager."""

    PENDING = "PENDING"
    PLANNED = "PLANNED"
    RUNNING = "RUNNING"
    BLOCKED = "BLOCKED"
    AWAITING_APPROVAL = "AWAITING_APPROVAL"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


class CapabilityStatus(StrEnum):
    """Implementation status classification mandated by CLAUDE.md §26.4."""

    PLANNED = "PLANNED"
    PARTIALLY_IMPLEMENTED = "PARTIALLY_IMPLEMENTED"
    EXPERIMENTAL = "EXPERIMENTAL"
    SIMULATED = "SIMULATED"
    IMPLEMENTED = "IMPLEMENTED"
    BLOCKED = "BLOCKED"


class ApprovalStatus(StrEnum):
    """State of a human-approval request (ARCHITECTURE §7.3)."""

    PENDING = "PENDING"
    APPROVED = "APPROVED"
    DENIED = "DENIED"
    EXPIRED = "EXPIRED"


class ModuleState(StrEnum):
    """Lifecycle state of a registered core module."""

    REGISTERED = "REGISTERED"
    INITIALIZING = "INITIALIZING"
    READY = "READY"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    ERROR = "ERROR"


__all__ = [
    "ApprovalStatus",
    "CapabilityStatus",
    "KnowledgeConfidence",
    "ModuleState",
    "OperationalProfile",
    "Severity",
    "TaskStatus",
]
