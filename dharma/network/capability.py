"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass, field

@dataclass
class CapabilityCard:
    node_id: str
    protocol: str
    features: list = field(default_factory=list)

    def advertise(self):
        return {
            "node": self.node_id,
            "protocol": self.protocol,
            "features": self.features,
        }

    def supports(self, feature):
        return feature in self.features
