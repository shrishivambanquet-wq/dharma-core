from copy import deepcopy

class AuthoritySnapshot:
    def __init__(self, registry):
        self._data = deepcopy(registry._authorities)

    def restore(self, registry):
        registry._authorities = deepcopy(self._data)

    def size(self):
        return len(self._data)

