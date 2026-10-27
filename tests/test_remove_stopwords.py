from textstats.remove_stopwords import remove_stopwords


def test_remove_stopwords_default_list_removes_common_words():
    assert remove_stopwords("a an the and or of to in") == []


def test_remove_stopwords_default_keeps_other_words_in_order():
    assert remove_stopwords("The cat and the hat") == ["cat", "hat"]


def test_remove_stopwords_is_case_insensitive():
    assert remove_stopwords("The THE the") == []


def test_remove_stopwords_keeps_apostrophe_words():
    # "it's" is one word, so it is not the stopword "it"
    assert remove_stopwords("it's in the box") == ["it's", "box"]


def test_remove_stopwords_custom_list_replaces_default():
    assert remove_stopwords("the cat is here", stopwords={"is"}) == ["the", "cat", "here"]


def test_remove_stopwords_custom_list_is_lower_cased():
    assert remove_stopwords("The cat", stopwords={"THE"}) == ["cat"]


def test_remove_stopwords_empty_list_keeps_everything():
    assert remove_stopwords("a the", stopwords=[]) == ["a", "the"]


def test_remove_stopwords_no_words_returns_empty_list():
    assert remove_stopwords("") == []
    assert remove_stopwords("123 !!!") == []
