from textstats.char_count import char_count


def test_char_count_includes_spaces_by_default():
    assert char_count("one two") == 7
    assert char_count("one two", include_spaces=True) == 7


def test_char_count_empty_string_is_zero():
    assert char_count("") == 0
    assert char_count("", include_spaces=False) == 0


def test_char_count_without_spaces_skips_spaces():
    assert char_count("one two", include_spaces=False) == 6


def test_char_count_without_spaces_skips_all_whitespace():
    # space, tab, newline, carriage return
    assert char_count(" a\tb\nc\r", include_spaces=False) == 3


def test_char_count_without_spaces_skips_fullwidth_space():
    assert char_count("你好　世界", include_spaces=False) == 4
    assert char_count("你好　世界") == 5


def test_char_count_only_whitespace_without_spaces_is_zero():
    assert char_count("  \t\n", include_spaces=False) == 0
    assert char_count("  \t\n") == 4
