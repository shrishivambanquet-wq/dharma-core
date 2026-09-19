from dharma.authority.registry import AuthorityRegistry
from dharma.authority.node import AuthorityNode
from dharma.authority.enums import AuthorityKind


def test_register():
    r = AuthorityRegistry()
    a = AuthorityNode(AuthorityKind.PERSON, "Alice", id="1")
    r.register(a)
    assert r.count() == 1


def test_get():
    r = AuthorityRegistry()
    a = AuthorityNode(AuthorityKind.PERSON, "Alice", id="1")
    r.register(a)
    assert r.get("1") == a


def test_exists():
    r = AuthorityRegistry()
    a = AuthorityNode(AuthorityKind.PERSON, "Alice", id="1")
    r.register(a)
    assert r.exists("1")


def test_by_name():
    r = AuthorityRegistry()
    r.register(AuthorityNode(AuthorityKind.PERSON, "Alice", id="1"))
    assert len(r.by_name("Alice")) == 1


def test_duplicate_id_replaces():
    r = AuthorityRegistry()
    r.register(AuthorityNode(AuthorityKind.PERSON, "Alice", id="1"))
    r.register(AuthorityNode(AuthorityKind.PERSON, "Alice Updated", id="1"))
    assert r.count() == 1
    assert r.get("1").name == "Alice Updated"
