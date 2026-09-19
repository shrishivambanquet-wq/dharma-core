from dataclasses import dataclass
import hashlib

from .dcp import DCPMessage
from .identity import NodeIdentity


@dataclass
class SignedMessage:
    message: DCPMessage
    signature: str

    @staticmethod
    def sign(message: DCPMessage, identity: NodeIdentity):
        text = message.encode() + identity.secret
        sig = hashlib.sha256(text.encode()).hexdigest()
        return SignedMessage(message, sig)

    def verify(self, identity: NodeIdentity):
        expected = hashlib.sha256(
            (self.message.encode() + identity.secret).encode()
        ).hexdigest()
        return expected == self.signature
