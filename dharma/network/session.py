from dataclasses import dataclass
import time


@dataclass
class TrustSession:
    session_id: str
    requester: str
    responder: str
    created_at: float = None
    active: bool = True

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = time.time()

    def close(self):
        self.active = False

    def is_active(self):
        return self.active
