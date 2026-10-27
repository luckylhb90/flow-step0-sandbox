"""A tiny text-statistics library (a test project for an automation pilot)."""
import re

_WORD = re.compile(r"[A-Za-z']+")


def words(text):
    """The words of text, lower-cased, in order."""
    return [w.lower() for w in _WORD.findall(text)]


def word_count(text):
    """How many words text has."""
    return len(words(text))
