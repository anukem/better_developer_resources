from shortest_way import shortest_way


def test_1():
    assert shortest_way("ab", "ab") == 1


def test_2():
    assert shortest_way("axxxxxb", "abx") == 2


def test_3():
    assert shortest_way("ab", "abx") == -1
