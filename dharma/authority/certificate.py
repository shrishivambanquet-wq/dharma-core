"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass, field
from uuid import uuid4
from datetime import datetime, timezone

@dataclass
class AuthorityCertificate:
    issuer_id: str
    subject_id: str
    purpose: str
    certificate_id: str = field(default_factory=lambda: str(uuid4()))
    issued_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    revoked: bool = False

    def revoke(self):
        self.revoked = True
