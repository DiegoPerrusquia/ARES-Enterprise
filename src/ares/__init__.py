"""ARES Enterprise — modular, governed cybersecurity engineering platform.

The top-level package intentionally exposes only the version. Subsystems are imported
from their own packages (``ares.contracts``, ``ares.interfaces``, ``ares.core``) so the
core stays lightweight and free of domain-specific logic.
"""

from __future__ import annotations

__version__ = "0.1.0"

__all__ = ["__version__"]
