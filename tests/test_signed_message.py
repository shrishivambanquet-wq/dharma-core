"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.dcp import DCPMessage
from dharma.network.identity import NodeIdentity
from dharma.network.signed_message import SignedMessage


def test_sign():
    i = NodeIdentity.create("A")
    m = DCPMessage("A","B","ping",{})
    assert SignedMessage.sign(m, i).verify(i)


def test_wrong_identity():
    a = NodeIdentity.create("A")
    b = NodeIdentity.create("B")
    m = DCPMessage("A","B","ping",{})
    assert not SignedMessage.sign(m, a).verify(b)


def test_signature_length():
    i = NodeIdentity.create("A")
    m = DCPMessage("A","B","ping",{})
    assert len(SignedMessage.sign(m, i).signature) == 64


def test_payload_kept():
    i = NodeIdentity.create("A")
    m = DCPMessage("A","B","ping",{"x":1})
    assert SignedMessage.sign(m, i).message.payload["x"] == 1


def test_sender_kept():
    i = NodeIdentity.create("A")
    m = DCPMessage("A","B","ping",{})
    assert SignedMessage.sign(m, i).message.sender == "A"
