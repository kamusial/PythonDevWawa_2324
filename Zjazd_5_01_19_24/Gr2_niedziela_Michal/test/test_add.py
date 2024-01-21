from src.add import add


def test_add_should_add_two_numbers():
    result = add(9, 6)
    assert result == 15
    # powyższy assert to skrót od:
    # if result != 15:
    #     raise AssertionError("Result should have been 15")
