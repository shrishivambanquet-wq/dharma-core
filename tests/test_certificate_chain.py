from dharma.authority.certificate_chain import CertificateChain
from dharma.authority.signed_certificate import SignedCertificate


def test_add_certificate():
    c = CertificateChain()
    c.add(SignedCertificate("A", "B", "delegates"))
    assert c.count() == 1


def test_first():
    c = CertificateChain()
    s = SignedCertificate("A", "B", "delegates")
    c.add(s)
    assert c.first() == s


def test_last():
    c = CertificateChain()
    c.add(SignedCertificate("A", "B", "delegates"))
    s = SignedCertificate("B", "C", "delegates")
    c.add(s)
    assert c.last() == s


def test_chain_size():
    c = CertificateChain()
    c.add(SignedCertificate("A", "B", "delegates"))
    c.add(SignedCertificate("B", "C", "delegates"))
    assert c.count() == 2


def test_order_preserved():
    c = CertificateChain()
    a = SignedCertificate("A", "B", "delegates")
    b = SignedCertificate("B", "C", "delegates")
    c.add(a)
    c.add(b)
    assert c.first() == a and c.last() == b
