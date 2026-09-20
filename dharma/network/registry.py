from dataclasses import dataclass

MESSAGE_TYPES = {
    "HELLO": 0x01,
    "ACCEPT": 0x02,
    "ROUTE_ANNOUNCEMENT": 0x03,
    "TRUST_PROPOSAL": 0x04,
    "SESSION_RESUME": 0x05,
    "DCP_MESSAGE": 0x06,
}

@dataclass
class ProtocolRegistry:

    def code(self, name):
        return MESSAGE_TYPES.get(name)

    def name(self, code):
        for k, v in MESSAGE_TYPES.items():
            if v == code:
                return k
        return None
