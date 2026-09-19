from dharma.network.discovery import DiscoveryRegistry


def test_announce():
    d = DiscoveryRegistry()
    d.announce("uni", "https://uni")
    assert d.count() == 1


def test_resolve():
    d = DiscoveryRegistry()
    d.announce("uni", "https://uni")
    assert d.resolve("uni") == "https://uni"


def test_missing():
    assert DiscoveryRegistry().resolve("x") is None


def test_replace():
    d = DiscoveryRegistry()
    d.announce("uni", "a")
    d.announce("uni", "b")
    assert d.resolve("uni") == "b"


def test_count():
    d = DiscoveryRegistry()
    d.announce("a", "1")
    d.announce("b", "2")
    assert d.count() == 2
