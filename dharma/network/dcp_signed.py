from dataclasses import dataclass

from .dcp import DCPMessage
from .ed25519 import Ed25519Identity, verify


@dataclass
class SignedDCPMessage:
    message: DCPMessage
    signature: bytes

    @staticmethod
    def sign(message: DCPMessage, identity: Ed25519Identity):
        return SignedDCPMessage(
            message=message,
            signature=identity.sign(message.encode().encode()),
        )

    def verify(self, verify_key):
        return verify(
            self.message.encode().encode(),
            self.signature,
            verify_key,
        )
