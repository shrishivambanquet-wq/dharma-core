"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass
import time
import secrets


@dataclass
class Heartbeat:
    heartbeat_id: str = ""
    timestamp: float = None

    def __post_init__(self):
        if not self.heartbeat_id:
            self.heartbeat_id = secrets.token_hex(8)
        if self.timestamp is None:
            self.timestamp = time.time()

    def ping(self):
        return {
            "type": "ping",
            "id": self.heartbeat_id,
            "timestamp": self.timestamp,
        }

    def pong(self):
        return {
            "type": "pong",
            "id": self.heartbeat_id,
            "timestamp": time.time(),
        }

    def alive(self, timeout=30):
        return (time.time() - self.timestamp) < timeout
