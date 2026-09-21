import json, glob

registry=[]
for p in glob.glob("config/node*/node.json"):
    with open(p) as f:
        registry.append(json.load(f)["node_id"])

with open("config/registry.json","w") as f:
    json.dump(registry,f,indent=2)

print("✓ Nodes discovered:",len(registry))
