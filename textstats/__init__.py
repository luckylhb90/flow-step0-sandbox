"""A tiny text-statistics library (a test project for an automation pilot)."""
import re

_WORD = re.compile(r"[A-Za-z']+")
_SENTENCE_END = re.compile(r"[.!?]+(?=\s|\Z)")


def words(text):
    """The words of text, lower-cased, in order."""
    return [w.lower() for w in _WORD.findall(text)]


def word_count(text):
    """How many words text has."""
    return len(words(text))


def sentence_count(text):
    """How many sentences text has."""
    terminal_runs = list(_SENTENCE_END.finditer(text))
    count = len(terminal_runs)
    trailing_text = text[terminal_runs[-1].end():] if terminal_runs else text
    if trailing_text.strip():
        count += 1
    return count
