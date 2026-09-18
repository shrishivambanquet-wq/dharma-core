from dharma.authority.certificate import AuthorityCertificate

def test_certificate_has_uuid():
    c = AuthorityCertificate("issuer", "subject", "represents")
    assert len(c.certificate_id) > 0

def test_certificate_has_timestamp():
    c = AuthorityCertificate("issuer", "subject", "represents")
    assert "T" in c.issued_at

def test_certificate_default_active():
    c = AuthorityCertificate("issuer", "subject", "represents")
    assert c.revoked is False

def test_certificate_revokes():
    c = AuthorityCertificate("issuer", "subject", "represents")
    c.revoke()
    assert c.revoked is True

def test_certificate_keeps_purpose():
    c = AuthorityCertificate("issuer", "subject", "represents")
    assert c.purpose == "represents"
