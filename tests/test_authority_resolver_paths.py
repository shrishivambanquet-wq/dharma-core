from dharma.authority.node import AuthorityNode
from dharma.authority.edge import AuthorityEdge
from dharma.authority.enums import AuthorityKind
from dharma.authority.graph import AuthorityGraph
from dharma.authority.resolver import AuthorityResolver


def test_can_reach_direct():
    graph = AuthorityGraph()

    person = AuthorityNode(AuthorityKind.PERSON, "Paresh")
    org = AuthorityNode(AuthorityKind.ORGANIZATION, "Somani Caterers")

    graph.add_node(person)
    graph.add_node(org)
    graph.add_edge(AuthorityEdge(person, org, "represents"))

    resolver = AuthorityResolver(graph)

    assert resolver.can_reach(person.id, org.id)


def test_cannot_reach_disconnected():
    graph = AuthorityGraph()

    a = AuthorityNode(AuthorityKind.PERSON, "A")
    b = AuthorityNode(AuthorityKind.PERSON, "B")

    graph.add_node(a)
    graph.add_node(b)

    resolver = AuthorityResolver(graph)

    assert resolver.can_reach(a.id, b.id) is False
