"""EX02: One-Shot Wordle"""

__author__: "730659395"

word = "python"
guess = input("What is your 6-letter guess? ")

while len(guess) != 6:
    guess = input("That was not 6 letters! Try again: ")

if guess != word:
    print("Not quite. Play again soon!")
if guess == word:
    print("Woo! You got it!")


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
print(GREEN_BOX, YELLOW_BOX, WHITE_BOX, GREEN_BOX)