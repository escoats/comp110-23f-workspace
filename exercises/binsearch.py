import math

def binary_search(a: list, x: float) -> int:
    found: bool = False
    i: int = math.floor((len(a)-1)/2)
    while not found:
        if x == a[i]:
            found = True
            return i
        elif x > a[i]:
            i = i + i/2
        elif x < a[i]:
            i = i - i/2
        else:
            found = True
            return -1
    

a = [0, 1.1, 1.1, 2.2, 3.3, 5.5, 8.8]
print(binary_search(a, 8.8))