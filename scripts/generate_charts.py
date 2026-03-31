import json
import matplotlib.pyplot as plt
import os


def load_metrics():
    metrics_path = "metrics/metrics.json"

    if not os.path.exists(metrics_path):
        print("metrics.json not found")
        return None

    with open(metrics_path, "r") as f:
        return json.load(f)


def generate_charts():
    metrics = load_metrics()

    if not metrics:
        print("No metrics available to generate charts")
        return

    os.makedirs("metrics/charts", exist_ok=True)

    # =========================
    # 1. PASS / FAIL / SKIP CHART
    # =========================
    labels = ["Passed", "Failed", "Skipped"]

    values = [
        metrics.get("passed", 0),
        metrics.get("failed", 0),
        metrics.get("skipped", 0)
    ]

    plt.figure()
    plt.bar(labels, values)
    plt.title("Test Results Overview")
    plt.ylabel("Number of Tests")
    plt.savefig("metrics/charts/test_results.png")
    plt.close()

    # =========================
    # 2. PERFORMANCE CHART
    # =========================
    plt.figure()
    plt.bar(["Avg Duration (ms)"], [metrics.get("avg_duration_ms", 0)])
    plt.title("Test Execution Performance")
    plt.ylabel("Milliseconds")
    plt.savefig("metrics/charts/performance.png")
    plt.close()

    print("Charts generated successfully")


if __name__ == "__main__":
    generate_charts()