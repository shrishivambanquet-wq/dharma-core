"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class AuditEvent:
    authority_id: str
    event: str
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def serialize(self):
        return {
            "authority_id": self.authority_id,
            "event": self.event,
            "timestamp": self.timestamp.isoformat(),
        }
