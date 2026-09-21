"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import socket
from .wire import WireMessage

class DharmaClient:
    def connect(self, host, port=4040):
        s = socket.socket()
        s.connect((host, port))

        s.send(
            WireMessage(
                1,
                {"message": "hello"}
            ).encode()
        )

        reply = WireMessage.decode(s.recv(4096))
        s.close()
        return reply.payload
