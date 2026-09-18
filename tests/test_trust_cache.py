from dharma.authority.trust_cache import TrustCache


def test_cache_starts_empty():
    c = TrustCache()
    assert c.size() == 0


def test_put_one():
    c = TrustCache()
    c.put("a", 1)
    assert c.get("a") == 1


def test_has_key():
    c = TrustCache()
    c.put("a", 1)
    assert c.has("a")


def test_missing_returns_none():
    c = TrustCache()
    assert c.get("missing") is None


def test_two_entries():
    c = TrustCache()
    c.put("a", 1)
    c.put("b", 2)
    assert c.size() == 2

