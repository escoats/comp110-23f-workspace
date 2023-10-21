"""Summing the elements of a list using different loops."""

__author__ = "730659395"


def w_sum(vals: list[float]) -> float:
    """Sums the elements of a list using a while loop. Returns the sum."""
    i: int = 0
    sum: float = 0
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Sums the elements of a list using a for loop. Returns the sum."""
    sum: float = 0
    for num in vals:
        sum += num
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Sums the elements of a list a for/in range loop. Returns the sum."""
    sum: float = 0
    for i in range(0, len(vals)):
        sum += vals[i]
    return sum