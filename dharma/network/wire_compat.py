from dataclasses import dataclass

from .wire import WireMessage


@dataclass
class WireCompatibility:

    @staticmethod
    def canonical(msg_type, payload):
        return WireMessage(msg_type, payload).encode()

    @staticmethod
    def identical(a, b):
        return a == b
