from dataclasses import dataclass
import json
import struct

VERSION = 1

@dataclass
class WireMessage:
    msg_type: int
    payload: dict

    def encode(self):
        body = json.dumps(self.payload, sort_keys=True).encode()
        header = struct.pack("!BBH", VERSION, self.msg_type, len(body))
        return header + body

    @staticmethod
    def decode(data: bytes):
        if len(data) < 4:
            raise ValueError("truncated header")

        version, msg_type, length = struct.unpack("!BBH", data[:4])

        if version != VERSION:
            raise ValueError("unsupported version")

        if len(data) != 4 + length:
            raise ValueError("length mismatch")

        body = json.loads(data[4:].decode())
        return WireMessage(msg_type, body)
