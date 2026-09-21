"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

class FederationState:
    def __init__(self):
        self.members = {}
        self.revoked = set()

    def join(self, node, endpoint):
        if node in self.revoked:
            return False
        self.members[node] = endpoint
        return True

    def leave(self, node):
        return self.members.pop(node, None) is not None

    def revoke(self, node):
        self.revoked.add(node)
        self.members.pop(node, None)

    def active(self, node):
        return node in self.members

    def count(self):
        return len(self.members)
