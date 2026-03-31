import json
import matplotlib.pyplot as plt
import os

METRICS_FILE = "project_1_ui_ecommerce/metrics/metrics.json"

if not os.path.exists(METRICS_FILE):
    print("No metrics file found")
    exit(1)

with open(METRICS_FILE) as f:
    data = json.load(f)

labels = ["Passed", "Failed"]
values = [data["passed"], data["failed"]]

plt.figure()
plt.bar(labels, values)
plt.title("Test Results")
plt.savefig("project_1_ui_ecommerce/metrics/results.png")

print("Chart generated")