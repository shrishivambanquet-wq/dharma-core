# Dharma Packet Format v2

## Header

| Field | Required |
|--------|----------|
|version|Yes|
|type|Yes|
|session|Yes|
|node|Yes|
|timestamp|Yes|
|nonce|Yes|
|payload_length|Yes|
|signature|Yes|

## Payload Rules

- Maximum payload: 64 KiB.
- `payload_length` MUST equal the transmitted payload.
- Unknown fields MUST be ignored.
- Missing required fields MUST reject the packet.

## Example

{
 "version":"2.0",
 "type":"handshake",
 "session":"uuid",
 "node":"node-A",
 "nonce":"abc123",
 "payload_length":128
}
