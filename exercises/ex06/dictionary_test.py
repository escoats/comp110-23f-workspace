"""EX05 - Dictionary Test."""

__author__ = "730659395"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_two() -> None:
    """Given {"a": "1", "b": "2"}, {"1": "a", "2": "b"} should be returned."""
    assert invert({"a": "1", "b": "2"}) == {"1": "a", "2": "b"}


def test_invert_one() -> None:
    """Tests a dictionary with only one pair."""
    assert invert({"a": "1"}) == {"1": "a"}


def test_invert_empty() -> None:
    """Given an empty dictionary, should return an empty dictionary."""
    assert invert({}) == {}


def test_favorite_color_tie() -> None:
    """When two colors have the same number of instances, the first one to appear in the dictionary should be returned."""
    assert favorite_color({"Lizzie": "green", "Kuhu": "red", "Heidi": "green", "Maanya": "red"}) == "green"


def test_favorite_color_winner() -> None:
    """favorite_color({"Lizzie": "green", "Kuhu": "red", "Heidi": "green"}) should return "green"."""
    assert favorite_color({"Lizzie": "green", "Kuhu": "red", "Heidi": "green"}) == "green"


def test_favorite_color_empty() -> None:
    """favorite_color({}) should return an empty string."""
    assert favorite_color({}) == ""


def test_count_three_items() -> None:
    """count(["a", "b", "c"]) should return {"a": 1, "b": 1, "c": 1}."""
    assert count(["a", "b", "c"]) == {"a": 1, "b": 1, "c": 1}


def test_count_same_value() -> None:
    """count(["a", "a", "a"]) should return {"a": 3}."""
    assert count(["a", "a", "a"]) == {"a": 3}


def test_count_empty() -> None:
    """count([]) should return an empty dict."""
    assert count([]) == {}


def test_alphabetizer_one_entry() -> None:
    """alphabetizer(["apple"]) should return {"a": "apple"}."""
    assert alphabetizer(["apple"]) == {"a": ["apple"]}


def test_alphabetizer_multiple_cases() -> None:
    """alphabetizer(["Ant", "apple"]) should return {"a": ["apple", "Ant"]}."""
    assert alphabetizer(["Ant", "apple"]) == {"a": ["Ant", "apple"]}


def test_alphabetizer_empty() -> None:
    """alphabetzier([]) should return an empty dict."""
    assert alphabetizer([]) == {}


def test_attendance_new_student() -> None:
    """update_attendance({"Monday": ["Lizzie"]}, "Monday", "Kuhu") should return {"Monday": ["Lizzie", "Kuhu"]}."""
    assert update_attendance({"Monday": ["Lizzie"]}, "Monday", "Kuhu") == {"Monday": ["Lizzie", "Kuhu"]}


def test_attendance_already_recorded() -> None:
    """If a student's name is already listed, it should not be added again."""
    assert update_attendance({"Monday": ["Lizzie"]}, "Monday", "Lizzie") == {"Monday": ["Lizzie"]}


def test_attendance_multiple_days() -> None:
    """update_attendance({"Monday": ["Lizzie"]}, "Tuesday", "Kuhu") should return {"Monday": ["Lizzie"], "Tuesday": ["Kuhu"]}."""
    assert update_attendance({"Monday": ["Lizzie"]}, "Tuesday", "Kuhu") == {"Monday": ["Lizzie"], "Tuesday": ["Kuhu"]}