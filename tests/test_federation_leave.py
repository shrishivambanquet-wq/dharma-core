"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.federation_leave import FederationLeave

def test_leave():
    f=FederationLeave()
    assert f.leave("A")

def test_duplicate():
    f=FederationLeave()
    f.leave("A")
    assert not f.leave("A")

def test_has_left():
    f=FederationLeave()
    f.leave("A")
    assert f.has_left("A")

def test_missing():
    assert not FederationLeave().has_left("X")

def test_count():
    f=FederationLeave()
    f.leave("A");f.leave("B")
    assert f.count()==2

def test_restore():
    f=FederationLeave()
    f.leave("A")
    f.restore("A")
    assert not f.has_left("A")

def test_restore_missing():
    FederationLeave().restore("X")

def test_all_sorted():
    f=FederationLeave()
    f.leave("B");f.leave("A")
    assert f.all()==["A","B"]

def test_empty():
    assert FederationLeave().count()==0

def test_releave():
    f=FederationLeave()
    f.leave("A")
    f.restore("A")
    assert f.leave("A")

def test_many():
    f=FederationLeave()
    [f.leave(str(i)) for i in range(5)]
    assert f.count()==5

def test_clear_one():
    f=FederationLeave()
    f.leave("A");f.leave("B")
    f.restore("A")
    assert f.all()==["B"]
