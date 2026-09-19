from dharma.federation.node import FederationNode
from dharma.federation.registry import FederationRegistry
from dharma.federation.resolver import RemoteResolver
from dharma.federation.trust import TrustRequest


def build():
    r = FederationRegistry()
    r.register(FederationNode("uni", "University", "https://uni"))
    return r


def test_known_node():
    res = RemoteResolver(build()).resolve(TrustRequest("A", "uni"))
    assert res.trusted


def test_unknown_node():
    res = RemoteResolver(build()).resolve(TrustRequest("A", "x"))
    assert not res.trusted


def test_responder():
    res = RemoteResolver(build()).resolve(TrustRequest("A", "uni"))
    assert res.responder == "University"


def test_authority_preserved():
    res = RemoteResolver(build()).resolve(TrustRequest("XYZ", "uni"))
    assert res.authority_id == "XYZ"


def test_unknown_responder():
    res = RemoteResolver(build()).resolve(TrustRequest("A", "x"))
    assert res.responder == "unknown"
