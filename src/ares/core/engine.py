"""The ARES Core Engine (ARCHITECTURE §3.1).

The Core Engine is deliberately lightweight: it wires configuration and logging, holds the
module registry, and drives the startup/shutdown lifecycle. It contains no attack logic,
no vendor integrations and no domain-specific research — those live in independent modules.
"""

from __future__ import annotations

from ares.contracts.enums import ModuleState
from ares.contracts.errors import ModuleError
from ares.core.config import Settings
from ares.core.logging import configure_logging, get_logger
from ares.core.registry import ModuleRegistry
from ares.interfaces.module import ModuleInterface

_COMPONENT = "core.engine"


class CoreEngine:
    """Central application component coordinating modules and lifecycle."""

    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or Settings()
        configure_logging(level=self.settings.log_level, json_logs=self.settings.log_json)
        self.logger = get_logger("ares.core")
        self.registry = ModuleRegistry()
        self._started = False

    @property
    def started(self) -> bool:
        """Whether the engine has completed startup."""

        return self._started

    def register_module(self, module: ModuleInterface) -> None:
        """Register a module with the engine."""

        self.registry.register(module)
        self.logger.info("module_registered", module_id=module.module_id, name=module.name)

    def startup(self) -> None:
        """Initialize all registered modules in registration order."""

        if self._started:
            return
        for module in self.registry.all():
            self.registry.set_state(module.module_id, ModuleState.INITIALIZING)
            try:
                module.initialize(self)
            except Exception as exc:
                self.registry.set_state(module.module_id, ModuleState.ERROR)
                self.logger.error(
                    "module_initialization_failed",
                    module_id=module.module_id,
                    error=str(exc),
                )
                raise ModuleError(
                    f"Failed to initialize module '{module.module_id}'",
                    component=_COMPONENT,
                    context={"module_id": module.module_id, "error": str(exc)},
                ) from exc
            self.registry.set_state(module.module_id, ModuleState.READY)
            self.logger.info("module_initialized", module_id=module.module_id)
        self._started = True
        self.logger.info("engine_started", modules=len(self.registry))

    def shutdown(self) -> None:
        """Shut down all modules in reverse registration order."""

        if not self._started:
            return
        for module in reversed(self.registry.all()):
            self.registry.set_state(module.module_id, ModuleState.STOPPING)
            try:
                module.shutdown()
            except Exception as exc:
                # A failing shutdown must not prevent the rest from shutting down.
                self.logger.error(
                    "module_shutdown_failed",
                    module_id=module.module_id,
                    error=str(exc),
                )
            self.registry.set_state(module.module_id, ModuleState.STOPPED)
        self._started = False
        self.logger.info("engine_stopped")

    def health(self) -> dict[str, bool]:
        """Return a per-module health map."""

        return {module.module_id: module.health() for module in self.registry.all()}


__all__ = ["CoreEngine"]
