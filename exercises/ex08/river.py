"""File to define River class."""

__author__ = "730659395"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Class to represent River."""
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of fish and bears and removes fish older than 3 and bears older than 5."""
        surviving_fish: list[Fish] = []
        surviving_bears: list[Bear] = []
        for fish1 in self.fish:
            if fish1.age <= 3:
                surviving_fish.append(fish1)
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.fish = surviving_fish
        self.bears = surviving_bears
        return None

    def remove_fish(self, amount: int):
        """Removes amount many Fish."""
        for removal in range(amount):
            self.fish.pop(0)
        return None
    
    def bears_eating(self):
        """Removes three Fish and feeds each Bear if there are at least 5 Fish left."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Kills off Bears that are starving."""
        surviving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None
        
    def repopulate_fish(self):
        """Breeds Fish."""
        num_babies: int = (len(self.fish) // 2) * 4
        for baby_fish in range(0, num_babies):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Breeds Bears."""
        num_babies: int = len(self.bears) // 2
        for baby_bear in range(0, num_babies):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Prints River information."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self):
        """Simulate one week of life in the river."""
        for day in range(0, 7):
            self.one_river_day()
        return None
            
