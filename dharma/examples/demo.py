"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.engine import DharmaEngine

engine=DharmaEngine()

# Financial authority
finance=engine.grant(
    issuer="Paresh Somani",
    subject="Agent-A",
    authority="purchase",
    constraints={
        "action":["purchase"],
        "amount":{"max":10000}
    }
)

print(engine.execute(
    finance.packet_id,
    {"action":"purchase","amount":2500}
))

# Hiring authority
hire=engine.grant(
    issuer="HR",
    subject="Recruiter",
    authority="hire",
    constraints={
        "action":["hire"],
        "role":["Intern"]
    }
)

# AI authority
ai=engine.grant(
    issuer="System",
    subject="Model-X",
    authority="api_access",
    constraints={
        "action":["api_call"],
        "api":["weather"]
    }
)