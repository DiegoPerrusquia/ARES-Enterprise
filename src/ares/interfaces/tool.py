"""Tool adapter port (ARCHITECTURE §6.1).

Tools are always invoked through adapters that declare a manifest and run requests; the
orchestrator never shells out to arbitrary commands directly.
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from ares.contracts.tools import ToolManifest, ToolRequest, ToolResult


@runtime_checkable
class ToolAdapter(Protocol):
    """An adapter wrapping an internal or external security tool."""

    @property
    def manifest(self) -> ToolManifest: ...

    def run(self, request: ToolRequest) -> ToolResult: ...


__all__ = ["ToolAdapter"]
