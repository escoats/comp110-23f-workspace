"""Node Class."""

from __future__ import annotations

__author__ = "730659395"


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self.next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Returns the data attribute for the first element in the linked list."""
        return self.data
    
    def tail(self) -> Node | None:
        """Returns a linked list of every element minus the head."""
        if self.next is None:
            return None
        else: 
            return self.next
    
    def last(self) -> int:
        """Returns the data attribute for the last element in the linked list."""
        while True:
            if self.next.next is not None:
                self.next = self.next.next
            else:
                return self.next.data