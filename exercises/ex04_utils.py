"""Exercise 04 - List Utils."""

__author__ = "730659395"


def all(nums_list: list[int], num: int) -> bool:
    """Checks to see if all the integers in nums_list match num."""
    idx: int = 0
    if len(nums_list) == 0:
        return False
    while idx < len(nums_list):
        if num != nums_list[idx]:
            return False
        idx += 1
    
    # If this point is reached, all the numbers match.
    return True


def max(nums_list: list[int]) -> int:
    """Returns the largest number in nums_list."""
    if len(nums_list) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        idx: int = 0
        largest: int = nums_list[0]
        while idx < len(nums_list):
            if largest < nums_list[idx]:
                largest = nums_list[idx]
            idx += 1
    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if two lists are equal."""
    if len(list1) != len(list2):
        return False
   
    # If this point is reached, lists are equal length.
    idx: int = 0
    while idx < len(list1):
        if list1[idx] != list2[idx]:
            return False
        idx += 1
    
    # If this point is reached, lists are equal.
    return True