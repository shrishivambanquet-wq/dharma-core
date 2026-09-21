"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass, field
import uuid, time

@dataclass
class DAP:
    issuer: str
    subject: str
    authority: str
    constraints: dict
    parent_id: str | None = None
    packet_id: str = field(default_factory=lambda: f"dpk_{uuid.uuid4().hex[:12]}")
    timestamp: int = field(default_factory=lambda: int(time.time()))
    revoked: bool = False
    expired: bool = False