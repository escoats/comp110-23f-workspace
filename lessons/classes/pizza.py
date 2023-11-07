"""Defining a class!"""


from __future__ import annotations
"""
Think of a class definiiton as a 'roadmap' or 
skeleton for objects that belong to the class. 
You are defining the underlying structure that 
every instance of this class will have.
"""

class Pizza:
    """This is my class to represent pizza!"""

    # attributes
    # syntax: attribute_name: type
    size: str
    toppings: list[str]
    gluten_free: bool

    def __init__(self, size_input: str, toppings_input: int, gluten_free_input: bool):
        self.size = size_input
        self.toppings = toppings_input
        self.gluten_free = gluten_free_input
        # returns self

    def price(self) -> float:
        """Method to compute price of pizza"""
        if self.size == "large":
            cost: float = 6.25
        else:
            cost: float = 5.00
        cost += self.toppings * 0.75
        if self.gluten_free:
            cost += 1.00
        return cost
    
    def add_toppings(self, num_extras: int):
        """Update an existing pizza order with num_extras extra toppings"""
        self.toppings += num_extras

    def add_toppings_new_order(self, num_extras: int) -> Pizza:
        """creates a new pizza with same attributes as the old pizza, but with num_extra extra toppings."""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_extras, self.gluten_free)
        return new_pizza

    def __str__(self) -> str:
        """The result when I call str()"""
        pizza_info: str = f"Pizza order: {self.toppings} toppings, size {self.size}, GF: {self.gluten_free}"
        return pizza_info

pie: Pizza = Pizza("medium", 2, False)
pie.add_toppings(2)
print(pie) # original str() is overwritten