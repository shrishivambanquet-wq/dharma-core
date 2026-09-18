from .node import AuthorityNode


class AuthorityIndex:
    def __init__(self):
        self._authorities = {}

    def add(self, authority: AuthorityNode):
        self._authorities[authority.id] = authority
        return authority

    def get(self, authority_id):
        return self._authorities.get(authority_id)

    def by_kind(self, kind):
        return [a for a in self._authorities.values() if a.kind == kind]

    def by_name(self, name):
        return [a for a in self._authorities.values() if a.name == name]

    def count(self):
        return len(self._authorities)
