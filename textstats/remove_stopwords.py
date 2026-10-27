"""Stopword removal."""
from textstats import words

DEFAULT_STOPWORDS = frozenset({"a", "an", "the", "and", "or", "of", "to", "in"})


def remove_stopwords(text, stopwords=None):
    """The words of text (lower-cased, as in words()) without the stopwords.

    stopwords defaults to DEFAULT_STOPWORDS; an empty collection keeps every word.
    Stopwords are compared lower-cased, like the words.
    """
    stop = DEFAULT_STOPWORDS if stopwords is None else {s.lower() for s in stopwords}
    return [w for w in words(text) if w not in stop]
