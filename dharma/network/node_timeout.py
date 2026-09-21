"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

class NodeTimeout:
    def expired(self,last_seen,now,limit):
        return (now-last_seen)>limit
