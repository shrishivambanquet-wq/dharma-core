# Wire Protocol
Message schema and version negotiation.
# Wire Protocol v2

## Required Fields

- version
- type
- session
- node
- timestamp
- signature

## Compatibility

- Unknown fields MUST be ignored.
- Missing required fields MUST reject the message.
- Major version mismatch MUST trigger compatibility negotiation.
