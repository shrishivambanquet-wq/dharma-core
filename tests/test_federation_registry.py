from dharma.federation.node import FederationNode
from dharma.federation.registry import FederationRegistry


def test_register():
    r = FederationRegistry()
    r.register(FederationNode("1", "Alpha", "https://alpha.org"))
    assert r.count() == 1


def test_get():
    r = FederationRegistry()
    n = FederationNode("1", "Alpha", "https://alpha.org")
    r.register(n)
    assert r.get("1") == n


def test_replace_duplicate():
    r = FederationRegistry()
    r.register(FederationNode("1", "Alpha", "https://a"))
    r.register(FederationNode("1", "Beta", "https://b"))
    assert r.count() == 1
    assert r.get("1").name == "Beta"


def test_all():
    r = FederationRegistry()
    r.register(FederationNode("1", "Alpha", "https://a"))
    r.register(FederationNode("2", "Beta", "https://b"))
    assert len(r.all()) == 2


def test_missing():
    assert FederationRegistry().get("x") is None
