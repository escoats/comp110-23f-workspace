"""EX05 - Dictionary Test."""

__author__ = "730659395"

from exercises.ex06 import dictionary

def test_invert_two() -> None:
    """Given {"a": "1", "b": "2"}, {"1": "a", "2": "b"} should be returned."""
    assert dictionary.invert({"a": "1", "b": "2"}) == {"1": "a", "2": "b"}

def test_invert_one() -> None:
    """Tests a dictionary with only one pair."""
    assert dictionary.invert({"a": "1"}) == {"1": "a"}

def test_invert_empty() -> None:
    """Given an empty dictionary, should return an empty dictionary."""
    assert dictionary.invert({}) == {}

def test_favorite_color_tie() -> None:
    """When two colors have the same number of instances, the first one to appear in the dictionary should be returned."""
    assert dictionary.favorite_color({"Lizzie": "green", "Kuhu": "red", "Heidi": "green", "Maanya": "red"}) == "green"

def test_favorite_color_winner() -> None:
    """favorite_color({"Lizzie": "green", "Kuhu": "red", "Heidi": "green"}) should return "green"."""
    assert dictionary.favorite_color({"Lizzie": "green", "Kuhu": "red", "Heidi": "green"}) == "green"

def test_favorite_color_empty() -> None:
    """favorite_color({}) should return an empty string."""
    assert dictionary.favorite_color({}) == ""
 
# use case: 
# use case:
# edge case: two 

# favorite color: normal use, tie, empty dict
# count: normal use, ###, empty list

# alphabetizer: only one letter, 
# update attendance