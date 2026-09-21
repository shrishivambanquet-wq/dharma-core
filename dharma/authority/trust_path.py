"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

class TrustPath:
    def __init__(self):
        self.nodes = []

    def add(self, node):
        self.nodes.append(node)

    def length(self):
        return len(self.nodes)

    def first(self):
        return self.nodes[0] if self.nodes else None

    def last(self):
        return self.nodes[-1] if self.nodes else None
