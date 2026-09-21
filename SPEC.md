# Dharma Protocol v2 Canonical Specification

Status: Release Candidate Draft

## 1. Mission

Dharma is a deterministic distributed protocol built around immutable identity, authenticated communication and verifiable consensus.

## 2. Layer Model

L1 Transport
L2 Identity
L3 Discovery
L4 Sessions
L5 Consensus
L6 Federation

## 3. Protocol Invariants

- Every node has one immutable Node ID.
- Every critical action requires a valid signature.
- Replay attacks MUST fail.
- Consensus commits require quorum proof.
- Final commits MUST remain immutable.

## 4. Wire Contract

All packets MUST follow PACKET_FORMAT.md.

## 5. State Machine

All nodes MUST follow STATE_TRANSITIONS.md.

## 6. Error Registry

All implementations MUST use ERROR_CODES.md.

## 7. Compatibility

Minor versions SHOULD remain compatible.
Major versions require explicit migration.

## 8. Extensions

Future functionality MUST ship as DSP extensions instead of expanding the canonical DRFC count.
