from enum import Enum

class AuthorityRelation(Enum):
    DELEGATES = "delegates"
    VERIFIES = "verifies"
    REVOKES = "revokes"
    DERIVES_FROM = "derives_from"
    AUTHORED = "authored"
    OWNS = "owns"
    GOVERNS = "governs"
