# DEP-1.0 — Dharma Engineered Protocol

**Founder:** Paresh Somani
**Version:** 1.0
**Status:** Founding Freeze
**Date:** 15 September 2026

> A universal authority protocol designed to work alongside existing protocols while preserving legitimate authority across humans, AI agents, enterprises, payment systems, APIs, and future autonomous systems.

---

# 1. Purpose

Dharma does not replace HTTP, TCP, OAuth, MCP, A2A, or payment protocols.

It introduces one shared authority layer that any of them can carry.

Mission:

> Preserve legitimate authority from origin to final effect.

---

# 2. Immutable Principle

## Principle 0

**Capability does not constitute authority.**

Every implementation MUST preserve this rule.

---

# 3. Protocol Architecture

```
Application
     │
     ▼
HTTP / MCP / A2A / UPI / APIs
     │
     ▼
DAP (Dharma Authority Packet)
     │
     ▼
Execution
     │
     ▼
Evidence
```

Dharma rides with existing protocols.

---

# 4. Core Components

The engineered product consists of five permanent components.

| Component | Purpose |
|-----------|---------|
| DAP | Authority Packet |
| DRE | Reference Engine |
| Validation Engine | Rule enforcement |
| Evidence Engine | Record keeping |
| Revocation Engine | Authority cancellation |

---

# 5. DAP — Dharma Authority Packet

Every authority is represented by exactly one packet.

## Layer Structure

```
DAP
├── Layer 0 Header
├── Layer 1 Authority Core
├── Layer 2 Constraints
├── Layer 3 Lineage
├── Layer 4 Evidence
└── Layer 5 Extensions
```

Older implementations ignore unknown extensions.

---

# 6. Layer Specification

## Layer 0 — Header

| Field | Meaning |
|--------|---------|
| Version | Protocol version |
| Mode | Packet behavior |
| Packet-ID | Opaque unique identifier |
| Timestamp | Creation time |

Example:

Version:1

Mode:GRANT

Packet-ID:dpk_83fa91...

---

## Layer 1 — Authority Core

| Field | Meaning |
|--------|---------|
| Issuer | Authority creator |
| Subject | Authority receiver |
| Purpose | Intended objective |

Example:

Issuer:Human

Subject:Agent-A

Purpose:Book Flight

---

## Layer 2 — Constraints

Constraints travel together with authority.

Examples:

- Money
- Time
- Geography
- Organization
- Risk
- Purpose

Example:

Max:₹15,000

Country:India

Time:24h

---

## Layer 3 — Lineage

Lineage preserves ancestry.

Example:

Human

↓

Agent-A

↓

Agent-B

Every implementation SHOULD preserve the complete ancestry.

---

## Layer 4 — Evidence

Evidence records the final effect.

Example:

Action:Flight Booked

Amount:₹12,850

Status:Success

Time:10:32

Evidence never rewrites history.

---

## Layer 5 — Extensions

Future protocol versions MAY introduce optional capabilities without breaking compatibility.

---

# 7. Packet Modes

DAP uses one packet format with five behaviors.

| Mode | Purpose |
|------|---------|
| GRANT | Create authority |
| DELEGATE | Pass authority |
| EXECUTE | Use authority |
| REVOKE | Cancel authority |
| EVIDENCE | Record outcome |

The packet structure never changes.

Only behavior changes.

---

# 8. Authority Handshake

Every authority follows the same lifecycle.

```
GRANT
   │
   ▼
ACCEPT
   │
   ▼
CONFIRM
   │
   ▼
EXECUTE
   │
   ▼
EVIDENCE
```

This handshake becomes the universal transaction model.

---

# 9. Validation Engine

Every packet MUST satisfy validation rules.

## GRANT

Required:

- Issuer
- Subject
- Purpose

## DELEGATE

Required:

- Parent authority
- Valid lineage
- Constraint preservation

## EXECUTE

Required:

- Active authority
- Valid constraints
- Non-expansion

## REVOKE

Required:

- Existing authority
- Revocation reason

## EVIDENCE

Required:

- Executed packet reference
- Recorded outcome

Invalid packets MUST be rejected.

---

# 10. Authority State Machine

Authority behaves as a controlled state-transition system.

Allowed transitions:

- Create
- Delegate
- Attenuate
- Merge
- Split
- Execute
- Revoke
- Expire

Illegal transitions MUST fail.

---

# 11. Engineering Invariants

Every implementation MUST preserve these rules.

## Invariant 1

A child authority MUST NOT exceed its parent.

## Invariant 2

Lineage MUST remain traceable.

## Invariant 3

Constraints MUST survive delegation.

## Invariant 4

Every successful execution SHOULD produce evidence.

## Invariant 5

Revocation SHOULD invalidate affected descendants.

---

# 12. Error Codes

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

Standardized errors simplify interoperability.

---

# 13. Cross-Protocol Compatibility

| Existing System | Dharma Role |
|----------------|-------------|
| HTTP | Carries requests |
| OAuth | Grants access |
| MCP | Connects tools |
| A2A | Coordinates agents |
| UPI | Executes payments |
| Enterprise Platforms | Apply organizational policy |

Dharma preserves authority across all of them.

---

# 14. Security Model

Future implementations SHOULD defend against:

- Prompt Injection
- Replay Attacks
- Forged Lineage
- Stolen Authority
- Authority Inflation
- Revoked Authority Reuse

This version intentionally avoids prescribing cryptographic algorithms.

---

# 15. Reference Transaction

Scenario:

Human grants ₹10,000.

Agent A receives authority.

Agent A delegates ₹3,000.

Agent B attempts ₹5,000.

Execution:

GRANT ✓

DELEGATE ✓

EXECUTE ✗

Reason:

Constraint violation.

Evidence:

Packet records the rejection.

---

# 16. Future Modules

Future specifications build on DEP-1.0.

- DRFC-0002 Constraint Model
- DRFC-0003 Evidence Specification
- DRFC-0004 Revocation Model
- DRFC-0005 Enterprise Profile
- DRE-1.0 Reference Engine

These documents extend DEP rather than replacing it.

---

# 17. Founder's Declaration

I, Paresh Somani, establish DEP-1.0 as the first engineered specification of the Dharma Protocol.

Its purpose is to preserve legitimate authority across autonomous systems while remaining compatible with the existing technological ecosystem.

Every future Dharma implementation SHOULD derive from this specification rather than redefining its foundation.