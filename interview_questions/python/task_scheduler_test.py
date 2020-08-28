from task_scheduler import task_scheduler


def test_multiple_tasks():
    assert task_scheduler(["a", "a", "a", "a", "b", "b", "b", "b",], 0) == 8


def test_2_breaks_between_tasks():
    assert task_scheduler(["a", "a", "a", "a", "b", "b", "b", "b",], 2) == 11


def test_no_stop():
    assert task_scheduler(["a", "b", "c"], 0) == 3


def test_no_stops():
    assert task_scheduler(["a", "a", "a"], 1) == 5


def test_one_stop():
    assert (
        task_scheduler(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2)
        == 16
    )
