from dataclasses import dataclass, field
from uuid import uuid4

from .node import AuthorityNode

@dataclass
class AuthorityEdge:
    source: AuthorityNode
    target: AuthorityNode
    relation: str
    id: str = field(default_factory=lambda: str(uuid4()))
