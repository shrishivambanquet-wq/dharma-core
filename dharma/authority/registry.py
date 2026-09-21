"""
DRFC-0058
Canonical Module
"""

"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import json
from pathlib import Path

from .node import AuthorityNode
from .enums import AuthorityKind


class AuthorityRegistry:
    def __init__(self):
        self._authorities = {}

    def register(self, authority: AuthorityNode):
        self._authorities[authority.id] = authority
        return authority

    def get(self, authority_id):
        return self._authorities.get(authority_id)

    def exists(self, authority_id):
        return authority_id in self._authorities

    def by_name(self, name):
        return [a for a in self._authorities.values() if a.name == name]

    def count(self):
        return len(self._authorities)

    def save(self, path):
        path = Path(path)
        data = [
            {
                "id": a.id,
                "name": a.name,
                "kind": a.kind.name,
            }
            for a in self._authorities.values()
        ]
        path.write_text(json.dumps(data, indent=2))

    def load(self, path):
        path = Path(path)

        if not path.exists():
            self._authorities = {}
            return

        data = json.loads(path.read_text())
        self._authorities = {}

        for item in data:
            self.register(
                AuthorityNode(
                    AuthorityKind[item["kind"]],
                    item["name"],
                    id=item["id"],
                )
            )
