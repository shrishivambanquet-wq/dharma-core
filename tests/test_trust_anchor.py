"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.trust_anchor import TrustAnchor
def test_add():
 a=TrustAnchor();a.add("A","k");assert a.trusted("A")
def test_get():
 a=TrustAnchor();a.add("A","k");assert a.get("A")=="k"
def test_missing():
 assert TrustAnchor().get("X") is None
def test_count():
 a=TrustAnchor();a.add("A","1");a.add("B","2");assert a.count()==2
def test_overwrite():
 a=TrustAnchor();a.add("A","1");a.add("A","2");assert a.get("A")=="2"
def test_empty():
 assert TrustAnchor().count()==0
def test_many():
 a=TrustAnchor();[a.add(str(i),"k") for i in range(5)];assert a.count()==5
def test_false():
 assert not TrustAnchor().trusted("X")
def test_keys():
 a=TrustAnchor();a.add("A","k");assert "A" in a.anchors
def test_value():
 a=TrustAnchor();a.add("A","v");assert a.anchors["A"]=="v"
def test_two():
 a=TrustAnchor();a.add("A","1");a.add("B","2");assert a.trusted("B")
def test_same():
 a=TrustAnchor();a.add("A","x");assert a.get("A")=="x"
