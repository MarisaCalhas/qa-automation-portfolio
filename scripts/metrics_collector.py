import json
import os

os.makedirs("metrics", exist_ok=True)

data = {
    "tests": 10,
    "passed": 9,
    "failed": 1
}

with open("metrics/metrics.json", "w") as f:
    json.dump(data, f, indent=2)

print("Metrics generated successfully")