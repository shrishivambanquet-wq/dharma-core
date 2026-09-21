"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.packet import Packet


def test_route():
    assert Packet("A","B",{}).route() == "A->B"


def test_receiver():
    assert Packet("A","B",{}).is_for("B")


def test_not_receiver():
    assert not Packet("A","B",{}).is_for("A")


def test_timestamp():
    assert Packet("A","B",{}).timestamp > 0


def test_payload():
    assert Packet("A","B",{"x":1}).payload["x"] == 1
