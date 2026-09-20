from dataclasses import dataclass

@dataclass
class PacketTTL:
    ttl: int = 8

    def hop(self):
        if self.ttl > 0:
            self.ttl -= 1
        return self.ttl

    def expired(self):
        return self.ttl == 0
