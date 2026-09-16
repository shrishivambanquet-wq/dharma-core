from .errors import DharmaError

def verify(packet, ledger):
    current = packet

    while current.parent_id is not None:

        if current.parent_id not in ledger:
            raise DharmaError("DAP-004","Invalid Lineage")

        parent = ledger[current.parent_id]

        if parent.revoked:
            raise DharmaError("DAP-006","Revoked Authority")

        if parent.expired:
            raise DharmaError("DAP-007","Expired Authority")

        current = parent

    return True