from asteroid_collision import asteroid_collision


def test_1():
    assert asteroid_collision([5, 19, -1]) == [5, 19]


def test_2():
    assert asteroid_collision([5, 19, -1, 100]) == [5, 19, 100]


def test_3():
    assert asteroid_collision([-3, 1, 2, 3, 4, 19, -100, 100]) == [-3, -100, 100]
