"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

from pathlib import Path

from dharma.authority.registry import AuthorityRegistry
from dharma.authority.node import AuthorityNode
from dharma.authority.enums import AuthorityKind


def test_save_creates_file(tmp_path: Path):
    r = AuthorityRegistry()
    r.register(AuthorityNode(AuthorityKind.PERSON, "Alice", id="1"))
    p = tmp_path / "registry.json"
    r.save(p)
    assert p.exists()


def test_load_restores_count(tmp_path: Path):
    r = AuthorityRegistry()
    r.register(AuthorityNode(AuthorityKind.PERSON, "Alice", id="1"))
    p = tmp_path / "registry.json"
    r.save(p)

    r2 = AuthorityRegistry()
    r2.load(p)
    assert r2.count() == 1


def test_load_restores_name(tmp_path: Path):
    r = AuthorityRegistry()
    r.register(AuthorityNode(AuthorityKind.PERSON, "Alice", id="1"))
    p = tmp_path / "registry.json"
    r.save(p)

    r2 = AuthorityRegistry()
    r2.load(p)
    assert r2.get("1").name == "Alice"


def test_empty_registry_roundtrip(tmp_path: Path):
    r = AuthorityRegistry()
    p = tmp_path / "registry.json"
    r.save(p)

    r2 = AuthorityRegistry()
    r2.load(p)
    assert r2.count() == 0


def test_missing_file_loads_empty(tmp_path: Path):
    r = AuthorityRegistry()
    r.load(tmp_path / "missing.json")
    assert r.count() == 0

