# Dharma Protocol v1.0.0-rc1

> An open protocol for verifiable delegation of authority between humans, AI agents, and institutions.

## Status

- DRFC: 0001–0100 Complete
- Reference Implementation: Python
- Test Suite: 790+ Passed
- Stage: Architecture Audit

---

# Architecture

| Layer | DRFC Range | Purpose |
|--------|------------|---------|
| Layer 1 | 0001–0020 | Core Wire & Transport |
| Layer 2 | 0021–0050 | Discovery & Federation |
| Layer 3 | 0051–0070 | Reliability & Routing |
| Layer 4 | 0071–0090 | Authority & Governance |
| Layer 5 | 0091–0100 | Trust & Finalization |

---

# Core Principles

1. Authority originates from Humans or Institutions.
2. AI may propagate delegated authority only within cryptographically verifiable limits.
3. Authority is revocable.
4. Authority expires unless renewed.
5. Every authority action is auditable.

---

# Quick Start

```python
from dharma import Node

node = Node()
node.join()

## Step 2 — Verify

```bash
cat INDEX.md

rm dharma/network/event_bus.py
rm dharma/network/event_subscription.py
rm dharma/network/event_replay.py
rm dharma/network/event_integrity.py
md
