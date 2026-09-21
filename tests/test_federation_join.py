"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.federation_join import FederationJoin

def test_join():
    f=FederationJoin()
    assert f.join("A","10.0.0.1")

def test_duplicate():
    f=FederationJoin()
    f.join("A","10.0.0.1")
    assert not f.join("A","10.0.0.2")

def test_exists():
    f=FederationJoin()
    f.join("A","10.0.0.1")
    assert f.exists("A")

def test_missing():
    assert not FederationJoin().exists("X")

def test_endpoint():
    f=FederationJoin()
    f.join("A","10.0.0.1")
    assert f.endpoint("A")=="10.0.0.1"

def test_count():
    f=FederationJoin()
    f.join("A","1")
    f.join("B","2")
    assert f.count()==2

def test_leave():
    f=FederationJoin()
    f.join("A","1")
    assert f.leave("A")

def test_leave_missing():
    assert not FederationJoin().leave("X")

def test_list():
    f=FederationJoin()
    f.join("B","2")
    f.join("A","1")
    assert f.list_members()==["A","B"]

def test_rejoin():
    f=FederationJoin()
    f.join("A","1")
    f.leave("A")
    assert f.join("A","2")

def test_endpoint_missing():
    assert FederationJoin().endpoint("X") is None

def test_count_empty():
    assert FederationJoin().count()==0
