"""EX02: One-Shot Wordle"""

__author__: "730659395"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

word = "python"
guess = input(f"What is your {len(word)}-letter guess? ")

while len(guess) != 6:
    guess = input(f"That was not {len(word)} letters! Try again: ")

if guess != word:
    print("Not quite. Play again soon!")
if guess == word:
    print("Woo! You got it!")

i: int = 0
display: str = "hi"

while i < len(word):
    if guess[i] == word[i]:
        display += GREEN_BOX
        display += 'hello'
    else: 
        letter_exists: bool = False
        alt_idx: int = 0
        while alt_idx < len(word) and not letter_exists:
            if guess[i] == word[alt_idx]:
                display += YELLOW_BOX
                letter_exists = True
        display += WHITE_BOX
        display += 'goodbye'

print(display)
        

'''
letter_in_word: bool = False
alt_i: int = 0
# Checks each letter of the guessed word against the secret word and adds corresponding emoji to the display.
while i < len(word):
    if guess[i] == word[i]:
        display += GREEN_BOX
    else:
        display += WHITE_BOX
    i += 1
print(display)

#while i < len(word) and not letter_in_word:


while not letter_in_word and alt_i < len(word):
    if guess[i] == word[alt_i]:
                letter_in_word = True
            alt_i += 1
        if letter_in_word == True:
            display += YELLOW_BOX
        else:
            display += WHITE_BOX
'''