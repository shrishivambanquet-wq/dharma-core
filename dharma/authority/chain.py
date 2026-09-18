from .certificate_validator import CertificateValidator


class CertificateChain:
    def __init__(self, certificates=None, validator=None):
        self.validator = validator or CertificateValidator()
        self.certificates = certificates or []

    def add(self, certificate):
        self.certificates.append(certificate)

    def is_valid(self):
        return all(self.validator.is_valid(c) for c in self.certificates)

    def length(self):
        return len(self.certificates)

    def first(self):
        return self.certificates[0] if self.certificates else None

    def last(self):
        return self.certificates[-1] if self.certificates else None
