"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730659395"


class Simpy:
    values: list[float]

    def __init__(self, input_values: list[float]):
        """Constructor."""
        self.values = input_values

    def __str__(self):
        """Creates a str representation of Simpy object."""
        return f"Simpy({self.values})"
    
    def fill(self, val: float, num_vals: int) -> None:
        """Fills a Simpy's values with num_vals number of value val."""
        self.values = []
        for item in range(0, num_vals):
            self.values.append(val)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills the values attribute with a range of values"""
        assert step != 0.0
        self.values = []
        current_val: float = start
        num_appends: int = int((stop - start)/step)
        for item in range(0, num_appends):
            self.values.append(current_val)
            current_val += step
        print(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Returns a new Simpy object."""
        new_simpy_vals: list = []
        if type(rhs) == float:
            for i in range(0, len(self.values)):
                new_simpy_vals.append(rhs + self.values[i])
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(0,len(rhs.values)):
                new_value = rhs.values[i] + self.values[i]
                new_simpy_vals.append(rhs.values[i] + self.values[i])
        return Simpy(new_simpy_vals)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy
    # TODO: Your constructor and methods will go here.
