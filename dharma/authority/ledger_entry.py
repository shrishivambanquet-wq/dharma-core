"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import hashlib
from dataclasses import dataclass


@dataclass
class LedgerEntry:
    payload: str
    previous_hash: str = ""

    def hash(self):
        text = f"{self.previous_hash}|{self.payload}"
        return hashlib.sha256(text.encode()).hexdigest()
