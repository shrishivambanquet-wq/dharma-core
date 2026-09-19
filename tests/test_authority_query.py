from dharma.authority.authority_index import AuthorityIndex
from dharma.authority.query import AuthorityQuery
from dharma.authority.node import AuthorityNode
from dharma.authority.enums import AuthorityKind


def test_query_by_id():
    idx = AuthorityIndex()
    n = AuthorityNode(AuthorityKind.PERSON, "Paresh")
    idx.add(n)
    assert AuthorityQuery(idx).by_id(n.id) == n


def test_query_by_name():
    idx = AuthorityIndex()
    n = AuthorityNode(AuthorityKind.PERSON, "Paresh")
    idx.add(n)
    assert AuthorityQuery(idx).by_name("Paresh") == n


def test_query_case_insensitive():
    idx = AuthorityIndex()
    n = AuthorityNode(AuthorityKind.PERSON, "Paresh")
    idx.add(n)
    assert AuthorityQuery(idx).by_name("PARESH") == n


def test_query_by_kind():
    idx = AuthorityIndex()
    idx.add(AuthorityNode(AuthorityKind.PERSON, "Paresh"))
    idx.add(AuthorityNode(AuthorityKind.ORGANIZATION, "Somani"))
    assert len(AuthorityQuery(idx).by_kind(AuthorityKind.PERSON)) == 1


def test_missing_returns_none():
    assert AuthorityQuery(AuthorityIndex()).by_name("Ghost") is None
