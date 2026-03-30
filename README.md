# UI Automation Framework (Python + Playwright)

![CI](https://github.com/MarisaCalhas/qa-automation-portfolio/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green)
![Pytest](https://img.shields.io/badge/Pytest-Framework-yellow)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)

---

## Overview (QA Project)


It demonstrates production-level skills in:

- Scalable automation architecture
- CI/CD pipeline integration
- Parallel test execution
- Maintainable test design (POM)
- Reporting and observability

---

## 🏗️ Architecture

- Page Object Model (POM)
- Separation of UI logic and test logic
- Reusable components
- Scalable structure for enterprise use

---

## ⚙️ CI/CD Pipeline

GitHub Actions automatically:

- Installs dependencies
- Executes test suite in parallel
- Runs Playwright browser tests
- Generates Allure results

✔ Triggered on every push and pull request

---

## 🧪 Test Execution Strategy

- Smoke tests → critical flows
- Regression tests → full suite
- Parallel execution using pytest-xdist
- Cross-browser ready (Playwright)

---

## 📊 Reporting (Allure)

- Test execution logs
- Failure tracking
- Attachments (screenshots)
- Structured reporting for QA analysis

---

## 🐳 Docker Support

```bash
docker build -t ui-tests .
docker run ui-tests

▶️ How to Run Locally
pip install -r requirements.txt
playwright install
Run tests
pytest -n 2
Smoke tests
pytest -m smoke
📈 Engineering Skills Demonstrated
UI Automation (Playwright)
Test Framework Design (Pytest)
Scalable Architecture (POM)
CI/CD Engineering (GitHub Actions)
Parallel Test Execution
Containerized Testing (Docker)
Reporting & Debugging (Allure)
🎯 Business Value

This framework simulates QA practices used in:

Swiss fintech companies
Consulting firms (Accenture-style environments)
Enterprise SaaS platforms
👩‍💻 Author

Marisa Calhas
QA Automation Engineer Portfolio