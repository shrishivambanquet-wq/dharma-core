import json, time, os
from nacl.signing import SigningKey

with open("config/node.json") as f:
    node = json.load(f)

sk = SigningKey(bytes.fromhex(node["private_key"]))

payload = {
    "version": "1.0",
    "type": "DRFC-0101-HANDSHAKE",
    "node_id": node["node_id"],
    "timestamp": int(time.time()),
    "capabilities": ["drfc","authority","trust"]
}

msg = json.dumps(payload, sort_keys=True).encode()
sig = sk.sign(msg).signature.hex()

packet = {"payload": payload, "signature": sig}

os.makedirs("config", exist_ok=True)
with open("config/handshake.json","w") as f:
    json.dump(packet, f, indent=2)

print(json.dumps(packet, indent=2))
