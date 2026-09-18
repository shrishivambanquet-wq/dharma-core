class RevocationList:
    def __init__(self):
        self._revoked = set()

    def revoke(self, certificate_id):
        self._revoked.add(certificate_id)

    def is_revoked(self, certificate_id):
        return certificate_id in self._revoked

    def count(self):
        return len(self._revoked)

    def clear(self):
        self._revoked.clear()
