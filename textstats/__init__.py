"""A tiny text-statistics library (a test project for an automation pilot)."""
import math
import re

_WORD = re.compile(r"[A-Za-z']+")


def words(text):
    """The words of text, lower-cased, in order."""
    return [w.lower() for w in _WORD.findall(text)]


def word_count(text):
    """How many words text has."""
    return len(words(text))


def reading_time(text, wpm=200):
    """Whole minutes to read text at wpm words per minute, rounded up."""
    if wpm <= 0:
        raise ValueError("wpm must be positive")

    count = word_count(text)
    if count == 0:
        return 0
    return math.ceil(count / wpm)
