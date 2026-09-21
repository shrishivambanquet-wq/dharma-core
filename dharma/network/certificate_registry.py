"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

class CertificateRegistry:
    def __init__(self):
        self.registry = {}

    def register(self, cert):
        self.registry[cert["node"]] = cert
        return True

    def get(self, node):
        return self.registry.get(node)

    def exists(self, node):
        return node in self.registry

    def revoke(self, node):
        return self.registry.pop(node, None) is not None

    def count(self):
        return len(self.registry)
