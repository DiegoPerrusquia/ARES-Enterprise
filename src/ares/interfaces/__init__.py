"""Abstract ports for ARES subsystems.

These Protocols decouple the Core and engines from concrete implementations: persistence,
modules, agents, tools, LLM/embedding providers, governance, knowledge retrieval and audit.
"""

from __future__ import annotations

from .agent import AgentInterface
from .audit import AuditSink
from .governance import AuthorizationService
from .knowledge import KnowledgeRetriever
from .llm import EmbeddingProvider, LLMProvider
from .module import BaseModule, ModuleInterface
from .repository import Repository
from .tool import ToolAdapter

__all__ = [
    "AgentInterface",
    "AuditSink",
    "AuthorizationService",
    "BaseModule",
    "EmbeddingProvider",
    "KnowledgeRetriever",
    "LLMProvider",
    "ModuleInterface",
    "Repository",
    "ToolAdapter",
]
