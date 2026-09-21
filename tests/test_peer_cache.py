"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.peer_cache import PeerCache

def test_save():
    c = PeerCache()
    c.remember("A","10.0.0.1")
    assert c.lookup("A") == "10.0.0.1"

def test_known():
    c = PeerCache()
    c.remember("A","1")
    assert c.known("A")

def test_unknown():
    assert PeerCache().lookup("X") is None

def test_overwrite():
    c = PeerCache()
    c.remember("A","1")
    c.remember("A","2")
    assert c.lookup("A") == "2"

def test_count():
    c = PeerCache()
    c.remember("A","1")
    c.remember("B","2")
    assert c.count() == 2

def test_multiple():
    c = PeerCache()
    for i in range(5):
        c.remember(str(i), str(i))
    assert c.count() == 5

def test_lookup_after_overwrite():
    c = PeerCache()
    c.remember("P","old")
    c.remember("P","new")
    assert c.lookup("P") == "new"

def test_known_false():
    assert not PeerCache().known("ghost")
