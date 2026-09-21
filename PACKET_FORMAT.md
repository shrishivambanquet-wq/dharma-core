# Dharma Packet Format v2

Header:
- version
- type
- session
- node
- timestamp
- nonce
- payload_length
- signature

Rules:
- Maximum payload: 64 KiB.
- Unknown fields MUST be ignored.
- Missing required fields MUST reject the packet.
- Packet length MUST match payload_length.

Handshake Example:

{
 "version":"2.0",
 "type":"handshake",
 "session":"uuid",
 "node":"node-A",
 "nonce":"abc123",
 "payload_length":128
}
