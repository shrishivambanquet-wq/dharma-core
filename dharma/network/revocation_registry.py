"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import time

class RevocationRegistry:
    def __init__(self):
        self.revoked = {}

    def revoke(self, node, reason="unspecified"):
        self.revoked[node] = {
            "timestamp": int(time.time()),
            "reason": reason,
        }
        return self.revoked[node]

    def is_revoked(self, node):
        return node in self.revoked

    def info(self, node):
        return self.revoked.get(node)

    def count(self):
        return len(self.revoked)

    def all(self):
        return dict(self.revoked)
