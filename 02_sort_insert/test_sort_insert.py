from sort_insert import *


def test_insert():
    a = [1, 6, 5, 4, 3, 2, 7]
    InsertionSortStep(a, 3, 1)
    assert a == [1, 3, 5, 4, 6, 2, 7]
