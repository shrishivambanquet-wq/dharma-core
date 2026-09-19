from dataclasses import dataclass

from .authority_index import AuthorityIndex
from .enums import AuthorityKind


@dataclass
class AuthoritySearch:
    index: AuthorityIndex

    def text(self, query: str):
        q = query.lower()
        return [
            node
            for node in self.index.by_id.values()
            if q in node.name.lower()
        ]

    def by_kind(self, kind: AuthorityKind):
        return [
            node
            for node in self.index.by_id.values()
            if node.kind == kind
        ]
