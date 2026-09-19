from dataclasses import dataclass

from .dcp import DCPMessage


@dataclass
class DCPHandshake:
    node_id: str
    protocol_version: str = "0.1"

    def hello(self, receiver: str):
        return DCPMessage(
            sender=self.node_id,
            receiver=receiver,
            message_type="hello",
            payload={"version": self.protocol_version},
        )

    def accepts(self, message: DCPMessage):
        return (
            message.message_type == "hello"
            and message.payload.get("version") == self.protocol_version
        )
