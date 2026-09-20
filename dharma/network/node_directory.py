from dataclasses import dataclass, field
import time

@dataclass
class NodeDirectory:
    nodes: dict = field(default_factory=dict)

    def remember(self, node_id, address):
        self.nodes[node_id] = {
            "address": address,
            "last_seen": time.time()
        }

    def lookup(self, node_id):
        return self.nodes.get(node_id)

    def known(self, node_id):
        return node_id in self.nodes

    def count(self):
        return len(self.nodes)

    def all(self):
        return self.nodes
