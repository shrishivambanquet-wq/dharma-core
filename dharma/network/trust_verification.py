"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

class TrustVerification:
    def verify(self,anchor,node):
        return anchor.trusted(node)
