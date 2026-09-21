"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.identity import NodeIdentity


def test_create():
    assert NodeIdentity.create("A").node_id == "A"


def test_public_key_length():
    assert len(NodeIdentity.create("A").public_key()) == 64


def test_fingerprint_length():
    assert len(NodeIdentity.create("A").fingerprint()) == 16


def test_unique_keys():
    assert NodeIdentity.create("A").public_key() != NodeIdentity.create("A").public_key()


def test_fingerprint_matches():
    n = NodeIdentity.create("A")
    assert n.fingerprint() == n.public_key()[:16]
