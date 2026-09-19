from dharma.authority.audit_log import AuditLog
from dharma.authority.audit_event import AuditEvent


def test_append():
    log = AuditLog()
    log.append(AuditEvent("A", "create"))
    assert log.count() == 1


def test_last():
    log = AuditLog()
    e = AuditEvent("A", "create")
    log.append(e)
    assert log.last() == e


def test_filter_authority():
    log = AuditLog()
    log.append(AuditEvent("A", "create"))
    log.append(AuditEvent("B", "create"))
    assert len(log.by_authority("A")) == 1


def test_empty_last():
    assert AuditLog().last() is None


def test_append_order():
    log = AuditLog()
    log.append(AuditEvent("A", "create"))
    log.append(AuditEvent("A", "revoke"))
    assert log.last().event == "revoke"
