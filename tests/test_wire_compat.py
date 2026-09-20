import pytest
from dharma.network.wire import WireMessage
from dharma.network.wire_compat import WireCompatibility


def test_canonical():
    assert WireCompatibility.canonical(1, {}) == WireMessage(1, {}).encode()


def test_roundtrip():
    m = WireMessage(2, {"x": 1})
    assert WireMessage.decode(m.encode()).payload == {"x": 1}


def test_unknown_type():
    assert WireMessage.decode(WireMessage(99, {}).encode()).msg_type == 99


def test_empty():
    assert WireMessage.decode(WireMessage(1, {}).encode()).payload == {}


def test_large():
    data = {"blob": "x" * 1000}
    assert WireMessage.decode(WireMessage(1, data).encode()).payload == data


def test_header():
    assert len(WireMessage(1, {}).encode()[:4]) == 4


def test_truncated():
    with pytest.raises(Exception):
        WireMessage.decode(WireMessage(1, {}).encode()[:2])


def test_bad_json():
    bad = WireMessage(1, {}).encode()[:4] + b"{"
    with pytest.raises(Exception):
        WireMessage.decode(bad)


def test_length():
    d = bytearray(WireMessage(1, {}).encode())
    d[3] = 99
    with pytest.raises(Exception):
        WireMessage.decode(bytes(d))


def test_identical():
    a = WireCompatibility.canonical(1, {"a": 1})
    b = WireCompatibility.canonical(1, {"a": 1})
    assert WireCompatibility.identical(a, b)


def test_deterministic():
    assert (
        WireCompatibility.canonical(1, {"b": 2, "a": 1})
        == WireCompatibility.canonical(1, {"a": 1, "b": 2})
    )


def test_multifield():
    m = WireMessage(7, {"a": 1, "b": 2})
    d = WireMessage.decode(m.encode())
    assert d.payload["a"] == 1
    assert d.payload["b"] == 2
