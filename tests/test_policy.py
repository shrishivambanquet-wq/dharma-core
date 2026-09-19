from dharma.authority.policy import AuthorityPolicy


def test_default_depth():
    assert AuthorityPolicy().allows_depth(5)


def test_depth_limit():
    assert not AuthorityPolicy(max_depth=2).allows_depth(3)


def test_self_blocked():
    assert not AuthorityPolicy().allows_self("A", "A")


def test_self_allowed():
    assert AuthorityPolicy(allow_self_delegation=True).allows_self("A", "A")


def test_normal_delegation():
    assert AuthorityPolicy().allows_self("A", "B")
