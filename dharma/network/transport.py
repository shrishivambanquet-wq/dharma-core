"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import socket

class Transport:
    def __init__(self, host="127.0.0.1", port=4040):
        self.host = host
        self.port = port

    def endpoint(self):
        return f"{self.host}:{self.port}"

    def server(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((self.host, self.port))
        s.listen(1)
        return s

    def client(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
        return s
