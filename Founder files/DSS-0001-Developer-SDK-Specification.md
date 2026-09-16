
# DSS-0001 — Dharma Developer SDK Specification

**Document ID:** DSS-0001
**Founder:** Paresh Somani
**Version:** 1.0
**Status:** Founding Freeze

> Defines the official programming interface for implementing the Dharma Protocol without binding it to any specific programming language.

---

# Abstract

DEP-1.0 defines how Dharma behaves.

DSS-0001 defines how software interacts with Dharma.

Every implementation SHOULD expose the same logical API regardless of whether it is written in Python, C, Rust, Go, Java, or JavaScript.

The SDK is language-neutral.

---

# 1. Design Goals

The SDK MUST:

- preserve DEP behavior,
- remain language independent,
- produce identical authority decisions,
- expose a minimal public interface.

---

# 2. Public API

Every conforming SDK exposes seven core operations.

| Function | Purpose |
|----------|---------|
| grant() | Create authority |
| delegate() | Pass authority |
| execute() | Attempt an action |
| revoke() | Cancel authority |
| verify() | Validate lineage |
| evidence() | Record outcome |
| lookup() | Retrieve authority |

These names are permanently reserved.

---

# 3. grant()

Purpose:

Create a new DAP packet.

Input:

- Issuer
- Subject
- Purpose
- Constraints

Output:

- Packet ID
- Status

Example

grant(
Issuer=Human,
Subject=Agent-A,
Money=10000
)

Result

PASS

---

# 4. delegate()

Purpose:

Transfer authority.

Requirements:

- Parent exists.
- Constraints preserved.
- Child authority ≤ Parent authority.

Example

delegate(
Parent=dpk_001,
Subject=Agent-B,
Money=3000
)

Result

PASS

---

# 5. execute()

Purpose:

Attempt a real-world effect.

Example

execute(
Packet=dpk_002,
Amount=2500
)

Possible results:

- PASS
- FAIL

Failure returns a Dharma error code.

---

# 6. revoke()

Purpose:

Invalidate authority.

Example

revoke(
Packet=dpk_002,
Reason="Manual Revocation"
)

Effect:

Future execution fails.

Historical evidence remains.

---

# 7. verify()

Purpose:

Run DRFC-0002 Lineage Verification.

Example

verify(
Packet=dpk_002
)

Output

PASS

or

FAIL

---

# 8. evidence()

Purpose:

Record execution.

Example

evidence(
Packet=dpk_002,
Result=PASS
)

Evidence becomes immutable.

---

# 9. lookup()

Purpose:

Retrieve authority information.

Returns:

- Current status
- Constraints
- Parent
- Checkpoint
- Evidence summary

Historical archives remain optional.

---

# 10. Standard Response Object

Every SDK returns the same logical response.

Example

Status: PASS

Packet: dpk_83fa91

Mode: EXECUTE

Code: DAP-000

Message: Success

Failures use standardized error codes.

---

# 11. SDK Validation Flow

Every operation follows the same sequence.

Request

↓

Validate

↓

Verify Lineage

↓

Check Constraints

↓

Execute

↓

Generate Evidence

↓

Return Response

This flow is mandatory.

---

# 12. Event Hooks

SDKs MAY expose events.

Examples:

- OnGrant
- OnDelegate
- OnExecute
- OnRevoke
- OnEvidence

Events never bypass validation.

---

# 13. Error Mapping

SDKs MUST preserve official registry codes.

Example

Constraint Violation

↓

DAP-005

Implementations may translate messages into different languages while preserving codes.

---

# 14. Multi-Language Compatibility

This SDK specification applies equally to:

- Python
- C
- Rust
- Go
- Java
- JavaScript
- Swift
- Kotlin

Behavior remains identical.

---

# 15. Worked Example

Step 1

grant()

↓

PASS

Step 2

delegate()

↓

PASS

Step 3

execute(2500)

↓

PASS

Step 4

evidence()

↓

Recorded

Step 5

execute(5000)

↓

FAIL

DAP-005

---

# 16. Performance Expectations

SDK implementations SHOULD:

- validate quickly,
- preserve lineage,
- avoid changing packet meaning,
- remain deterministic.

Performance optimizations MUST NOT change protocol decisions.

---

# 17. Conformance

An SDK SHALL NOT claim Dharma compatibility unless every public operation behaves consistently with:

- DEP-1.0
- DRFC-0002
- DRFC-0003
- DRFC-0004
- DRFC-0005
- DTS-001

---

# Change Log

| Version | Change |
|----------|--------|
| 1.0 | Initial Founder Draft |
