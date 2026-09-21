"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass

from nacl.signing import SigningKey, VerifyKey
from nacl.exceptions import BadSignatureError


@dataclass
class Ed25519Identity:
    signing_key: SigningKey

    @staticmethod
    def create():
        return Ed25519Identity(SigningKey.generate())

    def verify_key(self):
        return self.signing_key.verify_key

    def sign(self, data: bytes):
        return self.signing_key.sign(data).signature


def verify(data: bytes, signature: bytes, verify_key: VerifyKey):
    try:
        verify_key.verify(data, signature)
        return True
    except BadSignatureError:
        return False
