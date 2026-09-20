from dataclasses import dataclass
from nacl.encoding import HexEncoder

from .ed25519 import Ed25519Identity


@dataclass
class KeyExchange:
    identity: Ed25519Identity

    def public_key(self):
        return self.identity.verify_key().encode(
            encoder=HexEncoder
        ).decode()

    def exchange(self, remote_public_key: str):
        return {
            "local": self.public_key(),
            "remote": remote_public_key,
            "trusted": bool(remote_public_key),
        }
