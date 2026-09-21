"""
DRFC-0032
Canonical Module
"""

"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import socket

PORT = 45671

class Discovery:
    def announce(self, name):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.sendto(name.encode(), ("255.255.255.255", PORT))
        s.close()
        return True
