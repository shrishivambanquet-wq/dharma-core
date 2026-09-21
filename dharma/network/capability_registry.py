class CapabilityRegistry:
    def __init__(self):
        self.capabilities = {}

    def add(self, node, capability):
        self.capabilities.setdefault(node, set()).add(capability)
        return True

    def remove(self, node, capability):
        if capability not in self.capabilities.get(node, set()):
            return False
        self.capabilities[node].remove(capability)
        return True

    def has(self, node, capability):
        return capability in self.capabilities.get(node, set())

    def list(self, node):
        return sorted(self.capabilities.get(node, set()))

    def count(self, node):
        return len(self.capabilities.get(node, set()))
