from dharma.authority.index import AuthorityIndex
from dharma.authority.node import AuthorityNode
from dharma.authority.enums import AuthorityKind


def test_add_authority():
    idx = AuthorityIndex()
    a = AuthorityNode(AuthorityKind.PERSON, "Alice", id="1")
    idx.add(a)
    assert idx.count() == 1


def test_get_authority():
    idx = AuthorityIndex()
    a = AuthorityNode(AuthorityKind.PERSON, "Alice", id="1")
    idx.add(a)
    assert idx.get("1") == a


def test_by_kind():
    idx = AuthorityIndex()
    idx.add(AuthorityNode(AuthorityKind.PERSON, "Alice", id="1"))
    assert len(idx.by_kind(AuthorityKind.PERSON)) == 1


def test_by_name():
    idx = AuthorityIndex()
    idx.add(AuthorityNode(AuthorityKind.PERSON, "Alice", id="1"))
    assert len(idx.by_name("Alice")) == 1


def test_count():
    idx = AuthorityIndex()
    idx.add(AuthorityNode(AuthorityKind.PERSON, "Alice", id="1"))
    idx.add(AuthorityNode(AuthorityKind.PERSON, "Bob", id="2"))
    assert idx.count() == 2
