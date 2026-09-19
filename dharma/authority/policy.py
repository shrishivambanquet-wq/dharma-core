from dataclasses import dataclass


@dataclass
class AuthorityPolicy:
    max_depth: int = 10
    allow_self_delegation: bool = False

    def allows_depth(self, depth: int):
        return depth <= self.max_depth

    def allows_self(self, issuer, subject):
        if self.allow_self_delegation:
            return True
        return issuer != subject
