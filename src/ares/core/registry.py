"""Module registry.

Tracks registered modules and their lifecycle state. Registration is explicit and
duplicate identifiers are rejected, so the set of active modules is always known.
"""

from __future__ import annotations

from ares.contracts.enums import ModuleState
from ares.contracts.errors import ModuleError
from ares.interfaces.module import ModuleInterface

_COMPONENT = "core.registry"


class ModuleRegistry:
    """An ordered collection of registered modules and their states."""

    def __init__(self) -> None:
        self._modules: dict[str, ModuleInterface] = {}
        self._states: dict[str, ModuleState] = {}

    def register(self, module: ModuleInterface) -> None:
        """Register a module. Raises ``ModuleError`` on duplicate ids."""

        module_id = module.module_id
        if module_id in self._modules:
            raise ModuleError(
                f"Module '{module_id}' is already registered",
                component=_COMPONENT,
                context={"module_id": module_id},
            )
        self._modules[module_id] = module
        self._states[module_id] = ModuleState.REGISTERED

    def get(self, module_id: str) -> ModuleInterface:
        """Return a registered module or raise ``ModuleError``."""

        try:
            return self._modules[module_id]
        except KeyError as exc:
            raise ModuleError(
                f"Module '{module_id}' is not registered",
                component=_COMPONENT,
                context={"module_id": module_id},
            ) from exc

    def all(self) -> list[ModuleInterface]:
        """Return all registered modules in registration order."""

        return list(self._modules.values())

    def state(self, module_id: str) -> ModuleState:
        """Return the lifecycle state of a registered module."""

        try:
            return self._states[module_id]
        except KeyError as exc:
            raise ModuleError(
                f"Module '{module_id}' is not registered",
                component=_COMPONENT,
                context={"module_id": module_id},
            ) from exc

    def set_state(self, module_id: str, state: ModuleState) -> None:
        """Update the lifecycle state of a registered module."""

        if module_id not in self._modules:
            raise ModuleError(
                f"Module '{module_id}' is not registered",
                component=_COMPONENT,
                context={"module_id": module_id},
            )
        self._states[module_id] = state

    def __contains__(self, module_id: object) -> bool:
        return module_id in self._modules

    def __len__(self) -> int:
        return len(self._modules)


__all__ = ["ModuleRegistry"]
