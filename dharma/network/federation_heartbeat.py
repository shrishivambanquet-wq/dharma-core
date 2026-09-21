"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import time

class FederationHeartbeat:
    def __init__(self):
        self.last={}

    def beat(self,node):
        self.last[node]=int(time.time())
        return self.last[node]

    def seen(self,node):
        return node in self.last

    def latest(self,node):
        return self.last.get(node)

    def count(self):
        return len(self.last)
