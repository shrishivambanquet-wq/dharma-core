"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.core.constitution import DharmaConstitution


def test_identity():
    assert DharmaConstitution().identity() == "Dharma/0.1-alpha"


def test_version():
    assert DharmaConstitution().version == "0.1-alpha"


def test_name():
    assert DharmaConstitution().protocol_name == "Dharma"


def test_governance():
    assert DharmaConstitution().governance == "DRFC"


def test_compatibility():
    assert DharmaConstitution().promises()["compatibility"] == "backward-compatible"
