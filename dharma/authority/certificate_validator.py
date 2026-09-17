from .certificate import AuthorityCertificate

class CertificateValidator:
    def is_valid(self, certificate: AuthorityCertificate) -> bool:
        return not certificate.revoked
