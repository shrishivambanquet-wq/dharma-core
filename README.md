# Dharma Core v2.0

A deterministic distributed protocol with immutable identity, authenticated communication and verifiable consensus.

## Quick Start

git clone <repository-url>
cd dharma-core

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

pytest

Expected: 868 tests passing.

## Project Structure

- drfc/ — Canonical specifications
- dharma/ — Reference implementation
- tests/ — Verification suite
- release/ — Release artifacts

## Documentation

- SPEC.md
- PACKET_FORMAT.md
- STATE_TRANSITIONS.md
- ERROR_CODES.md
- TRACEABILITY.md

