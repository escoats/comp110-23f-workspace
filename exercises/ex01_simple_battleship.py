"""EX01 - Simple Battleship."""

__author__ = "730659395"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

secret: int = int(input("Pick a secret boat location between 1 and 4: "))
if secret < 1:
    print(f"Error! {secret} too low!")
    exit()
elif secret > 4:
    print(f"Error! {secret} too high!")
    exit()

guess: int = int(input("Guess a number between 1 and 4: "))
if guess < 1:
    print(f"Error! {guess} too low!")
    exit()
elif guess > 4:
    print(f"Error! {guess} too high!")
    exit()

result: str = ""
if secret == guess:
    result = RED_BOX
else:
    result = WHITE_BOX

display: str = ""
if guess == 1:
    display += result
else:
    display += BLUE_BOX
if guess == 2:
    display += result
else:
    display += BLUE_BOX
if guess == 3:
    display += result
else:
    display += BLUE_BOX
if guess == 4:
    display += result
else:
    display += BLUE_BOX

print(display)

if secret == guess:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")