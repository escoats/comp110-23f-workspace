"""File to define Fish class."""

__author__ = "730659395"


class Fish:
    """Class to represent Fish."""
    age: int

    def __init__(self):
        """Constructor."""
        self.age = 0
        return None
    
    def one_day(self):
        """Simulates one day."""
        self.age += 1
        return None