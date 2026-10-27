from textstats.capitalize_sentences import capitalize_sentences


def test_capitalizes_first_letter_of_text():
    assert capitalize_sentences("hello world") == "Hello world"


def test_capitalizes_after_period_question_and_exclamation():
    assert capitalize_sentences("one. two? three! four") == "One. Two? Three! Four"


def test_leaves_rest_of_each_sentence_unchanged():
    assert capitalize_sentences("it's ok. ALREADY big") == "It's ok. ALREADY big"


def test_delimiter_without_following_whitespace_is_not_a_boundary():
    assert capitalize_sentences("version 1.2 is out") == "Version 1.2 is out"


def test_multiple_whitespace_after_delimiter():
    assert capitalize_sentences("a.   b") == "A.   B"


def test_leading_whitespace_is_kept():
    assert capitalize_sentences("  hi there") == "  Hi there"


def test_sentence_starting_with_digit_is_unchanged():
    assert capitalize_sentences("end. 9 lives") == "End. 9 lives"


def test_empty_string_returns_empty():
    assert capitalize_sentences("") == ""
