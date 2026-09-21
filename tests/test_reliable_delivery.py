"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.reliable_delivery import ReliableDelivery

def test_send():
    assert ReliableDelivery().send({"x":1})

def test_ack():
    r = ReliableDelivery()
    i = r.send({})
    assert r.ack(i)

def test_unknown():
    assert not ReliableDelivery().ack("bad")

def test_pending():
    r = ReliableDelivery()
    r.send({})
    assert r.waiting() == 1

def test_ack_removes():
    r = ReliableDelivery()
    i = r.send({})
    r.ack(i)
    assert r.waiting() == 0

def test_duplicate():
    r = ReliableDelivery()
    i = r.send({})
    assert r.ack(i)
    assert not r.ack(i)

def test_multiple():
    r = ReliableDelivery()
    r.send({})
    r.send({})
    assert r.waiting() == 2

def test_unique():
    r = ReliableDelivery()
    assert r.send({}) != r.send({})
