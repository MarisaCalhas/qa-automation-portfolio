import json
import matplotlib.pyplot as plt
import os

METRICS_FILE = "metrics/metrics.json"
OUTPUT_DIR = "metrics"

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(METRICS_FILE, "r") as f:
    data = json.load(f)

tests = data.get("tests", [])
passed = data.get("passed", 0)
failed = data.get("failed", 0)

labels = ["Passed", "Failed"]
values = [passed, failed]

plt.figure()
plt.bar(labels, values)
plt.title("Test Results")
plt.savefig(f"{OUTPUT_DIR}/test_results.png")