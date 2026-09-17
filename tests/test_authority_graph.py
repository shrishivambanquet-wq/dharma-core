from dharma.authority.graph import AuthorityGraph
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
