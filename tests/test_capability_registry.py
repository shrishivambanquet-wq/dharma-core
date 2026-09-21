"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.capability_registry import CapabilityRegistry

def test_add():
    c=CapabilityRegistry(); assert c.add("A","mesh")
def test_has():
    c=CapabilityRegistry(); c.add("A","mesh"); assert c.has("A","mesh")
def test_missing():
    assert not CapabilityRegistry().has("A","mesh")
def test_list():
    c=CapabilityRegistry(); c.add("A","b"); c.add("A","a"); assert c.list("A")==["a","b"]
def test_count():
    c=CapabilityRegistry(); c.add("A","x"); c.add("A","y"); assert c.count("A")==2
def test_duplicate():
    c=CapabilityRegistry(); c.add("A","x"); c.add("A","x"); assert c.count("A")==1
def test_remove():
    c=CapabilityRegistry(); c.add("A","x"); c.remove("A","x"); assert not c.has("A","x")
def test_remove_missing():
    c=CapabilityRegistry(); assert c.remove("A","x")==False
def test_other_node():
    c=CapabilityRegistry(); c.add("A","x"); c.add("B","y"); assert c.list("B")==["y"]
def test_empty():
    assert CapabilityRegistry().count("A")==0
def test_many():
    c=CapabilityRegistry(); [c.add("A",str(i)) for i in range(5)]; assert c.count("A")==5
def test_sorted():
    c=CapabilityRegistry(); c.add("A","transport"); c.add("A","discover"); c.add("A","mesh"); assert c.list("A")==["discover","mesh","transport"]
