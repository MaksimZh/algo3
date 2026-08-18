from merge_sort import *

from itertools import permutations

def test_merge_sort():
    assert MergeSort([]) == []
    assert MergeSort([1]) == [1]
    for a in permutations([1, 2]):
        assert MergeSort(a) == [1, 2]
    for a in permutations([1, 2, 3]):
        assert MergeSort(a) == [1, 2, 3]
    MergeSort([7, 5, 6, 4, 3, 1, 2]) == [1, 2, 3, 4, 5, 6, 7]
    MergeSort([7, 5, 6, 4, 3, 1, 2, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

