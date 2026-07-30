from sort_insert import *


def test_insert():
    a = [7, 6, 5, 4, 3, 2, 1]
    InsertionSortStep(a, 3, 0)
    assert a == [1, 6, 5, 4, 3, 2, 7]
    InsertionSortStep(a, 3, 1)
    assert a == [1, 3, 5, 4, 6, 2, 7]
    InsertionSortStep(a, 3, 2)
    assert a == [1, 3, 2, 4, 6, 5, 7]
    InsertionSortStep(a, 3, 3)
    assert a == [1, 3, 2, 4, 6, 5, 7]
