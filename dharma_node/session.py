import json, os, hashlib
from nacl.signing import SigningKey

nodes=["node_b","node_c","node_d","node_e"]
sessions={}
for n in nodes:
    with open(f"config/{n}/node.json") as f:
        node=json.load(f)
    sessions[node["node_id"]]=hashlib.sha256(node["public_key"].encode()).hexdigest()[:32]

with open("config/sessions.json","w") as f:
    json.dump(sessions,f,indent=2)

print("✓ Sessions created:",len(sessions))
