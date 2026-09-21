"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import pytest
from dharma.network.router import NetworkRouter


def test_register():
    r = NetworkRouter()
    r.register("A", "https://a")
    assert r.count() == 1


def test_lookup():
    r = NetworkRouter()
    r.register("A", "https://a")
    assert r.resolve("A") == "https://a"


def test_unknown():
    assert NetworkRouter().resolve("X") is None


def test_update():
    r = NetworkRouter()
    r.register("A", "1")
    r.register("A", "2")
    assert r.resolve("A") == "2"


def test_multiple():
    r = NetworkRouter()
    r.register("A", "1")
    r.register("B", "2")
    assert r.count() == 2


def test_invalid():
    with pytest.raises(ValueError):
        NetworkRouter().register("", "x")
