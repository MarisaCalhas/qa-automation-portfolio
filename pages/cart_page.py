class CartPage:
    """Page Object Model for Cart Page."""

    def __init__(self, page):
        self.page = page

    def open_cart(self):
        """Navigate to cart page."""
        self.page.goto("https://www.saucedemo.com/cart.html")