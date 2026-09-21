"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.audit_log import AuditLog

def test_record():
    l=AuditLog()
    assert l.record("A","join")["actor"]=="A"

def test_action():
    l=AuditLog()
    assert l.record("A","join")["action"]=="join"

def test_target():
    l=AuditLog()
    assert l.record("A","grant","B")["target"]=="B"

def test_latest():
    l=AuditLog()
    l.record("A","join")
    assert l.latest()["action"]=="join"

def test_count():
    l=AuditLog()
    l.record("A","join"); l.record("B","leave")
    assert l.count()==2

def test_empty():
    assert AuditLog().latest() is None

def test_timestamp():
    assert AuditLog().record("A","join")["timestamp"]>0

def test_all():
    l=AuditLog()
    l.record("A","join")
    assert len(l.all())==1

def test_order():
    l=AuditLog()
    l.record("A","one"); l.record("A","two")
    assert l.all()[0]["action"]=="one"

def test_many():
    l=AuditLog()
    [l.record("A",str(i)) for i in range(5)]
    assert l.count()==5

def test_none_target():
    assert AuditLog().record("A","join")["target"] is None

def test_keys():
    e=AuditLog().record("A","join")
    assert set(e.keys())=={"timestamp","actor","action","target"}
