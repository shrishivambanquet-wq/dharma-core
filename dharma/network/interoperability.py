from dataclasses import dataclass

from .ed25519 import Ed25519Identity
from .key_exchange import KeyExchange
from .session_resume import SessionResume


@dataclass
class DharmaNode:
    node_id: str

    def __post_init__(self):
        self.identity = Ed25519Identity.create()
        self.keys = KeyExchange(self.identity)

    def hello(self):
        return {
            "node": self.node_id,
            "public_key": self.keys.public_key(),
        }

    def establish(self, remote):
        self.session = SessionResume(
            f"{self.node_id}-{remote.node_id}"
        )
        return self.session.resume()
