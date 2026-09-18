
from dharma.authority.trust_resolver import TrustResolver
from dharma.authority.trust_score import TrustScore


def test_empty_scores():
    assert TrustResolver().resolve([]).value == 0.0


def test_single_score():
    assert TrustResolver().resolve([TrustScore(0.8)]).value == 0.8


def test_average_two_scores():
    assert TrustResolver().resolve([TrustScore(0.6), TrustScore(1.0)]).value == 0.8


def test_average_three_scores():
    assert TrustResolver().resolve([
        TrustScore(0.3),
        TrustScore(0.6),
        TrustScore(0.9),
    ]).value == 0.6


def test_returns_trustscore():
    result = TrustResolver().resolve([TrustScore(1.0)])
    assert isinstance(result, TrustScore)

