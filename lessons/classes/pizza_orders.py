"""Instantiating a class."""

"""
This is where we instnatiate the 
class we defined in classes.py. 
In other words, we're creating objects
that belong to that class.
"""

# import the class
# from filename.modulename import classname
from lessons.classes.pizza import Pizza

#my_pizza: Pizza = Pizza() # Constructor

my_pizza: Pizza = Pizza("medium", 5, False)
print(my_pizza.size)

def price(input_pizza: Pizza) -> float:
    """Function to compute the price of a pizza"""
    if input_pizza.size == "large":
        cost: float = 6.25
    else:
        cost: float = 5.00
    cost += input_pizza.toppings * 0.75
    if input_pizza.gluten_free:
        cost += 1.00
    return cost

print(price(my_pizza)) # calling function
print(my_pizza.price()) # calling method

my_pizza.add_toppings(3)
print(my_pizza.price())

second_pizza = my_pizza.add_toppings_new_order(2)
print(second_pizza.toppings)