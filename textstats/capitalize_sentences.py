"""Capitalize the first letter of each sentence."""
import re

# A sentence starts at the beginning of the text (after any leading
# whitespace) or right after '.', '!' or '?' followed by whitespace.
# The first letter after such a boundary is upper-cased.
_SENTENCE_START = re.compile(r"(^\s*|[.!?]\s+)([^\W\d_])")


def capitalize_sentences(text):
    """Upper-case the first letter of every sentence of text.

    Sentences are split at '.', '!' or '?' followed by whitespace. Everything
    else is left unchanged.
    """
    return _SENTENCE_START.sub(lambda m: m.group(1) + m.group(2).upper(), text)
