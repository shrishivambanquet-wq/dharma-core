"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.core.manifest import DharmaManifest


def test_protocol():
    assert DharmaManifest().protocol == "Dharma"


def test_release():
    assert DharmaManifest().release == "v0.1-alpha"


def test_drfc():
    assert DharmaManifest().drfc == 30


def test_stable_api():
    assert DharmaManifest().stable_api


def test_summary():
    assert DharmaManifest().summary()["release"] == "v0.1-alpha"
