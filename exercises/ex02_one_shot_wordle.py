"""EX02: One-Shot Wordle"""

__author__: "730659395"

word = "python"
guess = input(f"What is your {len(word)}-letter guess? ")

while len(guess) != len(word):
    guess = input(f"That was not {len(word)} letters! Try again: ")

if guess != word:
    print("Not quite. Play again soon!")
if guess == word:
    print("Woo! You got it!")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
display: str = ""

# Checks if the letters in the guess match the secret word
while i < len(word):
    if guess[i] == word[i]:
        display += GREEN_BOX
    else: 
        letter_exists: bool = False
        letter_idx: int = 0
        # Checks if the letter is found somewhere else in the word
        while letter_idx < len(word) and not letter_exists:
            if guess[i] == word[letter_idx]:
                display += YELLOW_BOX
                letter_exists = True
            letter_idx += 1
        if not letter_exists:
            display += WHITE_BOX
    i += 1

print(display)