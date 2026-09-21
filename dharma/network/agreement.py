"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass

PENDING = "pending"
ACCEPTED = "accepted"
REJECTED = "rejected"


@dataclass
class TrustAgreement:
    requester: str
    responder: str
    status: str = PENDING

    def accept(self):
        self.status = ACCEPTED

    def reject(self):
        self.status = REJECTED

    def is_final(self):
        return self.status in (ACCEPTED, REJECTED)
