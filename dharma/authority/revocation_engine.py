"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from .revocation_list import RevocationList


class RevocationEngine:
    def __init__(self, revocations=None):
        self.revocations = revocations or RevocationList()

    def revoke(self, certificate):
        self.revocations.revoke(certificate.certificate_id)
        certificate.revoke()

    def is_valid(self, certificate):
        return (
            not certificate.revoked
            and not self.revocations.is_revoked(certificate.certificate_id)
        )

    def revoked_count(self):
        return self.revocations.count()
