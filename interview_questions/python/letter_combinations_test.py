from letter_combinations import letter_combinations


def test_two_digits():
    assert letter_combinations("23") == [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf",
    ]


def test_one_digit():
    assert letter_combinations("2") == ["a", "b", "c"]
