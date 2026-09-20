from dharma.network.auth_discovery import AuthDiscoveryRegistry
from dharma.network.federation_sync import FederationSync


def build():
    return AuthDiscoveryRegistry(), AuthDiscoveryRegistry()


def test_empty():
    a, b = build()
    assert FederationSync(a).sync(b) == 0


def test_single():
    a, b = build()
    b.nodes["A"] = "1"
    FederationSync(a).sync(b)
    assert a.discover("A") == "1"


def test_multiple():
    a, b = build()
    b.nodes["A"] = "1"
    b.nodes["B"] = "2"
    FederationSync(a).sync(b)
    assert a.count() == 2


def test_update():
    a, b = build()
    a.nodes["A"] = "old"
    b.nodes["A"] = "new"
    FederationSync(a).sync(b)
    assert a.discover("A") == "new"


def test_duplicate():
    a, b = build()
    a.nodes["A"] = "1"
    b.nodes["A"] = "1"
    FederationSync(a).sync(b)
    assert a.count() == 1


def test_source_unchanged():
    a, b = build()
    b.nodes["A"] = "1"
    FederationSync(a).sync(b)
    assert b.count() == 1


def test_destination_grows():
    a, b = build()
    b.nodes["A"] = "1"
    assert FederationSync(a).sync(b) == 1


def test_unknown():
    a, _ = build()
    assert a.discover("X") is None


def test_idempotent():
    a, b = build()
    b.nodes["A"] = "1"
    FederationSync(a).sync(b)
    FederationSync(a).sync(b)
    assert a.count() == 1


def test_count():
    a, b = build()
    b.nodes["A"] = "1"
    b.nodes["B"] = "2"
    FederationSync(a).sync(b)
    assert a.count() == 2
