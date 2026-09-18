from dataclasses import dataclass, field

from .node import AuthorityNode
from .edge import AuthorityEdge
from .enums import AuthorityKind
from .relations import AuthorityRelation

@dataclass
class AuthorityGraph:
    nodes: dict = field(default_factory=dict)
    edges: list = field(default_factory=list)

    def add_authority(self, name: str):
        if name in self.nodes:
            return self.nodes[name]

        node = AuthorityNode(
            AuthorityKind.PERSON,
            name,
            id=name,
        )
        self.add_node(node)
        return node

    def add_node(self, node: AuthorityNode):
        self.nodes[node.id] = node
        return node

    def add_edge(self, edge, child=None, relation=None):
        if isinstance(edge, AuthorityEdge):
            actual_edge = edge
        else:
            parent = edge
            actual_edge = AuthorityEdge(parent, child, relation)

        self.add_node(actual_edge.source)
        self.add_node(actual_edge.target)

        if actual_edge not in self.edges:
            self.edges.append(actual_edge)

        return actual_edge

    def outgoing(self, node_id):
        return [
            edge
            for edge in self.edges
            if edge.source.id == node_id
        ]

    def incoming(self, node_id):
        return [
            edge
            for edge in self.edges
            if edge.target.id == node_id
        ]

    def neighbors(self, node_id):
        return [
            edge.target.id
            for edge in self.outgoing(node_id)
        ]

    def children(self, node_id):
        return sorted(self.neighbors(node_id))

    def exists(self, node_or_id):
        if hasattr(node_or_id, "id"):
            return node_or_id.id in self.nodes

        if node_or_id in self.nodes:
            return True

        return any(
            node.name == node_or_id
            for node in self.nodes.values()
        )

    def connect(self, parent, child):
        if isinstance(parent, str):
            parent = self.nodes.get(parent) or self.add_authority(parent)

        if isinstance(child, str):
            child = self.nodes.get(child) or self.add_authority(child)

        edge = AuthorityEdge(
            parent,
            child,
            AuthorityRelation.DELEGATES,
        )

        return self.add_edge(edge)
