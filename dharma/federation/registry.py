from dataclasses import dataclass, field

from .node import FederationNode


@dataclass
class FederationRegistry:
    nodes: dict = field(default_factory=dict)

    def register(self, node: FederationNode):
        self.nodes[node.node_id] = node
        return node

    def get(self, node_id):
        return self.nodes.get(node_id)

    def count(self):
        return len(self.nodes)

    def all(self):
        return list(self.nodes.values())
