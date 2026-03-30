# 🧪 UI Automation Framework (Python + Playwright)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green)
![Pytest](https://img.shields.io/badge/Pytest-Test%20Framework-yellow)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-lightblue)

---

## 📌 Overview

This project is a **scalable UI test automation framework** built with **Python, Playwright and Pytest**.

It simulates a **real-world QA Automation environment** used in modern engineering teams.

The goal of this project is to demonstrate **industry-level automation skills**, including:

- Scalable test architecture
- Maintainable Page Object Model (POM)
- CI/CD pipeline integration
- Containerized execution
- Automated reporting

---

## 🏗️ Architecture

This framework follows the **Page Object Model (POM)** design pattern:

- Each page is represented as an independent class
- UI logic is separated from test logic
- Promotes reusability and maintainability
- Easy to scale for large test suites

### 📁 Main structure:

- `pages/` → Page Object classes
- `tests/` → Test cases
- `utils/` → Helpers (logging, test data)
- `conftest.py` → Fixtures & hooks

---

## 🧰 Tech Stack

- Python 3.11+
- Playwright
- Pytest
- GitHub Actions (CI/CD)
- Docker
- Allure Reports

---

## 🚀 CI/CD Pipeline

This project uses **GitHub Actions** to automate testing.

On every push or pull request:

- Dependencies are installed
- Test suite is executed
- Playwright runs UI automation tests
- Results are uploaded as artifacts

📄 Workflow file:
`.github/workflows/tests.yml`

---

## 📊 Reporting

The framework integrates **Allure Reports** for advanced test reporting.

### Features:
- Step-by-step execution logs
- Automatic failure screenshots
- Test categorization (smoke/regression)
- Historical execution tracking

---

## 🐳 Docker Support

Run tests in a containerized environment:

```bash
docker build -t ui-tests .
docker run ui-tests



▶️ How to Run Locally
1. Install dependencies
pip install -r requirements.txt
playwright install
2. Run all tests
pytest
3. Run smoke tests
pytest -m smoke
4. Generate Allure report
pytest --alluredir=allure-results
allure serve allure-results
🧪 Test Strategy

The framework supports:

Smoke testing (critical flows)
Regression testing (full suite)
UI functional validation
Cross-browser testing (Playwright capability)
📈 Skills Demonstrated

This project demonstrates real-world QA Automation Engineering skills:

End-to-end UI test automation (Playwright)
Scalable test framework design (Pytest)
Page Object Model (POM) architecture
CI/CD integration (GitHub Actions)
Containerized execution (Docker)
Test reporting (Allure Reports)
Clean code and maintainable test design
🎯 Project Goal

This project was built as part of a QA Automation portfolio to demonstrate readiness for:

QA Automation Engineer roles
SDET Junior/Mid positions
International remote QA opportunities
👩‍💻 Author

Marisa Calhas
QA Automation Engineer Portfolio Project