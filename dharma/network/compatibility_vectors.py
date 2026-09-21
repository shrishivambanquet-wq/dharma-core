"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

class CompatibilityVectors:
    def compatible(self,a,b):
        return a["protocol"]==b["protocol"]

    def shared(self,a,b):
        return sorted(set(a["features"]) & set(b["features"]))
