"""
Dharma Protocol - Reference Engine (DRE-PY v1.0)

Canonical Python implementation of:
- DEP-1.0
- DRFC-0002 to DRFC-0007
- DTS-001
"""

from .engine import DharmaEngine
from .packets import DAP
from .errors import DharmaError
from .registry import PACKET_MODES, TRUST_LEVELS

__version__ = "1.0.0"
__protocol__ = "DEP-1.0"

__all__ = [
    "DharmaEngine",
    "DAP",
    "DharmaError",
    "PACKET_MODES",
    "TRUST_LEVELS",
]