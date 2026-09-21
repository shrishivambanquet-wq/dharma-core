"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass
import hashlib
import secrets


@dataclass
class NodeIdentity:
    node_id: str
    secret: str

    @staticmethod
    def create(node_id: str):
        return NodeIdentity(node_id, secrets.token_hex(32))

    def public_key(self):
        return hashlib.sha256(self.secret.encode()).hexdigest()

    def fingerprint(self):
        return self.public_key()[:16]
