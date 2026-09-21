from dataclasses import dataclass

STATES = [
    "DISCOVERED",
    "NEGOTIATING",
    "CONNECTED",
    "ACTIVE",
    "DISCONNECTED",
]

@dataclass
class SessionLifecycle:
    state: str = "DISCOVERED"

    def transition(self, next_state):
        if next_state not in STATES:
            raise ValueError("invalid state")
        self.state = next_state
        return self.state

    def current(self):
        return self.state
