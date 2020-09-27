import pytest
from first_missing_integer import firstMissingPositive

def test():
    assert firstMissingPositive([1, 2]) == 3

def test2():
    assert firstMissingPositive([-1, -2, 1, 2]) == 3

def test3():
    assert firstMissingPositive([-1, -2, 1, 3, 5, 6]) == 2

def test4():
    assert firstMissingPositive([3,4,-1,1]) == 2
