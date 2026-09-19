from dataclasses import dataclass

from .registry import FederationRegistry
from .trust import TrustRequest, TrustResponse


@dataclass
class RemoteResolver:
    registry: FederationRegistry

    def resolve(self, request: TrustRequest):
        node = self.registry.get(request.requester)

        if node is None:
            return TrustResponse(
                request.authority_id,
                False,
                "unknown",
            )

        return TrustResponse(
            request.authority_id,
            True,
            node.name,
        )
