"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.expiry_enforcement import ExpiryEnforcement
def test_expired():
 e=ExpiryEnforcement();assert e.expired(10,10)
def test_before():
 e=ExpiryEnforcement();assert not e.expired(9,10)
def test_after():
 e=ExpiryEnforcement();assert e.expired(11,10)
def test_zero():
 e=ExpiryEnforcement();assert e.expired(0,0)
def test_many():
 e=ExpiryEnforcement();assert e.expired(100,1)
def test_equal():
 e=ExpiryEnforcement();assert e.expired(5,5)
def test_small():
 e=ExpiryEnforcement();assert not e.expired(1,2)
def test_large():
 e=ExpiryEnforcement();assert e.expired(1000,2)
def test_negative():
 e=ExpiryEnforcement();assert e.expired(-1,-2)
def test_negative2():
 e=ExpiryEnforcement();assert not e.expired(-3,-2)
def test_type():
 e=ExpiryEnforcement();assert isinstance(e.expired(1,1),bool)
def test_int():
 e=ExpiryEnforcement();assert e.expired(2,1)
