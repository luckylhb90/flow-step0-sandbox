from textstats.unique_words import unique_words


def test_unique_words_removes_duplicates_and_sorts():
    assert unique_words("the cat and the hat") == ["and", "cat", "hat", "the"]


def test_unique_words_is_case_insensitive():
    assert unique_words("Cat CAT cat") == ["cat"]


def test_unique_words_keeps_apostrophes_as_part_of_word():
    assert unique_words("it's its it's") == ["it's", "its"]


def test_unique_words_ignores_non_word_characters():
    assert unique_words("123 !!! one, two.") == ["one", "two"]


def test_unique_words_no_words_returns_empty_list():
    assert unique_words("") == []
    assert unique_words("123 !!!") == []
