from dharma.network.dcp import DCPMessage
from dharma.network.dcp_signed import SignedDCPMessage
from dharma.network.ed25519 import Ed25519Identity


def test_sign_verify():
    i = Ed25519Identity.create()
    m = DCPMessage("A","B","hello",{})
    assert SignedDCPMessage.sign(m, i).verify(i.verify_key())


def test_wrong_key():
    a = Ed25519Identity.create()
    b = Ed25519Identity.create()
    m = DCPMessage("A","B","hello",{})
    assert not SignedDCPMessage.sign(m, a).verify(b.verify_key())


def test_signature_exists():
    i = Ed25519Identity.create()
    m = DCPMessage("A","B","hello",{})
    assert len(SignedDCPMessage.sign(m, i).signature) > 0


def test_sender_kept():
    i = Ed25519Identity.create()
    m = DCPMessage("A","B","hello",{})
    assert SignedDCPMessage.sign(m, i).message.sender == "A"


def test_receiver_kept():
    i = Ed25519Identity.create()
    m = DCPMessage("A","B","hello",{})
    assert SignedDCPMessage.sign(m, i).message.receiver == "B"
