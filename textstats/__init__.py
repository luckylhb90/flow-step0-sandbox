"""A tiny text-statistics library (a test project for an automation pilot)."""
import re

_WORD = re.compile(r"[A-Za-z']+")


def words(text):
    """The words of text, lower-cased, in order."""
    return [w.lower() for w in _WORD.findall(text)]


def word_count(text):
    """How many words text has."""
    return len(words(text))


def longest_word(text):
    """The longest word of text (lower-cased, as in words()).

    Ties go to the word that appears first; returns "" if there are no words.
    """
    best = ""
    for w in words(text):
        if len(w) > len(best):
            best = w
    return best
