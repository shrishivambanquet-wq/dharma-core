"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass

from .policy import AuthorityPolicy


@dataclass
class PolicyEngine:
    policy: AuthorityPolicy

    def evaluate(self, issuer, subject, depth):
        return (
            self.policy.allows_self(issuer, subject)
            and self.policy.allows_depth(depth)
        )

    def reason(self, issuer, subject, depth):
        if not self.policy.allows_self(issuer, subject):
            return "self_delegation_denied"

        if not self.policy.allows_depth(depth):
            return "depth_limit_exceeded"

        return "allowed"
