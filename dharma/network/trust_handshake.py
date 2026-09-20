from dataclasses import dataclass

from .key_exchange import KeyExchange


@dataclass
class TrustHandshake:
    local: KeyExchange
    remote: KeyExchange

    def hello(self):
        return {
            "type": "hello",
            "public_key": self.local.public_key(),
        }

    def accept(self):
        return {
            "type": "accept",
            "public_key": self.remote.public_key(),
        }

    def established(self):
        return self.hello()["public_key"] != self.accept()["public_key"]
