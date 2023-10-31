"""Quiz Review 2"""

__author__ = "730659395"

def value_exists(dict1: dict[str, int], num: int) -> bool:
    """Checks if a given value exists in the dictionary."""
    for key in dict1:
        if num == dict1[key]:
            return True
    return False