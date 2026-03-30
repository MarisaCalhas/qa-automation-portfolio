from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://example.com/cart")