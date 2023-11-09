"""File to define Bear class."""

__author__ = "730659395"


class Bear:
    """Class to represent Bears."""
    age: int
    hunger_score: int

    def __init__(self):
        """Constructor."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Simulates one day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Increases hunger score by num_fish."""
        self.hunger_score += num_fish
        return None