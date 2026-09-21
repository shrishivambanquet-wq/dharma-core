"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.negotiation import TrustNegotiation

def test_type():
    assert TrustNegotiation("A").propose("B").message_type == "trust_proposal"

def test_sender():
    assert TrustNegotiation("A").propose("B").sender == "A"

def test_receiver():
    assert TrustNegotiation("A").propose("B").receiver == "B"

def test_accept():
    n = TrustNegotiation("A")
    assert n.accepts(n.propose("B"))

def test_reject():
    n = TrustNegotiation("A")
    m = n.propose("B")
    m.payload["version"] = "9.9"
    assert not n.accepts(m)
