from dataclasses import dataclass
import json


@dataclass
class DCPMessage:
    sender: str
    receiver: str
    message_type: str
    payload: dict

    def encode(self):
        return json.dumps({
            "sender": self.sender,
            "receiver": self.receiver,
            "message_type": self.message_type,
            "payload": self.payload,
        })

    @staticmethod
    def decode(data: str):
        obj = json.loads(data)
        return DCPMessage(
            obj["sender"],
            obj["receiver"],
            obj["message_type"],
            obj["payload"],
        )
