from textstats import lexical_density


def test_lexical_density_all_distinct_is_one():
    assert lexical_density("one two three") == 1.0


def test_lexical_density_counts_repeats_case_insensitively():
    # words: the, cat, and, the, hat -> 5 total, 4 distinct -> 0.8
    assert lexical_density("The cat and the hat") == 0.8


def test_lexical_density_rounds_to_three_decimals():
    # 2 distinct / 3 total = 0.6667
    assert lexical_density("a a b") == 0.667


def test_lexical_density_no_words_returns_zero():
    assert lexical_density("") == 0.0
    assert lexical_density("123 !!!") == 0.0
