from textstats import sentence_count


def test_empty_and_whitespace_text_has_no_sentences():
    assert sentence_count("") == 0
    assert sentence_count("   \n\t ") == 0


def test_terminal_punctuation_ends_sentences():
    assert sentence_count("Hello world. Bye!") == 2


def test_consecutive_terminal_punctuation_counts_once():
    # "..." and "?!" each form one terminal run.
    assert sentence_count("Wait... what?!") == 2
    assert sentence_count("?!") == 1


def test_trailing_text_without_punctuation_counts_as_one_sentence():
    assert sentence_count("Hi. there") == 2
    assert sentence_count("no punctuation") == 1


def test_trailing_whitespace_is_not_a_sentence():
    assert sentence_count("Hi.   ") == 1


def test_periods_inside_unspaced_text_do_not_end_sentences():
    assert sentence_count("3.14 is pi.") == 1
    assert sentence_count("a.b") == 1
