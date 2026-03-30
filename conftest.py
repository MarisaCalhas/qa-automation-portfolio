import pytest
from playwright.sync_api import sync_playwright
import allure


@pytest.fixture
def browser_page():
    """Creates browser instance for each test."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Take screenshot on failure and attach to Allure report."""

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("browser_page")

        if page:
            screenshot = page.screenshot()

            allure.attach(
                screenshot,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )