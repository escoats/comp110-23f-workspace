'''counters - counts how many odd numbers are in a string of numbers'''

# initializes string of numbers to be counted
num_string: str = '123'

num_odds: int = 0

for num in num_string:
    if int(num) % 2 == 1:
        num_odds += 1

print(num_odds)