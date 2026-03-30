class LoginPage:
    """Page Object Model for Login Page."""

    def __init__(self, page):
        self.page = page

        # Locators
        self.username_input = "#username"
        self.password_input = "#password"
        self.login_button = "button[type='submit']"

    def open(self):
        """Navigate to login page."""
        self.page.goto("https://the-internet.herokuapp.com/login")

    def login(self, username, password):
        """Perform login action."""
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)