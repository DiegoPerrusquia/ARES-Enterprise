"""Specialized agent port (ARCHITECTURE §3.4)."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from ares.contracts.agents import AgentContract, AgentRequest, AgentResponse


@runtime_checkable
class AgentInterface(Protocol):
    """A specialized agent that handles requests within its declared contract."""

    @property
    def contract(self) -> AgentContract: ...

    def handle(self, request: AgentRequest) -> AgentResponse: ...


__all__ = ["AgentInterface"]
