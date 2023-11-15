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

    def arange(self, start: float, stop: float, step: float = 1.0):
        
        """Fills the values attribute with a range of values"""
    # TODO: Your constructor and methods will go here.