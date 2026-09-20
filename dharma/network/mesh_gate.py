from dharma.network.packet_ttl import PacketTTL
from dharma.network.duplicate_guard import DuplicateGuard

class MeshGate:
    def __init__(self):
        self.guard = DuplicateGuard()

    def forward(self, packet_id, ttl):
        if not self.guard.accept(packet_id):
            return "duplicate"

        p = PacketTTL(ttl)
        p.hop()

        if p.expired():
            return "expired"

        return "forward"
