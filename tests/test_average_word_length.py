from textstats import average_word_length


def test_average_word_length_basic():
    assert average_word_length("a bb ccc dd") == 2.0


def test_average_word_length_rounds_to_two_decimals():
    # (3 + 3 + 4) / 3 = 3.333... -> 3.33
    assert average_word_length("cat dog bird") == 3.33


def test_average_word_length_ignores_punctuation():
    # "Hello, world!" -> hello(5), world(5)
    assert average_word_length("Hello, world!") == 5.0


def test_average_word_length_no_words_returns_zero():
    assert average_word_length("") == 0.0
    assert average_word_length("123 !!! ...") == 0.0
