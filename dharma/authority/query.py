"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass

from .authority_index import AuthorityIndex
from .enums import AuthorityKind


@dataclass
class AuthorityQuery:
    index: AuthorityIndex

    def by_id(self, node_id):
        return self.index.get(node_id)

    def by_name(self, name):
        return self.index.find(name)

    def by_kind(self, kind: AuthorityKind):
        return [
            node
            for node in self.index.by_id.values()
            if node.kind == kind
        ]
