from dataclasses import dataclass, field

@dataclass
class PeerCache:
    peers: dict = field(default_factory=dict)

    def remember(self, peer_id, address):
        self.peers[peer_id] = address

    def lookup(self, peer_id):
        return self.peers.get(peer_id)

    def known(self, peer_id):
        return peer_id in self.peers

    def count(self):
        return len(self.peers)
