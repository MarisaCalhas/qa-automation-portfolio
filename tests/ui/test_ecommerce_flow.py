import pytest
from pages.login_page import LoginPage
from utils.test_data import TestData


@pytest.mark.regression
def test_valid_login(page):

    login = LoginPage(page)

    login.open()
    login.login(
        TestData.VALID_USERNAME,
        TestData.VALID_PASSWORD
    )

    assert "secure" in page.url