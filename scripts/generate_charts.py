import json
import matplotlib.pyplot as plt
import os


def load_metrics():
    with open("metrics/metrics.json", "r") as f:
        return json.load(f)


def generate_charts():
    metrics = load_metrics()

    os.makedirs("metrics/charts", exist_ok=True)

    # =========================
    # 1. PASS/FAIL CHART
    # =========================
    labels = ["Passed", "Failed", "Skipped"]
    values = [
        metrics["passed"],
        metrics["failed"],
        metrics["skipped"]
    ]

    plt.figure()
    plt.bar(labels, values)
    plt.title("Test Results Overview")
    plt.savefig("metrics/charts/test_results.png")

    # =========================
    # 2. PERFORMANCE CHART
    # =========================
    plt.figure()
    plt.bar(["Avg Duration (ms)"], [metrics["avg_duration_ms"]])
    plt.title("Test Execution Performance")
    plt.savefig("metrics/charts/performance.png")

    print("Charts generated successfully")



if __name__ == "__main__":
    generate_charts()