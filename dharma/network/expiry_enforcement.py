"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

class ExpiryEnforcement:
    def expired(self,now,expiry):
        return now>=expiry
