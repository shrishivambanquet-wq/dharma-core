
# DP-0001 — dharma-core Repository Blueprint

**Document ID:** DP-0001
**Founder:** Paresh Somani
**Version:** 1.0
**Status:** Founding Freeze

> Defines the official repository structure for the first executable implementation of the Dharma Protocol.

---

# 1. Purpose

The `dharma-core` repository is the canonical reference implementation.

It proves that DEP-1.0 can execute as software while remaining compatible with every Dharma specification.

---

# 2. Repository Layout

dharma-core/

├── README.md

├── LICENSE

├── docs/

│   ├── DEP-1.0.md

│   ├── DRFC/

│   ├── DTS/

│   └── DPC/

├── dharma/

│   ├── engine.py

│   ├── parser.py

│   ├── validator.py

│   ├── lvp.py

│   ├── constraints.py

│   ├── evidence.py

│   ├── ledger.py

│   ├── packets.py

│   ├── errors.py

│   └── registry.py

├── corpus/

│   ├── valid/

│   ├── invalid/

│   ├── lineage/

│   ├── revocation/

│   └── compression/

├── tests/

│   ├── test_dts001.py

│   ├── test_lvp.py

│   ├── test_constraints.py

│   └── test_desp.py

├── sdk/

│   ├── python/

│   └── future/

└── examples/

    ├── grant.py

    ├── delegate.py

    └── execute.py

---

# 3. Core Modules

## engine.py

Runs the complete execution pipeline.

Responsibilities:

- receive packets,
- coordinate validation,
- execute decisions,
- generate responses.

---

## parser.py

Reads serialized DAP packets.

Output:

Structured packet object.

---

## validator.py

Performs structural validation.

Checks:

- version,
- packet mode,
- required fields,
- integrity.

---

## lvp.py

Implements DRFC-0002.

Responsibilities:

- locate root,
- walk lineage,
- detect cycles,
- verify chronology.

---

## constraints.py

Evaluates inherited limits.

Examples:

- money,
- time,
- geography,
- risk.

---

## evidence.py

Creates immutable execution records.

Output includes:

- packet ID,
- timestamp,
- result.

---

## ledger.py

Maintains historical evidence.

Supports:

- lookup,
- checkpoints,
- archived history.

---

## packets.py

Defines the internal DAP object.

Every packet contains:

- header,
- authority,
- constraints,
- parent,
- checkpoint.

---

## errors.py

Maps official Dharma error codes.

Examples:

DAP-005

Constraint Violation.

---

## registry.py

Implements DPR-0001.

Provides:

- packet modes,
- trust levels,
- reserved identifiers.

---

# 4. Corpus Folder

The repository ships with the official packet corpus.

Examples:

corpus/valid/DPC-0001.json

corpus/invalid/DPC-0020.json

These files become permanent test fixtures.

---

# 5. Test Architecture

Every DTS-001 test runs automatically.

Pipeline:

Load Packet

↓

Parse

↓

Validate

↓

LVP

↓

Constraints

↓

Execute

↓

Compare Expected Result

Any mismatch immediately fails certification.

---

# 6. Public SDK

The first SDK profile is Python.

Public API

grant()

delegate()

execute()

verify()

revoke()

evidence()

lookup()

Future languages implement identical behavior.

---

# 7. Example Programs

Example

grant.py

Creates a new authority packet.

delegate.py

Transfers authority.

execute.py

Attempts execution.

These examples double as developer documentation.

---

# 8. Logging

Every execution records:

- Packet ID,
- Mode,
- Decision,
- Error Code,
- Timestamp.

Logs never modify evidence.

---

# 9. Conformance Workflow

Developer runs:

Run Tests

↓

Load DPC Corpus

↓

Execute DTS-001

↓

Generate Report

Example output

Mandatory: PASS

Security: PASS

Stress: PASS

Certification: SUCCESS

---

# 10. Future Profiles

The repository reserves space for:

- Rust
- Go
- C
- Java
- JavaScript

Behavior remains identical.

---

# 11. Founder's Declaration

I, Paresh Somani, establish `dharma-core` as the canonical repository blueprint for the executable Dharma Reference Engine.

Its purpose is to transform the Dharma Protocol from written specifications into deterministic software while preserving Principle 0.

---

# Change Log

| Version | Change |
|----------|--------|
| 1.0 | Initial Repository Blueprint |
