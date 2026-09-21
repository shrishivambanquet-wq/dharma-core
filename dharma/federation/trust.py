"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass


@dataclass
class TrustRequest:
    authority_id: str
    requester: str


@dataclass
class TrustResponse:
    authority_id: str
    trusted: bool
    responder: str
