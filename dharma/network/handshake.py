from dataclasses import dataclass
import secrets

@dataclass
class Handshake:
    local_nonce: str = ""
    remote_nonce: str | None = None

    def hello(self):
        self.local_nonce = secrets.token_hex(16)
        return {"type": "hello", "nonce": self.local_nonce}

    def accept(self, remote_nonce):
        if remote_nonce == self.local_nonce:
            raise ValueError("nonce reuse")
        self.remote_nonce = remote_nonce
        return {"type": "accept", "nonce": secrets.token_hex(16)}

    def established(self):
        return self.local_nonce != "" and self.remote_nonce is not None
