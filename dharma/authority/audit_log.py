"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass, field

from .audit_event import AuditEvent


@dataclass
class AuditLog:
    events: list[AuditEvent] = field(default_factory=list)

    def append(self, event: AuditEvent):
        self.events.append(event)

    def count(self):
        return len(self.events)

    def by_authority(self, authority_id: str):
        return [
            e for e in self.events
            if e.authority_id == authority_id
        ]

    def last(self):
        return self.events[-1] if self.events else None
