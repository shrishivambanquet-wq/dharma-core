"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from .certificate_validator import CertificateValidator

class CertificateStore:
    def __init__(self, validator=None):
        self.validator = validator or CertificateValidator()
        self.certificates = []

    def add(self, certificate):
        self.certificates.append(certificate)

    def is_valid(self):
        return all(self.validator.is_valid(c) for c in self.certificates)

    def length(self):
        return len(self.certificates)
