"""Unit tests for the Core Engine and module registry."""

from __future__ import annotations

import pytest

from ares.contracts.enums import ModuleState
from ares.contracts.errors import ModuleError
from ares.core.config import Settings
from ares.core.engine import CoreEngine
from ares.interfaces.module import BaseModule, ModuleInterface


class DummyModule(BaseModule):
    module_id = "dummy"
    name = "Dummy Module"

    def __init__(self) -> None:
        self.initialized = False
        self.stopped = False

    def initialize(self, engine: CoreEngine) -> None:
        self.initialized = True

    def shutdown(self) -> None:
        self.stopped = True


class FailingModule(BaseModule):
    module_id = "failing"
    name = "Failing Module"

    def initialize(self, engine: CoreEngine) -> None:
        raise RuntimeError("boom")


def make_engine() -> CoreEngine:
    return CoreEngine(Settings(_env_file=None))  # type: ignore[call-arg]


def test_dummy_module_conforms_to_interface() -> None:
    assert isinstance(DummyModule(), ModuleInterface)


def test_register_and_lifecycle() -> None:
    engine = make_engine()
    module = DummyModule()
    engine.register_module(module)

    assert "dummy" in engine.registry
    assert engine.registry.state("dummy") is ModuleState.REGISTERED
    assert engine.started is False

    engine.startup()
    assert engine.started is True
    assert module.initialized is True
    assert engine.registry.state("dummy") is ModuleState.READY
    assert engine.health() == {"dummy": True}

    engine.shutdown()
    assert engine.started is False
    assert module.stopped is True
    assert engine.registry.state("dummy") is ModuleState.STOPPED


def test_duplicate_registration_rejected() -> None:
    engine = make_engine()
    engine.register_module(DummyModule())
    with pytest.raises(ModuleError):
        engine.register_module(DummyModule())


def test_startup_is_idempotent() -> None:
    engine = make_engine()
    engine.register_module(DummyModule())
    engine.startup()
    engine.startup()  # second call is a no-op
    assert engine.started is True


def test_failing_module_raises_and_marks_error() -> None:
    engine = make_engine()
    engine.register_module(FailingModule())
    with pytest.raises(ModuleError):
        engine.startup()
    assert engine.registry.state("failing") is ModuleState.ERROR
    assert engine.started is False


def test_get_unregistered_module_raises() -> None:
    engine = make_engine()
    with pytest.raises(ModuleError):
        engine.registry.get("nope")
