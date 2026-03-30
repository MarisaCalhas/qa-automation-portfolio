import pytest
import allure


# ---------------------------
# PLAYWRIGHT FIXTURE
# ---------------------------
@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


# ---------------------------
# SCREENSHOT ON FAILURE
# ---------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        try:
            page = item.funcargs.get("page")

            if page:
                screenshot = page.screenshot()

                allure.attach(
                    screenshot,
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
        except Exception as e:
            print(f"Screenshot error: {e}")