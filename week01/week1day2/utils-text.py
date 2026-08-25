
from__future__ import annotations # type: ignore

def clean_text(text: str) -> str:
    """convert text to lowercase and remove extra spaces."""
    cleaned_text = text.strip().lower()
    return cleaned_text 

def tokenize_text(text: str) -> list:
    """split text into words."""
    tokens = text.split()
    return tokens

def  count_chars(text: str) -> dict[str, int]:
    """count the number of characters in the text."""
    count = {}
    for char in text:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count