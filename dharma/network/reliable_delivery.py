from dataclasses import dataclass, field
import secrets

@dataclass
class ReliableDelivery:
    pending: dict = field(default_factory=dict)

    def send(self, payload):
        msg_id = secrets.token_hex(6)
        self.pending[msg_id] = payload
        return msg_id

    def ack(self, msg_id):
        if msg_id not in self.pending:
            return False
        del self.pending[msg_id]
        return True

    def waiting(self):
        return len(self.pending)
