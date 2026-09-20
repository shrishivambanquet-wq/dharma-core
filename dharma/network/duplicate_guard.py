from dataclasses import dataclass, field

@dataclass
class DuplicateGuard:
    seen: set = field(default_factory=set)

    def accept(self, packet_id):
        if packet_id in self.seen:
            return False
        self.seen.add(packet_id)
        return True

    def count(self):
        return len(self.seen)
