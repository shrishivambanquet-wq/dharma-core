"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.engine import DharmaEngine
import pytest

def test_grant_delegate_execute():

    engine=DharmaEngine()

    root=engine.grant(
        issuer="Paresh Somani",
        subject="Agent-A",
        authority="purchase",
        constraints={
            "action":["purchase"],
            "amount":{"max":10000}
        }
    )

    child=engine.delegate(
        root.packet_id,
        "Agent-B",
        {"amount":{"max":3000}}
    )

    result=engine.execute(
        child.packet_id,
        {"action":"purchase","amount":2500}
    )

    assert result["result"]=="PASS"

def test_constraint_violation():

    engine=DharmaEngine()

    root=engine.grant(
        "P",
        "A",
        "purchase",
        {"action":["purchase"],"amount":{"max":1000}}
    )

    with pytest.raises(Exception):
        engine.execute(
            root.packet_id,
            {"action":"purchase","amount":2000}
        )