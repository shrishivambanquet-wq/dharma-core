from dharma.network.revocation_registry import RevocationRegistry

def test_revoke():
    r=RevocationRegistry()
    assert r.revoke("A")["reason"]=="unspecified"

def test_custom_reason():
    r=RevocationRegistry()
    assert r.revoke("A","expired")["reason"]=="expired"

def test_is_revoked():
    r=RevocationRegistry(); r.revoke("A")
    assert r.is_revoked("A")

def test_missing():
    assert not RevocationRegistry().is_revoked("X")

def test_info():
    r=RevocationRegistry(); r.revoke("A","expired")
    assert r.info("A")["reason"]=="expired"

def test_count():
    r=RevocationRegistry(); r.revoke("A"); r.revoke("B")
    assert r.count()==2

def test_timestamp():
    assert RevocationRegistry().revoke("A")["timestamp"]>0

def test_overwrite():
    r=RevocationRegistry()
    r.revoke("A","one")
    r.revoke("A","two")
    assert r.info("A")["reason"]=="two"

def test_all():
    r=RevocationRegistry(); r.revoke("A")
    assert "A" in r.all()

def test_empty():
    assert RevocationRegistry().count()==0

def test_many():
    r=RevocationRegistry()
    [r.revoke(str(i)) for i in range(5)]
    assert r.count()==5

def test_keys():
    info=RevocationRegistry().revoke("A")
    assert set(info.keys())=={"timestamp","reason"}
