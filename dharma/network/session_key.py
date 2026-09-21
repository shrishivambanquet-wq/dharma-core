"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import hashlib

class SessionKey:
    @staticmethod
    def derive(local_nonce, remote_nonce):
        data = "|".join(sorted([local_nonce, remote_nonce])).encode()
        return hashlib.sha256(data).hexdigest()
