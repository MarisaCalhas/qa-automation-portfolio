import random

class TestData:
    """Centralized test data for automation framework."""

    VALID_USERNAME = "tomsmith"
    VALID_PASSWORD = "SuperSecretPassword!"

    @staticmethod
    def generate_random_user():
        return f"user_{random.randint(1000, 9999)}"