"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.duplicate_guard import DuplicateGuard

def test_first_packet():
    g = DuplicateGuard()
    assert g.accept("p1")

def test_duplicate():
    g = DuplicateGuard()
    g.accept("p1")
    assert not g.accept("p1")

def test_multiple():
    g = DuplicateGuard()
    for i in range(5):
        assert g.accept(f"p{i}")

def test_count():
    g = DuplicateGuard()
    g.accept("a")
    g.accept("b")
    assert g.count() == 2

def test_duplicate_count():
    g = DuplicateGuard()
    g.accept("x")
    g.accept("x")
    assert g.count() == 1

def test_new_packet():
    g = DuplicateGuard()
    assert g.accept("new")

def test_many_duplicates():
    g = DuplicateGuard()
    g.accept("z")
    for _ in range(10):
        assert not g.accept("z")

def test_unique_ids():
    g = DuplicateGuard()
    assert g.accept("1")
    assert g.accept("2")
