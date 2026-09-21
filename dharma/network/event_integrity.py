"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import hashlib
import json

class EventIntegrity:
    def digest(self,event):
        return hashlib.sha256(json.dumps(event,sort_keys=True).encode()).hexdigest()

    def verify(self,event,digest):
        return self.digest(event)==digest
