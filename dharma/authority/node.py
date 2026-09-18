from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4

from .enums import AuthorityKind, AuthorityStatus


@dataclass(eq=True)
class AuthorityNode:
    kind: AuthorityKind
    name: str
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    status: AuthorityStatus = AuthorityStatus.ACTIVE
    metadata: dict = field(default_factory=dict)

    def __hash__(self):
        return hash(self.id)
