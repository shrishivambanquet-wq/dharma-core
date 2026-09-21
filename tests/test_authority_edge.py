"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.authority.node import AuthorityNode
from dharma.authority.edge import AuthorityEdge
from dharma.authority.enums import AuthorityKind

def test_edge_has_uuid():
    a = AuthorityNode(AuthorityKind.PERSON, "Paresh")
    b = AuthorityNode(AuthorityKind.ORGANIZATION, "Somani Caterers")
    edge = AuthorityEdge(a, b, "delegates")
    assert len(edge.id) > 0

def test_relation_is_preserved():
    a = AuthorityNode(AuthorityKind.PERSON, "Paresh")
    b = AuthorityNode(AuthorityKind.ORGANIZATION, "Somani Caterers")
    edge = AuthorityEdge(a, b, "delegates")
    assert edge.relation == "delegates"

def test_source_is_preserved():
    a = AuthorityNode(AuthorityKind.PERSON, "Paresh")
    b = AuthorityNode(AuthorityKind.ORGANIZATION, "Somani Caterers")
    edge = AuthorityEdge(a, b, "delegates")
    assert edge.source is a

def test_target_is_preserved():
    a = AuthorityNode(AuthorityKind.PERSON, "Paresh")
    b = AuthorityNode(AuthorityKind.ORGANIZATION, "Somani Caterers")
    edge = AuthorityEdge(a, b, "delegates")
    assert edge.target is b
