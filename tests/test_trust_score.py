from dharma.authority.trust import TrustScore
from dharma.authority.trust_enums import TrustLevel

def test_verified_score():
    assert TrustScore.from_level(TrustLevel.VERIFIED).value == 1.0

def test_clamp_high():
    assert TrustScore(1.5).clamp().value == 1.0

def test_clamp_low():
    assert TrustScore(-0.5).clamp().value == 0.0
def test_propagate_full_weight():
    assert TrustScore(1.0).propagate(1.0).value == 1.0

def test_propagate_half_weight():
    assert TrustScore(0.8).propagate(0.5).value == 0.4

def test_propagate_zero_weight():
    assert TrustScore(0.9).propagate(0.0).value == 0.0
