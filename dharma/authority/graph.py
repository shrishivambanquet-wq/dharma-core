"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from .node import AuthorityNode
from .edge import AuthorityEdge

class AuthorityGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node: AuthorityNode):
        self.nodes[node.id] = node

    def add_edge(self, edge: AuthorityEdge):
        self.edges.append(edge)

    def outgoing(self, node_id):
        return [e for e in self.edges if e.source.id == node_id]

    def incoming(self, node_id):
        return [e for e in self.edges if e.target.id == node_id]
    def neighbors(self, node_id: str):
        result = []
        for edge in self.edges:
            if edge.source.id == node_id:
                result.append(edge.target.id)
        return result
