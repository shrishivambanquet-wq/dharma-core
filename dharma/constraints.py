from .errors import DharmaError
import time

def check(packet, request):

    c = packet.constraints

    # Action
    if "action" in c:
        if request.get("action") not in c["action"]:
            raise DharmaError("DAP-005","Action Not Allowed")

    # Money
    if "amount" in c:
        if request.get("amount",0) > c["amount"]["max"]:
            raise DharmaError("DAP-005","Amount Exceeded")

    # Location
    if "location" in c:
        if request.get("location") not in c["location"]["allowed"]:
            raise DharmaError("DAP-005","Location Restricted")

    # Time
    if "expires_at" in c:
        if time.time() > c["expires_at"]:
            raise DharmaError("DAP-007","Authority Expired")

    return True