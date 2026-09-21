"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import time
from dharma.network.node_directory import NodeDirectory

def test_save():
    d = NodeDirectory()
    d.remember("A","192.168.1.10")
    assert d.lookup("A")["address"] == "192.168.1.10"

def test_known():
    d = NodeDirectory()
    d.remember("A","1")
    assert d.known("A")

def test_unknown():
    assert NodeDirectory().lookup("X") is None

def test_overwrite():
    d = NodeDirectory()
    d.remember("A","1")
    first = d.lookup("A")["last_seen"]
    time.sleep(0.01)
    d.remember("A","2")
    assert d.lookup("A")["address"] == "2"
    assert d.lookup("A")["last_seen"] > first

def test_count():
    d = NodeDirectory()
    d.remember("A","1")
    d.remember("B","2")
    assert d.count() == 2

def test_all():
    d = NodeDirectory()
    d.remember("A","1")
    assert "A" in d.all()

def test_last_seen():
    d = NodeDirectory()
    d.remember("A","1")
    assert d.lookup("A")["last_seen"] > 0

def test_multiple():
    d = NodeDirectory()
    for i in range(5):
        d.remember(str(i), f"10.0.0.{i}")
    assert d.count() == 5
