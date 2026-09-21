"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.ed25519 import Ed25519Identity
from dharma.network.route_announcement import RouteAnnouncement


def test_sign_verify():
    i = Ed25519Identity.create()
    r = RouteAnnouncement("A","https://a").sign(i)
    assert r.verify(i.verify_key())


def test_tampered_route():
    i = Ed25519Identity.create()
    r = RouteAnnouncement("A","https://a").sign(i)
    r.endpoint = "https://evil"
    assert not r.verify(i.verify_key())


def test_wrong_key():
    a = Ed25519Identity.create()
    b = Ed25519Identity.create()
    r = RouteAnnouncement("A","https://a").sign(a)
    assert not r.verify(b.verify_key())


def test_signature_exists():
    i = Ed25519Identity.create()
    assert RouteAnnouncement("A","https://a").sign(i).signature is not None


def test_endpoint_preserved():
    assert RouteAnnouncement("A","https://a").endpoint == "https://a"


def test_node_preserved():
    assert RouteAnnouncement("A","https://a").node_id == "A"
