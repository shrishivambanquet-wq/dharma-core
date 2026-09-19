from dataclasses import dataclass

from .dcp import DCPMessage


@dataclass
class TrustNegotiation:
    node_id: str
    version: str = "0.1"

    def propose(self, receiver):
        return DCPMessage(
            sender=self.node_id,
            receiver=receiver,
            message_type="trust_proposal",
            payload={"version": self.version},
        )

    def accepts(self, message):
        return (
            message.message_type == "trust_proposal"
            and message.payload.get("version") == self.version
        )
