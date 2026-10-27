"""Character counting."""


def char_count(text, include_spaces=True):
    """How many characters text has.

    With include_spaces=False, whitespace characters (spaces, tabs, newlines, ...) are not counted.
    """
    if include_spaces:
        return len(text)
    return sum(1 for c in text if not c.isspace())
