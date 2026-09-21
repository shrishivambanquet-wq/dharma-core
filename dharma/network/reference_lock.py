"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

class ReferenceLock:
    def __init__(self):
        self.version=None

    def lock(self,version):
        self.version=version

    def current(self):
        return self.version
