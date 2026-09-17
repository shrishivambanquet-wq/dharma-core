from dharma.authority.graph import AuthorityGraph
from dharma.authority.node import AuthorityNode
from dharma.authority.edge import AuthorityEdge
from dharma.authority.resolver import AuthorityResolver
from dharma.authority.enums import AuthorityKind
from dharma.authority.relations import AuthorityRelation

def build_graph():
    g = AuthorityGraph()

    paresh = AuthorityNode(AuthorityKind.PERSON, "Paresh")
    somani = AuthorityNode(AuthorityKind.ORGANIZATION, "Somani Caterers")
    drfc = AuthorityNode(AuthorityKind.DOCUMENT, "DRFC-0009")

    g.add_node(paresh)
    g.add_node(somani)
    g.add_node(drfc)

    g.add_edge(AuthorityEdge(paresh, somani, AuthorityRelation.DELEGATES))
    g.add_edge(AuthorityEdge(somani, drfc, AuthorityRelation.VERIFIES))

    return g, paresh, somani, drfc

def test_direct_reach():
    g, paresh, somani, _ = build_graph()
    r = AuthorityResolver(g)
    assert r.can_reach(paresh.id, somani.id)

def test_transitive_reach():
    g, paresh, _, drfc = build_graph()
    r = AuthorityResolver(g)
    assert r.can_reach(paresh.id, drfc.id)

def test_unreachable():
    g, paresh, somani, _ = build_graph()
    r = AuthorityResolver(g)
    assert not r.can_reach(somani.id, paresh.id)
