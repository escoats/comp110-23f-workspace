"""practice writing functions"""

def mimic(my_words: str) -> str:
    """Given the string my_words, outputs the same string."""
    return my_words

my_words: str = "hello"
response: str = mimic(my_words)
print(response)


def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    if (letter_idx + 1) > len(my_words):
        response = "Index too high."
    else:
        response: str = my_words[letter_idx]
    return response

print(mimic_letter("hi", 2))