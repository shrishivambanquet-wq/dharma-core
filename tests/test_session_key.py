"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.session_key import SessionKey

def test_same_inputs():
    a = SessionKey.derive("a","b")
    b = SessionKey.derive("a","b")
    assert a == b

def test_order_independent():
    assert SessionKey.derive("a","b") == SessionKey.derive("b","a")

def test_length():
    assert len(SessionKey.derive("a","b")) == 64

def test_hex():
    int(SessionKey.derive("a","b"),16)

def test_unique():
    assert SessionKey.derive("a","b") != SessionKey.derive("a","c")

def test_not_empty():
    assert SessionKey.derive("x","y")

def test_repeatable():
    assert SessionKey.derive("1","2") == SessionKey.derive("1","2")

def test_case_sensitive():
    assert SessionKey.derive("A","b") != SessionKey.derive("a","b")
