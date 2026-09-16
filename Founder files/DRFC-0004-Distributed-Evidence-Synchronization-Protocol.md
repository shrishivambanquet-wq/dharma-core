
# DRFC-0004 — Distributed Evidence Synchronization Protocol (DESP)

**Document ID:** DRFC-0004
**Founder:** Paresh Somani
**Version:** 1.0
**Status:** Founding Freeze

> Defines how independent Dharma implementations exchange and verify evidence without exposing their complete internal history.

---

# Abstract

A Dharma implementation may belong to a company, government, bank, AI provider, or personal device.

These systems cannot assume they share the same database.

DESP allows two independent Dharma implementations to verify authority outcomes using standardized evidence exchange.

DESP does not synchronize entire ledgers.

It synchronizes only the evidence required for verification.

---

# 1. Purpose

DESP answers one question:

> "How can System A trust an authority decision made by System B?"

The protocol guarantees that evidence remains portable while authority remains independently verifiable.

---

# 2. Design Principles

DESP follows four principles.

- Evidence before trust.
- Minimum necessary exchange.
- Independent verification.
- Compatibility before replacement.

---

# 3. Participants

| Role | Purpose |
|------|---------|
| Origin Node | Created authority |
| Remote Node | Receives authority |
| Verifier Node | Validates evidence |
| Ledger | Stores permanent records |

Every implementation MAY perform multiple roles.

---

# 4. Synchronization Model

DESP exchanges evidence—not databases.

Before synchronization:

Origin Ledger

Packet A

Packet B

Packet C

Remote Ledger

Packet X

Packet Y

After synchronization:

Remote Ledger receives only the required evidence proving Packet C.

Historical records remain local unless requested.

---

# 5. Evidence Exchange Packet (DEPX)

DESP introduces a transport-neutral evidence packet.

A DEPX contains:

- Packet ID
- Checkpoint ID
- Parent Packet
- Evidence Status
- Timestamp

Example:

Packet: dpk_83fa91

Checkpoint: CP-42

Status: VERIFIED

---

# 6. Synchronization Modes

| Mode | Purpose |
|------|---------|
| VERIFY | Request verification |
| SHARE | Send evidence |
| UPDATE | Send newer evidence |
| REVOKE | Broadcast revocation |
| ACK | Confirm receipt |

The packet structure remains unchanged.

Only synchronization behavior changes.

---

# 7. Verification Handshake

Every synchronization follows the same lifecycle.

REQUEST

↓

VERIFY

↓

SHARE

↓

VALIDATE

↓

ACKNOWLEDGE

If validation fails, synchronization stops.

---

# 8. Synchronization Rules

## DESP-001

Packet IDs MUST be globally unique.

## DESP-002

Every shared packet MUST reference a valid checkpoint.

## DESP-003

Synchronization MUST preserve chronology.

## DESP-004

Revocation MUST propagate.

## DESP-005

Evidence MUST remain immutable after verification.

---

# 9. Revocation Broadcast

When authority is revoked:

Origin

↓

Remote A

↓

Remote B

↓

Remote C

Every receiving implementation MUST invalidate affected descendants.

---

# 10. Conflict Resolution

Conflicts may occur when:

- duplicate packets appear,
- timestamps disagree,
- checkpoints differ.

Resolution order:

1. Invalid lineage fails.
2. Revoked authority wins.
3. Expired authority fails.
4. Otherwise request additional evidence.

---

# 11. Minimal Disclosure

DESP intentionally limits information sharing.

A verifier SHOULD receive only:

- Packet ID
- Checkpoint
- Required evidence
- Verification result

Business-sensitive history remains local.

---

# 12. Failure Codes

| Code | Meaning |
|------|---------|
| DESP-001 | Unknown Packet |
| DESP-002 | Missing Checkpoint |
| DESP-003 | Duplicate Packet |
| DESP-004 | Revocation Conflict |
| DESP-005 | Chronology Conflict |
| DESP-006 | Synchronization Failed |

These integrate with DEP validation behavior.

---

# 13. Worked Example

Company A grants authority.

Company B receives delegated authority.

Company B requests verification.

Flow:

REQUEST

↓

VERIFY

↓

SHARE

↓

VALIDATE

↓

ACK

Result:

Authority accepted without copying Company A's complete ledger.

---

# 14. Security Considerations

DESP protects against:

- forged evidence,
- duplicate synchronization,
- replayed verification,
- revoked authority reuse,
- inconsistent checkpoints.

Future versions MAY define cryptographic proofs for stronger verification.

---

# 15. Conformance Requirement

An implementation SHALL NOT claim DESP compatibility unless it performs the complete synchronization handshake and produces identical verification outcomes.

---

# Change Log

| Version | Change |
|----------|--------|
| 1.0 | Initial Founder Draft |
