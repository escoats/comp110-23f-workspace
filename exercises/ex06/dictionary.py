"""EX06 - Dictionary Functions."""

__author__ = "730659395"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a given dictionary."""
    dict2: dict[str, str] = dict()
    for old_key in dict1:
        new_key = dict1[old_key]
        new_val = old_key
        if new_key in dict2:
            # key already exists
            raise KeyError("Cannot have two values with the same key!")
        dict2[new_key] = new_val
    print(dict2)


def favorite_color(favs: dict[str, str]) -> None:
    """Returns the most popular color."""
    
dict1: dict = {'a': 'z', 
               'b': 'y', 
               'c': 'x'}

invert(dict1)