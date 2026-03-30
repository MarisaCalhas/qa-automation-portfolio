
🧪 UI Automation Framework (Python + Playwright)

📌 Project Overview

This is a scalable UI test automation framework built with Python, Playwright and Pytest.

It replicates a real-world QA Automation setup used in modern software engineering teams.

The framework is designed with focus on:

Scalability
Maintainability
Clean architecture
CI/CD integration
Automated reporting

It is intended for QA Automation Engineer portfolio purposes.

🏗️ Architecture

The project is based on the Page Object Model (POM) design pattern:

Each page is represented as an independent class
Test logic is separated from page logic
Promotes reusable and maintainable automation code

Main modules:

Login Page
Product Page
Cart Page
🧰 Tech Stack
Python 3.11+
Playwright
Pytest
GitHub Actions (CI/CD)
Docker
Allure Report
🚀 CI/CD Pipeline

This project uses GitHub Actions to ensure continuous test validation.

On every push:

Dependencies are installed
Test suite is executed
Browser automation is triggered (Playwright)
Test results are generated

👉 CI configuration:
.github/workflows/tests.yml

📊 Reporting

The framework uses Allure Report for advanced test reporting.

Key features:

Step-by-step execution tracking
Failure screenshots attached automatically
Test categorization (feature/story)
Historical execution visibility
🐳 Docker Support

The framework is fully containerized to ensure consistent execution across environments.

docker build -t ui-tests .
docker run ui-tests
🧠 Key Features
Page Object Model architecture
Reusable automation components
Centralized test data handling
Logging system for debugging
Automatic screenshot capture on failure
CI/CD pipeline integration
Dockerized execution
📈 Skills Demonstrated

This project demonstrates:

UI Test Automation (Playwright)
Test Framework Design (Pytest)
Automation Architecture (POM)
CI/CD implementation (GitHub Actions)
Containerization (Docker)
Test Reporting (Allure)
Clean Code principles

