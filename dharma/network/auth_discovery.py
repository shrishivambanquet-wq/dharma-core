"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass, field

from .route_announcement import RouteAnnouncement


@dataclass
class AuthDiscoveryRegistry:
    nodes: dict = field(default_factory=dict)

    def register(self, announcement: RouteAnnouncement, verify_key):
        if not announcement.verify(verify_key):
            return False
        self.nodes[announcement.node_id] = announcement.endpoint
        return True

    def discover(self, node_id):
        return self.nodes.get(node_id)

    def count(self):
        return len(self.nodes)
