"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import hashlib

class Fingerprint:
    @staticmethod
    def of(text: str):
        return hashlib.sha256(text.encode()).hexdigest()
