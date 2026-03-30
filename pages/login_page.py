from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        # locators
        self.username = "#username"
        self.password = "#password"
        self.submit = "button[type='submit']"

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

        # garante que a página carregou
        self.page.wait_for_selector(self.username)

    def login(self, username: str, password: str):
        self.page.wait_for_selector(self.username, state="visible")

        self.page.fill(self.username, username)
        self.page.fill(self.password, password)

        self.page.click(self.submit)

        # validação simples de login
        self.page.wait_for_timeout(1000)