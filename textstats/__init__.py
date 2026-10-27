"""A tiny text-statistics library (a test project for an automation pilot)."""
import math
import re
from fractions import Fraction

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
        raise ValueError("wpm must be finite and positive")

    try:
        rate = Fraction(int(wpm)) if isinstance(wpm, bool) else Fraction(str(wpm))
    except (OverflowError, ValueError, ZeroDivisionError) as exc:
        raise ValueError("wpm must be finite and positive") from exc

    count = word_count(text)
    if count == 0:
        return 0
    return math.ceil(Fraction(count) / rate)
