"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import json
from pathlib import Path
from .wire import WireMessage

def verify_vector(path):
    data = json.loads(Path(path).read_text())
    encoded = WireMessage(
        data["message_type"],
        data["payload"]
    ).encode().hex()
    return encoded == data["expected_hex"]
