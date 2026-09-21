"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from .trust_score import TrustScore


class TrustResolver:
    def resolve(self, scores):
        if not scores:
            return TrustScore(0.0)

        total = sum(s.value for s in scores)
        return TrustScore(total / len(scores))
