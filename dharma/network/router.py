"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass, field


@dataclass
class NetworkRouter:
    routes: dict = field(default_factory=dict)

    def register(self, node_id, endpoint):
        if not node_id:
            raise ValueError("node_id required")
        self.routes[node_id] = endpoint

    def resolve(self, node_id):
        return self.routes.get(node_id)

    def count(self):
        return len(self.routes)
