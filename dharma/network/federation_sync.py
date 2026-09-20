from dataclasses import dataclass

from .auth_discovery import AuthDiscoveryRegistry


@dataclass
class FederationSync:
    registry: AuthDiscoveryRegistry

    def sync(self, remote: AuthDiscoveryRegistry):
        before = self.registry.count()

        for node, endpoint in remote.nodes.items():
            self.registry.nodes[node] = endpoint

        return self.registry.count() - before
