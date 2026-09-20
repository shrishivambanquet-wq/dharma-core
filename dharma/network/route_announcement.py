from dataclasses import dataclass
import json

from .ed25519 import Ed25519Identity, verify


@dataclass
class RouteAnnouncement:
    node_id: str
    endpoint: str
    signature: bytes | None = None

    def payload(self):
        return json.dumps({
            "node_id": self.node_id,
            "endpoint": self.endpoint,
        }, sort_keys=True).encode()

    def sign(self, identity: Ed25519Identity):
        self.signature = identity.sign(self.payload())
        return self

    def verify(self, verify_key):
        if self.signature is None:
            return False
        return verify(self.payload(), self.signature, verify_key)
