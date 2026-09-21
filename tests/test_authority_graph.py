"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.authority.graph import AuthorityGraph
from dharma.authority.authority_graph import AuthorityGraph

def test_add_authority():
    g = AuthorityGraph()
    g.add_authority("root")
    assert g.exists("root")

def test_connect():
    g = AuthorityGraph()
    g.connect("root", "alice")
    assert "alice" in g.children("root")

def test_children_sorted():
    g = AuthorityGraph()
    g.connect("root", "bob")
    g.connect("root", "alice")
    assert g.children("root") == ["alice", "bob"]

def test_missing_children():
    assert AuthorityGraph().children("x") == []

def test_exists_false():
    assert not AuthorityGraph().exists("ghost")
from dharma.authority.node import AuthorityNode
from dharma.authority.edge import AuthorityEdge
from dharma.authority.enums import AuthorityKind
from dharma.authority.relations import AuthorityRelation

def test_add_node():
    g = AuthorityGraph()
    p = AuthorityNode(AuthorityKind.PERSON, "Paresh")
    g.add_node(p)
    assert p.id in g.nodes

def test_add_edge():
    g = AuthorityGraph()
    p = AuthorityNode(AuthorityKind.PERSON, "Paresh")
    o = AuthorityNode(AuthorityKind.ORGANIZATION, "Somani Caterers")
    g.add_node(p)
    g.add_node(o)

    e = AuthorityEdge(p, o, AuthorityRelation.DELEGATES)
    g.add_edge(e)

    assert len(g.edges) == 1

def test_outgoing():
    g = AuthorityGraph()
    p = AuthorityNode(AuthorityKind.PERSON, "Paresh")
    o = AuthorityNode(AuthorityKind.ORGANIZATION, "Somani Caterers")

    g.add_node(p)
    g.add_node(o)

    e = AuthorityEdge(p, o, AuthorityRelation.DELEGATES)
    g.add_edge(e)

    assert len(g.outgoing(p.id)) == 1

def test_incoming():
    g = AuthorityGraph()
    p = AuthorityNode(AuthorityKind.PERSON, "Paresh")
    o = AuthorityNode(AuthorityKind.ORGANIZATION, "Somani Caterers")

    g.add_node(p)
    g.add_node(o)

    e = AuthorityEdge(p, o, AuthorityRelation.DELEGATES)
    g.add_edge(e)

    assert len(g.incoming(o.id)) == 1
def test_graph_starts_empty():
    graph = AuthorityGraph()
    assert len(graph.nodes) == 0
    assert len(graph.edges) == 0


def test_unknown_node_returns_empty():
    graph = AuthorityGraph()
    assert graph.neighbors("missing-node") == []
