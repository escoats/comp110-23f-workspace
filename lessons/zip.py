"""Combining two lists into a dictionary."""

__author__ = "730659395"


def zip(keys: list[str], vals: list[int]) -> dict[str, int]:
    """Turns two lists into a dictionary, with the first list as keys and the second as values."""
    zipped: dict[str, int] = dict()
    i: int = 0
    if len(keys) == 0 or len(vals) == 0 or len(keys) != len(vals):
        return zipped
    for key in keys:
        zipped[key] = vals[i]
        i += 1
    return zipped