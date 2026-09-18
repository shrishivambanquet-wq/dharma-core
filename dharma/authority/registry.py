from .node import AuthorityNode


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
