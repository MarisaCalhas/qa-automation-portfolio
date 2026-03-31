from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = "#username"
        self.password = "#password"
        self.button = "button[type='submit']"

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/login")
        self.page.wait_for_selector(self.username)

    def login(self, user, pwd):
        self.page.locator(self.username).fill(user)
        self.page.locator(self.password).fill(pwd)
        self.page.click(self.button)