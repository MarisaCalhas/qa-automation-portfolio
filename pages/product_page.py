class ProductPage:
    """Page Object Model for Product Page."""

    def __init__(self, page):
        self.page = page

    def select_first_product(self):
        """Select first available product."""
        self.page.click(".inventory_item:first-child")

    def add_to_cart(self):
        """Add selected product to cart."""
        self.page.click("button")