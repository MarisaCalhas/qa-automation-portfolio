import allure
from pages.login_page import LoginPage
from utils.test_data import TestData


@allure.feature("Authentication")
@allure.story("Valid login")

def test_valid_login(browser_page):
    """Verify user can login with valid credentials."""

    page = page
    login_page = LoginPage(page)

    with allure.step("Open login page"):
        login_page.open()

    with allure.step("Enter credentials and login"):
        login_page.login(
            TestData.VALID_USERNAME,
            TestData.VALID_PASSWORD
        )

    with allure.step("Verify successful login"):
        assert "secure" in page.url