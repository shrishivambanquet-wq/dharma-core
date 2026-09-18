from dharma.authority.certificate import AuthorityCertificate
from dharma.authority.certificate_validator import CertificateValidator

def test_valid_certificate():
    c = AuthorityCertificate("issuer", "subject", "represents")
    assert CertificateValidator().is_valid(c)

def test_revoked_certificate_invalid():
    c = AuthorityCertificate("issuer", "subject", "represents")
    c.revoke()
    assert not CertificateValidator().is_valid(c)

def test_new_certificate_not_revoked():
    c = AuthorityCertificate("issuer", "subject", "represents")
    assert c.revoked is False

def test_validator_returns_bool():
    c = AuthorityCertificate("issuer", "subject", "represents")
    assert isinstance(CertificateValidator().is_valid(c), bool)
