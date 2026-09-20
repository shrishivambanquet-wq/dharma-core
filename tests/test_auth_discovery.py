from dharma.network.auth_discovery import AuthDiscoveryRegistry
from dharma.network.ed25519 import Ed25519Identity
from dharma.network.route_announcement import RouteAnnouncement


def test_signed_registration():
    i = Ed25519Identity.create()
    r = AuthDiscoveryRegistry()
    a = RouteAnnouncement("A","127.0.0.1:4040").sign(i)
    assert r.register(a, i.verify_key())


def test_wrong_key():
    a = Ed25519Identity.create()
    b = Ed25519Identity.create()
    r = AuthDiscoveryRegistry()
    ann = RouteAnnouncement("A","1").sign(a)
    assert not r.register(ann, b.verify_key())


def test_tampered():
    i = Ed25519Identity.create()
    r = AuthDiscoveryRegistry()
    ann = RouteAnnouncement("A","1").sign(i)
    ann.endpoint = "2"
    assert not r.register(ann, i.verify_key())


def test_discovery():
    i = Ed25519Identity.create()
    r = AuthDiscoveryRegistry()
    ann = RouteAnnouncement("A","1").sign(i)
    r.register(ann, i.verify_key())
    assert r.discover("A") == "1"


def test_unknown():
    assert AuthDiscoveryRegistry().discover("X") is None


def test_update():
    i = Ed25519Identity.create()
    r = AuthDiscoveryRegistry()
    r.register(RouteAnnouncement("A","1").sign(i), i.verify_key())
    r.register(RouteAnnouncement("A","2").sign(i), i.verify_key())
    assert r.discover("A") == "2"


def test_invalid_signature():
    i = Ed25519Identity.create()
    r = AuthDiscoveryRegistry()
    ann = RouteAnnouncement("A","1")
    assert not r.register(ann, i.verify_key())


def test_count():
    i = Ed25519Identity.create()
    r = AuthDiscoveryRegistry()
    r.register(RouteAnnouncement("A","1").sign(i), i.verify_key())
    assert r.count() == 1
