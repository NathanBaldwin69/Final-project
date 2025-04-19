class Investor:
    # Add other attributes and methods later
    def __init__(self, name):
        self.name = name

    def evaluate(self, stock):
        """Each investor must implement their own evaluation logic."""
        raise NotImplementedError
