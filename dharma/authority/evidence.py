from dataclasses import dataclass, field
from .trust import TrustScore

@dataclass
class TrustEvidence:
    source: str
    description: str
    trust: TrustScore
    weight: float = 1.0

@dataclass
class EvidenceLedger:
    items: list = field(default_factory=list)

    def add(self, evidence: TrustEvidence):
        self.items.append(evidence)

    def confidence(self):
        if not self.items:
            return 0.0

        total_weight = sum(e.weight for e in self.items)
        if total_weight == 0:
            return 0.0

        return sum(e.trust.value * e.weight for e in self.items) / total_weight
