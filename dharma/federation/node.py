from dataclasses import dataclass


@dataclass
class FederationNode:
    node_id: str
    name: str
    endpoint: str

    def identity(self):
        return f"{self.node_id}:{self.name}"

    def is_remote(self):
        return self.endpoint.startswith("http")
