from dataclasses import dataclass
import time


@dataclass
class Packet:
    sender: str
    receiver: str
    payload: dict
    timestamp: float = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = time.time()

    def route(self):
        return f"{self.sender}->{self.receiver}"

    def is_for(self, node):
        return self.receiver == node
