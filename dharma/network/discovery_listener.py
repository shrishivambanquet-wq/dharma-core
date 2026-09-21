"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import socket

PORT = 45671

class DiscoveryListener:
    def receive_once(self, timeout=1):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("", PORT))
        s.settimeout(timeout)
        try:
            data, addr = s.recvfrom(1024)
            return data.decode(), addr[0]
        except socket.timeout:
            return None
        finally:
            s.close()
