from hoar_sort import *

def test_hoar_sort():
    a = []
    QuickSort(a, 0, 0)
    assert a == []

    a = [1]
    QuickSort(a, 0, 0)
    assert a == [1]

    a = [1, 2]
    QuickSort(a, 0, 1)
    assert a == [1, 2]

    a = [2, 1]
    QuickSort(a, 0, 1)
    assert a == [1, 2]

    for a in [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]:
        QuickSort(a, 0, 2)
        assert a == [1, 2, 3]

    a = [7, 5, 6, 4, 9, 1, 2, 8, 3]
    QuickSort(a, 0, 8)
    assert a == [1, 2, 3, 4, 5, 6, 7, 8, 9]
