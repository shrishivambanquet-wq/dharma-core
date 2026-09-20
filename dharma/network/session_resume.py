from dataclasses import dataclass
import time


@dataclass
class SessionResume:
    session_id: str
    last_seen: float = None

    def __post_init__(self):
        if self.last_seen is None:
            self.last_seen = time.time()

    def resume(self):
        self.last_seen = time.time()
        return True

    def active(self):
        return self.last_seen > 0
