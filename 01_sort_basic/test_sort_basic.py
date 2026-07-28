# import pytest
from sort_basic import *


def test_selection():
    a = [4, 3, 1, 2]
    SelectionSortStep(a, 0)
    assert a == [1, 3, 4, 2]


def test_bubble():
    a = [4, 3, 1, 2]
    assert BubbleSortStep(a)
    assert a == [3, 1, 2, 4]
