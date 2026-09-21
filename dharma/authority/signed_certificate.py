"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass

from .fingerprint import Fingerprint
from .signer import AuthoritySigner


@dataclass
class SignedCertificate:
    issuer: str
    subject: str
    relation: str

    def payload(self):
        return f"{self.issuer}|{self.subject}|{self.relation}"

    def fingerprint(self):
        return Fingerprint.of(self.payload())

    def sign(self, signer: AuthoritySigner):
        return signer.sign(self.fingerprint().encode())

    def verify(self, signer: AuthoritySigner, signature: bytes):
        return signer.verify(self.fingerprint().encode(), signature)
