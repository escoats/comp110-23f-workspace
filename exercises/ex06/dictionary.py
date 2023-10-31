"""EX06 - Dictionary Functions."""

__author__ = "730659395"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a given dictionary."""
    dict2: dict[str, str] = dict()
    for old_key in dict1:
        new_key: str = dict1[old_key]
        new_val: str = old_key
        if new_key in dict2:
            # key already exists
            raise KeyError("Cannot have two values with the same key!")
        dict2[new_key] = new_val
    return dict2


def favorite_color(favorites: dict[str, str]) -> str:
    """Returns the most popular color."""
    colors: dict[str, int] = {}
    for name in favorites:
        color: str = favorites[name]
        if color in colors:
            # color is already in dictionary
            colors[color] += 1
        else:
            colors[color] = 1
    
    max_count: int = 0
    most_popular: str = ""
    for color in colors:
        print(color, colors[color])
        if colors[color] > max_count:
            most_popular = color
            max_count = colors[color]
    return most_popular         


def count(keys: list[str]) -> dict[str, int]:
    """Produces a dictionary that gives the count of each value's instances."""
    frequencies: dict[str, int] = {}
    for key in keys:
        if key in frequencies:
            frequencies[key] += 1
        elif key not in frequencies:
            frequencies[key] = 1
    return frequencies


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Produces a dictionary where each key is a letter in the alphabet and each value is a list of words that begin with that letter."""
    alphabet: dict[str, list[str]] = {}
    for word in words:
        letter: str = word.lower()[0]
        if letter not in alphabet:
            alphabet[letter] = [word]
        elif letter in alphabet:
            alphabet[letter].append(word)
    return alphabet
          

def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates the dictionary with new attendance information, then returns it."""
    if day not in attendance:
        attendance[day] = [student]
    elif day in attendance:
        attendance[day].append(student)
    return attendance