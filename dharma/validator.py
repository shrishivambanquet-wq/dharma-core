"""
DRFC-0084
Canonical Module
"""

"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from .errors import DharmaError

def validate(packet):
    if not packet.issuer:
        raise DharmaError("DAP-002","Missing Issuer")

    if not packet.subject:
        raise DharmaError("DAP-003","Missing Subject")

    if not packet.authority:
        raise DharmaError("DAP-004","Missing Authority")

    return True