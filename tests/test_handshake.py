"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import pytest
from dharma.network.handshake import Handshake

def test_hello():
    assert Handshake().hello()["type"] == "hello"

def test_nonce_exists():
    assert Handshake().hello()["nonce"] != ""

def test_accept():
    h = Handshake()
    h.hello()
    assert h.accept("abcd")["type"] == "accept"

def test_store_remote():
    h = Handshake()
    h.hello()
    h.accept("abcd")
    assert h.remote_nonce == "abcd"

def test_established():
    h = Handshake()
    h.hello()
    h.accept("abcd")
    assert h.established()

def test_nonce_reuse():
    h = Handshake()
    n = h.hello()["nonce"]
    with pytest.raises(ValueError):
        h.accept(n)

def test_two_instances():
    assert Handshake().hello()["nonce"] != Handshake().hello()["nonce"]

def test_accept_nonce():
    h = Handshake()
    h.hello()
    assert h.accept("xyz")["nonce"] != ""
