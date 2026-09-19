import hashlib

class Fingerprint:
    @staticmethod
    def of(text: str):
        return hashlib.sha256(text.encode()).hexdigest()
