"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.ed25519 import Ed25519Identity
from dharma.network.key_exchange import KeyExchange


def test_public_key_exists():
    assert len(KeyExchange(Ed25519Identity.create()).public_key()) > 0


def test_exchange_returns_remote():
    a = KeyExchange(Ed25519Identity.create())
    b = KeyExchange(Ed25519Identity.create())
    assert a.exchange(b.public_key())["remote"] == b.public_key()


def test_exchange_trusted():
    a = KeyExchange(Ed25519Identity.create())
    b = KeyExchange(Ed25519Identity.create())
    assert a.exchange(b.public_key())["trusted"]


def test_local_key_kept():
    a = KeyExchange(Ed25519Identity.create())
    b = KeyExchange(Ed25519Identity.create())
    assert a.exchange(b.public_key())["local"] == a.public_key()


def test_public_keys_differ():
    a = KeyExchange(Ed25519Identity.create())
    b = KeyExchange(Ed25519Identity.create())
    assert a.public_key() != b.public_key()
