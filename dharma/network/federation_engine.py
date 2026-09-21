"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from .federation_join import FederationJoin
from .federation_leave import FederationLeave
from .federation_coordinator import FederationCoordinator

class FederationEngine:
    def __init__(self):
        self.joiner = FederationJoin()
        self.leaver = FederationLeave()
        self.coordinator = FederationCoordinator()

    def join(self, node):
        self.coordinator.join(node)
        return self.joiner.join(node)

    def leave(self, node):
        self.coordinator.leave(node)
        return self.leaver.leave(node)

    def active(self, node):
        return self.coordinator.active(node)

    def count(self):
        return self.coordinator.count()
