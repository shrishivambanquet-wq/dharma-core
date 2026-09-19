# Dharma Protocol

> Open protocol for authority, trust, delegation and verifiable governance.

![Status](https://img.shields.io/badge/status-v0.1--alpha-blue)
![Tests](https://img.shields.io/badge/tests-300-brightgreen)
![Language](https://img.shields.io/badge/language-Python-blue)

## Overview

Dharma is a reference implementation of an open protocol designed to model authority, delegation, trust negotiation and verifiable governance through DRFC (Dharma Request for Comments).

This repository contains the v0.1 Alpha reference implementation developed using a DRFC-driven workflow.

## Highlights

- 300 automated tests
- DRFC-based development process
- Authority Graph
- Delegation Engine
- Policy Engine
- Trust Negotiation
- Session Management
- Network Discovery
- Signed Messages
- Python reference implementation

## Project Structure



```
dharma/
tests/
.github/workflows/
Founder files/
```

## Quick Start

```bash
pip install -r requirements.txt
python -m pytest -q
```

Expected output:

```text
300 passed
```

## Version

- Release: **v0.1-alpha**
- Protocol Level: **DRFC-0030**

## Philosophy

Dharma separates the protocol from its implementations. The protocol evolves through DRFCs while maintaining backward compatibility where practical.

## Contributing

Future changes should be proposed through new DRFCs before becoming part of the protocol.

## License

The Dharma Protocol is an open protocol. Commercial infrastructure may be built on top of open specifications while the core protocol remains publicly documented.

