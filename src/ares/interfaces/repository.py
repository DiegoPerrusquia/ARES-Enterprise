"""Generic persistence port (ARCHITECTURE §9.1).

The Core and specialized engines depend on this abstraction, never on database-specific
queries. Concrete repositories (SQLAlchemy, in-memory, …) implement it in later phases.
"""

from __future__ import annotations

from typing import Protocol, TypeVar, runtime_checkable

T = TypeVar("T")


@runtime_checkable
class Repository(Protocol[T]):
    """A minimal CRUD-style persistence contract for a single entity type."""

    def add(self, entity: T) -> T: ...

    def get(self, entity_id: str) -> T | None: ...

    def list(self) -> list[T]: ...

    def delete(self, entity_id: str) -> bool: ...


__all__ = ["Repository"]
