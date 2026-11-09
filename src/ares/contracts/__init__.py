"""ARES typed data contracts.

This package is the single home for the schemas exchanged between subsystems. Importing
from ``ares.contracts`` gives access to every contract and shared enum/error.
"""

from __future__ import annotations

from .agents import AgentContract, AgentRequest, AgentResponse
from .ai import EmbeddingResponse, LLMMessage, LLMResponse, Role
from .audit import AuditEvent
from .base import AresModel, TimestampedModel, new_id, utcnow
from .enums import (
    ApprovalStatus,
    CapabilityStatus,
    KnowledgeConfidence,
    ModuleState,
    OperationalProfile,
    Severity,
    TaskStatus,
)
from .errors import (
    AresError,
    AuthorizationError,
    ConfigurationError,
    ContractValidationError,
    ModuleError,
    ScopeError,
    ToolExecutionError,
)
from .findings import SecurityFinding
from .governance import (
    ApprovalRecord,
    ApprovalRequest,
    AuthorizationDecision,
    ScopeDefinition,
)
from .knowledge import KnowledgeQuery, KnowledgeResult
from .tasks import TaskError, TaskRequest, TaskResult
from .tools import ToolManifest, ToolRequest, ToolResult

__all__ = [
    # agents
    "AgentContract",
    "AgentRequest",
    "AgentResponse",
    # governance
    "ApprovalRecord",
    "ApprovalRequest",
    # enums
    "ApprovalStatus",
    # errors
    "AresError",
    # base
    "AresModel",
    "AuditEvent",
    "AuthorizationDecision",
    "AuthorizationError",
    "CapabilityStatus",
    "ConfigurationError",
    "ContractValidationError",
    # ai
    "EmbeddingResponse",
    "KnowledgeConfidence",
    # knowledge
    "KnowledgeQuery",
    "KnowledgeResult",
    "LLMMessage",
    "LLMResponse",
    "ModuleError",
    "ModuleState",
    "OperationalProfile",
    "Role",
    "ScopeDefinition",
    "ScopeError",
    # findings / audit
    "SecurityFinding",
    "Severity",
    # tasks
    "TaskError",
    "TaskRequest",
    "TaskResult",
    "TaskStatus",
    "TimestampedModel",
    "ToolExecutionError",
    # tools
    "ToolManifest",
    "ToolRequest",
    "ToolResult",
    "new_id",
    "utcnow",
]
