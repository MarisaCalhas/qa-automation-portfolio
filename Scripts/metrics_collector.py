import json
import os
import time


ALLURE_RESULTS_DIR = "allure-results"


def load_results():
    results = []

    if not os.path.exists(ALLURE_RESULTS_DIR):
        return results

    for file in os.listdir(ALLURE_RESULTS_DIR):
        if file.endswith("-result.json"):
            with open(os.path.join(ALLURE_RESULTS_DIR, file), "r") as f:
                results.append(json.load(f))

    return results


def generate_metrics():
    results = load_results()

    passed = 0
    failed = 0
    skipped = 0
    durations = []

    for r in results:
        status = r.get("status")

        if status == "passed":
            passed += 1
        elif status == "failed":
            failed += 1
        elif status == "skipped":
            skipped += 1

        if "stop" in r and "start" in r:
            durations.append(r["stop"] - r["start"])

    total = passed + failed + skipped
    success_rate = (passed / total * 100) if total > 0 else 0
    avg_duration = sum(durations) / len(durations) if durations else 0

    metrics = {
        "total_tests": total,
        "passed": passed,
        "failed": failed,
        "skipped": skipped,
        "success_rate": round(success_rate, 2),
        "avg_duration_ms": round(avg_duration, 2)
    }

    os.makedirs("metrics", exist_ok=True)

    with open("metrics/metrics.json", "w") as f:
        json.dump(metrics, f, indent=4)

    print("Metrics generated:", metrics)


if __name__ == "__main__":
    generate_metrics()