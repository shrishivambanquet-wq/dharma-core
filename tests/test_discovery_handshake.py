from dharma.network.discovery_handshake import DiscoveryHandshake


def test_type():
    assert DiscoveryHandshake("A").discover("B").message_type == "discover"


def test_sender():
    assert DiscoveryHandshake("A").discover("B").sender == "A"


def test_receiver():
    assert DiscoveryHandshake("A").discover("B").receiver == "B"


def test_accept():
    h = DiscoveryHandshake("A")
    assert h.accepts(h.discover("B"))


def test_reject_version():
    h = DiscoveryHandshake("A")
    m = h.discover("B")
    m.payload["version"] = "9.9"
    assert not h.accepts(m)
