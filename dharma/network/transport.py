from dataclasses import dataclass
import socket


@dataclass
class Transport:
    host: str = "127.0.0.1"
    port: int = 4040

    def server(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(1)
        return s

    def client(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
        return s

    def endpoint(self):
        return f"{self.host}:{self.port}"
