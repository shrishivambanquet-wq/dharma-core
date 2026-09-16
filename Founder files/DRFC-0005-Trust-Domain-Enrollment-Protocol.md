
# DRFC-0005 — Trust Domain Enrollment Protocol (TDEP)

**Document ID:** DRFC-0005
**Founder:** Paresh Somani
**Version:** 1.0
**Status:** Founding Freeze

> Defines how an organization, individual, device, or AI system becomes a recognized Dharma Trust Domain without requiring a single central authority.

---

# Abstract

DEP-1.0 defines authority.

DRFC-0002 verifies lineage.

DRFC-0003 compresses history.

DRFC-0004 synchronizes evidence.

DRFC-0005 defines how new participants enter the Dharma ecosystem while preserving independent governance.

---

# 1. Purpose

TDEP answers one question:

> "How does a new participant become a Dharma Trust Domain?"

Enrollment creates a recognized identity capable of issuing, receiving, and verifying Dharma authority.

---

# 2. Design Principles

Enrollment MUST preserve independence.

Enrollment MUST preserve traceability.

Enrollment MUST NOT require universal central ownership.

Enrollment MUST remain compatible with existing identity systems.

---

# 3. Trust Domains

A Trust Domain is an administrative boundary that manages its own authority.

Examples include:

- Individual
- Company
- Government agency
- Bank
- AI provider
- Personal device

Every Trust Domain has its own internal policies.

---

# 4. Domain Identifier

Every enrolled domain receives a permanent identifier.

Example

Domain-ID: TD-000001

The identifier uniquely represents the Trust Domain.

It does not represent authority itself.

---

# 5. Domain Roles

| Role | Purpose |
|------|---------|
| Issuer | Creates authority |
| Subject | Receives authority |
| Verifier | Validates authority |
| Ledger Operator | Maintains evidence |
| Domain Administrator | Manages enrollment |

One implementation MAY perform multiple roles.

---

# 6. Enrollment Handshake

Every enrollment follows the same lifecycle.

REQUEST

↓

VERIFY

↓

REGISTER

↓

ACTIVATE

↓

ACKNOWLEDGE

Enrollment completes only after activation.

---

# 7. Enrollment Packet

TDEP introduces a Domain Enrollment Packet (DEPK).

Required fields:

- Domain-ID
- Domain Type
- Enrollment Timestamp
- Requested Roles
- Status

Example

Domain-ID: TD-000001

Type: Company

Roles: Issuer, Verifier

Status: Pending

---

# 8. Enrollment Rules

## TDEP-001

Every domain MUST possess one Domain-ID.

## TDEP-002

A domain MUST complete enrollment before issuing authority.

## TDEP-003

Enrollment MUST preserve chronology.

## TDEP-004

Revoked enrollment invalidates future authority issuance.

## TDEP-005

Domain identity MUST remain stable after activation.

---

# 9. Trust Levels

TDEP separates enrollment from operational capability.

| Level | Capability |
|------|-------------|
| T0 | Identity only |
| T1 | Receive authority |
| T2 | Delegate authority |
| T3 | Issue authority |
| T4 | Verify authority |
| T5 | Operate a ledger |

Higher levels include lower-level capabilities.

---

# 10. Federation

Independent domains MAY cooperate without sharing internal governance.

Example

Company A

↓

Bank

↓

Government

↓

AI Provider

Each remains an independent Trust Domain.

---

# 11. Revocation

Enrollment itself may be revoked.

When revoked:

- Future authority issuance stops.
- Existing historical evidence remains valid.
- Descendant domains remain independently evaluated.

Historical records MUST NOT disappear.

---

# 12. Domain Migration

Organizations may evolve.

Example

Startup

↓

Enterprise

↓

Holding Company

Migration MUST preserve Domain-ID continuity or explicitly record succession.

---

# 13. Conflict Resolution

Conflicts include:

- duplicate Domain IDs,
- disputed enrollment,
- conflicting roles,
- revoked enrollment.

Resolution order:

1. Invalid enrollment fails.
2. Duplicate IDs fail.
3. Revoked enrollment loses future issuance rights.
4. Otherwise request additional evidence.

---

# 14. Failure Codes

| Code | Meaning |
|------|---------|
| TDEP-001 | Missing Domain ID |
| TDEP-002 | Duplicate Domain |
| TDEP-003 | Invalid Enrollment |
| TDEP-004 | Unauthorized Issuer |
| TDEP-005 | Revoked Domain |
| TDEP-006 | Enrollment Failed |

These integrate with DEP validation behavior.

---

# 15. Worked Example

### Enrollment

Organization requests enrollment.

REQUEST

↓

VERIFY

↓

REGISTER

↓

ACTIVATE

↓

ACK

Result:

Trust Domain activated.

The organization can now issue authority according to its assigned trust level.

---

# 16. Security Considerations

TDEP protects against:

- duplicate domain creation,
- unauthorized authority issuance,
- revoked enrollment reuse,
- conflicting domain identities.

Future versions MAY introduce stronger cryptographic enrollment mechanisms.

---

# 17. Conformance Requirement

An implementation SHALL NOT claim TDEP compatibility unless it performs the complete enrollment handshake and preserves Domain-ID stability throughout the domain lifecycle.

---

# Change Log

| Version | Change |
|----------|--------|
| 1.0 | Initial Founder Draft |
