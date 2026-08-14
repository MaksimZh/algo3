from order_stat import *

from itertools import permutations

def test_order_stat():
    assert KthOrderStatisticsStep([], 0, 0, 0) == []
    assert KthOrderStatisticsStep([5], 0, 0, 0) == [0, 0]
    for a in permutations([1, 2]):
        a = list(a)
        assert KthOrderStatisticsStep(a, 0, 1, 0) == [0, 0]
        assert KthOrderStatisticsStep(a, 0, 1, 1) == [1, 1]
    for a in permutations([1, 2, 3]):
        a = list(a)
        assert KthOrderStatisticsStep(a, 0, 2, 0) == [0, 0]
        assert KthOrderStatisticsStep(a, 0, 2, 1) == [1, 1]
        assert KthOrderStatisticsStep(a, 0, 2, 2) == [2, 2]
    KthOrderStatisticsStep([7, 5, 6, 4, 3, 1, 2], 0, 6, 0) == [0, 2]
    KthOrderStatisticsStep([7, 5, 6, 4, 3, 1, 2], 0, 6, 1) == [0, 2]
    KthOrderStatisticsStep([7, 5, 6, 4, 3, 1, 2], 0, 6, 2) == [0, 2]
    KthOrderStatisticsStep([7, 5, 6, 4, 3, 1, 2], 0, 6, 3) == [3, 3]
    KthOrderStatisticsStep([7, 5, 6, 4, 3, 1, 2], 0, 6, 4) == [4, 6]
    KthOrderStatisticsStep([7, 5, 6, 4, 3, 1, 2], 0, 6, 5) == [4, 6]
    KthOrderStatisticsStep([7, 5, 6, 4, 3, 1, 2], 0, 6, 6) == [4, 6]
    KthOrderStatisticsStep([7, 5, 6, 4, 3, 1, 2, 8, 9], 0, 8, 1) == [0, 1]
    KthOrderStatisticsStep([7, 5, 6, 4, 3, 1, 2, 8, 9], 0, 8, 2) == [2, 2]
    KthOrderStatisticsStep([7, 5, 6, 4, 3, 1, 2, 8, 9], 0, 8, 5) == [3, 8]
