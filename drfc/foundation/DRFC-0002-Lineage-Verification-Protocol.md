
# DRFC-0002 — Lineage Verification Protocol (LVP)

**Document ID:** DRFC-0002
**Founder:** Paresh Somani
**Version:** 1.0
**Status:** Founding Freeze

> Defines how every Dharma implementation MUST verify authority lineage before execution.

---

# Abstract

The Lineage Verification Protocol (LVP) specifies the deterministic algorithm used to verify that authority has been delegated legitimately from its original issuer to its current holder.

Without LVP, two Dharma implementations could reach different conclusions about the same DAP packet.

LVP guarantees identical verification decisions across implementations.

---

# 1. Purpose

LVP answers one question:

> "Is this authority legitimately inherited?"

Every EXECUTE operation MUST complete LVP verification before producing a real-world effect.

---

# 2. Definitions

| Term | Meaning |
|------|---------|
| Root Authority | Original issuer |
| Parent Authority | Immediate delegator |
| Child Authority | Receiver |
| Active Authority | Currently valid authority |
| Lineage Chain | Ordered delegation history |

---

# 3. Lineage Chain

Every DAP packet carries an ordered authority chain.

Example:

Human
↓

Agent-A
↓

Agent-B

↓

Agent-C

The first entry is always the Root Authority.

---

# 4. Verification Rules

A lineage is valid only if ALL rules succeed.

## Rule LVP-001

Exactly one Root Authority MUST exist.

PASS

Human

FAIL

Two independent roots.

---

## Rule LVP-002

Every child MUST reference one parent.

Broken ancestry is invalid.

---

## Rule LVP-003

The chain MUST remain continuous.

Valid:

Human

↓

A

↓

B

↓

C

Invalid:

Human

↓

A

↓

C

(missing B)

---

## Rule LVP-004

No cycles are permitted.

Invalid:

A → B → C → A

Circular authority MUST fail.

---

## Rule LVP-005

Delegation MUST preserve chronology.

A child cannot exist before its parent.

---

## Rule LVP-006

Authority MUST remain active.

Revoked or expired ancestors invalidate descendants.

---

# 5. Verification Algorithm

Every implementation executes the same procedure.

Input:

Current DAP packet.

Procedure:

1. Locate Root Authority.
2. Walk the chain.
3. Verify every parent.
4. Verify chronology.
5. Verify constraints.
6. Verify active status.
7. Return PASS or FAIL.

Output:

Deterministic decision.

---

# 6. Decision Tree

START

↓

Root Exists?

↓

NO → FAIL

↓

YES

↓

Continuous Chain?

↓

NO → FAIL

↓

YES

↓

Cycle?

↓

YES → FAIL

↓

NO

↓

Constraints Valid?

↓

NO → FAIL

↓

YES

↓

Authority Active?

↓

NO → FAIL

↓

YES

↓

PASS

---

# 7. Constraint Inheritance

Constraints travel through every delegation.

Example:

Human grants ₹10,000.

Agent-A delegates ₹3,000.

Agent-B attempts ₹5,000.

Verification:

Inherited limit = ₹3,000.

Result:

FAIL

Error:

DAP-005.

---

# 8. Revocation Cascade

Revocation propagates downward.

Example:

Human

↓

Agent-A

↓

Agent-B

↓

Agent-C

If Agent-A is revoked:

- Agent-B becomes invalid.
- Agent-C becomes invalid.

The Root Authority remains unchanged.

---

# 9. Expiration

Authority may expire.

Example:

Grant:

24 hours.

After expiration:

Every descendant becomes inactive.

Error:

DAP-007.

---

# 10. Merge Verification

Future versions may allow multiple authorities to merge.

Current rule:

Every merged authority MUST independently pass LVP before merging.

---

# 11. Split Verification

Splitting authority creates multiple children.

Example:

₹10,000

↓

₹4,000

+

₹6,000

The total delegated authority MUST NOT exceed the parent's remaining authority.

---

# 12. Failure Codes

| Code | Meaning |
|------|---------|
| LVP-001 | Missing Root |
| LVP-002 | Broken Parent |
| LVP-003 | Discontinuous Chain |
| LVP-004 | Circular Lineage |
| LVP-005 | Chronology Error |
| LVP-006 | Revoked Ancestor |
| LVP-007 | Expired Ancestor |

These map to DEP-1.0 validation behavior.

---

# 13. Worked Example

### Grant

Human → Agent-A

₹10,000

PASS

### Delegate

Agent-A → Agent-B

₹3,000

PASS

### Execute

Agent-B

₹2,500

PASS

### Execute

Agent-B

₹5,000

FAIL

Reason:

Constraint Violation.

---

# 14. Security Considerations

LVP prevents:

- Forged ancestry
- Missing delegation steps
- Circular authority
- Revoked authority reuse
- Expired authority execution

Future cryptographic verification MAY strengthen these guarantees.

---

# 15. Conformance Requirement

A Dharma implementation SHALL NOT claim compliance with DEP-1.0 unless every EXECUTE operation performs Lineage Verification according to DRFC-0002.

---

# Change Log

| Version | Change |
|----------|--------|
| 1.0 | Initial Founder Draft |
