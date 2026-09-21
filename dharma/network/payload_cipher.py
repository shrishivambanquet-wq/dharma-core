"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import hashlib

class PayloadCipher:
    @staticmethod
    def _keystream(key, length):
        stream = b""
        counter = 0
        while len(stream) < length:
            stream += hashlib.sha256(f"{key}:{counter}".encode()).digest()
            counter += 1
        return stream[:length]

    @staticmethod
    def encrypt(key, plaintext):
        data = plaintext.encode()
        ks = PayloadCipher._keystream(key, len(data))
        return bytes(a ^ b for a, b in zip(data, ks)).hex()

    @staticmethod
    def decrypt(key, ciphertext_hex):
        data = bytes.fromhex(ciphertext_hex)
        ks = PayloadCipher._keystream(key, len(data))
        return bytes(a ^ b for a, b in zip(data, ks)).decode()
