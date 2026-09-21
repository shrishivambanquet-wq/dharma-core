"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from enum import Enum

class TrustLevel(Enum):
    NONE = 0.0
    LOW = 0.25
    MEDIUM = 0.50
    HIGH = 0.75
    VERIFIED = 1.0
