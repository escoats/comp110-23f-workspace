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

'''
def favorite_color(names: dict[str, str]) -> str:
    """Returns the most popular color."""
    colors: dict[str, int] = {}

    # adding colors to new dictionary with counts
    for entry in names:
        color = names[entry]
        if color not in colors:
            # first instance of color
            colors[color] = 1
        else:
            colors[color] += 1
    print(colors)

    # this is not working! need to access first entry to set it as default biggest
    most_popular = colors[entry]
    for entry in colors:
        print(entry)
        most_popular = entry
        if colors[entry] > colors[most_popular]:
            most_popular = colors[entry]
    print(most_popular)
'''
def favorite_color2(favorites: dict[str, str]) -> str:
    """Returns the most popular color."""
    colors: dict[str, int] = {}
    for name in favorites:
        color = favorites[name]
        if color in colors:
            # color is already in dict
            colors[color] += 1
        else:
            colors[color] = 1
    
    max_count: int = 0
    most_popular: str = ""
    for color in colors:
        if colors[color] > max_count:
            most_popular = color
            max_count = colors[color]



def count(keys: list[str]) -> dict[str, int]:
    """Produces a dictionary """
    frequencies: dict[str, int] = {}
    for key in keys:
        if key in frequencies:
            frequencies[key] += 1
        elif key not in frequencies:
            frequencies[key] = 1
    return frequencies
    

dict1: dict = {'a': 'z', 
               'b': 'y', 
               'c': 'x'}

favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Ellie": "red", "name1": "red", "name": "blue"})


"""
3. count
Given a list[str], this function will produce a dict[str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list.

Function name: count
Parameter: list[str] - list of values to count the frequencies of
Return Type: dict[str, int] - a dictionary of the counts of each of the items in the input list
Implementation strategy:

Establish an empty dictionary to store your built-up result in
Loop through each item in the input list
Check to see if that item has already been established as a key in your dictionary. Try the following boolean conditional: if <item> in <dict>: – replacing <item> with the variable name of the current value and <dict> with the name of your result dictionary.
If the item is found in the dict, that means there is already a key/value pair where the item is a key. Increase the value associated with that key by 1 (counting it!)
If the item is not found in the dict, that means this is the first time you are encountering the value and should assign an initial count of 1 to that key in the result dictionary.
Return the resulting dictionary.
4. alphabetizer
Given a list[str], this function will produce a dict[str, list[str]] where each key is a unique letter in the alphabet and each value is a list of the words that begin with that letter.

Function name: alphabetizer
Parameter: list[str] - list of words to categorize into different lists
Return Type: dict[str, list[str]] - a dictionary of the letters and the lists of words that belong to that letter
Example usage:

>>> alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"])
{'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}
>>> alphabetizer(["Python", "sugar", "Turtle", "party", "table"])
{'p': ['Python', 'party'], 's': ['sugar'], 't': ['Turtle', 'table']}

Hint: The built-in Python method .lower() takes in no arguments and returns the lower cased string of a given string.

5. update_attendance
Given a dict[str, list[str]], this function will mutate and return that dictionary. It should meet the following specifications:

It has three parameters:
dict[str, list[str]] - an existing dictionary that contains days of the week as keys and a list of students who were in attendance as the values
str - a day of the week
str - a student who attended class
Update the dict[str, list[str]] that was passed in with the new attendance information, then return it.
An example:

 attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
 update_attendance(attendance_log, "Tuesday" , "Vrinda")
 update_attendance(attendance_log, "Wednesday" , "Kaleb")
 print(attendance_log)
The results of which would look like:

$ python -m exercises.ex06.update_attendance
{'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda'], 'Wednesday': ['Kaleb']}
"""