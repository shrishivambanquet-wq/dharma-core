"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.authority.trust_policy import TrustPolicy
from dharma.authority.trust_score import TrustScore


def test_default_threshold():
    assert TrustPolicy().threshold == 0.5


def test_allows_above_threshold():
    assert TrustPolicy().allows(TrustScore(0.8))


def test_denies_below_threshold():
    assert TrustPolicy().deny(TrustScore(0.2))


def test_custom_threshold():
    p = TrustPolicy(0.8)
    assert p.allows(TrustScore(0.8))


def test_set_threshold():
    p = TrustPolicy()
    p.set_threshold(0.7)
    assert p.threshold == 0.7
