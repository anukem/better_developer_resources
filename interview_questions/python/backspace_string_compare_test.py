from backspace_string_compare import backspace_string_compare


def test_1():
    assert backspace_string_compare("#a", "a") is True


def test_2():
    assert backspace_string_compare("#aba", "a") is False


def test_3():
    assert backspace_string_compare("#aba##", "a") is True


def test_4():
    assert backspace_string_compare("#aba###", "a###") is True
