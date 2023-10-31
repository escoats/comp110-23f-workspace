"""Quiz Review 1"""

__author__ = "730659395"

def odd_and_even(inputs: list[int]) -> list[int]:
    """Returns a list containing the elements of the input list that are odd with an even index."""
    i: int = 0
    output: list[int] = []
    while i < len(output):
        if (i % 2 == 0) and (inputs[i] % 2 != 0):
            output.append(inputs[i])
        i += 1
    return output

if __name__ == "odd_and_even":
    odd_and_even()