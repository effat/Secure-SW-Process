import yaml
import hashlib
import glob
import sys

def compute_hash(rule):
    return hashlib.sha256(
        yaml.dump(rule, sort_keys=True).encode()
    ).hexdigest()

rule_files = glob.glob("rules/*.yaml")

for rule_file in rule_files:
    with open(rule_file) as f:
        rule = yaml.safe_load(f)

    expected_hash = compute_hash(rule)
    generated_file = f'k8s/generated/{rule["metadata"]["name"]}-crd.yaml'

    with open(generated_file) as f:
        generated = yaml.safe_load(f)

    actual_hash = generated["metadata"]["annotations"]["ruleHash"]

    if expected_hash != actual_hash:
        print("ERROR: Taint propagation failed.")
        sys.exit(1)

print("Static taint verification passed.")
