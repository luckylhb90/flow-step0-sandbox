from textstats import word_frequencies


def test_word_frequencies_counts_words():
    assert word_frequencies("the cat and the hat") == {"the": 2, "cat": 1, "and": 1, "hat": 1}


def test_word_frequencies_is_case_insensitive_and_ignores_punctuation():
    assert word_frequencies("Hi, hi! HI.") == {"hi": 3}


def test_word_frequencies_keeps_apostrophes():
    assert word_frequencies("it's it's its") == {"it's": 2, "its": 1}


def test_word_frequencies_empty():
    assert word_frequencies("") == {}
    assert word_frequencies("123 !!!") == {}
