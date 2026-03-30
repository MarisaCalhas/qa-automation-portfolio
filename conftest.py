import pytest
import allure


# ==============================
# PLAYWRIGHT FIXTURE (CORRETO)
# ==============================
@pytest.fixture
def page(playwright):
    browser = playwright.chromium.launch(
        headless=True,
        args=["--no-sandbox"]
    )

    context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )

    page = context.new_page()
    yield page

    context.close()
    browser.close()


# ==============================
# ALLURE DEBUG (SCREENSHOT FAIL)
# ==============================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            allure.attach(
                page.screenshot(full_page=True),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            allure.attach(
                page.url,
                name="Last URL",
                attachment_type=allure.attachment_type.TEXT
            )