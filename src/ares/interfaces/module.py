"""Core module port and a convenience base class.

Every pluggable subsystem registered with the Core Engine implements ``ModuleInterface``.
``BaseModule`` provides sane defaults so modules only override what they need.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, Protocol, runtime_checkable

if TYPE_CHECKING:
    from ares.core.engine import CoreEngine


@runtime_checkable
class ModuleInterface(Protocol):
    """A subsystem that can be registered and lifecycle-managed by the Core Engine."""

    module_id: str
    name: str

    def initialize(self, engine: CoreEngine) -> None: ...

    def shutdown(self) -> None: ...

    def health(self) -> bool: ...


class BaseModule:
    """Convenience base for modules. Subclasses set ``module_id`` and ``name``."""

    module_id: ClassVar[str]
    name: ClassVar[str]

    def initialize(self, engine: CoreEngine) -> None:
        """Set up the module. Override as needed. Default is a no-op."""

    def shutdown(self) -> None:
        """Release resources. Override as needed. Default is a no-op."""

    def health(self) -> bool:
        """Return readiness. Default: healthy."""

        return True


__all__ = ["BaseModule", "ModuleInterface"]
