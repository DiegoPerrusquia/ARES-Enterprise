"""ARES Core Engine: configuration, logging, module registry and lifecycle."""

from __future__ import annotations

from .config import Settings
from .engine import CoreEngine
from .logging import configure_logging, get_logger
from .registry import ModuleRegistry

__all__ = [
    "CoreEngine",
    "ModuleRegistry",
    "Settings",
    "configure_logging",
    "get_logger",
]
