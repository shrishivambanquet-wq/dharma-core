"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass

from .token import SessionToken


@dataclass
class SessionAuth:
    token: SessionToken

    def authenticate(self, presented: str):
        return self.token.value == presented

    def short(self):
        return self.token.short()
