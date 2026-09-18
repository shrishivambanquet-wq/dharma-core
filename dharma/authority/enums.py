from enum import Enum

class AuthorityKind(Enum):
    PERSON = "person"
    ORGANIZATION = "organization"
    INSTITUTION = "institution"
    AI_AGENT = "ai_agent"
    DOCUMENT = "document"

class AuthorityStatus(Enum):
    ACTIVE = "active"
    SUSPENDED = "suspended"
    REVOKED = "revoked"
