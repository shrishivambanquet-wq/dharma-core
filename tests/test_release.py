"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.version import VERSION, PROTOCOL

def test_version():
    assert VERSION == "0.2.0-alpha"

def test_protocol_name():
    assert PROTOCOL["name"] == "Dharma Protocol"

def test_wire():
    assert PROTOCOL["wire"] == "v1"

def test_status():
    assert PROTOCOL["status"] == "alpha"
