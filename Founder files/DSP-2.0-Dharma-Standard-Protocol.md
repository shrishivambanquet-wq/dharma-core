# DSP-2.0
## Dharma Standard Protocol

**Status:** Founding Freeze v1
**Founder:** Paresh Somani

---

# Abstract

DSP defines how Dharma behaves.

The Constitution defines values.

DSP defines protocol behavior.

---

# Protocol Principle 1

## Compatibility Before Replacement

Existing protocols SHOULD continue working.

Dharma SHOULD layer above them instead of replacing them.

---

# Protocol Guarantees

Every implementation MUST preserve:

1. Authority Chain
2. Lineage
3. Constraint Preservation
4. Non-expansion of Authority
5. Evidence Generation
6. Revocation Propagation

---

# DAP — Dharma Authority Packet

Every Dharma interaction uses one canonical packet.

```
+-----------------------------+
| Layer 0 | Header            |
+-----------------------------+
| Layer 1 | Authority Core    |
+-----------------------------+
| Layer 2 | Constraints       |
+-----------------------------+
| Layer 3 | Lineage           |
+-----------------------------+
| Layer 4 | Evidence          |
+-----------------------------+
| Layer 5 | Extensions        |
+-----------------------------+
```

---

# Layer Definitions

## Layer 0

Protocol metadata.

## Layer 1

Issuer

Subject

Purpose

## Layer 2

Operational limits.

## Layer 3

Authority ancestry.

## Layer 4

Execution evidence.

## Layer 5

Future compatibility.

---

# Packet Modes

DAP uses one packet format with five modes.

| Mode | Purpose |
|------|---------|
| GRANT | Create authority |
| DELEGATE | Pass authority |
| EXECUTE | Use authority |
| REVOKE | Cancel authority |
| EVIDENCE | Record outcome |

---

# Authority Handshake

```
GRANT
 ↓
ACCEPT
 ↓
CONFIRM
 ↓
EXECUTE
 ↓
EVIDENCE
```

This becomes the common transaction model.

---

# Authority State Machine

Authority evolves through:

- Create
- Delegate
- Attenuate
- Merge
- Split
- Revoke
- Expire

---

# Foundational Invariant

A child authority MUST NOT exceed its parent.

Future mathematical specifications MAY formalize this invariant.

---

# Cross-Protocol Compatibility

| Existing Protocol | Dharma Role |
|-------------------|-------------|
| HTTP | Carries requests |
| OAuth | Grants access |
| MCP | Connects tools |
| A2A | Coordinates agents |
| Payment Systems | Execute effects |

DAP preserves authority continuity across all of them.

---

# Security Considerations

Future implementations SHOULD protect against:

- Prompt Injection
- Replay Attacks
- Unauthorized Delegation
- Authority Inflation
- Revoked Authority Reuse