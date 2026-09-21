"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

class ConflictResolution:
    def choose(self,left,right):
        return max(left,right,key=lambda x:x["version"])
