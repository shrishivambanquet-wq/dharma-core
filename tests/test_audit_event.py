"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.authority.audit_event import AuditEvent


def test_create_event():
    e = AuditEvent("A", "create")
    assert e.authority_id == "A"


def test_event_name():
    e = AuditEvent("A", "revoke")
    assert e.event == "revoke"


def test_timestamp_exists():
    assert AuditEvent("A", "create").timestamp is not None


def test_serialize():
    s = AuditEvent("A", "create").serialize()
    assert s["authority_id"] == "A"


def test_iso_timestamp():
    s = AuditEvent("A", "create").serialize()
    assert "T" in s["timestamp"]
