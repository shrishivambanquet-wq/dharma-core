"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.registry import ProtocolRegistry


def test_hello():
    assert ProtocolRegistry().code("HELLO") == 1


def test_accept():
    assert ProtocolRegistry().name(2) == "ACCEPT"


def test_route():
    assert ProtocolRegistry().code("ROUTE_ANNOUNCEMENT") == 3


def test_unknown_code():
    assert ProtocolRegistry().name(99) is None


def test_unknown_name():
    assert ProtocolRegistry().code("UNKNOWN") is None


def test_dcp():
    assert ProtocolRegistry().code("DCP_MESSAGE") == 6


def test_session():
    assert ProtocolRegistry().name(5) == "SESSION_RESUME"


def test_unique():
    r = ProtocolRegistry()
    values = [r.code(k) for k in ["HELLO","ACCEPT","ROUTE_ANNOUNCEMENT","TRUST_PROPOSAL","SESSION_RESUME","DCP_MESSAGE"]]
    assert len(values) == len(set(values))


def test_reverse():
    r = ProtocolRegistry()
    assert r.name(r.code("HELLO")) == "HELLO"
