"""
DRFC-0006 — Dharma Wire Format (DWF)
Canonical parser and serializer for DAP packets.
"""

import json
from .packets import DAP


class DharmaParser:
    VERSION = 1

    @staticmethod
    def serialize(packet: DAP) -> bytes:
        """
        Convert a DAP object into deterministic wire bytes.
        """

        payload = {
            "version": DharmaParser.VERSION,
            "packet_id": packet.packet_id,
            "timestamp": packet.timestamp,
            "issuer": packet.issuer,
            "subject": packet.subject,
            "authority": packet.authority,
            "constraints": packet.constraints,
            "parent_id": packet.parent_id,
            "revoked": packet.revoked,
            "expired": packet.expired,
        }

        return json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":")
        ).encode("utf-8")

    @staticmethod
    def deserialize(data: bytes) -> DAP:
        """
        Convert wire bytes back into a DAP object.
        """

        payload = json.loads(data.decode("utf-8"))

        if payload.get("version") != DharmaParser.VERSION:
            raise ValueError("Unsupported Dharma version")

        packet = DAP(
            issuer=payload["issuer"],
            subject=payload["subject"],
            authority=payload["authority"],
            constraints=payload["constraints"],
            parent_id=payload["parent_id"]
        )

        packet.packet_id = payload["packet_id"]
        packet.timestamp = payload["timestamp"]
        packet.revoked = payload["revoked"]
        packet.expired = payload["expired"]

        return packet

    @staticmethod
    def to_dict(packet: DAP) -> dict:
        """
        Human-readable packet representation.
        """

        return {
            "packet_id": packet.packet_id,
            "issuer": packet.issuer,
            "subject": packet.subject,
            "authority": packet.authority,
            "constraints": packet.constraints,
            "parent_id": packet.parent_id,
            "revoked": packet.revoked,
            "expired": packet.expired,
            "timestamp": packet.timestamp,
        }