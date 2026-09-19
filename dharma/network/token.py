from dataclasses import dataclass
import secrets


@dataclass
class SessionToken:
    value: str

    @staticmethod
    def create():
        return SessionToken(secrets.token_hex(16))

    def short(self):
        return self.value[:8]
