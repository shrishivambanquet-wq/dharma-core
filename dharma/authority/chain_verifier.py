"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass

from .certificate_chain import CertificateChain
from .signer import AuthoritySigner


@dataclass
class ChainVerifier:
    signer: AuthoritySigner

    def verify(self, chain: CertificateChain, signatures: list[bytes]):
        if chain.count() != len(signatures):
            return False

        for cert, sig in zip(chain.certificates, signatures):
            if not cert.verify(self.signer, sig):
                return False

        return True
