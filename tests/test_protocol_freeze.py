"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.protocol_freeze import ProtocolFreeze
def test_default():
 p=ProtocolFreeze(); assert not p.status()
def test_freeze():
 p=ProtocolFreeze(); p.freeze(); assert p.status()
def test_twice():
 p=ProtocolFreeze(); p.freeze(); p.freeze(); assert p.status()
def test_bool():
 assert isinstance(ProtocolFreeze().status(),bool)
def test_true():
 p=ProtocolFreeze(); p.freeze(); assert p.frozen
def test_false():
 assert not ProtocolFreeze().frozen
def test_again():
 p=ProtocolFreeze(); p.freeze(); assert p.status()
def test_type():
 assert type(ProtocolFreeze().status()) is bool
def test_repeat():
 p=ProtocolFreeze(); p.freeze(); assert p.status()
def test_empty():
 p=ProtocolFreeze(); assert not p.status()
def test_flag():
 p=ProtocolFreeze(); p.freeze(); assert p.frozen
def test_lock():
 p=ProtocolFreeze(); p.freeze(); assert p.status()
