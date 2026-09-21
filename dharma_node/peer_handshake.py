import json
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder

with open("config/node.json") as f:
    node_a = json.load(f)

with open("config/node_b/node.json") as f:
    node_b = json.load(f)

with open("config/handshake.json") as f:
    packet = json.load(f)

payload = json.dumps(packet["payload"], sort_keys=True).encode()

try:
    VerifyKey(node_a["public_key"], encoder=HexEncoder).verify(
        payload,
        bytes.fromhex(packet["signature"])
    )

    print("=== DRFC-0103 PEER HANDSHAKE ===")
    print("Node A:", node_a["node_id"])
    print("Node B:", node_b["node_id"])
    print("Status: TRUST ESTABLISHED")
except Exception:
    print("Status: VERIFICATION FAILED")
