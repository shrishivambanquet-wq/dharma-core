class DharmaError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message
        super().__init__(f"{code}: {message}")

ERRORS = {
    "DAP-002":"Missing Issuer",
    "DAP-003":"Missing Subject",
    "DAP-004":"Invalid Lineage",
    "DAP-005":"Constraint Violation",
    "DAP-006":"Revoked Authority",
    "DAP-007":"Expired Authority",
}