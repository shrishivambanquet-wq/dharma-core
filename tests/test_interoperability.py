from dharma.network.interoperability import DharmaNode
from dharma.network.replay_guard import ReplayGuard, ReplayPacket


def build():
    return DharmaNode("A"), DharmaNode("B")


def test_nodes_exist():
    a, b = build()
    assert a.node_id == "A"
    assert b.node_id == "B"


def test_hello():
    a, _ = build()
    assert "public_key" in a.hello()


def test_keys_differ():
    a, b = build()
    assert a.hello()["public_key"] != b.hello()["public_key"]


def test_establish():
    a, b = build()
    assert a.establish(b)


def test_session_exists():
    a, b = build()
    a.establish(b)
    assert a.session.active()


def test_replay():
    g = ReplayGuard()
    p = ReplayPacket("A","B")
    assert g.accept(p)
    assert not g.accept(p)


def test_node_name():
    a, _ = build()
    assert a.hello()["node"] == "A"


def test_connection_id():
    a, b = build()
    a.establish(b)
    assert "A-B" in a.session.session_id
