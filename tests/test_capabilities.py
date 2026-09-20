from dharma.network.capabilities import CapabilitySet


def test_default_contains_wire():
    assert "wire_v1" in CapabilitySet().advertise()


def test_default_contains_ed25519():
    assert "ed25519" in CapabilitySet().advertise()


def test_negotiate_common():
    a = CapabilitySet({"wire_v1","ed25519"})
    b = CapabilitySet({"wire_v1","replay_guard"})
    assert a.negotiate(b) == ["wire_v1"]


def test_negotiate_multiple():
    a = CapabilitySet({"wire_v1","ed25519"})
    b = CapabilitySet({"wire_v1","ed25519"})
    assert a.negotiate(b) == ["ed25519","wire_v1"]


def test_empty_negotiation():
    a = CapabilitySet({"wire_v1"})
    b = CapabilitySet({"session_resume"})
    assert a.negotiate(b) == []


def test_advertise_sorted():
    assert CapabilitySet({"b","a"}).advertise() == ["a","b"]


def test_add_capability():
    c = CapabilitySet({"wire_v1"})
    c.supported.add("compression")
    assert "compression" in c.advertise()


def test_remove_capability():
    c = CapabilitySet({"wire_v1","ed25519"})
    c.supported.remove("ed25519")
    assert "ed25519" not in c.advertise()
