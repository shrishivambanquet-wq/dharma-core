
### DRFC-0001

Dharma Authority Packet (DAP)

Document ID: DRFC-0001

Version: 0.1 (Founder's Draft)

Founder: Paresh Somani

Status: Confidential Working Draft

> This document defines the first protocol specification of the Dharma ecosystem. It is written in RFC style and serves as the normative foundation for future implementations.

### Abstract

The Dharma Authority Packet (DAP) defines a protocol for representing, delegating, constraining, revoking, and proving authority across autonomous systems.

Unlike transport protocols, which deliver information, or authorization systems, which grant access, DAP proposes a common representation for authority that can remain traceable across multiple agents, tools, enterprises, and payment systems while remaining compatible with existing protocols.

### Status of this Memo

This document is an internal founder draft.

It is not an Internet Standard.

Future revisions may evolve through public review, implementation feedback, and formal standardization processes.

### Table of Contents

* Introduction

* Design Philosophy

* Terminology

* Principle 0

* Protocol Principles

* Dharma Authority Packet

* Packet Layers

* Packet Modes

* Authority Handshake

* Authority State Machine

* Cross-Protocol Compatibility

* Security Considerations

* Future Extensions

* Founder's Declaration

### 1\. Introduction

Modern software systems exchange requests extremely well.

They do not always preserve authority equally well.

A single human decision may travel through multiple AI agents, APIs, enterprise systems, payment networks, and robots before producing a real-world effect.

DAP proposes that authority should remain visible throughout that journey.

The protocol is intentionally additive rather than replacement-oriented.

### 2\. Design Philosophy

DAP follows four founding principles.

### 2.1 Compatibility Before Replacement

Existing protocols SHOULD continue operating unchanged.

DAP SHOULD layer on top of existing ecosystems whenever possible.

### 2.2 Minimal Reinvention

DAP SHOULD reuse existing transport, networking, and authentication mechanisms instead of replacing them.

### 2.3 Authority First

Capability MUST NOT be interpreted as authority.

### 2.4 Future Compatibility

Unknown extensions SHOULD be safely ignored rather than breaking interoperability.

### 3\. Terminology

| Term       | Meaning                                    |
| ---------- | ------------------------------------------ |
| Authority  | Legitimate permission to produce an effect |
| Issuer     | Creator of authority                       |
| Subject    | Receiver of authority                      |
| Constraint | Operational limitation                     |
| Lineage    | Parent-child authority chain               |
| Effect     | Real-world outcome                         |
| Evidence   | Verifiable proof                           |
| Revocation | Cancellation of authority                  |

These terms SHOULD remain stable across future Dharma documents.

### 4\. Principle 0

Capability does not constitute authority.

This is the immutable constitutional foundation of Dharma.

Every future implementation MUST remain compatible with Principle 0.

### 5\. Protocol Principles

Every conforming implementation MUST preserve these six guarantees.

| ID    | Rule                                                    |
| ----- | ------------------------------------------------------- |
| DSP-1 | Every consequential action requires an Authority Chain. |
| DSP-2 | Every delegation preserves lineage.                     |
| DSP-3 | Authority cannot expand during delegation.              |
| DSP-4 | Constraints travel with authority.                      |
| DSP-5 | Every effect produces evidence.                         |
| DSP-6 | Revocation propagates through descendants.              |

These rules define protocol behavior independently of implementation language.

### 6\. Dharma Authority Packet

DAP is the canonical packet format of the Dharma ecosystem.

Every packet consists of six conceptual layers.

The serialization format is intentionally left unspecified in Version 0.1.

### 7\. Packet Layers

### Layer 0 — Header

Contains protocol metadata.

Conceptually includes:

* Version

* Packet Mode

* Packet Identifier

### Layer 1 — Authority Core

Defines the authority itself.

Conceptually contains:

* Issuer

* Subject

* Purpose

### Layer 2 — Constraints

Authority travels together with its limitations.

Examples include:

* Monetary limits

* Time limits

* Geographic limits

* Organizational limits

* Risk limits

Constraints MUST remain attached throughout delegation.

### Layer 3 — Lineage

This layer preserves ancestry.

Example:

Human

→ Agent A

→ Agent B

→ Agent C

Every descendant SHOULD remain traceable to the original issuer.

### Layer 4 — Evidence

After execution, evidence SHOULD preserve:

* Issuer

* Subject

* Action

* Effect

* Timestamp

### Layer 5 — Extensions

Future protocol versions MAY introduce optional capabilities without breaking compatibility.

### 8\. Packet Modes

DAP uses one packet structure with multiple operating modes.

| Mode     | Purpose            |
| -------- | ------------------ |
| GRANT    | Create authority   |
| DELEGATE | Transfer authority |
| EXECUTE  | Use authority      |
| REVOKE   | Cancel authority   |
| EVIDENCE | Record outcome     |

Changing mode changes behavior while preserving packet structure.

### 9\. Authority Handshake

DAP defines a five-stage authority lifecycle.

Each stage exists to preserve legitimacy before producing real-world consequences.

### 10\. Authority State Machine

Authority behaves as a state-transition system.

Supported conceptual transitions include:

* Create

* Delegate

* Attenuate

* Merge

* Split

* Revoke

* Expire

Future versions may define additional transitions without violating Principle 0.

### Foundational Invariant

A_{child} \\subseteq A_{parent}

No child authority may exceed its parent.

### 11\. Cross-Protocol Compatibility

DAP is intentionally protocol-agnostic.

| Existing System      | Dharma Role                 |
| -------------------- | --------------------------- |
| HTTP                 | Carries requests            |
| OAuth                | Grants access               |
| MCP                  | Connects tools              |
| A2A                  | Coordinates agents          |
| Payment Systems      | Execute financial effects   |
| Enterprise Platforms | Apply organizational policy |

DAP SHOULD preserve authority continuity across all of them.

### 12\. Security Considerations

Future implementations SHOULD consider:

* Prompt injection

* Replay attacks

* Unauthorized delegation

* Stolen authority

* Revoked authority reuse

* Authority inflation

Version 0.1 identifies these risks without prescribing cryptographic mechanisms.

### 13\. Future Extensions

The Dharma ecosystem is expected to expand through additional RFCs.

| RFC       | Purpose             |
| --------- | ------------------- |
| DRFC-0002 | Constraint Model    |
| DRFC-0003 | Evidence Model      |
| DRFC-0004 | Revocation Protocol |
| DRFC-0005 | Enterprise Profile  |

These remain planned documents.

### 14\. Founder's Declaration

> I, Paresh Somani, establish this Founder's Draft with the intention of exploring a universal authority protocol that prioritizes legitimate authority over raw capability while remaining compatible with existing technological ecosystems.

This document is the constitutional protocol foundation from which future Dharma specifications, reference implementations, and public RFCs may evolve.

### One thing I realized while writing this RFC

Real RFCs have a very strict writing style defined by RFC 2119 and later RFC 8174, where words like MUST, SHOULD, MAY, and MUST NOT have precise meanings.

I think we should adopt that discipline from the next revision. Instead of writing "authority should travel with constraints," we'd write "an implementation MUST preserve constraints during delegation." That would make DRFC-0001 read much closer to an authentic standards-track document while keeping it clearly identified as a founder draft rather than an official IETF RFC.
