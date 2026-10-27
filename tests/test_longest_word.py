from textstats import longest_word


def test_longest_word_basic():
    assert longest_word("a bb ccc dd") == "ccc"


def test_longest_word_ties_return_first():
    assert longest_word("cat dog bird fish") == "bird"
    assert longest_word("ab cd") == "ab"


def test_longest_word_ignores_punctuation():
    assert longest_word("Hello, wonderful world!") == "wonderful"


def test_longest_word_is_lowercased():
    assert longest_word("SUPERCALIFRAGILISTIC small") == "supercalifragilistic"


def test_longest_word_no_words_returns_empty_string():
    assert longest_word("") == ""
    assert longest_word("123 !!! ...") == ""
