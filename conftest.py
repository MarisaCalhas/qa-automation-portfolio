import pytest
import allure


# -----------------------------
# PLAYWRIGHT FIXTURE CORRETA
# -----------------------------
@pytest.fixture
def page(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    yield page

    browser.close()


# -----------------------------
# SCREENSHOT ON FAILURE (ALLURE)
# -----------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        try:
            page = item.funcargs.get("page")

            if page:
                allure.attach(
                    page.screenshot(),
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
        except Exception as e:
            print(f"Screenshot error: {e}")