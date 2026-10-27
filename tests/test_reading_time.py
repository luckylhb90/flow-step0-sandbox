import pytest

from textstats import reading_time


def test_empty_text_takes_no_time():
    assert reading_time("") == 0
    assert reading_time("...") == 0


def test_exact_multiple_of_wpm_is_not_rounded_up():
    text = "word " * 200
    assert reading_time(text, wpm=200) == 1


def test_remainder_rounds_up_to_next_minute():
    text = "word " * 201
    assert reading_time(text, wpm=200) == 2


def test_fractional_wpm_uses_exact_decimal_rate():
    assert reading_time("w " * 21, wpm=0.7) == 30


def test_default_wpm_is_200():
    text = "word " * 400
    assert reading_time(text) == 2


def test_wpm_one_counts_one_minute_per_word():
    assert reading_time("one two three", wpm=1) == 3


@pytest.mark.parametrize("wpm", [0, -1, -200])
def test_nonpositive_wpm_raises_value_error(wpm):
    with pytest.raises(ValueError):
        reading_time("some words here", wpm=wpm)


def test_wpm_is_validated_even_for_empty_text():
    with pytest.raises(ValueError):
        reading_time("", wpm=0)


@pytest.mark.parametrize("wpm", [float("inf"), float("-inf"), float("nan")])
def test_non_finite_wpm_raises_value_error(wpm):
    with pytest.raises(ValueError, match="wpm must be finite and positive"):
        reading_time("one two", wpm=wpm)
