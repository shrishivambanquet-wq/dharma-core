from dharma.authority.chain_verifier import ChainVerifier
from dharma.authority.certificate_chain import CertificateChain
from dharma.authority.signed_certificate import SignedCertificate
from dharma.authority.signer import AuthoritySigner


def build_chain():
    c = CertificateChain()
    c.add(SignedCertificate("A", "B", "delegates"))
    c.add(SignedCertificate("B", "C", "delegates"))
    return c


def test_valid_chain():
    s = AuthoritySigner.generate()
    chain = build_chain()
    sigs = [c.sign(s) for c in chain.certificates]
    assert ChainVerifier(s).verify(chain, sigs)


def test_tampered_chain_fails():
    s = AuthoritySigner.generate()
    chain = build_chain()
    sigs = [c.sign(s) for c in chain.certificates]
    chain.certificates[1].subject = "X"
    assert not ChainVerifier(s).verify(chain, sigs)


def test_missing_signature_fails():
    s = AuthoritySigner.generate()
    chain = build_chain()
    sigs = [chain.certificates[0].sign(s)]
    assert not ChainVerifier(s).verify(chain, sigs)


def test_empty_chain():
    s = AuthoritySigner.generate()
    assert ChainVerifier(s).verify(CertificateChain(), [])


def test_order_matters():
    s = AuthoritySigner.generate()
    chain = build_chain()
    sigs = [c.sign(s) for c in reversed(chain.certificates)]
    assert not ChainVerifier(s).verify(chain, sigs)
