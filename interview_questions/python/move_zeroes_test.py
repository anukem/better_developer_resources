from move_zeroes import move_zeroes


def test_one():
    assert move_zeroes([1, 2, 3, 0, 0]) == [1, 2, 3, 0, 0]


def test_two():
    assert move_zeroes([1, 2, 0, 3, 0]) == [1, 2, 3, 0, 0]


def test_three():
    assert move_zeroes([0, 1, 2, 0]) == [1, 2, 0, 0]
