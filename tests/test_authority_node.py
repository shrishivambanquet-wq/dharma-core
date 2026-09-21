"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from dharma.authority.node import AuthorityNode
from dharma.authority.enums import AuthorityKind, AuthorityStatus

def test_node_has_uuid():
    node = AuthorityNode(AuthorityKind.PERSON, "Paresh")
    assert len(node.id) > 0

def test_default_status_active():
    node = AuthorityNode(AuthorityKind.PERSON, "Paresh")
    assert node.status == AuthorityStatus.ACTIVE

def test_kind_is_preserved():
    node = AuthorityNode(AuthorityKind.ORGANIZATION, "Somani Caterers")
    assert node.kind == AuthorityKind.ORGANIZATION

def test_metadata_defaults_empty():
    node = AuthorityNode(AuthorityKind.PERSON, "Paresh")
    assert node.metadata == {}
