"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.version import VERSION, PROTOCOL

def test_drfc_number():
    assert PROTOCOL["drfc"] == 60

def test_expected_tests():
    assert PROTOCOL["tests"] == 500

def test_release_semver():
    assert VERSION.startswith("0.2.")

def test_alpha_status():
    assert PROTOCOL["status"] == "alpha"

def test_protocol_manifest():
    assert set(PROTOCOL.keys()) == {
        "name", "drfc", "tests", "wire", "status"
    }
