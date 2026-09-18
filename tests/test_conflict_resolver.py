from dharma.authority.conflict_resolver import ConflictResolver
from dharma.authority.trust_score import TrustScore


def test_choose_higher_score():
    r = ConflictResolver()
    assert r.choose(TrustScore(0.9), TrustScore(0.4)).value == 0.9


def test_choose_second_when_higher():
    r = ConflictResolver()
    assert r.choose(TrustScore(0.3), TrustScore(0.8)).value == 0.8


def test_tie_detected():
    r = ConflictResolver()
    assert r.tie(TrustScore(0.7), TrustScore(0.7))


def test_gap_calculation():
    r = ConflictResolver()
    assert r.confidence_gap(TrustScore(0.9), TrustScore(0.4)) == 0.5


def test_gap_zero_on_equal():
    r = ConflictResolver()
    assert r.confidence_gap(TrustScore(0.6), TrustScore(0.6)) == 0.0

