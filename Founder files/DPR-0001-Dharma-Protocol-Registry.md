
# DPR-0001 — Dharma Protocol Registry

**Document ID:** DPR-0001
**Founder:** Paresh Somani
**Version:** 1.0
**Status:** Founding Freeze

> Defines the official registry for document identifiers, packet modes, error codes, trust levels, namespaces, and future extensions within the Dharma ecosystem.

---

# Abstract

The Dharma ecosystem consists of multiple specifications.

Without a common registry, future extensions could reuse identifiers and create incompatible implementations.

DPR-0001 reserves the official namespaces used by every future Dharma document.

---

# 1. Purpose

The Protocol Registry guarantees:

- unique identifiers,
- stable naming,
- collision prevention,
- predictable versioning.

Every future Dharma specification MUST register new permanent identifiers here.

---

# 2. Registry Structure

The registry contains seven permanent namespaces.

| Namespace | Purpose |
|-----------|---------|
| DRFC | Technical RFCs |
| DEP | Engineered Protocols |
| DTS | Test Suites |
| DPR | Registries |
| DL | Founder Ledger |
| DIP | Integration Profiles |
| DRE | Reference Engine |

These prefixes are permanently reserved.

---

# 3. Document Registry

## DRFC Series

| ID | Title |
|----|-------|
| DRFC-0001 | Dharma Authority Packet |
| DRFC-0002 | Lineage Verification Protocol |
| DRFC-0003 | Evidence & Lineage Compression |
| DRFC-0004 | Distributed Evidence Synchronization |
| DRFC-0005 | Trust Domain Enrollment |

Reserved:

DRFC-0006 onward.

---

## DEP Series

| ID | Title |
|----|-------|
| DEP-1.0 | Dharma Engineered Protocol |

Reserved:

DEP-2.0 onward.

---

## DTS Series

| ID | Title |
|----|-------|
| DTS-001 | Conformance Test Suite |

Reserved:

DTS-002 onward.

---

## DPR Series

| ID | Title |
|----|-------|
| DPR-0001 | Dharma Protocol Registry |

Reserved:

DPR-0002 onward.

---

## DIP Series

Reserved for integrations.

Examples:

- WhatsApp
- Email
- MCP
- HTTP
- Banking
- Enterprise

---

## DRE Series

Reserved for executable reference engines.

---

# 4. Packet Mode Registry

The following packet modes are permanently assigned.

| Code | Name |
|------|------|
| 01 | GRANT |
| 02 | DELEGATE |
| 03 | EXECUTE |
| 04 | REVOKE |
| 05 | EVIDENCE |

Values 06–255 remain reserved.

---

# 5. Layer Registry

DAP contains six permanent layers.

| Layer | Name |
|--------|------|
| L0 | Header |
| L1 | Authority Core |
| L2 | Constraints |
| L3 | Lineage |
| L4 | Evidence |
| L5 | Extensions |

No future specification may rename Layers L0–L5.

---

# 6. Trust Level Registry

| Level | Capability |
|--------|------------|
| T0 | Identity |
| T1 | Receive |
| T2 | Delegate |
| T3 | Issue |
| T4 | Verify |
| T5 | Ledger |

Higher levels inherit lower capabilities.

---

# 7. Error Code Registry

## DAP Errors

| Code | Meaning |
|------|---------|
| DAP-001 | Invalid Header |
| DAP-002 | Missing Issuer |
| DAP-003 | Missing Subject |
| DAP-004 | Invalid Lineage |
| DAP-005 | Constraint Violation |
| DAP-006 | Revoked Authority |
| DAP-007 | Expired Authority |
| DAP-008 | Invalid Packet Mode |
| DAP-009 | Missing Evidence |

---

## LVP Errors

| Code | Meaning |
|------|---------|
| LVP-001 | Missing Root |
| LVP-002 | Broken Parent |
| LVP-003 | Discontinuous Chain |
| LVP-004 | Circular Lineage |
| LVP-005 | Chronology Error |
| LVP-006 | Revoked Ancestor |
| LVP-007 | Expired Ancestor |

---

## ELCP Errors

| Code | Meaning |
|------|---------|
| ELCP-001 | Missing Checkpoint |
| ELCP-002 | Corrupted Ledger |
| ELCP-003 | Duplicate Packet |
| ELCP-004 | Broken Archive |
| ELCP-005 | Invalid Compression |

---

## DESP Errors

| Code | Meaning |
|------|---------|
| DESP-001 | Unknown Packet |
| DESP-002 | Missing Checkpoint |
| DESP-003 | Duplicate Packet |
| DESP-004 | Revocation Conflict |
| DESP-005 | Chronology Conflict |
| DESP-006 | Synchronization Failed |

---

## TDEP Errors

| Code | Meaning |
|------|---------|
| TDEP-001 | Missing Domain ID |
| TDEP-002 | Duplicate Domain |
| TDEP-003 | Invalid Enrollment |
| TDEP-004 | Unauthorized Issuer |
| TDEP-005 | Revoked Domain |
| TDEP-006 | Enrollment Failed |

Future error codes MUST be registered before use.

---

# 8. Packet Identifier Namespace

Packet IDs are opaque identifiers.

Example:

dpk_7f3a91c4e82b

Implementations MUST NOT encode packet meaning inside Packet IDs.

---

# 9. Checkpoint Namespace

Checkpoint identifiers follow:

CP-000001

Reserved range:

CP-000001 onward.

---

# 10. Domain Namespace

Trust Domains use:

TD-000001

Reserved range:

TD-000001 onward.

---

# 11. Compatibility Registry

Future extensions MUST satisfy Compatibility Before Replacement.

Unknown extensions SHOULD be safely ignored by older implementations.

---

# 12. Registration Policy

Permanent assignments require:

- unique identifier,
- documented purpose,
- compatibility review,
- registry update.

Reserved identifiers MUST NOT be reused.

---

# 13. Reserved Ranges

| Range | Purpose |
|--------|---------|
| DRFC-0006–0999 | Future RFCs |
| DPR-0002–0999 | Future Registries |
| DTS-002–0999 | Future Tests |
| DIP-001–0999 | Integration Profiles |
| DRE-001–0999 | Reference Engines |
| Packet Modes 06–255 | Reserved |
| Trust Levels T6–T255 | Reserved |

---

# 14. Registry Integrity

The registry exists to preserve long-term stability.

Historical assignments MUST remain permanently recorded.

Future revisions MAY extend the registry but SHALL NOT redefine existing assignments without explicit superseding specifications.

---

# Change Log

| Version | Change |
|----------|--------|
| 1.0 | Initial Founder Draft |
