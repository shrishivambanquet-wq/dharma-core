"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.dcp import DCPMessage


def test_encode():
    m = DCPMessage("A", "B", "trust_request", {"id": "123"})
    assert "trust_request" in m.encode()


def test_decode():
    m = DCPMessage("A", "B", "trust_request", {"id": "123"})
    d = DCPMessage.decode(m.encode())
    assert d.sender == "A"


def test_receiver():
    d = DCPMessage.decode(
        DCPMessage("A", "B", "trust_request", {}).encode()
    )
    assert d.receiver == "B"


def test_payload():
    d = DCPMessage.decode(
        DCPMessage("A", "B", "trust_request", {"x": 1}).encode()
    )
    assert d.payload["x"] == 1


def test_roundtrip():
    m = DCPMessage("A", "B", "ping", {"ok": True})
    assert DCPMessage.decode(m.encode()) == m
