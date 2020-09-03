import pytest


def split_balanced_string(s):
    count = 0
    lr_map = {}
    for char in s:
        lr_map[char] = 1 if char not in lr_map else lr_map[char] + 1

        if "L" in lr_map and "R" in lr_map and lr_map["L"] == lr_map["R"]:
            count += 1
    return count


def test_1():
    assert split_balanced_string("LRLRLRLR") == 4


def test_2():
    assert split_balanced_string("LRLRLLRRLR") == 4


def test_3():
    assert split_balanced_string("LLLLRRRR") == 1


pytest.main()
