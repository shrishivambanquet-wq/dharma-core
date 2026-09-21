"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.packet_ttl import PacketTTL

def test_default():
    assert PacketTTL().ttl == 8

def test_hop():
    p = PacketTTL(3)
    p.hop()
    assert p.ttl == 2

def test_zero():
    p = PacketTTL(1)
    p.hop()
    assert p.expired()

def test_not_negative():
    p = PacketTTL(0)
    p.hop()
    assert p.ttl == 0

def test_multiple():
    p = PacketTTL(5)
    for _ in range(3):
        p.hop()
    assert p.ttl == 2

def test_expired_false():
    assert not PacketTTL(2).expired()

def test_last_hop():
    p = PacketTTL(1)
    assert p.hop() == 0

def test_extra_hop():
    p = PacketTTL(1)
    p.hop()
    p.hop()
    assert p.ttl == 0
