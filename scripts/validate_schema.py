import sys
import yaml
import json
from jsonschema import validate

rule_file = sys.argv[1]

with open("schemas/rule_schema.json") as f:
    schema = json.load(f)

with open(rule_file) as f:
    rule = yaml.safe_load(f)

validate(instance=rule, schema=schema)

print("Schema validation passed.")
