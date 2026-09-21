"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.authority.ledger_entry import LedgerEntry


def test_hash_length():
    assert len(LedgerEntry("A").hash()) == 64


def test_same_payload_same_hash():
    assert LedgerEntry("A").hash() == LedgerEntry("A").hash()


def test_previous_hash_changes():
    a = LedgerEntry("A", "x").hash()
    b = LedgerEntry("A", "y").hash()
    assert a != b


def test_payload_changes():
    a = LedgerEntry("A").hash()
    b = LedgerEntry("B").hash()
    assert a != b


def test_genesis():
    assert LedgerEntry("Genesis").previous_hash == ""
