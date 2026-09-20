from dataclasses import dataclass
import json
import time

from .ed25519 import Ed25519Identity, verify


@dataclass
class FederationCertificate:
    issuer: str
    subject: str
    issued_at: int
    expires_at: int
    signature: bytes | None = None

    def payload(self):
        return json.dumps({
            "issuer": self.issuer,
            "subject": self.subject,
            "issued_at": self.issued_at,
            "expires_at": self.expires_at,
        }, sort_keys=True).encode()

    def sign(self, identity: Ed25519Identity):
        self.signature = identity.sign(self.payload())
        return self

    def verify(self, verify_key):
        if self.signature is None:
            return False
        if self.expires_at < int(time.time()):
            return False
        return verify(self.payload(), self.signature, verify_key)
