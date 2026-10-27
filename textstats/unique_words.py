"""Distinct words of a text, sorted."""
from textstats import words


def unique_words(text):
    """The distinct words of text (lower-cased, as in words()), sorted alphabetically.

    Returns [] if there are no words.
    """
    return sorted(set(words(text)))
