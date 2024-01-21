import pytest
from src.transactions import process_transactions


def test_transactions():
    result = process_transactions([{"amount": 5, "type": "credit"}])
    assert result == 5


def test_empty_list():
    """Test negatywny:
    Jeżeli wyjątek wystąpi: PASS
    Jeżeli wyjątek NIE wystąpi: FAIL

    wersja 'prymitywna':
    try:
        result = process_transactions([])
    except ValueError:
        print("PASS")
    else:
        raise AssertionError("When providing empty list [], ValueError should be raised.")
    """
    with pytest.raises(ValueError, match="list is empty"):
        process_transactions([])


def test_transaction_is_not_dict():
    with pytest.raises(ValueError):
        process_transactions([5])


def test_invalid_transaction_dict():
    with pytest.raises(ValueError):
        process_transactions([{"invalid_key": "invalid_value"}])


def test_invalid_amount_type():
    with pytest.raises(ValueError):
        process_transactions([{"amount": "54", "type": 3}])


def test_invalid_type():
    with pytest.raises(ValueError):
        process_transactions([{"amount": 54, "type": "gołąbki"}])


def test_insufficient_funds():
    with pytest.raises(ValueError):
        process_transactions([{"amount": 54, "type": "debit"}])


def test_transfered_money_negative():
    with pytest.raises(ValueError):
        process_transactions([{"amount": -54, "type": "debit"}])


def test_example_transaction_set():
    result = process_transactions(
        [
            {"amount": 5000, "type": "credit"},
            {"amount": 1000, "type": "debit"},
            {"amount": 500, "type": "credit"},
            {"amount": 50, "type": "debit"},
        ])
    assert result == 4450
