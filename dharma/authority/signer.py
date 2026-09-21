"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from nacl.signing import SigningKey, VerifyKey
from nacl.encoding import HexEncoder


class AuthoritySigner:
    def __init__(self, signing_key: SigningKey):
        self._signing_key = signing_key
        self._verify_key = signing_key.verify_key

    @classmethod
    def generate(cls):
        return cls(SigningKey.generate())

    def public_key(self):
        return self._verify_key.encode(encoder=HexEncoder).decode()

    def sign(self, message: bytes):
        return self._signing_key.sign(message).signature

    def verify(self, message: bytes, signature: bytes):
        try:
            self._verify_key.verify(message, signature)
            return True
        except Exception:
            return False
