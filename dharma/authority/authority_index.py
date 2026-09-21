"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass, field

from .node import AuthorityNode


@dataclass
class AuthorityIndex:
    by_id: dict = field(default_factory=dict)
    by_name: dict = field(default_factory=dict)

    def add(self, node: AuthorityNode):
        self.by_id[node.id] = node
        self.by_name[node.name.lower()] = node

    def get(self, node_id):
        return self.by_id.get(node_id)

    def find(self, name):
        return self.by_name.get(name.lower())

    def count(self):
        return len(self.by_id)
