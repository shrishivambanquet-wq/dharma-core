"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.federation_recovery import FederationRecovery

def test_save():
    f=FederationRecovery(); assert f.save("A","10.0.0.1")
def test_recover():
    f=FederationRecovery(); f.save("A","10.0.0.1"); assert f.recover("A")=="10.0.0.1"
def test_missing():
    assert FederationRecovery().recover("X") is None
def test_exists():
    f=FederationRecovery(); f.save("A","1"); assert f.exists("A")
def test_remove():
    f=FederationRecovery(); f.save("A","1"); assert f.remove("A")
def test_remove_missing():
    assert not FederationRecovery().remove("X")
def test_count():
    f=FederationRecovery(); f.save("A","1"); f.save("B","2"); assert f.count()==2
def test_nodes():
    f=FederationRecovery(); f.save("B","2"); f.save("A","1"); assert f.nodes()==["A","B"]
def test_overwrite():
    f=FederationRecovery(); f.save("A","1"); f.save("A","2"); assert f.recover("A")=="2"
def test_empty():
    assert FederationRecovery().count()==0
def test_rejoin():
    f=FederationRecovery(); f.save("A","1"); f.remove("A"); f.save("A","2"); assert f.recover("A")=="2"
def test_many():
    f=FederationRecovery(); [f.save(str(i),str(i)) for i in range(5)]; assert f.count()==5
