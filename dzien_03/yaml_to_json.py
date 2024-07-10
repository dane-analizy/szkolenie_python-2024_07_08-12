import json

import yaml

yaml_file = "konfiguracja.yaml"
json_file = "data.json"

with open(yaml_file, "r") as f:
    data = yaml.safe_load(f)

with open(json_file, "w") as f:
    json.dump(data, f)
