from dataclasses import dataclass, field


@dataclass
class DiscoveryRegistry:
    nodes: dict = field(default_factory=dict)

    def announce(self, node_id, endpoint):
        self.nodes[node_id] = endpoint

    def resolve(self, node_id):
        return self.nodes.get(node_id)

    def count(self):
        return len(self.nodes)
