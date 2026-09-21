"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import hashlib
import json
import time

def record(packet, request, result):

    payload = {
        "packet":packet.packet_id,
        "issuer":packet.issuer,
        "subject":packet.subject,
        "authority":packet.authority,
        "request":request,
        "result":result,
        "timestamp":int(time.time())
    }

    payload["hash"] = hashlib.sha256(
        json.dumps(payload,sort_keys=True).encode()
    ).hexdigest()

    return payload