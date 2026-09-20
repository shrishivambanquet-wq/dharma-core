from dharma.network.capability import CapabilityCard

def test_node():
    assert CapabilityCard("A","0.2",[]).advertise()["node"] == "A"

def test_protocol():
    assert CapabilityCard("A","0.2",[]).advertise()["protocol"] == "0.2"

def test_features():
    c = CapabilityCard("A","0.2",["wire"])
    assert c.advertise()["features"] == ["wire"]

def test_support_true():
    assert CapabilityCard("A","0.2",["ttl"]).supports("ttl")

def test_support_false():
    assert not CapabilityCard("A","0.2",["ttl"]).supports("mesh")

def test_multiple():
    c = CapabilityCard("A","0.2",["a","b","c"])
    assert len(c.features) == 3

def test_empty():
    assert CapabilityCard("A","0.2").features == []

def test_advertise_keys():
    assert set(CapabilityCard("A","0.2").advertise().keys()) == {"node","protocol","features"}
