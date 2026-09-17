from dharma.authority.certificate import AuthorityCertificate
from dharma.authority.certificate_store import CertificateStore
from dharma.authority.certificate_validator import CertificateValidator
def test_store_starts_empty():
    s = CertificateStore()
    assert s.length() == 0

def test_store_adds_certificate():
    s = CertificateStore()
    s.add(AuthorityCertificate("a","b","represents"))
    assert s.length() == 1

def test_store_two_certificates():
    s = CertificateStore()
    s.add(AuthorityCertificate("a","b","represents"))
    s.add(AuthorityCertificate("x","y","represents"))
    assert s.length() == 2

def test_empty_store_is_valid():
    s = CertificateStore()
    assert s.is_valid() is True

def test_valid_store_is_valid():
    s = CertificateStore()
    s.add(AuthorityCertificate("a","b","represents"))
    assert s.is_valid() is True
