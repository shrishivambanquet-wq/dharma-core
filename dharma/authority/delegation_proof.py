"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass

from .certificate_chain import CertificateChain


@dataclass
class DelegationProof:
    chain: CertificateChain

    def is_valid(self):
        if self.chain.count() == 0:
            return True

        certs = self.chain.certificates

        for current, nxt in zip(certs, certs[1:]):
            if current.subject != nxt.issuer:
                return False

        return True

    def root(self):
        return self.chain.first().issuer if self.chain.count() else None

    def target(self):
        return self.chain.last().subject if self.chain.count() else None
