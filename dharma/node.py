"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from .network.federation_engine import FederationEngine

class Node:
    def __init__(self):
        self.engine = FederationEngine()

    def join(self, node="local"):
        return self.engine.join(node)

    def leave(self, node="local"):
        return self.engine.leave(node)
