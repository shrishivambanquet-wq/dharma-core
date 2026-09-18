from dharma.authority.signer import AuthoritySigner

def test_generate_keypair():
    s = AuthoritySigner.generate()
    assert s.public_key()

def test_sign_verify():
    s = AuthoritySigner.generate()
    msg = b"dharma"
    sig = s.sign(msg)
    assert s.verify(msg, sig)

def test_tampered_message_fails():
    s = AuthoritySigner.generate()
    sig = s.sign(b"hello")
    assert not s.verify(b"world", sig)
