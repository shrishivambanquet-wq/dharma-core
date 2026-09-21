# DRFC-0003 — Evidence & Lineage Compression Protocol (ELCP)

**Document ID:** DRFC-0003
**Founder:** Paresh Somani
**Version:** 1.0
**Status:** Founding Freeze

> Defines how Dharma preserves verifiable authority history while keeping DAP packets compact enough for real-world systems.

---

# Abstract

DEP-1.0 stores authority inside the Dharma Authority Packet (DAP).

DRFC-0002 verifies lineage.

DRFC-0003 introduces compression.

Instead of carrying unlimited history inside every packet, Dharma separates **active authority** from **historical evidence** while ensuring that any implementation can still verify legitimacy.

---

# 1. Purpose

ELCP solves three problems.

1. Unlimited lineage growth.
2. Large packet sizes.
3. Slow verification.

The protocol guarantees that compression never changes authority decisions.

---

# 2. Design Principles

Compression MUST preserve truth.

Compression MUST NOT alter authority.

Verification MUST produce identical decisions before and after compression.

---

# 3. Dual-Record Model

Every authority now has two records.

| Record | Purpose |
|---------|---------|
| Active Packet | Current authority |
| Evidence Ledger | Permanent history |

The Active Packet stays small.

The Evidence Ledger keeps history.

---

# 4. Packet Structure

Before compression

Human

↓

Agent-A

↓

Agent-B

↓

Agent-C

↓

Agent-D

After compression

Current Packet

Agent-D

↓

Checkpoint

Historical chain moves into the Evidence Ledger.

---

# 5. Checkpoint

A Checkpoint represents a verified historical boundary.

Example

Checkpoint ID:

CP-000001

Meaning:

Everything before this checkpoint has already been verified.

Future verification begins from the checkpoint.

---

# 6. Evidence Ledger

The Evidence Ledger stores immutable records.

Each record contains:

- Packet ID
- Parent Packet
- Issuer
- Subject
- Action
- Constraints
- Timestamp
- Result

Example

Ledger Entry

Packet: dpk_83fa91

Parent: dpk_72bc10

Action: DELEGATE

Result: PASS

---

# 7. Compression Rule

Compression may occur only after authority has become stable.

A packet becomes compressible when:

- execution completed,
- evidence recorded,
- lineage verified.

Pending packets MUST NOT compress.

---

# 8. Verification After Compression

Input:

Current Packet

Procedure:

1. Verify checkpoint.
2. Verify