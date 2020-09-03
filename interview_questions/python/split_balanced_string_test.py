from split_balanced_string import split_balanced_string


def test_1():
    assert split_balanced_string("LRLRLRLR") == 4


def test_2():
    assert split_balanced_string("LRLRLLRRLR") == 4


def test_3():
    assert split_balanced_string("LLLLRRRR") == 1
