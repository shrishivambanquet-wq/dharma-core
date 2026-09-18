from dharma.authority.certificate import AuthorityCertificate
from dharma.authority.chain import CertificateChain


def test_empty_chain_valid():
    assert CertificateChain().is_valid()


def test_single_certificate_chain():
    chain = CertificateChain()
    chain.add(AuthorityCertificate("a", "b", "represents"))
    assert chain.is_valid()


def test_revoked_breaks_chain():
    c = AuthorityCertificate("a", "b", "represents")
    c.revoke()
    chain = CertificateChain([c])
    assert not chain.is_valid()


def test_chain_length():
    chain = CertificateChain()
    chain.add(AuthorityCertificate("a", "b", "represents"))
    chain.add(AuthorityCertificate("b", "c", "delegates"))
    assert chain.length() == 2


def test_multiple_valid_certificates():
    chain = CertificateChain([
        AuthorityCertificate("a", "b", "represents"),
        AuthorityCertificate("b", "c", "delegates"),
    ])
    assert chain.is_valid()

