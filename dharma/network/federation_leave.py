"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

class FederationLeave:
    def __init__(self):
        self.left = set()

    def leave(self, node_id):
        if node_id in self.left:
            return False
        self.left.add(node_id)
        return True

    def has_left(self, node_id):
        return node_id in self.left

    def restore(self, node_id):
        return self.left.discard(node_id) is None

    def count(self):
        return len(self.left)

    def all(self):
        return sorted(self.left)
