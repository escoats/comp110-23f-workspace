"""EX01 - Chardle"""

__author__ = "730659396"


# Asks the user to input a word and character, and checks length of both inputs.
word: str = input("Enter a five-character word: ")
if len(word) != 5:
    print("Error: Word must contain five characters.")
    exit()
character: str = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for", character, "in", word)

# Counts how many times the character is found in the word, and prints a statement whenever the character is found.
num_matches: int = 0
index: int = 0
for letter in word:
    if character == letter:
        print(character, "found at index", index )
        num_matches += 1
    index += 1

# Prints how many instances of the character is found in the word.
if num_matches > 1:
    print(num_matches, "instances of", character, "found in", word)
elif num_matches == 1:
    print(num_matches, "instance of", character, "in", word)
elif num_matches == 0:
    print("No instances of", character, "found in", word)
