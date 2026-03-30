import allure
from pages.login_page import LoginPage
from utils.test_data import TestData


@allure.feature("Authentication")
@allure.story("Valid login")
def test_valid_login(page):

    login_page = LoginPage(page)

    with allure.step("Open login page"):
        login_page.open()

    with allure.step("Login with valid credentials"):
        login_page.login(
            TestData.VALID_USERNAME,
            TestData.VALID_PASSWORD
        )

    # validação final
    assert "secure" in page.url
    