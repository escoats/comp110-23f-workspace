"""EX03."""

__author__ = "730659395"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def input_guess(grid_size: int, guess_type: str) -> int:
    assert guess_type == "row" or guess_type == "column"
    guess: int = int(input(f"Guess a {guess_type}: "))
    while guess < 1 or guess > grid_size:
        guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    return guess


def print_grid(grid_size: int, row_guess: int, column_guess: int, correct: bool) -> None:
    result: str = ""
    if correct is True:
        result = RED_BOX
    else:
        result = WHITE_BOX
    row_counter: int = 1
    while row_counter <= grid_size:
        row: str = ""
        column_counter: int = 1
        while column_counter <= grid_size:
            if column_guess == column_counter and row_guess == row_counter:
                row += result
            else:
                row += BLUE_BOX
            column_counter += 1
        print(row)
        row_counter += 1
 

def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    if row_guess == secret_row and column_guess == secret_column:
        return True
    else:
        return False
    

def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    turn: int = 1
    playing: bool = True
    while playing:
        print(f"=== Turn {turn}/5 ===")
        row_guess: int = input_guess(grid_size, "row")
        column_guess: int = input_guess(grid_size, "column")
        correct: bool = correct_guess(secret_row, secret_column, row_guess, column_guess)
        print_grid(grid_size, row_guess, column_guess, correct)
        if correct is True:
            print("Hit!")
            print(f"You won in {turn}/6 turns!")
            playing = False
        else:
            print("Miss!")
        turn += 1

        if turn == 6:
            print("X/6 - Better luck next time!")
            playing = False

main(4, 3, 2)