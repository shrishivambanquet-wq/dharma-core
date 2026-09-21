from nacl.signing import SigningKey
import json, os, hashlib

CONFIG = "config/node.json"

def init_node():
    if os.path.exists(CONFIG):
        with open(CONFIG) as f:
            return json.load(f)

    sk = SigningKey.generate()
    vk = sk.verify_key

    node = {
        "version": "1.0",
        "node_id": "dharma:node:" + hashlib.sha256(bytes(vk)).hexdigest()[:16],
        "public_key": bytes(vk).hex(),
        "private_key": bytes(sk).hex()
    }

    os.makedirs("config", exist_ok=True)
    with open(CONFIG, "w") as f:
        json.dump(node, f, indent=2)

    return node

if __name__ == "__main__":
    n = init_node()
    print("Node ID:", n["node_id"])
