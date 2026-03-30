from playwright.sync_api import Page


class ProductPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://example.com")