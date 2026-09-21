"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass, field
import secrets


@dataclass
class ReplayPacket:
    sender: str
    receiver: str
    nonce: str = ""

    def __post_init__(self):
        if not self.nonce:
            self.nonce = secrets.token_hex(8)


@dataclass
class ReplayGuard:
    seen: set = field(default_factory=set)

    def accept(self, packet: ReplayPacket):
        if packet.nonce in self.seen:
            return False
        self.seen.add(packet.nonce)
        return True

    def count(self):
        return len(self.seen)
