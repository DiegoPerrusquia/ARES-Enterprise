"""Audit sink port (ARCHITECTURE §7.4).

Audit records must be durable and protected against unauthorized modification. The concrete
append-only sink is implemented in Phase 2; this port lets earlier code emit audit events.
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from ares.contracts.audit import AuditEvent


@runtime_checkable
class AuditSink(Protocol):
    """Receives audit events for durable, tamper-evident storage."""

    def record(self, event: AuditEvent) -> None: ...


__all__ = ["AuditSink"]
