
# DRFC-0006 — Dharma Wire Format (DWF)

**Document ID:** DRFC-0006
**Founder:** Paresh Somani
**Version:** 1.0
**Status:** Founding Freeze

> Defines the exact byte-level structure used to serialize Dharma Authority Packets (DAP) for transmission across networks.

---

# Abstract

Previous Dharma RFCs define behavior.

DWF defines the bytes.

Every Dharma implementation MUST serialize packets in a deterministic format so that independent implementations exchange identical packets.

---

# 1. Design Goals

The wire format MUST:

- remain compact,
- remain deterministic,
- remain language-neutral,
- preserve DAP semantics.

---

# 2. Packet Layout

+--------------------------------------------------+
| Fixed Header                                     |
+--------------------------------------------------+
| Authority Core                                   |
+--------------------------------------------------+
| Constraint Block                                 |
+--------------------------------------------------+
| Parent Packet ID                                 |
+--------------------------------------------------+
| Checkpoint ID                                    |
+--------------------------------------------------+
| Signature                                        |
+--------------------------------------------------+

Only these fields travel on the network.

---

# 3. Fixed Header

| Field | Size |
|--------|------|
| Version | 1 byte |
| Mode | 1 byte |
| Flags | 2 bytes |
| Packet ID | 16 bytes |
| Timestamp | 8 bytes |

Header size:

28 bytes.

---

# 4. Authority Core

| Field | Size |
|--------|------|
| Issuer ID | 16 bytes |
| Subject ID | 16 bytes |
| Purpose ID | 8 bytes |

Total:

40 bytes.

Purpose IDs reference standardized meanings rather than carrying long text.

---

# 5. Constraint Block

A compact constraint format.

Example fields:

- Money
- Time
- Geography
- Risk

Unused constraints occupy zero space.

The block is variable-length.

---

# 6. Parent Reference

Instead of carrying full lineage, every packet carries:

Parent Packet ID

16 bytes.

Complete history remains recoverable through DRFC-0003.

---

# 7. Checkpoint

Checkpoint IDs compress historical verification.

Example:

CP-42

Wire size:

16 bytes.

---

# 8. Signature

Every packet ends with a fixed signature field.

Default allocation:

64 bytes.

Future RFCs may define signature algorithms.

---

# 9. Total Packet Size

Typical packet

| Component | Bytes |
|-----------|-------|
| Header | 28 |
| Authority | 40 |
| Constraints | 20 |
| Parent | 16 |
| Checkpoint | 16 |
| Signature | 64 |

Approximate total:

184 bytes.

Large packets remain possible when optional extensions are used.

---

# 10. Packet Modes

Mode values are encoded numerically.

| Value | Mode |
|--------|------|
| 01 | GRANT |
| 02 | DELEGATE |
| 03 | EXECUTE |
| 04 | REVOKE |
| 05 | EVIDENCE |

Unknown values MUST be rejected.

---

# 11. Flags

Reserved flags allow future capabilities without changing packet layout.

Unused flags MUST be zero.

---

# 12. Serialization Rules

Every implementation MUST serialize fields in the same order.

Field order never changes.

Unknown extensions appear only after the fixed packet structure.

---

# 13. Compression Compatibility

DRFC-0003 remains compatible.

Compressed packets transmit only:

- Parent Packet
- Checkpoint

Historical retrieval remains optional.

---

# 14. Validation Before Parsing

Receivers perform:

1. Header validation.
2. Version check.
3. Mode validation.
4. Packet integrity.
5. Signature verification.

Only then may execution continue.

---

# 15. Example Packet

Version:1

Mode:GRANT

Packet:dpk_83fa91

Issuer:Human

Subject:Agent-A

Limit:₹10,000

Parent:None

Checkpoint:CP-0

Signature:...

Wire size:

~184 bytes.

---

# 16. Conformance

A Dharma implementation SHALL NOT claim DWF compatibility unless it produces identical serialized packets for identical inputs.

---

# Change Log

| Version | Change |
|----------|--------|
| 1.0 | Initial Founder Draft |
