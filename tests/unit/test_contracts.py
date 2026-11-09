"""Unit tests for the typed contracts."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from ares.contracts import (
    AresError,
    AuditEvent,
    AuthorizationError,
    OperationalProfile,
    ScopeDefinition,
    SecurityFinding,
    Severity,
    TaskRequest,
    TaskResult,
    TaskStatus,
    new_id,
)


def test_new_id_has_prefix() -> None:
    identifier = new_id("task")
    assert identifier.startswith("task_")
    assert len(identifier) > len("task_")


def test_task_request_defaults_and_id() -> None:
    task = TaskRequest(intent="enumerate", description="Enumerate the domain")
    assert task.task_id.startswith("task_")
    assert task.profile is OperationalProfile.PASSIVE
    assert task.parameters == {}


def test_contract_forbids_extra_fields() -> None:
    with pytest.raises(ValidationError):
        TaskRequest(intent="x", description="y", unexpected="boom")  # type: ignore[call-arg]


def test_security_finding_requires_title_and_description() -> None:
    with pytest.raises(ValidationError):
        SecurityFinding(title="", description="")

    finding = SecurityFinding(
        title="Kerberoastable service account",
        description="A service account with an SPN uses a weak password.",
        severity=Severity.HIGH,
        attack_ids=["T1558.003"],
    )
    assert finding.finding_id.startswith("find_")
    assert finding.severity is Severity.HIGH


def test_task_result_roundtrip() -> None:
    result = TaskResult(task_id="task_abc", status=TaskStatus.SUCCEEDED, summary="done")
    dumped = result.model_dump()
    assert dumped["status"] == TaskStatus.SUCCEEDED
    assert dumped["summary"] == "done"


def test_audit_event_minimal() -> None:
    event = AuditEvent(actor="diego", action="startup", component="core.engine")
    assert event.event_id.startswith("audit_")
    assert event.severity is Severity.INFO


def test_scope_definition_requires_owner() -> None:
    with pytest.raises(ValidationError):
        ScopeDefinition(name="lab", owner="", profile=OperationalProfile.LAB)


def test_ares_error_to_dict() -> None:
    err = AuthorizationError(
        "operation not permitted",
        component="governance",
        context={"operation": "scan"},
    )
    data = err.to_dict()
    assert data["code"] == "authorization_error"
    assert data["severity"] == Severity.HIGH.value
    assert data["component"] == "governance"
    assert data["context"] == {"operation": "scan"}
    assert isinstance(err, AresError)
