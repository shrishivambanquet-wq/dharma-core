"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.replay_guard import ReplayGuard, ReplayPacket


def test_new_packet():
    g = ReplayGuard()
    assert g.accept(ReplayPacket("A","B"))


def test_replay_rejected():
    g = ReplayGuard()
    p = ReplayPacket("A","B")
    assert g.accept(p)
    assert not g.accept(p)


def test_different_nonce():
    g = ReplayGuard()
    assert g.accept(ReplayPacket("A","B"))
    assert g.accept(ReplayPacket("A","B"))


def test_sender():
    assert ReplayPacket("A","B").sender == "A"


def test_receiver():
    assert ReplayPacket("A","B").receiver == "B"


def test_nonce_exists():
    assert ReplayPacket("A","B").nonce != ""


def test_count():
    g = ReplayGuard()
    g.accept(ReplayPacket("A","B"))
    g.accept(ReplayPacket("A","B"))
    assert g.count() == 2
