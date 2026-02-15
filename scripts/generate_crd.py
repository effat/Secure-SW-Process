import yaml
import hashlib
import sys
import os

rule_file = sys.argv[1]

with open(rule_file) as f:
    rule = yaml.safe_load(f)

rule_hash = hashlib.sha256(
    yaml.dump(rule, sort_keys=True).encode()
).hexdigest()

output = {
    "apiVersion": "compliance.example.org/v1",
    "kind": "RuleConfig",
    "metadata": {
        "name": rule["metadata"]["name"],
        "annotations": {
            "ruleHash": rule_hash
        }
    },
    "spec": rule["spec"]
}

os.makedirs("k8s/generated", exist_ok=True)
output_path = f'k8s/generated/{rule["metadata"]["name"]}-crd.yaml'

with open(output_path, "w") as f:
    yaml.dump(output, f)

print(f"Generated: {output_path}")
