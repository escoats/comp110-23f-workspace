"""Mutating functions"""

def manual_append(input: list[int], elem: int) -> None:
    input.append(elem)

def double(input: list[int], factor: int) -> None:
    i: int = 0
    while len(input) > i:
        input[i] *= factor
        i += 1