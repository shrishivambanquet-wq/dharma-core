from dharma.authority.trust_enums import TrustLevel

def test_verified_equals_one():
    assert TrustLevel.VERIFIED.value == 1.0

def test_low_less_than_high():
    assert TrustLevel.LOW.value < TrustLevel.HIGH.value
