"""Test my zip function."""

__author__ = "730659396"

from lessons.zip import zip


def test_empty_lists() -> None:
    """If both lists are empty, zip should return an empty dictionary."""
    assert zip([], []) == {}


def test_two_elements() -> None:
    """zip(["a", "b"], [1, 2]) should return {"a": 1, "b": 2}."""
    assert zip(["a", "b"], [1, 2]) == {'a': 1, 'b': 2}


def test_one_element() -> None:
    """zip(["a"], [1]) should return {'a': 1}."""
    assert zip(["a"], [1]) == {'a': 1}