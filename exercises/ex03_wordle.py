"""EX03 - Structured Wordle."""

__author__ = "730659395"


def contains_char(secret: str, char: str) -> bool:
    """Recieves the secret word and one character, and checks to see if the char is found anywhere within the word. Returns True or False."""
    assert len(char) == 1
    i: int = 0
    while i < len(secret):
        if secret[i] == char:
            return True
        i += 1
    # If this point is reached, the character has not been found anywhere in the word
    return False


def emojified(guess: str, secret: str) -> str:
    """Recieves the user's guess and the secret word, and returns an emoji display corresponding to the correctness of the guess."""
    assert len(guess) == len(secret)
    i: int = 0
    display: str = ""
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    WHITE_BOX: str = "\U00002B1C"

    while i < len(secret):
        char_present: bool = contains_char(secret, guess[i])
        # Character is found somewhere in the word
        if char_present is True:
            if guess[i] == secret[i]:
                display += GREEN_BOX
            else: 
                display += YELLOW_BOX
        # Character is not in the word
        if char_present is False:
            display += WHITE_BOX
        i += 1
    return display


def input_guess(expected_length: int) -> str:
    """Recieves the length of the secret word and asks the user to guess a word. Returns the guessed word."""
    guess: str = input(f"Enter a {str(expected_length)} character word: ")
    # Guess is the right length
    if len(guess) == expected_length:
        return guess
    # Guess is the wrong length
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    playing: bool = True
    turn_num: int = 1
    secret = "codes"
    
    # Loops through turns
    while playing is True and turn_num <= 6:
        print(f"=== Turn {turn_num}/6 ===")
        guess = input_guess(len(secret))
        display = emojified(guess, secret)
        print(display)
        # Checks if player has won
        if guess == secret:
            print(f"You won in {turn_num}/6 turns!")
            playing = False
        # Checks if player has lost
        if turn_num == 6:
            print("X/6 - Sorry, try again tomorrow!")
        turn_num += 1


if __name__ == "__main__":
    main()