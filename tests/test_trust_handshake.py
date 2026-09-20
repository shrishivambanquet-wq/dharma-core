from dharma.network.ed25519 import Ed25519Identity
from dharma.network.key_exchange import KeyExchange
from dharma.network.trust_handshake import TrustHandshake


def make():
    return TrustHandshake(
        KeyExchange(Ed25519Identity.create()),
        KeyExchange(Ed25519Identity.create()),
    )


def test_hello():
    assert make().hello()["type"] == "hello"


def test_accept():
    assert make().accept()["type"] == "accept"


def test_established():
    assert make().established()


def test_keys_exist():
    h = make()
    assert h.hello()["public_key"]
    assert h.accept()["public_key"]


def test_keys_are_different():
    h = make()
    assert h.hello()["public_key"] != h.accept()["public_key"]
