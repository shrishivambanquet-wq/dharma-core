from dharma.federation.node import FederationNode


def test_identity():
    n = FederationNode("1", "Alpha", "https://alpha.org")
    assert n.identity() == "1:Alpha"


def test_remote_true():
    assert FederationNode("1", "A", "https://x").is_remote()


def test_http_true():
    assert FederationNode("1", "A", "http://x").is_remote()


def test_local_false():
    assert not FederationNode("1", "A", "local").is_remote()


def test_name():
    assert FederationNode("1", "Alpha", "x").name == "Alpha"
