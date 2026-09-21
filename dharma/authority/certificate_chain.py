"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass, field

from .signed_certificate import SignedCertificate


@dataclass
class CertificateChain:
    certificates: list[SignedCertificate] = field(default_factory=list)

    def add(self, certificate: SignedCertificate):
        self.certificates.append(certificate)

    def first(self):
        return self.certificates[0]

    def last(self):
        return self.certificates[-1]

    def count(self):
        return len(self.certificates)
