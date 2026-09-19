from dharma.authority.policy import AuthorityPolicy
from dharma.authority.policy_engine import PolicyEngine


def test_allowed():
    p = PolicyEngine(AuthorityPolicy())
    assert p.evaluate("A", "B", 1)


def test_self_denied():
    p = PolicyEngine(AuthorityPolicy())
    assert not p.evaluate("A", "A", 1)


def test_depth_denied():
    p = PolicyEngine(AuthorityPolicy(max_depth=2))
    assert not p.evaluate("A", "B", 3)


def test_reason_self():
    p = PolicyEngine(AuthorityPolicy())
    assert p.reason("A", "A", 1) == "self_delegation_denied"


def test_reason_allowed():
    p = PolicyEngine(AuthorityPolicy())
    assert p.reason("A", "B", 1) == "allowed"
