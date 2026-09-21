"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.authority.authority_index import AuthorityIndex
from dharma.authority.search import AuthoritySearch
from dharma.authority.node import AuthorityNode
from dharma.authority.enums import AuthorityKind


def test_text_search():
    idx = AuthorityIndex()
    n = AuthorityNode(AuthorityKind.PERSON, "Paresh Somani")
    idx.add(n)
    assert AuthoritySearch(idx).text("Paresh")[0] == n


def test_partial_search():
    idx = AuthorityIndex()
    n = AuthorityNode(AuthorityKind.ORGANIZATION, "Somani Caterers")
    idx.add(n)
    assert AuthoritySearch(idx).text("Cater")[0] == n


def test_case_insensitive_search():
    idx = AuthorityIndex()
    n = AuthorityNode(AuthorityKind.PERSON, "Paresh")
    idx.add(n)
    assert AuthoritySearch(idx).text("PARESH")[0] == n


def test_search_by_kind():
    idx = AuthorityIndex()
    idx.add(AuthorityNode(AuthorityKind.PERSON, "Paresh"))
    idx.add(AuthorityNode(AuthorityKind.ORGANIZATION, "Somani"))
    assert len(AuthoritySearch(idx).by_kind(AuthorityKind.ORGANIZATION)) == 1


def test_missing_search():
    assert AuthoritySearch(AuthorityIndex()).text("Ghost") == []
