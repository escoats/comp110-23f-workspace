"""Quiz Review 3"""

__author__ = "730659395"

def short_words(words_list: list[str]) -> list[int]:
    """Returns list of words that are shorter than 5 characters."""
    shorts: list[str] = []
    for word in words_list:
        if len(word) < 5:
            shorts.append(word)
        else:
            print(f"{word} is too long!")
    return shorts

print(short_words(['sun', 'cloud', 'sky']))