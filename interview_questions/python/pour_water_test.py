from pour_water import Solution


def test_case2():
    assert Solution().pourWater([1, 2, 3, 4], 2, 2) == [2, 3, 3, 4]


def test_case3():
    assert Solution().pourWater([2, 1, 1, 2, 1, 2, 2], 4, 3) == [2, 2, 2, 3, 2, 2, 2]


def test_case1():
    assert Solution().pourWater([3, 1, 3], 5, 1) == [4, 4, 4]
