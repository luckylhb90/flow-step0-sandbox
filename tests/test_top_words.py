from textstats import top_words


def test_orders_by_count_descending():
    text = "b a b c a b"
    # b=3, a=2, c=1
    assert top_words(text, 3) == [("b", 3), ("a", 2), ("c", 1)]


def test_ties_broken_alphabetically():
    text = "pear apple fig fig apple kiwi"
    # apple=2, fig=2, kiwi=1, pear=1: ties use alphabetical order.
    assert top_words(text, 3) == [("apple", 2), ("fig", 2), ("kiwi", 1)]


def test_case_insensitive_counting():
    text = "The the THE cat"
    assert top_words(text, 2) == [("the", 3), ("cat", 1)]


def test_default_n_is_three():
    text = "a b c d e"
    assert len(top_words(text)) == 3


def test_nonpositive_n_returns_empty_list():
    assert top_words("a b", 0) == []
    assert top_words("a b", -1) == []


def test_n_larger_than_vocabulary_returns_all_words():
    assert top_words("x y", 10) == [("x", 1), ("y", 1)]


def test_empty_or_punctuation_only_text_returns_empty_list():
    assert top_words("") == []
    assert top_words("  ,.! ") == []


def test_uses_words_tokenizer_for_apostrophes_and_hyphens():
    text = "don't-stop don't"
    # words() splits this into "don't", "stop", and "don't".
    assert top_words(text, 2) == [("don't", 2), ("stop", 1)]


def test_returns_tuples_not_lists():
    result = top_words("hi hi", 1)
    assert result == [("hi", 2)]
    assert isinstance(result[0], tuple)
