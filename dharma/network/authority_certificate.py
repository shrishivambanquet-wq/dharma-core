"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import time
from dataclasses import dataclass

@dataclass
class AuthorityCertificate:
    node: str
    public_key: str
    ttl: int = 3600

    def issue(self):
        issued = int(time.time())
        return {
            "node": self.node,
            "public_key": self.public_key,
            "issued_at": issued,
            "expires_at": issued + self.ttl,
        }

    @staticmethod
    def valid(cert, now=None):
        if now is None:
            now = int(time.time())
        return now <= cert["expires_at"]
