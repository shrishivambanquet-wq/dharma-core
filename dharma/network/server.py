"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import socket
from .wire import WireMessage

class DharmaServer:
    def __init__(self, host="0.0.0.0", port=4040):
        self.host = host
        self.port = port

    def serve_once(self):
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((self.host, self.port))
        s.listen(1)

        conn, _ = s.accept()
        data = conn.recv(4096)

        msg = WireMessage.decode(data)

        conn.send(
            WireMessage(
                2,
                {"reply": "hello_from_dharma"}
            ).encode()
        )

        conn.close()
        s.close()

        return msg.payload
