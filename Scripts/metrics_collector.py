import os
import json

RESULTS_DIR = "allure-results"
OUTPUT_DIR = "project_1_ui_ecommerce/metrics"

os.makedirs(OUTPUT_DIR, exist_ok=True)

total = 0
passed = 0
failed = 0

if os.path.exists(RESULTS_DIR):
    for file in os.listdir(RESULTS_DIR):
        if file.endswith("-result.json"):
            total += 1
            with open(os.path.join(RESULTS_DIR, file)) as f:
                data = json.load(f)
                if data.get("status") == "passed":
                    passed += 1
                else:
                    failed += 1

metrics = {
    "total": total,
    "passed": passed,
    "failed": failed
}

with open(f"{OUTPUT_DIR}/metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

print("Metrics generated:", metrics)