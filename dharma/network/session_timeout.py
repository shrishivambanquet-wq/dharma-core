"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass
import time

@dataclass
class SessionTimeout:
    session_id: str
    timeout: int = 30
    last_activity: float = None

    def __post_init__(self):
        if self.last_activity is None:
            self.last_activity = time.time()

    def active(self):
        return (time.time() - self.last_activity) < self.timeout

    def touch(self):
        self.last_activity = time.time()

    def reconnect(self):
        self.touch()
        return True
