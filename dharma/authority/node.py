from dataclasses import dataclass, field
from uuid import uuid4
from datetime import datetime

from .enums import AuthorityKind, AuthorityStatus

@dataclass
class AuthorityNode:
    kind: AuthorityKind
    name: str
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    status: AuthorityStatus = AuthorityStatus.ACTIVE
    metadata: dict = field(default_factory=dict)
