import pytest
from dharma.network.discovery_registry import DiscoveryRegistry


def test_register():
    r = DiscoveryRegistry()
    r.register("A","127.0.0.1:4040")
    assert r.count() == 1


def test_discover():
    r = DiscoveryRegistry()
    r.register("A","127.0.0.1:4040")
    assert r.discover("A") == "127.0.0.1:4040"


def test_unknown():
    assert DiscoveryRegistry().discover("X") is None


def test_update():
    r = DiscoveryRegistry()
    r.register("A","1")
    r.register("A","2")
    assert r.discover("A") == "2"


def test_remove():
    r = DiscoveryRegistry()
    r.register("A","1")
    assert r.remove("A") == "1"
    assert r.count() == 0


def test_multiple():
    r = DiscoveryRegistry()
    r.register("A","1")
    r.register("B","2")
    assert r.count() == 2


def test_count():
    r = DiscoveryRegistry()
    assert r.count() == 0


def test_invalid():
    with pytest.raises(ValueError):
        DiscoveryRegistry().register("", "x")
