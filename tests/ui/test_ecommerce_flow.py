import allure
from pages.login_page import LoginPage
from utils.test_data import TestData


@allure.feature("E2E Flow")
@allure.story("Login flow")
def test_valid_login(page):

    login = LoginPage(page)

    login.open()
    login.login(
        TestData.VALID_USERNAME,
        TestData.VALID_PASSWORD
    )

    assert "secure" in page.url