"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dataclasses import dataclass

from .dcp import DCPMessage


@dataclass
class DiscoveryHandshake:
    node_id: str
    version: str = "0.1"

    def discover(self, receiver):
        return DCPMessage(
            sender=self.node_id,
            receiver=receiver,
            message_type="discover",
            payload={"version": self.version},
        )

    def accepts(self, message):
        return (
            message.message_type == "discover"
            and message.payload.get("version") == self.version
        )
