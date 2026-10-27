from textstats import word_count, words


def test_words_lowercases_and_splits():
    assert words("Hello, World! It's fine.") == ["hello", "world", "it's", "fine"]


def test_word_count():
    assert word_count("one two  three") == 3
    assert word_count("") == 0
