import json
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder

with open("config/node.json") as f:
    node = json.load(f)

with open("config/handshake.json") as f:
    packet = json.load(f)

payload = json.dumps(packet["payload"], sort_keys=True).encode()
vk = VerifyKey(node["public_key"], encoder=HexEncoder)

try:
    vk.verify(payload, bytes.fromhex(packet["signature"]))
    print("✅ DRFC-0102 VERIFIED")
except Exception:
    print("❌ VERIFICATION FAILED")
