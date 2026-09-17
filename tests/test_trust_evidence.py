from dharma.authority.evidence import TrustEvidence, EvidenceLedger
from dharma.authority.trust import TrustScore

def test_evidence_holds_source():
    e = TrustEvidence("DRFC-0012", "Verified by protocol", TrustScore(1.0))
    assert e.source == "DRFC-0012"

def test_evidence_holds_description():
    e = TrustEvidence("Audit", "External audit passed", TrustScore(0.9))
    assert e.description == "External audit passed"

def test_evidence_holds_trust():
    e = TrustEvidence("Audit", "External audit passed", TrustScore(0.9))
    assert e.trust.value == 0.9

def test_empty_ledger():
    assert EvidenceLedger().confidence() == 0.0

def test_single_evidence():
    ledger = EvidenceLedger()
    ledger.add(TrustEvidence("A", "Verified", TrustScore(1.0)))
    assert ledger.confidence() == 1.0

def test_average_confidence():
    ledger = EvidenceLedger()
    ledger.add(TrustEvidence("A", "Verified", TrustScore(1.0)))
    ledger.add(TrustEvidence("B", "Audit", TrustScore(0.5)))
    assert ledger.confidence() == 0.75

def test_add_increases_items():
    ledger = EvidenceLedger()
    ledger.add(TrustEvidence("A", "Verified", TrustScore(1.0)))
    assert len(ledger.items) == 1

def test_weighted_confidence():
    ledger = EvidenceLedger()
    ledger.add(TrustEvidence("A", "Protocol", TrustScore(1.0), weight=2))
    ledger.add(TrustEvidence("B", "Audit", TrustScore(0.5), weight=1))
    assert ledger.confidence() == (2.5 / 3)

def test_zero_weight_returns_zero():
    ledger = EvidenceLedger()
    ledger.add(TrustEvidence("A", "Ignored", TrustScore(1.0), weight=0))
    assert ledger.confidence() == 0.0

def test_default_weight_is_one():
    evidence = TrustEvidence("A", "Default", TrustScore(0.8))
    assert evidence.weight == 1.0

def test_heavier_evidence_has_more_influence():
    ledger = EvidenceLedger()
    ledger.add(TrustEvidence("A", "Strong", TrustScore(1.0), weight=5))
    ledger.add(TrustEvidence("B", "Weak", TrustScore(0.0), weight=1))
    assert ledger.confidence() == (5 / 6)
