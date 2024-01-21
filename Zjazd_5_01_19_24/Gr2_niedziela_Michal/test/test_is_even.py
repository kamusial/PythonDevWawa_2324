from src.even_or_odd import is_even


def test_even():
    result = is_even(8)
    assert result is True


def test_odd():
    result = is_even(7)
    assert result is False
