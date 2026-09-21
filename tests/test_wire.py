"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import pytest
from dharma.network.wire import WireMessage, VERSION


def test_roundtrip():
    m = WireMessage(2, {"node":"A"})
    assert WireMessage.decode(m.encode()).payload["node"] == "A"


def test_version():
    m = WireMessage(1,{})
    assert m.encode()[0] == VERSION


def test_type():
    assert WireMessage.decode(WireMessage(9,{}).encode()).msg_type == 9


def test_payload():
    assert WireMessage.decode(WireMessage(3,{"x":1}).encode()).payload["x"] == 1


def test_length():
    data = WireMessage(1,{"a":"b"}).encode()
    length = int.from_bytes(data[2:4],"big")
    assert length == len(data)-4


def test_invalid_version():
    bad = bytearray(WireMessage(1,{}).encode())
    bad[0]=99
    with pytest.raises(ValueError):
        WireMessage.decode(bytes(bad))


def test_empty_payload():
    assert WireMessage.decode(WireMessage(1,{}).encode()).payload == {}


def test_header_size():
    assert len(WireMessage(1,{}).encode()[:4]) == 4


def test_json_sorted():
    m = WireMessage(1,{"b":2,"a":1})
    assert b'"a"' in m.encode()


def test_multiple_fields():
    m = WireMessage(5,{"node":"A","ok":True})
    d = WireMessage.decode(m.encode())
    assert d.payload["ok"] is True
