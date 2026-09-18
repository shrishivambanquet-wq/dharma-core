class TrustCache:
    def __init__(self):
        self._cache = {}

    def put(self, key, value):
        self._cache[key] = value

    def get(self, key):
        return self._cache.get(key)

    def has(self, key):
        return key in self._cache

    def size(self):
        return len(self._cache)

