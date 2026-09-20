from dharma.network.ed25519 import Ed25519Identity, verify


def test_sign_verify():
    i = Ed25519Identity.create()
    msg = b"Dharma"
    assert verify(msg, i.sign(msg), i.verify_key())


def test_wrong_message():
    i = Ed25519Identity.create()
    sig = i.sign(b"A")
    assert not verify(b"B", sig, i.verify_key())


def test_wrong_key():
    a = Ed25519Identity.create()
    b = Ed25519Identity.create()
    sig = a.sign(b"Dharma")
    assert not verify(b"Dharma", sig, b.verify_key())


def test_signature_exists():
    assert len(Ed25519Identity.create().sign(b"x")) > 0


def test_verify_key_exists():
    assert Ed25519Identity.create().verify_key() is not None
