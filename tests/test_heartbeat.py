import time
from dharma.network.heartbeat import Heartbeat


def test_ping():
    assert Heartbeat().ping()["type"] == "ping"


def test_pong():
    assert Heartbeat().pong()["type"] == "pong"


def test_same_id():
    h = Heartbeat()
    assert h.ping()["id"] == h.pong()["id"]


def test_timestamp():
    assert Heartbeat().timestamp > 0


def test_alive():
    assert Heartbeat().alive()


def test_dead():
    h = Heartbeat()
    h.timestamp -= 100
    assert not h.alive(timeout=30)


def test_multiple():
    h = Heartbeat()
    for _ in range(5):
        h.ping()
        h.pong()
    assert h.alive()


def test_id_exists():
    assert Heartbeat().heartbeat_id != ""
