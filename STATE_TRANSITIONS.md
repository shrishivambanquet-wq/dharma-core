# Node State Machine

BOOTSTRAP
→ TRANSPORT_READY
→ DISCOVERING
→ HANDSHAKING
→ SESSION_CREATED
→ SYNCING
→ ACTIVE

Recovery:

ACTIVE → RECOVERING
RECOVERING → ACTIVE
RECOVERING → QUARANTINED
QUARANTINED → BOOTSTRAP

Rules:
- Invalid signatures return to BOOTSTRAP.
- Timeout enters RECOVERING.
- Quarantine requires manual or protocol-authorized recovery.
