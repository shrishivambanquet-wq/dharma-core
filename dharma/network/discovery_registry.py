"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass, field


@dataclass
class DiscoveryRegistry:
    nodes: dict = field(default_factory=dict)

    def register(self, node_id, endpoint):
        if not node_id:
            raise ValueError("node_id required")
        self.nodes[node_id] = endpoint

    def discover(self, node_id):
        return self.nodes.get(node_id)

    def remove(self, node_id):
        return self.nodes.pop(node_id, None)

    def count(self):
        return len(self.nodes)
