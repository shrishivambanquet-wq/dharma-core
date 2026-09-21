"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.network.test_vector import verify_vector

def test_vector_0001():
    assert verify_vector("compatibility-vectors/vector-0001.json")
