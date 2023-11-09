"""Challenge Question 07."""

from __future__ import annotations

__author__ = "730659395"


class Point:
    """Creates a point with x and y coordinates."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Constructor."""
        self.x = x_init
        self.y = y_init
    
    def scale_by(self, factor: int) -> None:
        """Mutates a Point by updating x and y by a given factor."""
        self.x *= factor
        self.y *= factor
    
    def scale(self, factor: int) -> Point:
        """Creates a new point using the old point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point

    def __str__(self) -> str:
        """Prints out the coordinates of a point."""
        point_info: str = f"x: {self.x}; y: {self.y}"
        return point_info
    
    def __mul__(self, factor: int | float) -> Point:
        """Returns a new point."""
        new_point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __add__(self, addend: int | float) -> Point:
        """Returns a new point."""
        new_point = Point(self.x + addend, self.y + addend)
        return new_point