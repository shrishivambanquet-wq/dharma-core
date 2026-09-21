"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.trust_verification import TrustVerification
from dharma.network.trust_anchor import TrustAnchor
def test_verify():
 a=TrustAnchor();a.add("A","k");assert TrustVerification().verify(a,"A")
def test_fail():
 a=TrustAnchor();assert not TrustVerification().verify(a,"A")
def test_two():
 a=TrustAnchor();a.add("A","k");a.add("B","k");assert TrustVerification().verify(a,"B")
def test_missing():
 a=TrustAnchor();assert not TrustVerification().verify(a,"X")
def test_empty():
 a=TrustAnchor();assert not TrustVerification().verify(a,"Z")
def test_many():
 a=TrustAnchor();[a.add(str(i),"k") for i in range(5)];assert TrustVerification().verify(a,"4")
def test_same():
 a=TrustAnchor();a.add("A","x");assert TrustVerification().verify(a,"A")
def test_bool():
 a=TrustAnchor();assert isinstance(TrustVerification().verify(a,"A"),bool)
def test_key():
 a=TrustAnchor();a.add("A","1");assert TrustVerification().verify(a,"A")
def test_root():
 a=TrustAnchor();a.add("root","k");assert TrustVerification().verify(a,"root")
def test_other():
 a=TrustAnchor();a.add("X","k");assert not TrustVerification().verify(a,"Y")
def test_final():
 a=TrustAnchor();a.add("node","k");assert TrustVerification().verify(a,"node")
