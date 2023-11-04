"""Challenge Question 07."""

from __future__ import annotations

__author__ = "730659395"


class Point:
    """Creates a point with x and y coordinates."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
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