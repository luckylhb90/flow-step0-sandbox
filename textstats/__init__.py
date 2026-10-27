"""A tiny text-statistics library (a test project for an automation pilot)."""
from collections import Counter
import re

_WORD = re.compile(r"[A-Za-z']+")


def words(text):
    """The words of text, lower-cased, in order."""
    return [w.lower() for w in _WORD.findall(text)]


def word_count(text):
    """How many words text has."""
    return len(words(text))


def top_words(text, n=3):
    """The n most frequent words of text as (word, count) pairs."""
    if n <= 0:
        return []

    counts = Counter(words(text))
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return ordered[:n]
