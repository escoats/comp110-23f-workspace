"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730659395"


class Simpy:
    """Simpy class!"""
    values: list[float]

    def __init__(self, input_values: list[float]):
        """Constructor."""
        self.values = input_values

    def __str__(self) -> str:
        """Creates a str representation of Simpy object."""
        return f"Simpy({self.values})"
    
    def fill(self, val: float, num_vals: int) -> None:
        """Fills a Simpy's values with num_vals number of value val."""
        self.values = []
        for item in range(0, num_vals):
            self.values.append(val)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills the values attribute with a range of values."""
        assert step != 0.0
        self.values = []
        current_val: float = start
        if step > 0:
            while current_val < stop:
                self.values.append(current_val)
                current_val += step
        else:
            while current_val > stop:
                self.values.append(current_val)
                current_val += step
    
    def sum(self) -> float:
        """Returns a sum of a Simpy's values."""
        list_sum = sum(self.values)
        return list_sum
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overloads the addition operator and returns a new Simpy object."""
        new_simpy_vals: list = []
        if isinstance(rhs, float):
            for i in range(0, len(self.values)):
                new_simpy_vals.append(rhs + self.values[i])
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                new_simpy_vals.append(rhs.values[i] + self.values[i])
        return Simpy(new_simpy_vals)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overloads the power operator and returns a new Simpy object."""
        new_simpy_vals: list = []
        if isinstance(rhs, float):
            for i in range(0, len(self.values)):
                new_simpy_vals.append(self.values[i] ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                new_simpy_vals.append(self.values[i] ** rhs.values[i])
        return Simpy(new_simpy_vals)
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overloads the == operator."""
        output: list[bool] = []
        if isinstance(rhs, float):
            for i in range(0, len(self.values)):
                if self.values[i] == rhs:
                    output.append(True)
                else:
                    output.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                if self.values[i] == rhs.values[i]:
                    output.append(True)
                else:
                    output.append(False)
        return output

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overloads the greater than operator."""
        output: list[bool] = []
        if isinstance(rhs, float):
            for i in range(0, len(self.values)):
                if self.values[i] > rhs:
                    output.append(True)
                else:
                    output.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                if self.values[i] > rhs.values[i]:
                    output.append(True)
                else:
                    output.append(False)
        return output
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overloads subscription notation to filter with masks."""
        if isinstance(rhs, int):
            item: float = self.values[rhs]
            return item
        else:
            new_simpy_vals: list[float] = []
            for i in range(0, len(self.values)):
                if rhs[i] is True:
                    new_simpy_vals.append(self.values[i])
            new_simpy: Simpy = Simpy(new_simpy_vals)
            return new_simpy