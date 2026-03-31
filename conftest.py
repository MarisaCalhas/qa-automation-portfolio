import pytest
import allure


# =========================
# BROWSER (WITH TRACE SUPPORT)
# =========================
@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=True)
    yield browser
    browser.close()


# =========================
# PAGE (WITH TRACE ENABLED)
# =========================
@pytest.fixture
def page(browser, request):
    context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    page = context.new_page()

    yield page

    # =========================
    # SAVE TRACE IF FAILURE
    # =========================
    if request.node.rep_call.failed:
        trace_path = "trace.zip"
        context.tracing.stop(path=trace_path)

        allure.attach.file(
            trace_path,
            name="Playwright Trace",
            attachment_type=allure.attachment_type.ZIP
        )
    else:
        context.tracing.stop()

    context.close()


# =========================
# SCREENSHOT ON FAILURE
# =========================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    item.rep_call = report

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            allure.attach(
                page.screenshot(full_page=True),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )