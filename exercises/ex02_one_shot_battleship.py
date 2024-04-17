"""EX02 - One Shot Battleship."""

__author__ = "730659395"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

grid_size: int = 4
secret_row: int = 3
secret_col: int = 2

guess_row: int = int(input("Guess a row: "))
while (guess_row > grid_size) or (guess_row < 1):
    guess_row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
guess_col: int = int(input("Guess a column: "))
while (guess_col > grid_size) or (guess_col < 1):
    guess_col = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

result: str = ""
if guess_row == secret_row and guess_col == secret_col:
    result = RED_BOX
else:
    result = WHITE_BOX

row_count: int = 1
while row_count <= grid_size:
    row: str = ""
    column_count: int = 1
    while column_count <= grid_size:
        if guess_col == column_count and guess_row == row_count:
            row += result
        else:
            row += BLUE_BOX
        column_count += 1
    print(row)
    row_count += 1

if guess_row == secret_row and guess_col == secret_col:
    print("Hit!")
elif guess_row == secret_row:
    print("Close! Correct row, wrong column.")
elif guess_col == secret_col:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")