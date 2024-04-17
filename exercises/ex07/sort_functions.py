"""Functions that implement sorting algorithms."""

__author__ = ""

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    sorted_index: int = 0
    while sorted_index < len(x)-1:
        unsorted_index: int = sorted_index + 1
        while unsorted_index > 0 and x[sorted_index] < x[unsorted_index - 1]:
            current_elem: int = x[unsorted_index]
            x[unsorted_index] = x[unsorted_index - 1]
            x[unsorted_index - 1] = current_elem
            unsorted_index -= 1
        sorted_index += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    idx: int = 0
    while idx < len(x):
        min_idx = idx
        idx2 = min_idx
        while idx2 < len(x):
            if x[idx] < x[min_idx]:
                min_idx = idx
            idx2 += 1
        temp: int = x[min_idx]
        x[min_idx] = x[idx]
        x[idx] = temp
        idx += 1

'''
list1: list[int] = [2, 4, 3, 6]
insertion_sort(list1)
print(list1)
list2: list[int] = [-7, -8, -9, -10]
insertion_sort(list2)
print(list2)
'''